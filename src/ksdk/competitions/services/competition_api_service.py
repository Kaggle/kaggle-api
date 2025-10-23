from kagglesdk.common.types.file_download import FileDownload
from kagglesdk.common.types.http_redirect import HttpRedirect
from kagglesdk.competitions.types.competition_api_service import ApiCompetition, ApiCreateCodeSubmissionRequest, ApiCreateCodeSubmissionResponse, ApiCreateSubmissionRequest, ApiCreateSubmissionResponse, ApiDownloadDataFileRequest, ApiDownloadDataFilesRequest, ApiDownloadLeaderboardRequest, ApiGetCompetitionDataFilesSummaryRequest, ApiGetCompetitionRequest, ApiGetLeaderboardRequest, ApiGetLeaderboardResponse, ApiGetSubmissionRequest, ApiListCompetitionsRequest, ApiListCompetitionsResponse, ApiListDataFilesRequest, ApiListDataFilesResponse, ApiListDataTreeFilesRequest, ApiListSubmissionsRequest, ApiListSubmissionsResponse, ApiStartSubmissionUploadRequest, ApiStartSubmissionUploadResponse, ApiSubmission
from kagglesdk.datasets.databundles.types.databundle_api_types import ApiDirectoryContent, ApiFilesSummary
from kagglesdk.kaggle_http_client import KaggleHttpClient

class CompetitionApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_competitions(self, request: ApiListCompetitionsRequest = None) -> ApiListCompetitionsResponse:
    r"""
    Args:
      request (ApiListCompetitionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListCompetitionsRequest()

    return self._client.call("competitions.CompetitionApiService", "ListCompetitions", request, ApiListCompetitionsResponse)

  def list_submissions(self, request: ApiListSubmissionsRequest = None) -> ApiListSubmissionsResponse:
    r"""
    Args:
      request (ApiListSubmissionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListSubmissionsRequest()

    return self._client.call("competitions.CompetitionApiService", "ListSubmissions", request, ApiListSubmissionsResponse)

  def list_data_files(self, request: ApiListDataFilesRequest = None) -> ApiListDataFilesResponse:
    r"""
    Args:
      request (ApiListDataFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListDataFilesRequest()

    return self._client.call("competitions.CompetitionApiService", "ListDataFiles", request, ApiListDataFilesResponse)

  def list_data_tree_files(self, request: ApiListDataTreeFilesRequest = None) -> ApiDirectoryContent:
    r"""
    Args:
      request (ApiListDataTreeFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListDataTreeFilesRequest()

    return self._client.call("competitions.CompetitionApiService", "ListDataTreeFiles", request, ApiDirectoryContent)

  def get_leaderboard(self, request: ApiGetLeaderboardRequest = None) -> ApiGetLeaderboardResponse:
    r"""
    Args:
      request (ApiGetLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetLeaderboardRequest()

    return self._client.call("competitions.CompetitionApiService", "GetLeaderboard", request, ApiGetLeaderboardResponse)

  def download_leaderboard(self, request: ApiDownloadLeaderboardRequest = None) -> FileDownload:
    r"""
    Args:
      request (ApiDownloadLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadLeaderboardRequest()

    return self._client.call("competitions.CompetitionApiService", "DownloadLeaderboard", request, FileDownload)

  def create_submission(self, request: ApiCreateSubmissionRequest = None) -> ApiCreateSubmissionResponse:
    r"""
    Args:
      request (ApiCreateSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateSubmissionRequest()

    return self._client.call("competitions.CompetitionApiService", "CreateSubmission", request, ApiCreateSubmissionResponse)

  def create_code_submission(self, request: ApiCreateCodeSubmissionRequest = None) -> ApiCreateCodeSubmissionResponse:
    r"""
    Args:
      request (ApiCreateCodeSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateCodeSubmissionRequest()

    return self._client.call("competitions.CompetitionApiService", "CreateCodeSubmission", request, ApiCreateCodeSubmissionResponse)

  def get_submission(self, request: ApiGetSubmissionRequest = None) -> ApiSubmission:
    r"""
    Args:
      request (ApiGetSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetSubmissionRequest()

    return self._client.call("competitions.CompetitionApiService", "GetSubmission", request, ApiSubmission)

  def start_submission_upload(self, request: ApiStartSubmissionUploadRequest = None) -> ApiStartSubmissionUploadResponse:
    r"""
    Args:
      request (ApiStartSubmissionUploadRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiStartSubmissionUploadRequest()

    return self._client.call("competitions.CompetitionApiService", "StartSubmissionUpload", request, ApiStartSubmissionUploadResponse)

  def download_data_files(self, request: ApiDownloadDataFilesRequest = None) -> HttpRedirect:
    r"""
    Args:
      request (ApiDownloadDataFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadDataFilesRequest()

    return self._client.call("competitions.CompetitionApiService", "DownloadDataFiles", request, HttpRedirect)

  def download_data_file(self, request: ApiDownloadDataFileRequest = None) -> HttpRedirect:
    r"""
    Args:
      request (ApiDownloadDataFileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadDataFileRequest()

    return self._client.call("competitions.CompetitionApiService", "DownloadDataFile", request, HttpRedirect)

  def get_competition(self, request: ApiGetCompetitionRequest = None) -> ApiCompetition:
    r"""
    Args:
      request (ApiGetCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetCompetitionRequest()

    return self._client.call("competitions.CompetitionApiService", "GetCompetition", request, ApiCompetition)

  def get_competition_data_files_summary(self, request: ApiGetCompetitionDataFilesSummaryRequest = None) -> ApiFilesSummary:
    r"""
    Args:
      request (ApiGetCompetitionDataFilesSummaryRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetCompetitionDataFilesSummaryRequest()

    return self._client.call("competitions.CompetitionApiService", "GetCompetitionDataFilesSummary", request, ApiFilesSummary)
