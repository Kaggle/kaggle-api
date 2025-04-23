from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.models.types.model_service import GetModelMetricsRequest, GetModelMetricsResponse

class ModelClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_model_metrics(self, request: GetModelMetricsRequest = None) -> GetModelMetricsResponse:
    r"""
    Args:
      request (GetModelMetricsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelMetricsRequest()

    return self._client.call("models.ModelService", "GetModelMetrics", request, GetModelMetricsResponse)
