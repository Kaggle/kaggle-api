from kagglesdk.kaggle_object import *
from typing import Optional

class Operation(KaggleObject):
  r"""
  This resource represents a long-running operation that is the result of a
  network API call.

  Attributes:
    name (str)
      The server-assigned name, which is only unique within the same service that
      originally returns it. If you use the default HTTP mapping, the
      `name` should be a resource name ending with `operations/{unique_id}`.
    metadata (object)
      Service-specific metadata associated with the operation.  It typically
      contains progress information and common metadata such as create time.
      Some services might not provide such metadata.  Any method that returns a
      long-running operation should document the metadata type, if any.
    done (bool)
      If the value is `false`, it means the operation is still in progress.
      If `true`, the operation is completed, and either `error` or `response` is
      available.
    error (Operation.Status)
      The error result of the operation in case of failure or cancellation.
    response (object)
      The normal, successful response of the operation.  If the original
      method returns no data on success, such as `Delete`, the response is
      `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx`
      is the original method name.  For example, if the original method name
      is `TakeSnapshot()`, the inferred response type is
      `TakeSnapshotResponse`.
  """

  class Status(KaggleObject):
    r"""
    Attributes:
      code (int)
        The HTTP status code that corresponds to `google.rpc.Status.code`.
      message (str)
        This corresponds to `google.rpc.Status.message`.
    """

    def __init__(self):
      self._code = 0
      self._message = ""
      self._freeze()

    @property
    def code(self) -> int:
      """The HTTP status code that corresponds to `google.rpc.Status.code`."""
      return self._code

    @code.setter
    def code(self, code: int):
      if code is None:
        del self.code
        return
      if not isinstance(code, int):
        raise TypeError('code must be of type int')
      self._code = code

    @property
    def message(self) -> str:
      """This corresponds to `google.rpc.Status.message`."""
      return self._message

    @message.setter
    def message(self, message: str):
      if message is None:
        del self.message
        return
      if not isinstance(message, str):
        raise TypeError('message must be of type str')
      self._message = message


  def __init__(self):
    self._name = ""
    self._metadata = None
    self._done = False
    self._error = None
    self._response = None
    self._freeze()

  @property
  def name(self) -> str:
    r"""
    The server-assigned name, which is only unique within the same service that
    originally returns it. If you use the default HTTP mapping, the
    `name` should be a resource name ending with `operations/{unique_id}`.
    """
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
  def metadata(self) -> object:
    r"""
    Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.
    """
    return self._metadata

  @metadata.setter
  def metadata(self, metadata: object):
    if metadata is None:
      del self.metadata
      return
    if not isinstance(metadata, object):
      raise TypeError('metadata must be of type object')
    self._metadata = metadata

  @property
  def done(self) -> bool:
    r"""
    If the value is `false`, it means the operation is still in progress.
    If `true`, the operation is completed, and either `error` or `response` is
    available.
    """
    return self._done

  @done.setter
  def done(self, done: bool):
    if done is None:
      del self.done
      return
    if not isinstance(done, bool):
      raise TypeError('done must be of type bool')
    self._done = done

  @property
  def error(self) -> Optional['Operation.Status']:
    """The error result of the operation in case of failure or cancellation."""
    return self._error or None

  @error.setter
  def error(self, error: Optional['Operation.Status']):
    if error is None:
      del self.error
      return
    if not isinstance(error, Operation.Status):
      raise TypeError('error must be of type Operation.Status')
    del self.response
    self._error = error

  @property
  def response(self) -> object:
    r"""
    The normal, successful response of the operation.  If the original
    method returns no data on success, such as `Delete`, the response is
    `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx`
    is the original method name.  For example, if the original method name
    is `TakeSnapshot()`, the inferred response type is
    `TakeSnapshotResponse`.
    """
    return self._response or None

  @response.setter
  def response(self, response: object):
    if response is None:
      del self.response
      return
    if not isinstance(response, object):
      raise TypeError('response must be of type object')
    del self.error
    self._response = response


Operation.Status._fields = [
  FieldMetadata("code", "code", "_code", int, 0, PredefinedSerializer()),
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
]

Operation._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("metadata", "metadata", "_metadata", object, None, PredefinedSerializer()),
  FieldMetadata("done", "done", "_done", bool, False, PredefinedSerializer()),
  FieldMetadata("error", "error", "_error", Operation.Status, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("response", "response", "_response", object, None, PredefinedSerializer(), optional=True),
]

