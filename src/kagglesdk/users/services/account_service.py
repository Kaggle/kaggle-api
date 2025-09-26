from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.account_service import ExpireApiTokenRequest, GenerateAccessTokenRequest, GenerateAccessTokenResponse

class AccountClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def expire_api_token(self, request: ExpireApiTokenRequest = None):
    r"""
    Args:
      request (ExpireApiTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ExpireApiTokenRequest()

    self._client.call("users.AccountService", "ExpireApiToken", request, None)

  def generate_access_token(self, request: GenerateAccessTokenRequest = None) -> GenerateAccessTokenResponse:
    r"""
    Args:
      request (GenerateAccessTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GenerateAccessTokenRequest()

    return self._client.call("users.AccountService", "GenerateAccessToken", request, GenerateAccessTokenResponse)
