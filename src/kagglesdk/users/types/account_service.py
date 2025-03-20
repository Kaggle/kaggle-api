from datetime import timedelta
import enum
from kagglesdk.kaggle_object import *
from kagglesdk.security.types.authentication import AuthorizationScope
from typing import Optional, List

class ApiVersion(enum.Enum):
  API_VERSION_UNSPECIFIED = 0
  API_VERSION_V1 = 1
  """Publicly available ('/api/v1' endpoints)."""
  API_VERSION_V2 = 2
  """Experimental, admin-only, internal ('/api/i' endpoints)."""

class GenerateAccessTokenRequest(KaggleObject):
  r"""
  Attributes:
    refresh_token (str)
      Refresh token used to generate a short-lived restricted access token.
      If not specified current user credentials will be used to generate an
      unrestricted access token.
    api_version (ApiVersion)
      Version of the Kaggle API for which this token will be used.
    expiration_duration (timedelta)
      Token expiration.
    authorization_context (AuthorizationContext)
      On which context (such as a Kaggle notebook) this token can be used.
    authorization_scopes (AuthorizationScope)
      Set of scopes to further restrict the token. If 'refresh_token' is
      specified, these should be a subset of the scopes allowed by the
      'refresh_token'.
  """

  def __init__(self):
    self._refresh_token = None
    self._api_version = ApiVersion.API_VERSION_UNSPECIFIED
    self._expiration_duration = None
    self._authorization_context = None
    self._authorization_scopes = []
    self._freeze()

  @property
  def refresh_token(self) -> str:
    r"""
    Refresh token used to generate a short-lived restricted access token.
    If not specified current user credentials will be used to generate an
    unrestricted access token.
    """
    return self._refresh_token or ""

  @refresh_token.setter
  def refresh_token(self, refresh_token: str):
    if refresh_token is None:
      del self.refresh_token
      return
    if not isinstance(refresh_token, str):
      raise TypeError('refresh_token must be of type str')
    self._refresh_token = refresh_token

  @property
  def api_version(self) -> 'ApiVersion':
    """Version of the Kaggle API for which this token will be used."""
    return self._api_version

  @api_version.setter
  def api_version(self, api_version: 'ApiVersion'):
    if api_version is None:
      del self.api_version
      return
    if not isinstance(api_version, ApiVersion):
      raise TypeError('api_version must be of type ApiVersion')
    self._api_version = api_version

  @property
  def expiration_duration(self) -> timedelta:
    """Token expiration."""
    return self._expiration_duration

  @expiration_duration.setter
  def expiration_duration(self, expiration_duration: timedelta):
    if expiration_duration is None:
      del self.expiration_duration
      return
    if not isinstance(expiration_duration, timedelta):
      raise TypeError('expiration_duration must be of type timedelta')
    self._expiration_duration = expiration_duration

  @property
  def authorization_context(self) -> Optional['AuthorizationContext']:
    """On which context (such as a Kaggle notebook) this token can be used."""
    return self._authorization_context

  @authorization_context.setter
  def authorization_context(self, authorization_context: Optional['AuthorizationContext']):
    if authorization_context is None:
      del self.authorization_context
      return
    if not isinstance(authorization_context, AuthorizationContext):
      raise TypeError('authorization_context must be of type AuthorizationContext')
    self._authorization_context = authorization_context

  @property
  def authorization_scopes(self) -> Optional[List[Optional['AuthorizationScope']]]:
    r"""
    Set of scopes to further restrict the token. If 'refresh_token' is
    specified, these should be a subset of the scopes allowed by the
    'refresh_token'.
    """
    return self._authorization_scopes

  @authorization_scopes.setter
  def authorization_scopes(self, authorization_scopes: Optional[List[Optional['AuthorizationScope']]]):
    if authorization_scopes is None:
      del self.authorization_scopes
      return
    if not isinstance(authorization_scopes, list):
      raise TypeError('authorization_scopes must be of type list')
    if not all([isinstance(t, AuthorizationScope) for t in authorization_scopes]):
      raise TypeError('authorization_scopes must contain only items of type AuthorizationScope')
    self._authorization_scopes = authorization_scopes

  def endpoint(self):
    path = '/api/v1/access-tokens/generate'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class GenerateAccessTokenResponse(KaggleObject):
  r"""
  Attributes:
    token (str)
  """

  def __init__(self):
    self._token = ""
    self._freeze()

  @property
  def token(self) -> str:
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token


class AuthorizationContext(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
      If set, access token is restricted to be used only from the specified
      notebook session.
  """

  def __init__(self):
    self._kernel_session_id = None
    self._freeze()

  @property
  def kernel_session_id(self) -> int:
    r"""
    If set, access token is restricted to be used only from the specified
    notebook session.
    """
    return self._kernel_session_id or 0

  @kernel_session_id.setter
  def kernel_session_id(self, kernel_session_id: int):
    if kernel_session_id is None:
      del self.kernel_session_id
      return
    if not isinstance(kernel_session_id, int):
      raise TypeError('kernel_session_id must be of type int')
    self._kernel_session_id = kernel_session_id


GenerateAccessTokenRequest._fields = [
  FieldMetadata("refreshToken", "refresh_token", "_refresh_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("apiVersion", "api_version", "_api_version", ApiVersion, ApiVersion.API_VERSION_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("expirationDuration", "expiration_duration", "_expiration_duration", timedelta, None, TimeDeltaSerializer()),
  FieldMetadata("authorizationContext", "authorization_context", "_authorization_context", AuthorizationContext, None, KaggleObjectSerializer()),
  FieldMetadata("authorizationScopes", "authorization_scopes", "_authorization_scopes", AuthorizationScope, [], ListSerializer(KaggleObjectSerializer())),
]

GenerateAccessTokenResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
]

AuthorizationContext._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, None, PredefinedSerializer(), optional=True),
]

