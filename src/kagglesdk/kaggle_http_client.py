import binascii
import codecs
import json
import os
import urllib.parse
from io import BytesIO
from pathlib import Path

import requests
from urllib3.fields import RequestField

from kagglesdk.kaggle_env import (
    get_endpoint,
    get_env,
    get_access_token_from_env,
    KaggleEnv,
)
from kagglesdk.kaggle_object import KaggleObject
from kagglesdk.common.types.file_download import FileDownload
from kagglesdk.common.types.http_redirect import HttpRedirect
from typing import Type

# TODO (http://b/354237483) Generate the client from the existing one.
# This was created from kaggle_api_client.py, prior to recent changes to
# auth handling. The new client requires KAGGLE_API_TOKEN, so it is not
# currently usable by the CLI.


def _headers_to_str(headers):
    return "\n".join(f"{k}: {v}" for k, v in headers.items())


def _get_apikey_creds():
    apikey_filename = os.path.expanduser("~/.kaggle/kaggle.json")
    if not os.path.exists(apikey_filename):
        return None

    kaggle_json = None
    with open(apikey_filename) as apikey_file:
        kaggle_json = apikey_file.read()

    if not kaggle_json or not kaggle_json.strip():
        return None

    api_key_data = json.loads(kaggle_json)
    username = api_key_data["username"]
    api_key = api_key_data["key"]
    return username, api_key


class KaggleHttpClient(object):
    _xsrf_cookie_name = "XSRF-TOKEN"
    _csrf_cookie_name = "CSRF-TOKEN"
    _xsrf_cookies = (_xsrf_cookie_name, _csrf_cookie_name)
    _xsrf_header_name = "X-XSRF-TOKEN"

    def __init__(
        self,
        env: KaggleEnv = None,
        verbose: bool = False,
        username: str = None,
        password: str = None,
        api_token: str = None,
    ):
        self._env = env or get_env()
        self._signed_in = None
        self._endpoint = get_endpoint(self._env)
        self._verbose = verbose
        self._session = None
        self._username = username
        self._password = password
        self._api_token = api_token

    def call(
        self,
        service_name: str,
        request_name: str,
        request: KaggleObject,
        response_type: Type[KaggleObject],
    ):
        self._init_session()
        http_request = self._prepare_request(service_name, request_name, request)

        # Merge environment settings into session
        settings = self._session.merge_environment_settings(http_request.url, {}, None, None, None)

        # Use stream=True for file downloads to avoid loading entire file into memory
        # See: https://github.com/Kaggle/kaggle-api/issues/754
        if response_type is not None and (response_type == FileDownload or response_type == HttpRedirect):
            settings["stream"] = True

        http_response = self._session.send(http_request, **settings)

        response = self._prepare_response(response_type, http_response)
        return response

    def _prepare_request(self, service_name: str, request_name: str, request: KaggleObject):
        request_url = self._get_request_url(service_name, request_name)
        http_request = requests.Request(
            method="POST",
            url=request_url,
            json=request.__class__.to_dict(request),
            headers=self._session.headers,
            auth=self._session.auth,
        )
        prepared_request = http_request.prepare()
        self._print_request(prepared_request)
        return prepared_request

    def _prepare_response(self, response_type, http_response):
        """Extract the kaggle response and raise an exception if it is an error."""
        self._print_response(http_response)
        try:
            if "application/json" in http_response.headers["Content-Type"]:
                resp = http_response.json()
                if "code" in resp and resp["code"] >= 400:
                    raise requests.exceptions.HTTPError(resp["message"], response=http_response)
        except KeyError:
            pass
        http_response.raise_for_status()
        if response_type is None:  # Method doesn't have a return type
            return None
        return response_type.prepare_from(http_response)

    def _print_request(self, request):
        if not self._verbose:
            return
        self._print("---------------------Request----------------------")
        self._print(f"{request.method} {request.url}\n{_headers_to_str(request.headers)}\n\n{request.body}")
        self._print("--------------------------------------------------")

    def _print_response(self, response, body=True):
        if not self._verbose:
            return
        self._print("---------------------Response---------------------")
        self._print(f"{response.status_code}\n{_headers_to_str(response.headers)}")
        if body:
            self._print(f"\n{response.text}")
        self._print("--------------------------------------------------")

    def _print(self, message: str):
        if self._verbose:
            print(message)

    def __enter__(self):
        self._init_session()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if self._session is not None:
            self._session.close()

    def _init_session(self):
        if self._session is not None:
            return self._session

        self._session = requests.Session()
        self._session.headers.update({"User-Agent": "kaggle-api/v1.8.0", "Content-Type": "application/json"})  # Was: V2

        iap_token = self._get_iap_token_if_required()
        if iap_token is not None:
            self._session.headers.update(
                {
                    # https://cloud.google.com/iap/docs/authentication-howto#authenticating_from_proxy-authorization_header
                    "Proxy-Authorization": f"Bearer {iap_token}",
                }
            )

        self._try_fill_auth()
        # self._fill_xsrf_token(iap_token)  # TODO Make this align with original handler.

    def _get_iap_token_if_required(self):
        if self._env not in (KaggleEnv.STAGING, KaggleEnv.ADMIN):
            return None
        iap_token = os.getenv("KAGGLE_IAP_TOKEN")
        if iap_token is None:
            raise Exception(f'Must set KAGGLE_IAP_TOKEN to access "{self._endpoint}"')
        return iap_token

    def _fill_xsrf_token(self, iap_token):
        initial_get_request = requests.Request(
            method="GET",
            url=self._endpoint,
            headers=self._session.headers,
            auth=self._session.auth,
        )
        prepared_request = initial_get_request.prepare()
        self._print_request(prepared_request)

        http_response = self._session.send(prepared_request)

        self._print_response(http_response, body=False)
        if iap_token is not None and http_response.status_code in (401, 403):
            raise requests.exceptions.HTTPError("IAP token invalid or expired")
        http_response.raise_for_status()

        self._session.headers.update(
            {
                KaggleHttpClient._xsrf_header_name: self._session.cookies[KaggleHttpClient._xsrf_cookie_name],
            }
        )

    def build_start_oauth_url(
        self,
        client_id: str,
        redirect_uri: str,
        scope: list[str],
        state: str,
        code_challenge: str,
    ) -> str:
        params = {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "scope": " ".join(scope),
            "state": state,
            "code_challenge": code_challenge,
            "code_challenge_method": "S256",
            "response_type": "code",
            "response_mode": "query",
        }
        auth_url = f"{self.get_non_api_endpoint()}/api/v1/oauth2/authorize"
        query_string = urllib.parse.urlencode(params, quote_via=urllib.parse.quote_plus)
        return f"{auth_url}?{query_string}"

    def get_oauth_default_redirect_url(self) -> str:
        return f"{self.get_non_api_endpoint()}/account/api/oauth/token"

    def get_non_api_endpoint(self) -> str:
        return "https://www.kaggle.com" if self._env == KaggleEnv.PROD else self._endpoint

    class BearerAuth(requests.auth.AuthBase):

        def __init__(self, token):
            self.token = token

        def __call__(self, r):
            r.headers["Authorization"] = f"Bearer {self.token}"
            return r

    def _try_fill_auth(self):
        if self._signed_in is not None:
            return

        if self._api_token is None:
            (api_token, _) = get_access_token_from_env()
            self._api_token = api_token

        if self._api_token is not None:
            self._session.auth = KaggleHttpClient.BearerAuth(self._api_token)
            self._signed_in = True
            return

        if self._username and self._password:
            apikey_creds = self._username, self._password
        else:
            apikey_creds = _get_apikey_creds()
        if apikey_creds is not None:
            self._session.auth = apikey_creds
            self._signed_in = True
            return

        self._signed_in = False

    def _get_request_url(self, service_name: str, request_name: str):
        # On prod, API endpoints are served under https://api.kaggle.com/v1,
        # but on staging/admin/local, they are served under http://localhost/api/v1.
        base_url = self._endpoint if self._env == KaggleEnv.PROD else f"{self._endpoint}/api"
        return f"{base_url}/v1/{service_name}/{request_name}"
