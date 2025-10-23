from kagglesdk.benchmarks.types.benchmarks_api_service import ApiBenchmarkLeaderboard, ApiGetBenchmarkLeaderboardRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BenchmarksApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_benchmark_leaderboard(self, request: ApiGetBenchmarkLeaderboardRequest = None) -> ApiBenchmarkLeaderboard:
    r"""
    Args:
      request (ApiGetBenchmarkLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetBenchmarkLeaderboardRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "GetBenchmarkLeaderboard", request, ApiBenchmarkLeaderboard)
