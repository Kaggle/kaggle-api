import os
import json
import urllib.parse

import requests
from kagglesdk.kaggle_env import get_endpoint, get_env, KaggleEnv
from kagglesdk.kaggle_object import KaggleObject
from typing import Type

# TODO (http://b/354237483) Generate the client from the existing one.
# This was created from kaggle_api_client.py, prior to recent changes to
# auth handling. The new client requires KAGGLE_API_TOKEN, so it is not
# currently usable by the CLI.


def _headers_to_str(headers):
  return '\n'.join(f'{k}: {v}' for k, v in headers.items())


def _get_apikey_creds():
  apikey_filename = os.path.expanduser('~/.kaggle/kaggle.json')
  if not os.path.exists(apikey_filename):
    return None

  kaggle_json = None
  with open(apikey_filename) as apikey_file:
    kaggle_json = apikey_file.read()

  if not kaggle_json or not kaggle_json.strip():
    return None

  api_key_data = json.loads(kaggle_json)
  username = api_key_data['username']
  api_key = api_key_data['key']
  return username, api_key


def clean_data(data):
  if isinstance(data, dict):
    return {k: clean_data(v) for k, v in data.items() if v is not None}
  if isinstance(data, list):
    return [clean_data(v) for v in data if v is not None]
  if data is True:
    return 'true'
  if data is False:
    return 'false'
  return data


class KaggleHttpClient(object):
  _xsrf_cookie_name = 'XSRF-TOKEN'
  _csrf_cookie_name = "CSRF-TOKEN"
  _xsrf_cookies = (_xsrf_cookie_name, _csrf_cookie_name)
  _xsrf_header_name = 'X-XSRF-TOKEN'

  def __init__(self,
               env: KaggleEnv = None,
               verbose: bool = False,
               renew_iap_token=None,
               username=None,
               password=None):
    self._env = env or get_env()
    self._signed_in = None
    self._endpoint = get_endpoint(self._env)
    self._verbose = verbose
    self._session = None
    self._username = username
    self._password = password

  def call(self, service_name: str, request_name: str, request: KaggleObject,
           response_type: Type[KaggleObject]):
    self._init_session()
    http_request = self._prepare_request(service_name, request_name, request)

    http_response = self._session.send(http_request)

    response = self._prepare_response(response_type, http_response)
    return response

  def _prepare_request(self, service_name: str, request_name: str,
                       request: KaggleObject):
    request_url = self._get_request_url(request)
    method = request.method()
    data = request.__class__.to_dict(request)
    if method == 'GET':
      request_url = f'{request_url}?{urllib.parse.urlencode(data)}'
      data = ''
      self._session.headers.update({
          'Accept': 'application/json',
          'Content-Type': 'text/plain',
      })
    elif method == 'POST':
      self._session.headers.update({
          'Accept': 'application/json',
          'Content-Type': 'application/json',
      })
      if isinstance(data, dict):
        fields = request.body_fields()
        if fields is not None:
          if fields != '*':
            data = data[fields]
        data = clean_data(data)
        data = data.__str__()
    http_request = requests.Request(
        method=method,
        url=request_url,
        data=data,
        headers=self._session.headers,
        # cookies=self._get_xsrf_cookies(),
        auth=self._session.auth)
    prepared_request = http_request.prepare()
    self._print_request(prepared_request)
    return prepared_request

  def _get_xsrf_cookies(self):
    cookies = requests.cookies.RequestsCookieJar()
    for cookie in self._session.cookies:
      if cookie.name in KaggleHttpClient._xsrf_cookies:
        cookies[cookie.name] = cookie.value
    return cookies

  def _prepare_response(self, response_type, http_response):
    self._print_response(http_response)
    http_response.raise_for_status()
    if 'application/json' in http_response.headers['Content-Type']:
      resp = http_response.json()
      if 'code' in resp and resp['code'] >= 400:
        raise requests.exceptions.HTTPError(
            resp['message'], response=http_response)
    if response_type is None:  # Method doesn't have a return type
      return None
    return response_type.prepare_from(http_response)

  def _print_request(self, request):
    if not self._verbose:
      return
    self._print('---------------------Request----------------------')
    self._print(
        f'{request.method} {request.url}\n{_headers_to_str(request.headers)}\n\n{request.body}'
    )
    self._print('--------------------------------------------------')

  def _print_response(self, response, body=True):
    if not self._verbose:
      return
    self._print('---------------------Response---------------------')
    self._print(f'{response.status_code}\n{_headers_to_str(response.headers)}')
    if body:
      self._print(f'\n{response.text}')
    self._print('--------------------------------------------------')

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
    self._session.headers.update({
        'User-Agent': 'kaggle-api/v1.0.0',  # Was: V2
        'Content-Type': 'application/x-www-form-urlencoded',  # Was: /json
    })

    iap_token = self._get_iap_token_if_required()
    if iap_token is not None:
      self._session.headers.update({
          # https://cloud.google.com/iap/docs/authentication-howto#authenticating_from_proxy-authorization_header
          'Proxy-Authorization': f'Bearer {iap_token}',
      })

    self._try_fill_auth()
    # self._fill_xsrf_token(iap_token)  # TODO Make this align with original handler.

  def _get_iap_token_if_required(self):
    if self._env not in (KaggleEnv.STAGING, KaggleEnv.ADMIN):
      return None
    iap_token = os.getenv('KAGGLE_IAP_TOKEN')
    if iap_token is None:
      raise Exception(f'Must set KAGGLE_IAP_TOKEN to access "{self._endpoint}"')
    return iap_token

  def _fill_xsrf_token(self, iap_token):
    initial_get_request = requests.Request(
        method='GET',
        url=self._endpoint,
        headers=self._session.headers,
        auth=self._session.auth)
    prepared_request = initial_get_request.prepare()
    self._print_request(prepared_request)

    http_response = self._session.send(prepared_request)

    self._print_response(http_response, body=False)
    if iap_token is not None and http_response.status_code in (401, 403):
      raise requests.exceptions.HTTPError('IAP token invalid or expired')
    http_response.raise_for_status()

    self._session.headers.update({
        KaggleHttpClient._xsrf_header_name:
            self._session.cookies[KaggleHttpClient._xsrf_cookie_name],
    })

  class BearerAuth(requests.auth.AuthBase):

    def __init__(self, token):
      self.token = token

    def __call__(self, r):
      r.headers["Authorization"] = f"Bearer {self.token}"
      return r

  def _try_fill_auth(self):
    if self._signed_in is not None:
      return

    api_token = os.getenv('KAGGLE_API_TOKEN')
    if api_token is not None:
      self._session.auth = KaggleHttpClient.BearerAuth(api_token)
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

  def _get_request_url(self, request):
    return f'{self._endpoint}{request.endpoint()}'
