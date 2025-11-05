from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.group_api_service import ApiListSynchronizedGroupMembershipsRequest, ApiListSynchronizedGroupMembershipsResponse, ApiListUserManagedGroupMembershipsRequest, ApiListUserManagedGroupMembershipsResponse

class GroupApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_user_managed_group_memberships(self, request: ApiListUserManagedGroupMembershipsRequest = None) -> ApiListUserManagedGroupMembershipsResponse:
    r"""
    Args:
      request (ApiListUserManagedGroupMembershipsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListUserManagedGroupMembershipsRequest()

    return self._client.call("users.GroupApiService", "ListUserManagedGroupMemberships", request, ApiListUserManagedGroupMembershipsResponse)

  def list_synchronized_group_memberships(self, request: ApiListSynchronizedGroupMembershipsRequest = None) -> ApiListSynchronizedGroupMembershipsResponse:
    r"""
    Args:
      request (ApiListSynchronizedGroupMembershipsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListSynchronizedGroupMembershipsRequest()

    return self._client.call("users.GroupApiService", "ListSynchronizedGroupMemberships", request, ApiListSynchronizedGroupMembershipsResponse)
