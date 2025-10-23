from kagglesdk.admin.services.inbox_file_service import InboxFileClient
from kagglesdk.benchmarks.services.benchmarks_api_service import BenchmarksApiClient
from kagglesdk.blobs.services.blob_api_service import BlobApiClient
from kagglesdk.common.services.operations_service import OperationsClient
from kagglesdk.competitions.services.competition_api_service import CompetitionApiClient
from kagglesdk.datasets.services.dataset_api_service import DatasetApiClient
from kagglesdk.education.services.education_api_service import EducationApiClient
from kagglesdk.kernels.services.kernels_api_service import KernelsApiClient
from kagglesdk.models.services.model_api_service import ModelApiClient
from kagglesdk.models.services.model_service import ModelClient
from kagglesdk.search.services.search_api_service import SearchApiClient
from kagglesdk.security.services.iam_service import IamClient
from kagglesdk.security.services.oauth_service import OAuthClient
from kagglesdk.users.services.account_service import AccountClient
from kagglesdk.users.services.group_api_service import GroupApiClient
from kagglesdk.kaggle_env import KaggleEnv
from kagglesdk.kaggle_http_client import KaggleHttpClient


class KaggleClient(object):
  class Admin(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.inbox_file_client = InboxFileClient(http_client)

  class Benchmarks(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.benchmarks_api_client = BenchmarksApiClient(http_client)

  class Blobs(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.blob_api_client = BlobApiClient(http_client)

  class Common(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.operations_client = OperationsClient(http_client)

  class Competitions(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.competition_api_client = CompetitionApiClient(http_client)

  class Datasets(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.dataset_api_client = DatasetApiClient(http_client)

  class Education(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.education_api_client = EducationApiClient(http_client)

  class Kernels(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.kernels_api_client = KernelsApiClient(http_client)

  class Models(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.model_api_client = ModelApiClient(http_client)
      self.model_client = ModelClient(http_client)

  class Search(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.search_api_client = SearchApiClient(http_client)

  class Security(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.iam_client = IamClient(http_client)
      self.oauth_client = OAuthClient(http_client)

  class Users(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.account_client = AccountClient(http_client)
      self.group_api_client = GroupApiClient(http_client)

  def __init__(self, env: KaggleEnv = None, verbose: bool = False, username: str = None, password: str = None, api_token: str = None):
    self._http_client = http_client = KaggleHttpClient(env, verbose, username=username, password=password, api_token=api_token)
    self.admin = KaggleClient.Admin(http_client)
    self.benchmarks = KaggleClient.Benchmarks(http_client)
    self.blobs = KaggleClient.Blobs(http_client)
    self.common = KaggleClient.Common(http_client)
    self.competitions = KaggleClient.Competitions(http_client)
    self.datasets = KaggleClient.Datasets(http_client)
    self.education = KaggleClient.Education(http_client)
    self.kernels = KaggleClient.Kernels(http_client)
    self.models = KaggleClient.Models(http_client)
    self.search = KaggleClient.Search(http_client)
    self.security = KaggleClient.Security(http_client)
    self.users = KaggleClient.Users(http_client)
    self.username = username
    self.password = password
    self.api_token = api_token

  def http_client(self) -> str:
    return self._http_client

  def _renew_iap_token(self) -> str:
    return self.admin.admin_client.renew_iap_token()

  def __enter__(self):
    self._http_client.__enter__()
    return self

  def __exit__(self, exc_type, exc_value, tb):
    self._http_client.__exit__(exc_type, exc_value, tb)
