from kagglesdk.common.types.http_redirect import HttpRedirect
from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.models.types.model_api_service import ApiCreateModelInstanceRequest, ApiCreateModelInstanceVersionRequest, ApiCreateModelRequest, ApiCreateModelResponse, ApiDeleteModelInstanceRequest, ApiDeleteModelInstanceVersionRequest, ApiDeleteModelRequest, ApiDeleteModelResponse, ApiDownloadModelInstanceVersionRequest, ApiGetModelInstanceRequest, ApiGetModelRequest, ApiListModelInstanceVersionFilesRequest, ApiListModelInstanceVersionFilesResponse, ApiListModelsRequest, ApiListModelsResponse, ApiModel, ApiModelInstance, ApiUpdateModelInstanceRequest, ApiUpdateModelRequest, ApiUpdateModelResponse, ApiUploadModelFileRequest, ApiUploadModelFileResponse

class ModelApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_model(self, request: ApiCreateModelRequest = None) -> ApiCreateModelResponse:
    r"""
    Args:
      request (ApiCreateModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateModelRequest()

    return self._client.call("models.ModelApiService", "ApiCreateModel", request, ApiCreateModelResponse)

  def create_model_instance(self, request: ApiCreateModelInstanceRequest = None) -> ApiCreateModelResponse:
    r"""
    Args:
      request (ApiCreateModelInstanceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateModelInstanceRequest()

    return self._client.call("models.ModelApiService", "ApiCreateModelInstance", request, ApiCreateModelResponse)

  def create_model_instance_version(self, request: ApiCreateModelInstanceVersionRequest = None) -> ApiCreateModelResponse:
    r"""
    Args:
      request (ApiCreateModelInstanceVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateModelInstanceVersionRequest()

    return self._client.call("models.ModelApiService", "ApiCreateModelInstanceVersion", request, ApiCreateModelResponse)

  def delete_model(self, request: ApiDeleteModelRequest = None) -> ApiDeleteModelResponse:
    r"""
    Args:
      request (ApiDeleteModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDeleteModelRequest()

    return self._client.call("models.ModelApiService", "ApiDeleteModel", request, ApiDeleteModelResponse)

  def delete_model_instance(self, request: ApiDeleteModelInstanceRequest = None) -> ApiDeleteModelResponse:
    r"""
    Args:
      request (ApiDeleteModelInstanceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDeleteModelInstanceRequest()

    return self._client.call("models.ModelApiService", "ApiDeleteModelInstance", request, ApiDeleteModelResponse)

  def delete_model_instance_version(self, request: ApiDeleteModelInstanceVersionRequest = None) -> ApiDeleteModelResponse:
    r"""
    Args:
      request (ApiDeleteModelInstanceVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDeleteModelInstanceVersionRequest()

    return self._client.call("models.ModelApiService", "ApiDeleteModelInstanceVersion", request, ApiDeleteModelResponse)

  def get_model(self, request: ApiGetModelRequest = None) -> ApiModel:
    r"""
    Args:
      request (ApiGetModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetModelRequest()

    return self._client.call("models.ModelApiService", "ApiGetModel", request, ApiModel)

  def get_model_instance(self, request: ApiGetModelInstanceRequest = None) -> ApiModelInstance:
    r"""
    Args:
      request (ApiGetModelInstanceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetModelInstanceRequest()

    return self._client.call("models.ModelApiService", "ApiGetModelInstance", request, ApiModelInstance)

  def download_model_instance_version(self, request: ApiDownloadModelInstanceVersionRequest = None) -> HttpRedirect:
    r"""
    Args:
      request (ApiDownloadModelInstanceVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadModelInstanceVersionRequest()

    return self._client.call("models.ModelApiService", "ApiDownloadModelInstanceVersion", request, HttpRedirect)

  def list_models(self, request: ApiListModelsRequest = None) -> ApiListModelsResponse:
    r"""
    Args:
      request (ApiListModelsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListModelsRequest()

    return self._client.call("models.ModelApiService", "ApiListModels", request, ApiListModelsResponse)

  def list_model_instance_version_files(self, request: ApiListModelInstanceVersionFilesRequest = None) -> ApiListModelInstanceVersionFilesResponse:
    r"""
    Args:
      request (ApiListModelInstanceVersionFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListModelInstanceVersionFilesRequest()

    return self._client.call("models.ModelApiService", "ApiListModelInstanceVersionFiles", request, ApiListModelInstanceVersionFilesResponse)

  def update_model(self, request: ApiUpdateModelRequest = None) -> ApiUpdateModelResponse:
    r"""
    Args:
      request (ApiUpdateModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiUpdateModelRequest()

    return self._client.call("models.ModelApiService", "ApiUpdateModel", request, ApiUpdateModelResponse)

  def update_model_instance(self, request: ApiUpdateModelInstanceRequest = None) -> ApiUpdateModelResponse:
    r"""
    Args:
      request (ApiUpdateModelInstanceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiUpdateModelInstanceRequest()

    return self._client.call("models.ModelApiService", "ApiUpdateModelInstance", request, ApiUpdateModelResponse)

  def upload_model_file(self, request: ApiUploadModelFileRequest = None) -> ApiUploadModelFileResponse:
    r"""
    Deprecated. Use the new unified BlobApiService#StartBlobUpload rpc.

    Args:
      request (ApiUploadModelFileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiUploadModelFileRequest()

    return self._client.call("models.ModelApiService", "ApiUploadModelFile", request, ApiUploadModelFileResponse)
