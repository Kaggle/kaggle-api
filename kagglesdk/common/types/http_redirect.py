from datetime import timedelta
from kagglesdk.kaggle_object import *
from typing import Optional

class HttpRedirect(KaggleObject):
  r"""
  Represents an HTTP redirect (e.g. 301 or 302) response.
  Patterned after ASP.NET MVC's RedirectResult.

  Attributes:
    url (str)
      Destination URL for the redirect.
    permanent (bool)
      Should it be an HTTP 301 (permanent) redirect or just temporary (HTTP
      302)?.
    bypass_encoding (bool)
      When `true`, the `url` is already encoded, so bypass `UriHelper.Encode`.
      Otherwise, invoke `UriHelper.Encode` on the `url` before returning to the
      client.
    expiry (timedelta)
      Specifies how long the redirected url can be cached.
  """

  def __init__(self):
    self._url = ""
    self._permanent = False
    self._bypass_encoding = None
    self._expiry = None
    self._freeze()

  @property
  def url(self) -> str:
    """Destination URL for the redirect."""
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def permanent(self) -> bool:
    r"""
    Should it be an HTTP 301 (permanent) redirect or just temporary (HTTP
    302)?.
    """
    return self._permanent

  @permanent.setter
  def permanent(self, permanent: bool):
    if permanent is None:
      del self.permanent
      return
    if not isinstance(permanent, bool):
      raise TypeError('permanent must be of type bool')
    self._permanent = permanent

  @property
  def bypass_encoding(self) -> bool:
    r"""
    When `true`, the `url` is already encoded, so bypass `UriHelper.Encode`.
    Otherwise, invoke `UriHelper.Encode` on the `url` before returning to the
    client.
    """
    return self._bypass_encoding or False

  @bypass_encoding.setter
  def bypass_encoding(self, bypass_encoding: bool):
    if bypass_encoding is None:
      del self.bypass_encoding
      return
    if not isinstance(bypass_encoding, bool):
      raise TypeError('bypass_encoding must be of type bool')
    self._bypass_encoding = bypass_encoding

  @property
  def expiry(self) -> timedelta:
    """Specifies how long the redirected url can be cached."""
    return self._expiry

  @expiry.setter
  def expiry(self, expiry: timedelta):
    if expiry is None:
      del self.expiry
      return
    if not isinstance(expiry, timedelta):
      raise TypeError('expiry must be of type timedelta')
    self._expiry = expiry

  @classmethod
  def prepare_from(cls, http_response):
    return http_response


HttpRedirect._fields = [
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("permanent", "permanent", "_permanent", bool, False, PredefinedSerializer()),
  FieldMetadata("bypassEncoding", "bypass_encoding", "_bypass_encoding", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("expiry", "expiry", "_expiry", timedelta, None, TimeDeltaSerializer()),
]

