import json
import os
from datetime import datetime, timedelta
from kagglesdk.kaggle_client import KaggleClient
from kagglesdk.security.types.oauth_service import IntrospectTokenRequest
from kagglesdk.users.types.account_service import ApiVersion, GenerateAccessTokenRequest

DEFAULT_CREDENTIALS_FILE = "~/.kaggle/credentials.json"

class KaggleCredentials:
  def __init__(self,
               client: KaggleClient,
               refresh_token:str = None,
               access_token:str = None,
               access_token_expiration:datetime = None,
               username:str = None,
               scopes: list[str]=None):
    self._client = client
    self._refresh_token = refresh_token
    self._access_token = access_token
    self._access_token_expiration = access_token_expiration
    self._username = username
    self._scopes = scopes if scopes is not None else []

  @classmethod
  def load(cls, client: KaggleClient, file_path:str = DEFAULT_CREDENTIALS_FILE):
    file_path = os.path.expanduser(file_path)
    if not os.path.exists(file_path):
      return None

    try:
      with open(file_path, 'r') as f:
        data = json.load(f)
    except (json.JSONDecodeError, KeyError):
      return None

    refresh_token = data.get("refresh_token")
    if not refresh_token:
      return None
    
    access_token_expiration = data.get("access_token_expiration")
    if access_token_expiration:
      access_token_expiration = datetime.fromisoformat(access_token_expiration)
    else:
      access_token_expiration = None

    return cls(
      client=client,
      refresh_token=refresh_token,
      access_token=data.get("access_token"),
      access_token_expiration=access_token_expiration,
      username=data.get("username"),
      scopes=data.get("scopes")
    )

  def save(self, file_path=DEFAULT_CREDENTIALS_FILE):
    if not self._refresh_token:
      raise Exception("Missing refresh token")
    
    file_path = os.path.expanduser(file_path)
    dir_name = os.path.dirname(file_path)
    if not os.path.exists(dir_name):
      os.makedirs(dir_name)

    data = {
      "refresh_token": self._refresh_token,
      "access_token": self._access_token or "",
      "access_token_expiration": self._access_token_expiration.isoformat() if self._access_token_expiration else "",
      "username": self._username or "",
      "scopes": self._scopes or []
    }

    with open(file_path, 'w') as f:
      json.dump(data, f, indent=2)

    try:
      os.chmod(file_path, 0o600)
    except OSError:
      pass  # Ignore errors, especially on Windows

  def introspect(self):
    request = IntrospectTokenRequest()
    request.token = self._access_token
    response = self._client.security.oauth_client.introspect_token(request)

    if not response.active or not response.username:
      raise Exception("Authentication failed.")

    self._username = response.username
    return response.username

  def refresh_access_token(self):
    if not self._refresh_token:
      raise Exception("Missing refresh token")

    request = GenerateAccessTokenRequest()
    request.refresh_token = self._refresh_token
    request.api_version = ApiVersion.API_VERSION_V1
    request.expiration_duration = timedelta(hours=12)
    response = self._client.users.account_client.generate_access_token(request)

    access_token_expires_in = request.expiration_duration.total_seconds()
    self._access_token_expiration = datetime.now(datetime.timezone.utc) + timedelta(seconds=access_token_expires_in)
    self._access_token = response.token
    self.save()
  
  def access_token_has_expired(self):
    return self._access_token_expiration > datetime.new(datetime.timezone.utc) + timedelta(minutes=30)

  def get_access_token(self):
    if not self._access_token or self.access_token_has_expired():
      if not self._refresh_token:
        return None
      self.refresh_access_token()
    return self._access_token
  
  def get_username(self):
    return self._username
