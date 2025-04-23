import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class ApiBlobType(enum.Enum):
  API_BLOB_TYPE_UNSPECIFIED = 0
  DATASET = 1
  MODEL = 2
  INBOX = 3

class ApiStartBlobUploadRequest(KaggleObject):
  r"""
  Attributes:
    type (ApiBlobType)
      The type of the blob.
    name (str)
      Name (e.g. file name) of the blob.
    content_type (str)
      Content/MIME type (e.g. 'text/plain').
    content_length (int)
      Size in bytes of the blob.
    last_modified_epoch_seconds (int)
      Optional user-reported time when the blob was last updated/modified.
  """

  def __init__(self):
    self._type = ApiBlobType.API_BLOB_TYPE_UNSPECIFIED
    self._name = ""
    self._content_type = None
    self._content_length = 0
    self._last_modified_epoch_seconds = None
    self._freeze()

  @property
  def type(self) -> 'ApiBlobType':
    """The type of the blob."""
    return self._type

  @type.setter
  def type(self, type: 'ApiBlobType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ApiBlobType):
      raise TypeError('type must be of type ApiBlobType')
    self._type = type

  @property
  def name(self) -> str:
    """Name (e.g. file name) of the blob."""
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def content_type(self) -> str:
    """Content/MIME type (e.g. 'text/plain')."""
    return self._content_type or ""

  @content_type.setter
  def content_type(self, content_type: Optional[str]):
    if content_type is None:
      del self.content_type
      return
    if not isinstance(content_type, str):
      raise TypeError('content_type must be of type str')
    self._content_type = content_type

  @property
  def content_length(self) -> int:
    """Size in bytes of the blob."""
    return self._content_length

  @content_length.setter
  def content_length(self, content_length: int):
    if content_length is None:
      del self.content_length
      return
    if not isinstance(content_length, int):
      raise TypeError('content_length must be of type int')
    self._content_length = content_length

  @property
  def last_modified_epoch_seconds(self) -> int:
    """Optional user-reported time when the blob was last updated/modified."""
    return self._last_modified_epoch_seconds or 0

  @last_modified_epoch_seconds.setter
  def last_modified_epoch_seconds(self, last_modified_epoch_seconds: Optional[int]):
    if last_modified_epoch_seconds is None:
      del self.last_modified_epoch_seconds
      return
    if not isinstance(last_modified_epoch_seconds, int):
      raise TypeError('last_modified_epoch_seconds must be of type int')
    self._last_modified_epoch_seconds = last_modified_epoch_seconds

  def endpoint(self):
    path = '/api/v1/blobs/upload'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiStartBlobUploadResponse(KaggleObject):
  r"""
  Attributes:
    token (str)
      Opaque string token used to reference the new blob/file.
    create_url (str)
      URL to use to start the upload.
  """

  def __init__(self):
    self._token = ""
    self._create_url = ""
    self._freeze()

  @property
  def token(self) -> str:
    """Opaque string token used to reference the new blob/file."""
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
  def create_url(self) -> str:
    """URL to use to start the upload."""
    return self._create_url

  @create_url.setter
  def create_url(self, create_url: str):
    if create_url is None:
      del self.create_url
      return
    if not isinstance(create_url, str):
      raise TypeError('create_url must be of type str')
    self._create_url = create_url

  @property
  def createUrl(self):
    return self.create_url


ApiStartBlobUploadRequest._fields = [
  FieldMetadata("type", "type", "_type", ApiBlobType, ApiBlobType.API_BLOB_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("contentType", "content_type", "_content_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("lastModifiedEpochSeconds", "last_modified_epoch_seconds", "_last_modified_epoch_seconds", int, None, PredefinedSerializer(), optional=True),
]

ApiStartBlobUploadResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
  FieldMetadata("createUrl", "create_url", "_create_url", str, "", PredefinedSerializer()),
]

