from datetime import datetime
from kagglesdk.kaggle_object import *
from typing import Optional, List

class BenchmarkResult(KaggleObject):
  r"""
  TODO(bml): Integrate this proto with personal benchmarks trials.
  Represents the outcome of a benchmark run. All fields are immutable.

  Attributes:
    numeric_result (NumericResult)
    boolean_result (bool)
    custom_additional_results (CustomResult)
      Generic additional results. These are rendered generically on the frontend:
    numeric_result_private (NumericResult)
      Numeric result on the private set of the benchmark version.
    numeric_result_public (NumericResult)
      Numeric result on the public set of the benchmark version.
    evaluation_date (datetime)
      The date on which evaluation was performed.
    task_version_id (int)
      Convenience fields for this result (for the frontend):
  """

  def __init__(self):
    self._numeric_result = None
    self._boolean_result = None
    self._custom_additional_results = []
    self._numeric_result_private = None
    self._numeric_result_public = None
    self._evaluation_date = None
    self._task_version_id = None
    self._freeze()

  @property
  def task_version_id(self) -> int:
    """Convenience fields for this result (for the frontend):"""
    return self._task_version_id or 0

  @task_version_id.setter
  def task_version_id(self, task_version_id: Optional[int]):
    if task_version_id is None:
      del self.task_version_id
      return
    if not isinstance(task_version_id, int):
      raise TypeError('task_version_id must be of type int')
    self._task_version_id = task_version_id

  @property
  def numeric_result(self) -> Optional['NumericResult']:
    return self._numeric_result or None

  @numeric_result.setter
  def numeric_result(self, numeric_result: Optional['NumericResult']):
    if numeric_result is None:
      del self.numeric_result
      return
    if not isinstance(numeric_result, NumericResult):
      raise TypeError('numeric_result must be of type NumericResult')
    del self.boolean_result
    self._numeric_result = numeric_result

  @property
  def boolean_result(self) -> bool:
    return self._boolean_result or False

  @boolean_result.setter
  def boolean_result(self, boolean_result: bool):
    if boolean_result is None:
      del self.boolean_result
      return
    if not isinstance(boolean_result, bool):
      raise TypeError('boolean_result must be of type bool')
    del self.numeric_result
    self._boolean_result = boolean_result

  @property
  def custom_additional_results(self) -> Optional[List[Optional['CustomResult']]]:
    """Generic additional results. These are rendered generically on the frontend:"""
    return self._custom_additional_results

  @custom_additional_results.setter
  def custom_additional_results(self, custom_additional_results: Optional[List[Optional['CustomResult']]]):
    if custom_additional_results is None:
      del self.custom_additional_results
      return
    if not isinstance(custom_additional_results, list):
      raise TypeError('custom_additional_results must be of type list')
    if not all([isinstance(t, CustomResult) for t in custom_additional_results]):
      raise TypeError('custom_additional_results must contain only items of type CustomResult')
    self._custom_additional_results = custom_additional_results

  @property
  def numeric_result_private(self) -> Optional['NumericResult']:
    """Numeric result on the private set of the benchmark version."""
    return self._numeric_result_private or None

  @numeric_result_private.setter
  def numeric_result_private(self, numeric_result_private: Optional[Optional['NumericResult']]):
    if numeric_result_private is None:
      del self.numeric_result_private
      return
    if not isinstance(numeric_result_private, NumericResult):
      raise TypeError('numeric_result_private must be of type NumericResult')
    self._numeric_result_private = numeric_result_private

  @property
  def numeric_result_public(self) -> Optional['NumericResult']:
    """Numeric result on the public set of the benchmark version."""
    return self._numeric_result_public or None

  @numeric_result_public.setter
  def numeric_result_public(self, numeric_result_public: Optional[Optional['NumericResult']]):
    if numeric_result_public is None:
      del self.numeric_result_public
      return
    if not isinstance(numeric_result_public, NumericResult):
      raise TypeError('numeric_result_public must be of type NumericResult')
    self._numeric_result_public = numeric_result_public

  @property
  def evaluation_date(self) -> datetime:
    """The date on which evaluation was performed."""
    return self._evaluation_date or None

  @evaluation_date.setter
  def evaluation_date(self, evaluation_date: Optional[datetime]):
    if evaluation_date is None:
      del self.evaluation_date
      return
    if not isinstance(evaluation_date, datetime):
      raise TypeError('evaluation_date must be of type datetime')
    self._evaluation_date = evaluation_date


class CustomResult(KaggleObject):
  r"""
  Attributes:
    key (str)
    value (str)
  """

  def __init__(self):
    self._key = ""
    self._value = ""
    self._freeze()

  @property
  def key(self) -> str:
    return self._key

  @key.setter
  def key(self, key: str):
    if key is None:
      del self.key
      return
    if not isinstance(key, str):
      raise TypeError('key must be of type str')
    self._key = key

  @property
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value


class NumericResult(KaggleObject):
  r"""
  Attributes:
    value (float)
    confidence_interval (float)
      Note, while we call this the 'confidence interval' - the value we store
      here is actually the 'confidence radius', it should always be displayed
      as a +- value.
    uneven_confidence_interval (UnevenConfidenceInterval)
      For asymmetric confidence intervals in which the +/- values differ
      If set, prioritized over confidence_interval
  """

  def __init__(self):
    self._value = 0.0
    self._confidence_interval = None
    self._uneven_confidence_interval = None
    self._freeze()

  @property
  def value(self) -> float:
    return self._value

  @value.setter
  def value(self, value: float):
    if value is None:
      del self.value
      return
    if not isinstance(value, float):
      raise TypeError('value must be of type float')
    self._value = value

  @property
  def confidence_interval(self) -> float:
    r"""
    Note, while we call this the 'confidence interval' - the value we store
    here is actually the 'confidence radius', it should always be displayed
    as a +- value.
    """
    return self._confidence_interval or 0.0

  @confidence_interval.setter
  def confidence_interval(self, confidence_interval: Optional[float]):
    if confidence_interval is None:
      del self.confidence_interval
      return
    if not isinstance(confidence_interval, float):
      raise TypeError('confidence_interval must be of type float')
    self._confidence_interval = confidence_interval

  @property
  def uneven_confidence_interval(self) -> Optional['UnevenConfidenceInterval']:
    r"""
    For asymmetric confidence intervals in which the +/- values differ
    If set, prioritized over confidence_interval
    """
    return self._uneven_confidence_interval or None

  @uneven_confidence_interval.setter
  def uneven_confidence_interval(self, uneven_confidence_interval: Optional[Optional['UnevenConfidenceInterval']]):
    if uneven_confidence_interval is None:
      del self.uneven_confidence_interval
      return
    if not isinstance(uneven_confidence_interval, UnevenConfidenceInterval):
      raise TypeError('uneven_confidence_interval must be of type UnevenConfidenceInterval')
    self._uneven_confidence_interval = uneven_confidence_interval


class UnevenConfidenceInterval(KaggleObject):
  r"""
  Attributes:
    plus (float)
    minus (float)
  """

  def __init__(self):
    self._plus = 0.0
    self._minus = 0.0
    self._freeze()

  @property
  def plus(self) -> float:
    return self._plus

  @plus.setter
  def plus(self, plus: float):
    if plus is None:
      del self.plus
      return
    if not isinstance(plus, float):
      raise TypeError('plus must be of type float')
    self._plus = plus

  @property
  def minus(self) -> float:
    return self._minus

  @minus.setter
  def minus(self, minus: float):
    if minus is None:
      del self.minus
      return
    if not isinstance(minus, float):
      raise TypeError('minus must be of type float')
    self._minus = minus


BenchmarkResult._fields = [
  FieldMetadata("numericResult", "numeric_result", "_numeric_result", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("booleanResult", "boolean_result", "_boolean_result", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("customAdditionalResults", "custom_additional_results", "_custom_additional_results", CustomResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("numericResultPrivate", "numeric_result_private", "_numeric_result_private", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("numericResultPublic", "numeric_result_public", "_numeric_result_public", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("evaluationDate", "evaluation_date", "_evaluation_date", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("taskVersionId", "task_version_id", "_task_version_id", int, None, PredefinedSerializer(), optional=True),
]

CustomResult._fields = [
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
]

NumericResult._fields = [
  FieldMetadata("value", "value", "_value", float, 0.0, PredefinedSerializer()),
  FieldMetadata("confidenceInterval", "confidence_interval", "_confidence_interval", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("unevenConfidenceInterval", "uneven_confidence_interval", "_uneven_confidence_interval", UnevenConfidenceInterval, None, KaggleObjectSerializer(), optional=True),
]

UnevenConfidenceInterval._fields = [
  FieldMetadata("plus", "plus", "_plus", float, 0.0, PredefinedSerializer()),
  FieldMetadata("minus", "minus", "_minus", float, 0.0, PredefinedSerializer()),
]

