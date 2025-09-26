from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.search.types.search_api_service import ListEntitiesRequest, ListEntitiesResponse

class SearchApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_entities(self, request: ListEntitiesRequest = None) -> ListEntitiesResponse:
    r"""
    Args:
      request (ListEntitiesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListEntitiesRequest()

    return self._client.call("search.SearchApiService", "ListEntities", request, ListEntitiesResponse)
