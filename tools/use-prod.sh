# Source this file to run Kaggle Api V1 against https://www.kaggle.com.

if [[ "$0" == "$BASH_SOURCE" ]]; then
  echo -e "Source this file to run kaggle api cli against prod:\n"
  echo "$ source use-prod.sh"
  echo
  exit 1
fi

unset KAGGLE_API_ENDPOINT
unset KAGGLE_CONFIG_DIR

if ! [[ -f ~/.kaggle/kaggle.json ]]; then
  echo "Warning: Please download an API token at https://www.kaggle.com/settings and"
  echo "copy it to home directory to run the client against prod."
  echo
else
  chmod 600 ~/.kaggle/kaggle.json
fi