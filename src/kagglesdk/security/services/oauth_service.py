from kagglesdk.common.types.http_redirect import HttpRedirect
from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.security.types.oauth_service import ExchangeOAuthTokenRequest, ExchangeOAuthTokenResponse, IntrospectTokenRequest, IntrospectTokenResponse, RegisterOAuthClientRequest, RegisterOAuthClientResponse, StartOAuthFlowRequest

class OAuthClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def start_oauth_flow(self, request: StartOAuthFlowRequest = None) -> HttpRedirect:
    r"""
    Args:
      request (StartOAuthFlowRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = StartOAuthFlowRequest()

    return self._client.call("security.OAuthService", "StartOAuthFlow", request, HttpRedirect)

  def exchange_oauth_token(self, request: ExchangeOAuthTokenRequest = None) -> ExchangeOAuthTokenResponse:
    r"""
    Args:
      request (ExchangeOAuthTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ExchangeOAuthTokenRequest()

    return self._client.call("security.OAuthService", "ExchangeOAuthToken", request, ExchangeOAuthTokenResponse)

  def introspect_token(self, request: IntrospectTokenRequest = None) -> IntrospectTokenResponse:
    r"""
    Args:
      request (IntrospectTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = IntrospectTokenRequest()

    return self._client.call("security.OAuthService", "IntrospectToken", request, IntrospectTokenResponse)

  def register_oauth_client(self, request: RegisterOAuthClientRequest = None) -> RegisterOAuthClientResponse:
    r"""
    Dynamic Client Registration Endpoint (RFC 7591)

    Args:
      request (RegisterOAuthClientRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RegisterOAuthClientRequest()

    return self._client.call("security.OAuthService", "RegisterOAuthClient", request, RegisterOAuthClientResponse)
