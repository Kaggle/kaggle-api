# Source this file to run Kaggle Api V1 against http://localhost.

if [[ "$0" == "$BASH_SOURCE" ]]; then
  echo -e "Source this file to run kaggle api cli against localhost:\n"
  echo "$ source use-localhost.sh"
  echo
  exit 1
fi

export KAGGLE_API_ENDPOINT=http://localhost
export KAGGLE_CONFIG_DIR=$(realpath "${XDG_CONFIG_HOME:-$HOME/.config}/kaggle/dev")

KAGGLE_CONFIG_FILE="$KAGGLE_CONFIG_DIR/kaggle.json"
if ! [[ -f "$KAGGLE_CONFIG_FILE" ]]; then
  # Generate a separate dev credentials file (kaggle.json) to use when running against
  # http://localhost. This token only works when the webtier is running locally in debug
  # mode. When running against localhost, we set KAGGLE_CONFIG_DIR env var to
  # "~/.config/kaggle/dev/" so that the Python client searches for kaggle.json under this folder
  # and uses dummy dev creds
  
  mkdir -p $KAGGLE_CONFIG_DIR
  username=${KAGGLE_DEVELOPER:-$USER}
  echo "Creating a dev credentials file (kaggle.json)..."
  echo "{\"username\":\"$username\",\"key\":\"local_api_token\"}" > $KAGGLE_CONFIG_FILE
  chmod 600 $KAGGLE_CONFIG_FILE
  echo "dev credentials created for username '$username'."
  echo "PLEASE VERIFY this matches your Kaggle username!"
  echo "If not, update the $KAGGLE_CONFIG_DIR/kaggle.json file manually to set your Kaggle username. You will only need to do this once."
fi
