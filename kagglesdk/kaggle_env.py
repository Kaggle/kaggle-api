import os
from enum import Enum


class KaggleEnv(Enum):
  LOCAL = 0  # localhost
  STAGING = 1  # staging.kaggle.com
  ADMIN = 2  # admin.kaggle.com
  QA = 3 # qa.kaggle.com
  # Direct prod access is not allowed to have IAP protection during testing, but we support basic auth.
  PROD = 4  # www.kaggle.com


_env_to_endpoint = {
  KaggleEnv.LOCAL: 'http://localhost',
  KaggleEnv.STAGING: 'https://staging.kaggle.com',
  KaggleEnv.ADMIN: 'https://admin.kaggle.com',
  KaggleEnv.QA: 'https://qa.kaggle.com',
  # See the comment above in KaggleEnv enum.
  KaggleEnv.PROD: "https://www.kaggle.com",
}


def get_endpoint(env: KaggleEnv):
  return _env_to_endpoint[env]


def get_env():
  env = os.getenv('KAGGLE_API_ENVIRONMENT')
  if env is None:
    raise Exception('Must specify KaggleEnv or set KAGGLE_API_ENVIRONMENT env var')
  if env == 'LOCALHOST':
    return KaggleEnv.LOCAL
  if env == 'ADMIN':
    return KaggleEnv.ADMIN
  if env == 'STAGING':
    return KaggleEnv.STAGING
  if env == 'QA':
    return KaggleEnv.QA
  if env == 'PROD':
    return KaggleEnv.PROD
  raise Exception(f'Unrecognized value in KAGGLE_API_ENVIRONMENT: "{env}"')
