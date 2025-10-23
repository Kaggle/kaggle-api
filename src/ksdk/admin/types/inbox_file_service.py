from kagglesdk.kaggle_object import *

class CreateInboxFileRequest(KaggleObject):
  r"""
  Attributes:
    virtual_directory (str)
      Directory name used for tagging the uploaded file.
    blob_file_token (str)
      Token representing the uploaded file.
  """

  def __init__(self):
    self._virtual_directory = ""
    self._blob_file_token = ""
    self._freeze()

  @property
  def virtual_directory(self) -> str:
    """Directory name used for tagging the uploaded file."""
    return self._virtual_directory

  @virtual_directory.setter
  def virtual_directory(self, virtual_directory: str):
    if virtual_directory is None:
      del self.virtual_directory
      return
    if not isinstance(virtual_directory, str):
      raise TypeError('virtual_directory must be of type str')
    self._virtual_directory = virtual_directory

  @property
  def blob_file_token(self) -> str:
    """Token representing the uploaded file."""
    return self._blob_file_token

  @blob_file_token.setter
  def blob_file_token(self, blob_file_token: str):
    if blob_file_token is None:
      del self.blob_file_token
      return
    if not isinstance(blob_file_token, str):
      raise TypeError('blob_file_token must be of type str')
    self._blob_file_token = blob_file_token

  def endpoint(self):
    path = '/api/v1/inbox/files/create'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class CreateInboxFileResponse(KaggleObject):
  r"""
  NOTE: This is sent to non-admins, so we're intentionally *NOT* sending back
  the full InboxFile (with its URL for a direct download).

  """

  pass

CreateInboxFileRequest._fields = [
  FieldMetadata("virtualDirectory", "virtual_directory", "_virtual_directory", str, "", PredefinedSerializer()),
  FieldMetadata("blobFileToken", "blob_file_token", "_blob_file_token", str, "", PredefinedSerializer()),
]

CreateInboxFileResponse._fields = []

