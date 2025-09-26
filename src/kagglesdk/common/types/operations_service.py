from kagglesdk.kaggle_object import *

class GetOperationRequest(KaggleObject):
  r"""
  The request message for
  [Operations.GetOperation][google.longrunning.Operations.GetOperation].

  Attributes:
    name (str)
      The name of the operation resource.
  """

  def __init__(self):
    self._name = ""
    self._freeze()

  @property
  def name(self) -> str:
    """The name of the operation resource."""
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  def endpoint(self):
    path = '/api/v1/operations/get'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


GetOperationRequest._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
]

