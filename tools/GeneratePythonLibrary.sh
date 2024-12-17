#!/usr/bin/env bash

set -e

readonly LOCAL_ENV="local"
readonly PROD_ENV="prod"

function usage {
  echo "Usage  : $1 [--install|--editable] [--test local|prod]"
  echo
  echo "         --install (-i): Install the package locally."
  echo "         --editable (-e): Make the installed package always reference your latest"
  echo "                          source code. Implies \"-i|--install\". Be aware that changes to the \"src\""
  echo "                          directory won't be reflected. See the README for details."
  echo "         --test (-t) [$LOCAL_ENV|$PROD_ENV]: Run tests (python_api_tests.py) against http://localhost" 
  echo "                                   or https://www.kaggle.com."
  echo "         --watch (-w): Run the script in watch mode. It will watch the files under the \"template\""
  echo "                       directory and KaggleSwagger* files, and regenerate the package when there is a change."
  echo ""
}

INSTALL="no"
INSTALL_EDITABLE="no"
TEST=""
WATCH="no"

while [[ $# -gt 0 ]]; do
  arg="$1"
  case $arg in
    --install|-i)
      INSTALL="yes"
      ;;
    --editable|-e|--editable-install|--install-editable)
      INSTALL_EDITABLE="yes"
      ;;
    --test|-t)
      TEST=$2
      if [[ "$TEST" != "$LOCAL_ENV" ]] && [[ "$TEST" != "$PROD_ENV" ]]; then
        echo -e "Invalid value for arg \"$1\": \"$TEST\". Must be \"$LOCAL_ENV\" or \"$PROD_ENV\".\n"
        usage $0
        exit 0
      fi
      shift
      ;;
    --watch|-w)
      WATCH="yes"
      INSTALL_EDITABLE="yes"
      ;;
    --help|-h)
      usage $0
      exit 0
      ;;
    *)
      echo -e "Invalid argument: \"$1\".\n"
      usage $0
      exit 1
      ;;
  esac
  shift  # Proceed with the next argument.
done

SELF_DIR=$(dirname $(realpath $0))
SELF_DIR=${SELF_DIR%/*} # remove the last directory (tools) from the path
cd $SELF_DIR

SWAGGER_YAML=$SELF_DIR/src/KaggleSwagger.yaml
SWAGGER_CONFIG=$SELF_DIR/src/KaggleSwaggerConfig.json
KAGGLE_XDG_CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/kaggle"
mkdir -p "$KAGGLE_XDG_CONFIG_DIR"
KAGGLE_DEV_CONFIG_DIR=$(realpath "$KAGGLE_XDG_CONFIG_DIR/dev")

trap cleanup EXIT

function init {
  cd $SELF_DIR

  mkdir -p "$KAGGLE_XDG_CONFIG_DIR" && chmod 700 "$KAGGLE_XDG_CONFIG_DIR"

  echo "rm -rf kaggle"
  rm -rf kaggle

  create-local-creds
}

function reset {
  cd $SELF_DIR

  echo rm -rf kaggle/*
  rm -rf kaggle/*

  echo "yapf3 -ir src/"
  if [ -x "$(command -v yapf3)" ]; then
    yapf3 -ir --style yapf src/
  else
    echo "yapf3 is not installed on your system"
  fi
}

function create-local-creds {
  # Generate a separate dev credentials file (kaggle.json) to use when running against
  # http://localhost. This token only works when the webtier is running locally in debug
  # mode. When running against localhost, we set KAGGLE_CONFIG_DIR env var to
  # "~/.config/kaggle/dev/" so that the Python client searches for kaggle.json under this folder
  # and uses dummy dev creds
  local kaggle_config_file="$KAGGLE_DEV_CONFIG_DIR/kaggle.json"
  mkdir -p $KAGGLE_DEV_CONFIG_DIR
  local username=${KAGGLE_DEVELOPER:-$USER}
  echo "{\"username\":\"$username\",\"key\":\"local_api_token\"}" > $kaggle_config_file
  chmod 600 $kaggle_config_file
}

function generate-package {
  # TODO Remove this.
  if [[ -f "kaggle/api/__init__.py" ]]; then
    sed -i -e 's/kaggle_api/kaggle_api_extended/g' kaggle/api/__init__.py
  fi

  if [[ -f "kaggle/configuration.py" ]]; then
    # Replace the hard-coded endpoint URL with an environment variable in configuration.py
    # to allow talking to localhost, staging, prod etc.
    sed -i 's|self.host = "http|self.host = _get_endpoint_from_env() or "http|g' kaggle/configuration.py
    echo -e "\n" >> kaggle/configuration.py
    cat <<-END >> kaggle/configuration.py
def _get_endpoint_from_env():
    import os
    endpoint = os.environ.get("KAGGLE_API_ENDPOINT")
    if endpoint is None:
        return None
    endpoint = endpoint.rstrip("/")
    if endpoint.endswith("/api/v1"):
        return endpoint
    return endpoint + "/api/v1"    
END
  fi
}

function copy-src {
  cp ./src/setup.py .
  cp ./src/setup.cfg .
  cp -r ./src/kaggle .
}

function run-autogen {
  find kaggle/ -type f -name \*.py -exec /tmp/autogen/autogen.sh --no-code --no-top-level-comment --in-place --copyright "Kaggle Inc" --license apache {} \;
}

function run-tests {
  if ! which kaggle > /dev/null 2> /dev/null; then
    echo "Warning: \"kaggle\" is not in PATH. Please add \"~/.local/bin\" to PATH in ~/.bashrc."
    return 0
  fi

  if [[ "$TEST" == "$LOCAL_ENV" ]]; then
    source ../use-localhost.sh
  elif [[ "$TEST" == "$PROD_ENV" ]]; then
    source ../use-prod.sh
  else
    return 0 # Nothing to do
  fi

  cp ../python_api_tests.py ../sample_submission.csv ./
  python3 python_api_tests.py
  rm -f ./python_api_tests.py
}

function install-package {
  pip3 install --break-system-packages --require-hashes -r requirements.txt 
  if [[ "$INSTALL_EDITABLE" == "yes" ]];  then
    pip3 install --break-system-packages --upgrade --editable .
  elif [[ "$INSTALL" == "yes" ]];  then
    pip3 install --break-system-packages --upgrade .
  fi
}

function cleanup {
  cd $SELF_DIR
  rm -rf tox.ini \
    test-requirements.txt \
    test \
    .swagger-codegen \
    .travis.yml \
    git_push.sh \
    python_api_tests.py \
    sample_submission.csv \
    ds_salaries.csv \
    test.csv \
    house-prices-advanced-regression-techniques.zip \
    data-science-salaries-2023.zip \
    kaggle/*.py-e \
    kaggle/api/*.py-e \
    kaggle/*.py.bak
}

function run {
  reset

  generate-package
  copy-src
  run-autogen
  install-package
  run-tests

  echo -e "\nGenerated the \"kaggle\" package successfully!"
}

WATCHED_EVENTS="-e create -e modify -e delete"

function watch-swagger {
  local watched_paths="$SWAGGER_YAML $SWAGGER_CONFIG"

  echo "Watching for changes to Swagger config..."
  while inotifywait -q -r $WATCHED_EVENTS --format "%e %w%f" $watched_paths; do
    echo "Deleting $SELF_DIR/kaggle/ $SELF_DIR/kaggle/"
    rm -rf $SELF_DIR/kaggle/*
    generate-package
    run-autogen
    copy-src
    echo -e "\nWatching for changes to Swagger config..."
  done
}

function watch-src {
  local watched_paths="$SELF_DIR/src"

  echo "Watching for changes under \"src\"..."
  while inotifywait -q -r $WATCHED_EVENTS --format "%e %w%f" $watched_paths; do
    # Do not delete the output directory when there is no Swagger change to avoid
    # having to run generate-package for each small code change as Swagger code
    # generation is a bit slow (can take 2-3 seconds).
    echo "Copying changes..."
    copy-src
    echo "Done!"
    echo -e "\nWatching for changes under \"src\"..."
  done
}

function watch {
  # Run once and wait for changes.
  run
  # Disable --editable for the following runs as it is enough to do --editable once and modify under the
  # "src" folder files which will be then copied to the "kaggle" folder by "run" below on file changes.
  INSTALL_EDITABLE="no"
  INSTALL="no"
  TEST="no"

  echo
  watch-swagger &
  local pid=$!
  watch-src
  wait $pid
}

init

if [[ "$WATCH" == "yes" ]]; then
  watch
else
  run
fi
