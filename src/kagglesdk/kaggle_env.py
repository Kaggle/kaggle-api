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
    # Direct prod access is not allowed to have IAP protection during testing, but we support basic auth.
    PROD = 4  # www.kaggle.com


_env_to_endpoint = {
    KaggleEnv.LOCAL: "http://localhost",
    KaggleEnv.STAGING: "https://staging.kaggle.com",
    KaggleEnv.ADMIN: "https://admin.kaggle.com",
    KaggleEnv.QA: "https://qa.kaggle.com",
    # See the comment above in KaggleEnv enum.
    KaggleEnv.PROD: "https://www.kaggle.com",
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
        return (None, None)

    token_path = Path(path)
    if not token_path.exists():
        return (None, None)

    token_value = token_path.read_text().strip()
    if not token_value:
        return (None, None)

    get_logger().debug(f'Using access token from file: "{path}"')
    return (token_value, path)


def get_access_token_from_env():
    if is_in_kaggle_notebook():
        token = _get_access_token_from_file(os.environ.get(KAGGLE_API_V1_TOKEN_PATH))
        if token:
            return (token, KAGGLE_API_V1_TOKEN_PATH)

    access_token = os.environ.get("KAGGLE_API_TOKEN")
    if access_token is not None:
        get_logger().debug("Using access token from KAGGLE_API_TOKEN environment variable")
        return (access_token, "KAGGLE_API_TOKEN")

    return (None, None)
