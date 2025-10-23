from kagglesdk.kaggle_object import *

class ListSearchContentRangeFilter(KaggleObject):
  r"""
  Attributes:
    min (int)
      The minimum value (inclusive) to apply to filtering
    max (int)
      The maximum value (inclusive) to apply to filtering
  """

  def __init__(self):
    self._min = 0
    self._max = 0
    self._freeze()

  @property
  def min(self) -> int:
    """The minimum value (inclusive) to apply to filtering"""
    return self._min

  @min.setter
  def min(self, min: int):
    if min is None:
      del self.min
      return
    if not isinstance(min, int):
      raise TypeError('min must be of type int')
    self._min = min

  @property
  def max(self) -> int:
    """The maximum value (inclusive) to apply to filtering"""
    return self._max

  @max.setter
  def max(self, max: int):
    if max is None:
      del self.max
      return
    if not isinstance(max, int):
      raise TypeError('max must be of type int')
    self._max = max


ListSearchContentRangeFilter._fields = [
  FieldMetadata("min", "min", "_min", int, 0, PredefinedSerializer()),
  FieldMetadata("max", "max", "_max", int, 0, PredefinedSerializer()),
]

