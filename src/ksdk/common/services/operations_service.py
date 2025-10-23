from kagglesdk.common.types.operations import Operation
from kagglesdk.common.types.operations_service import GetOperationRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class OperationsClient(object):
  r"""
  Manages long-running operations with an API service.

  When an API method normally takes long time to complete, it can be designed
  to return [Operation][google.longrunning.Operation] to the client, and the
  client can use this interface to receive the real response asynchronously by
  polling the operation resource, or pass the operation resource to another API
  (such as Pub/Sub API) to receive the response.  Any API service that returns
  long-running operations should implement the `Operations` interface so
  developers can have a consistent client experience.
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_operation(self, request: GetOperationRequest = None, name: str = None) -> Operation:
    r"""
    Gets the latest state of a long-running operation.  Clients can use this
    method to poll the operation result at intervals as recommended by the API
    service.

    Args:
      request (GetOperationRequest):
        The request object; initialized to empty instance if not specified.
        May not be specified if any of the flattened field params are specified.
      name (str)
        This corresponds to the ``name`` field on the ``request`` instance;
        if ``request`` is provided, this should not be set.
    """

    has_flattened_args = any([name])
    if request is not None and has_flattened_args:
      raise ValueError('If the `request` argument is set, then none of '
                       'the individual field arguments should be set.')

    if request is None:
      request = GetOperationRequest()
      if name is not None:
        request.name = name

    return self._client.call("common.OperationsService", "GetOperation", request, Operation)
