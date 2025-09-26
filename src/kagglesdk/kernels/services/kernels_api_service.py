from kagglesdk.common.types.file_download import FileDownload
from kagglesdk.common.types.http_redirect import HttpRedirect
from kagglesdk.common.types.operations import Operation
from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.kernels.types.kernels_api_service import ApiCancelKernelSessionRequest, ApiCancelKernelSessionResponse, ApiCreateKernelSessionRequest, ApiDeleteKernelRequest, ApiDeleteKernelResponse, ApiDownloadKernelOutputRequest, ApiDownloadKernelOutputZipRequest, ApiGetKernelRequest, ApiGetKernelResponse, ApiGetKernelSessionStatusRequest, ApiGetKernelSessionStatusResponse, ApiListKernelFilesRequest, ApiListKernelFilesResponse, ApiListKernelSessionOutputRequest, ApiListKernelSessionOutputResponse, ApiListKernelsRequest, ApiListKernelsResponse, ApiSaveKernelRequest, ApiSaveKernelResponse

class KernelsApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_kernels(self, request: ApiListKernelsRequest = None) -> ApiListKernelsResponse:
    r"""
    Args:
      request (ApiListKernelsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListKernelsRequest()

    return self._client.call("kernels.KernelsApiService", "ListKernels", request, ApiListKernelsResponse)

  def list_kernel_files(self, request: ApiListKernelFilesRequest = None) -> ApiListKernelFilesResponse:
    r"""
    Args:
      request (ApiListKernelFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListKernelFilesRequest()

    return self._client.call("kernels.KernelsApiService", "ListKernelFiles", request, ApiListKernelFilesResponse)

  def get_kernel(self, request: ApiGetKernelRequest = None) -> ApiGetKernelResponse:
    r"""
    Args:
      request (ApiGetKernelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetKernelRequest()

    return self._client.call("kernels.KernelsApiService", "GetKernel", request, ApiGetKernelResponse)

  def save_kernel(self, request: ApiSaveKernelRequest = None) -> ApiSaveKernelResponse:
    r"""
    Args:
      request (ApiSaveKernelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiSaveKernelRequest()

    return self._client.call("kernels.KernelsApiService", "SaveKernel", request, ApiSaveKernelResponse)

  def list_kernel_session_output(self, request: ApiListKernelSessionOutputRequest = None) -> ApiListKernelSessionOutputResponse:
    r"""
    Args:
      request (ApiListKernelSessionOutputRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListKernelSessionOutputRequest()

    return self._client.call("kernels.KernelsApiService", "ListKernelSessionOutput", request, ApiListKernelSessionOutputResponse)

  def get_kernel_session_status(self, request: ApiGetKernelSessionStatusRequest = None) -> ApiGetKernelSessionStatusResponse:
    r"""
    Args:
      request (ApiGetKernelSessionStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetKernelSessionStatusRequest()

    return self._client.call("kernels.KernelsApiService", "GetKernelSessionStatus", request, ApiGetKernelSessionStatusResponse)

  def download_kernel_output(self, request: ApiDownloadKernelOutputRequest = None) -> HttpRedirect:
    r"""
    Meant for use by Kaggle Hub (http bindings and terminology align with that)

    Args:
      request (ApiDownloadKernelOutputRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadKernelOutputRequest()

    return self._client.call("kernels.KernelsApiService", "DownloadKernelOutput", request, HttpRedirect)

  def download_kernel_output_zip(self, request: ApiDownloadKernelOutputZipRequest = None) -> FileDownload:
    r"""
    Meant for use by Kaggle Hub (and DownloadKernelOutput above)

    Args:
      request (ApiDownloadKernelOutputZipRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadKernelOutputZipRequest()

    return self._client.call("kernels.KernelsApiService", "DownloadKernelOutputZip", request, FileDownload)

  def delete_kernel(self, request: ApiDeleteKernelRequest = None) -> ApiDeleteKernelResponse:
    r"""
    Args:
      request (ApiDeleteKernelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDeleteKernelRequest()

    return self._client.call("kernels.KernelsApiService", "DeleteKernel", request, ApiDeleteKernelResponse)

  def cancel_kernel_session(self, request: ApiCancelKernelSessionRequest = None) -> ApiCancelKernelSessionResponse:
    r"""
    Args:
      request (ApiCancelKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCancelKernelSessionRequest()

    return self._client.call("kernels.KernelsApiService", "CancelKernelSession", request, ApiCancelKernelSessionResponse)

  def create_kernel_session(self, request: ApiCreateKernelSessionRequest = None) -> Operation:
    r"""
    Args:
      request (ApiCreateKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateKernelSessionRequest()

    return self._client.call("kernels.KernelsApiService", "CreateKernelSession", request, Operation)
