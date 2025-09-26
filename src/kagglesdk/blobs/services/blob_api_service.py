from kagglesdk.blobs.types.blob_api_service import ApiStartBlobUploadRequest, ApiStartBlobUploadResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BlobApiClient(object):
  r"""
  Binary Large OBject (BLOB) service used for uploading files to Google Cloud
  Storage (GCS).
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def start_blob_upload(self, request: ApiStartBlobUploadRequest = None) -> ApiStartBlobUploadResponse:
    r"""
    Starts a blob upload (i.e. reserves a spot for the upload on GCS).

    Args:
      request (ApiStartBlobUploadRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiStartBlobUploadRequest()

    return self._client.call("blobs.BlobApiService", "StartBlobUpload", request, ApiStartBlobUploadResponse)
