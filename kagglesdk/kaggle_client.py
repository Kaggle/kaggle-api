from kagglesdk.kernels.services.kernels_api_service import KernelsApiClient
from kagglesdk.models.services.model_api_service import ModelApiClient
from kagglesdk.models.services.model_service import ModelClient
from kagglesdk.competitions.services.competition_api_service import CompetitionApiClient
from kagglesdk.datasets.services.dataset_api_service import DatasetApiClient
from kagglesdk.kaggle_env import KaggleEnv
from kagglesdk.kaggle_http_client import KaggleHttpClient


class KaggleClient(object):
  class Kernels(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.kernels_api_client = KernelsApiClient(http_client)

  class Models(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.model_api_client = ModelApiClient(http_client)
      self.model_client = ModelClient(http_client)

  class Competitions(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.competition_api_client = CompetitionApiClient(http_client)

  class Datasets(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.dataset_api_client = DatasetApiClient(http_client)

  def __init__(self, env: KaggleEnv = None, verbose: bool = False, username: str = None, password: str = None):
    self._http_client = http_client = KaggleHttpClient(env, verbose, self._renew_iap_token, username=username, password=password)
    self.kernels = KaggleClient.Kernels(http_client)
    self.models = KaggleClient.Models(http_client)
    self.competitions = KaggleClient.Competitions(http_client)
    self.datasets = KaggleClient.Datasets(http_client)
    self.username = username
    self.password = password

  def _renew_iap_token(self):
    return self.admin.admin_client.renew_iap_token()

  def __enter__(self):
    self._http_client.__enter__()
    return self

  def __exit__(self, exc_type, exc_value, tb):
    self._http_client.__exit__(exc_type, exc_value, tb)
