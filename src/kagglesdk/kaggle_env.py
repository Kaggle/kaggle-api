import logging
import os
from enum import Enum
from pathlib import Path

KAGGLE_NOTEBOOK_ENV_VAR_NAME = "KAGGLE_KERNEL_RUN_TYPE"
KAGGLE_DATA_PROXY_URL_ENV_VAR_NAME = "KAGGLE_DATA_PROXY_URL"
KAGGLE_API_V1_TOKEN_PATH = "KAGGLE_API_V1_TOKEN"


def get_logger():
    return logging.getLogger(__name__)


class KaggleEnv(Enum):
    LOCAL = 0  # localhost
    STAGING = 1  # staging.kaggle.com
    ADMIN = 2  # admin.kaggle.com
    QA = 3  # qa.kaggle.com
    PROD = 4  # api.kaggle.com


_env_to_endpoint = {
    KaggleEnv.LOCAL: "http://localhost",
    KaggleEnv.STAGING: "https://staging.kaggle.com",
    KaggleEnv.ADMIN: "https://admin.kaggle.com",
    KaggleEnv.QA: "https://qa.kaggle.com",
    KaggleEnv.PROD: "https://api.kaggle.com",
}


def get_endpoint(env: KaggleEnv):
    return _env_to_endpoint[env]


def get_env():
    env = os.getenv("KAGGLE_API_ENVIRONMENT")
    if env is None or env == "PROD":
        return KaggleEnv.PROD
    if env == "LOCALHOST":
        return KaggleEnv.LOCAL
    if env == "ADMIN":
        return KaggleEnv.ADMIN
    if env == "STAGING":
        return KaggleEnv.STAGING
    if env == "QA":
        return KaggleEnv.QA
    raise Exception(f'Unrecognized value in KAGGLE_API_ENVIRONMENT: "{env}"')


def is_in_kaggle_notebook() -> bool:
    if os.getenv(KAGGLE_NOTEBOOK_ENV_VAR_NAME) is not None:
        if os.getenv(KAGGLE_DATA_PROXY_URL_ENV_VAR_NAME) is None:
            # Missing endpoint for the Jwt client
            get_logger().warning(
                "Can't use the Kaggle Cache. "
                f"The '{KAGGLE_DATA_PROXY_URL_ENV_VAR_NAME}' environment variable is not set."
            )
            return False
        return True
    return False


def _get_access_token_from_file(path):
    if not path:
        return None

    token_path = Path(path)
    if not token_path.exists():
        return None

    token_value = token_path.read_text().strip()
    if not token_value:
        return None

    get_logger().debug(f'Using access token from file: "{path}"')
    return token_value


def get_access_token_from_env():
    if is_in_kaggle_notebook():
        token = _get_access_token_from_file(os.environ.get(KAGGLE_API_V1_TOKEN_PATH))
        if token:
            return (token, KAGGLE_API_V1_TOKEN_PATH)

    access_token = os.environ.get("KAGGLE_API_TOKEN")
    if access_token:
        if Path(access_token).exists():
            return (_get_access_token_from_file(access_token), "KAGGLE_API_TOKEN")
        get_logger().debug(
            "Using access token from KAGGLE_API_TOKEN environment variable"
        )
        return (access_token, "KAGGLE_API_TOKEN")

    access_token = _get_access_token_from_file(os.path.expanduser("~/.kaggle/access_token"))
    if access_token:
        return (access_token, "access_token")

    # Check ".txt" as well in case Windows users create the file with this extension.
    access_token = _get_access_token_from_file(os.path.expanduser("~/.kaggle/access_token.txt"))
    if access_token:
        return (access_token, "access_token")

    return (None, None)
