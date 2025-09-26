import json
import os
from datetime import datetime, timedelta, timezone
from kagglesdk.kaggle_client import KaggleClient
from kagglesdk.security.types.oauth_service import IntrospectTokenRequest
from kagglesdk.users.types.account_service import (
    ApiVersion,
    GenerateAccessTokenRequest,
    GenerateAccessTokenResponse,
    ExpireApiTokenRequest,
)


class KaggleCredentials:
    DEFAULT_CREDENTIALS_FILE = "~/.kaggle/credentials.json"
    DEFAULT_ACCESS_TOKEN_EXPIRATION = timedelta(hours=12)

    def __init__(
        self,
        client: KaggleClient,
        refresh_token: str = None,
        access_token: str = None,
        access_token_expiration: datetime = None,
        username: str = None,
        scopes: list[str] = None,
    ):
        self._client = client
        self._refresh_token = refresh_token
        self._access_token = access_token
        self._access_token_expiration = access_token_expiration
        self._username = username
        self._scopes = scopes if scopes is not None else []

    @classmethod
    def load(cls, client: KaggleClient, file_path: str = None) -> "KaggleCredentials":
        file_path = os.path.expanduser(file_path or KaggleCredentials.DEFAULT_CREDENTIALS_FILE)
        if not os.path.exists(file_path):
            return None

        try:
            with open(file_path, "r") as f:
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
            scopes=data.get("scopes"),
        )

    def delete(self, file_path=DEFAULT_CREDENTIALS_FILE) -> None:
        file_path = os.path.expanduser(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)

    def save(self, file_path=DEFAULT_CREDENTIALS_FILE) -> None:
        if not self._refresh_token:
            raise Exception("Missing refresh token")

        file_path = os.path.expanduser(file_path)
        dir_name = os.path.dirname(file_path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        data = {
            "refresh_token": self._refresh_token,
            "access_token": self._access_token or "",
            "access_token_expiration": (
                self._access_token_expiration.isoformat() if self._access_token_expiration else ""
            ),
            "username": self._username or "",
            "scopes": self._scopes or [],
        }

        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)

        try:
            os.chmod(file_path, 0o600)
        except OSError:
            pass  # Ignore errors, especially on Windows

    def introspect(self) -> str:
        request = IntrospectTokenRequest()
        request.token = self._access_token
        response = self._client.security.oauth_client.introspect_token(request)

        if not response.active or not response.username:
            raise Exception("Authentication failed.")

        self._username = response.username
        return response.username

    def refresh_access_token(self) -> None:
        if not self._refresh_token:
            raise Exception("Missing refresh token")

        response = self.generate_access_token()
        self._access_token_expiration = datetime.now(timezone.utc) + timedelta(seconds=response.expires_in)
        self._access_token = response.token
        self.save()

    def access_token_has_expired(self) -> bool:
        return not self._access_token_expiration or self._access_token_expiration < datetime.now(
            timezone.utc
        ) - timedelta(minutes=30)

    def get_access_token(self) -> str:
        if not self._access_token or self.access_token_has_expired():
            if not self._refresh_token:
                return None
            self.refresh_access_token()
        return self._access_token

    def generate_access_token(self, expiration_duration: timedelta = None) -> GenerateAccessTokenResponse:
        if not self._refresh_token:
            return None
        request = GenerateAccessTokenRequest()
        request.refresh_token = self._refresh_token
        request.api_version = ApiVersion.API_VERSION_V1
        request.expiration_duration = expiration_duration or KaggleCredentials.DEFAULT_ACCESS_TOKEN_EXPIRATION
        return self._client.users.account_client.generate_access_token(request)

    def revoke_token(self, reason: str) -> None:
        if not self._refresh_token:
            return
        request = ExpireApiTokenRequest()
        request.token = self._refresh_token
        request.reason = reason
        self._client.users.account_client.expire_api_token(request)
        self.delete()

    def get_username(self) -> str:
        return self._username
