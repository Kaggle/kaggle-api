from kagglesdk.common.types.http_redirect import HttpRedirect
from kagglesdk.datasets.types.dataset_api_service import ApiCreateDatasetRequest, ApiCreateDatasetResponse, ApiCreateDatasetVersionByIdRequest, ApiCreateDatasetVersionRequest, ApiDataset, ApiDeleteDatasetRequest, ApiDeleteDatasetResponse, ApiDownloadDatasetRawRequest, ApiDownloadDatasetRequest, ApiGetDatasetMetadataRequest, ApiGetDatasetMetadataResponse, ApiGetDatasetRequest, ApiGetDatasetStatusRequest, ApiGetDatasetStatusResponse, ApiListDatasetFilesRequest, ApiListDatasetFilesResponse, ApiListDatasetsRequest, ApiListDatasetsResponse, ApiUpdateDatasetMetadataRequest, ApiUpdateDatasetMetadataResponse, ApiUploadDatasetFileRequest, ApiUploadDatasetFileResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class DatasetApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_datasets(self, request: ApiListDatasetsRequest = None) -> ApiListDatasetsResponse:
    r"""
    Args:
      request (ApiListDatasetsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListDatasetsRequest()

    return self._client.call("datasets.DatasetApiService", "ApiListDatasets", request, ApiListDatasetsResponse)

  def get_dataset(self, request: ApiGetDatasetRequest = None) -> ApiDataset:
    r"""
    Args:
      request (ApiGetDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetDatasetRequest()

    return self._client.call("datasets.DatasetApiService", "ApiGetDataset", request, ApiDataset)

  def list_dataset_files(self, request: ApiListDatasetFilesRequest = None) -> ApiListDatasetFilesResponse:
    r"""
    Args:
      request (ApiListDatasetFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListDatasetFilesRequest()

    return self._client.call("datasets.DatasetApiService", "ApiListDatasetFiles", request, ApiListDatasetFilesResponse)

  def get_dataset_metadata(self, request: ApiGetDatasetMetadataRequest = None) -> ApiGetDatasetMetadataResponse:
    r"""
    Args:
      request (ApiGetDatasetMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetDatasetMetadataRequest()

    return self._client.call("datasets.DatasetApiService", "ApiGetDatasetMetadata", request, ApiGetDatasetMetadataResponse)

  def update_dataset_metadata(self, request: ApiUpdateDatasetMetadataRequest = None) -> ApiUpdateDatasetMetadataResponse:
    r"""
    Args:
      request (ApiUpdateDatasetMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiUpdateDatasetMetadataRequest()

    return self._client.call("datasets.DatasetApiService", "ApiUpdateDatasetMetadata", request, ApiUpdateDatasetMetadataResponse)

  def download_dataset(self, request: ApiDownloadDatasetRequest = None) -> HttpRedirect:
    r"""
    Args:
      request (ApiDownloadDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadDatasetRequest()

    return self._client.call("datasets.DatasetApiService", "ApiDownloadDataset", request, HttpRedirect)

  def download_dataset_raw(self, request: ApiDownloadDatasetRawRequest = None) -> HttpRedirect:
    r"""
    Note: This API method has extremely low usage, and can be considered for
    deprecation. The existing DownloadDataset RPC, with `raw=true` set on the
    request, is equivalent.

    Args:
      request (ApiDownloadDatasetRawRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadDatasetRawRequest()

    return self._client.call("datasets.DatasetApiService", "ApiDownloadDatasetRaw", request, HttpRedirect)

  def create_dataset_version(self, request: ApiCreateDatasetVersionRequest = None) -> ApiCreateDatasetResponse:
    r"""
    Args:
      request (ApiCreateDatasetVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateDatasetVersionRequest()

    return self._client.call("datasets.DatasetApiService", "ApiCreateDatasetVersion", request, ApiCreateDatasetResponse)

  def create_dataset_version_by_id(self, request: ApiCreateDatasetVersionByIdRequest = None) -> ApiCreateDatasetResponse:
    r"""
    Args:
      request (ApiCreateDatasetVersionByIdRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateDatasetVersionByIdRequest()

    return self._client.call("datasets.DatasetApiService", "ApiCreateDatasetVersionById", request, ApiCreateDatasetResponse)

  def create_dataset(self, request: ApiCreateDatasetRequest = None) -> ApiCreateDatasetResponse:
    r"""
    Args:
      request (ApiCreateDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateDatasetRequest()

    return self._client.call("datasets.DatasetApiService", "ApiCreateDataset", request, ApiCreateDatasetResponse)

  def get_dataset_status(self, request: ApiGetDatasetStatusRequest = None) -> ApiGetDatasetStatusResponse:
    r"""
    Args:
      request (ApiGetDatasetStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetDatasetStatusRequest()

    return self._client.call("datasets.DatasetApiService", "ApiGetDatasetStatus", request, ApiGetDatasetStatusResponse)

  def upload_dataset_file(self, request: ApiUploadDatasetFileRequest = None) -> ApiUploadDatasetFileResponse:
    r"""
    Deprecated. Use the new unified BlobApiService#StartBlobUpload rpc.

    Args:
      request (ApiUploadDatasetFileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiUploadDatasetFileRequest()

    return self._client.call("datasets.DatasetApiService", "ApiUploadDatasetFile", request, ApiUploadDatasetFileResponse)

  def delete_dataset(self, request: ApiDeleteDatasetRequest = None) -> ApiDeleteDatasetResponse:
    r"""
    Args:
      request (ApiDeleteDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDeleteDatasetRequest()

    return self._client.call("datasets.DatasetApiService", "ApiDeleteDataset", request, ApiDeleteDatasetResponse)
