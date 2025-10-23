from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.security.types.iam_service import GetIamPolicyRequest, IamPolicy, SetIamPolicyRequest

class IamClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_iam_policy(self, request: GetIamPolicyRequest = None) -> IamPolicy:
    r"""
    Args:
      request (GetIamPolicyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetIamPolicyRequest()

    return self._client.call("security.IamService", "GetIamPolicy", request, IamPolicy)

  def set_iam_policy(self, request: SetIamPolicyRequest = None) -> IamPolicy:
    r"""
    Args:
      request (SetIamPolicyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetIamPolicyRequest()

    return self._client.call("security.IamService", "SetIamPolicy", request, IamPolicy)
