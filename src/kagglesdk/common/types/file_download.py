from kagglesdk.kaggle_object import *
from typing import Optional

class FileDownload(KaggleObject):
  r"""
  Standard response object representing a file download.
  See http://go/kaggle-proto-handler-file-downloads
  Some field names/descriptions borrowed from
  google3/gdata/rosy/proto/data.proto

  Attributes:
    content_type (str)
      MIME type of the data
      TODO(aip.dev/143): (-- api-linter: core::0143::standardized-codes=disabled
      --)
    file_name (str)
      Original file name
    token (str)
      A unique fingerprint for the file/media data
    content_length (int)
      Size of the data, in bytes (if known)
  """

  def __init__(self):
    self._content_type = ""
    self._file_name = ""
    self._token = ""
    self._content_length = None
    self._freeze()

  @property
  def content_type(self) -> str:
    r"""
    MIME type of the data
    TODO(aip.dev/143): (-- api-linter: core::0143::standardized-codes=disabled
    --)
    """
    return self._content_type

  @content_type.setter
  def content_type(self, content_type: str):
    if content_type is None:
      del self.content_type
      return
    if not isinstance(content_type, str):
      raise TypeError('content_type must be of type str')
    self._content_type = content_type

  @property
  def file_name(self) -> str:
    """Original file name"""
    return self._file_name

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

  @property
  def token(self) -> str:
    """A unique fingerprint for the file/media data"""
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token

  @property
  def content_length(self) -> int:
    """Size of the data, in bytes (if known)"""
    return self._content_length or 0

  @content_length.setter
  def content_length(self, content_length: int):
    if content_length is None:
      del self.content_length
      return
    if not isinstance(content_length, int):
      raise TypeError('content_length must be of type int')
    self._content_length = content_length

  @classmethod
  def prepare_from(cls, http_response):
    return http_response


FileDownload._fields = [
  FieldMetadata("contentType", "content_type", "_content_type", str, "", PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
  FieldMetadata("contentLength", "content_length", "_content_length", int, None, PredefinedSerializer(), optional=True),
]

