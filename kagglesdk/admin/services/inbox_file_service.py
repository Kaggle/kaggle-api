from kagglesdk.admin.types.inbox_file_service import CreateInboxFileRequest, CreateInboxFileResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class InboxFileClient(object):
  """File drop/pickup functionality."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_inbox_file(self, request: CreateInboxFileRequest = None) -> CreateInboxFileResponse:
    r"""
    Creates (aka 'drops') a new file into the inbox.

    Args:
      request (CreateInboxFileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateInboxFileRequest()

    return self._client.call("admin.InboxFileService", "CreateInboxFile", request, CreateInboxFileResponse)
