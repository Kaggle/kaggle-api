from datetime import datetime
from kagglesdk.kaggle_object import *
from typing import Optional, List

class BenchmarkVersionIdentifier(KaggleObject):
  r"""
  Identifier for selecting a specific benchmark version.

  Attributes:
    version_id_selector (VersionIdSelector)
    published_latest_selector (PublishedLatestSelector)
    published_number_selector (PublishedNumberSelector)
    draft_selector (DraftSelector)
    benchmark_slug_selector (BenchmarkSlugSelector)
  """

  def __init__(self):
    self._version_id_selector = None
    self._published_latest_selector = None
    self._published_number_selector = None
    self._draft_selector = None
    self._benchmark_slug_selector = None
    self._freeze()

  @property
  def version_id_selector(self) -> Optional['VersionIdSelector']:
    return self._version_id_selector or None

  @version_id_selector.setter
  def version_id_selector(self, version_id_selector: Optional['VersionIdSelector']):
    if version_id_selector is None:
      del self.version_id_selector
      return
    if not isinstance(version_id_selector, VersionIdSelector):
      raise TypeError('version_id_selector must be of type VersionIdSelector')
    del self.published_latest_selector
    del self.published_number_selector
    del self.draft_selector
    del self.benchmark_slug_selector
    self._version_id_selector = version_id_selector

  @property
  def published_latest_selector(self) -> Optional['PublishedLatestSelector']:
    return self._published_latest_selector or None

  @published_latest_selector.setter
  def published_latest_selector(self, published_latest_selector: Optional['PublishedLatestSelector']):
    if published_latest_selector is None:
      del self.published_latest_selector
      return
    if not isinstance(published_latest_selector, PublishedLatestSelector):
      raise TypeError('published_latest_selector must be of type PublishedLatestSelector')
    del self.version_id_selector
    del self.published_number_selector
    del self.draft_selector
    del self.benchmark_slug_selector
    self._published_latest_selector = published_latest_selector

  @property
  def published_number_selector(self) -> Optional['PublishedNumberSelector']:
    return self._published_number_selector or None

  @published_number_selector.setter
  def published_number_selector(self, published_number_selector: Optional['PublishedNumberSelector']):
    if published_number_selector is None:
      del self.published_number_selector
      return
    if not isinstance(published_number_selector, PublishedNumberSelector):
      raise TypeError('published_number_selector must be of type PublishedNumberSelector')
    del self.version_id_selector
    del self.published_latest_selector
    del self.draft_selector
    del self.benchmark_slug_selector
    self._published_number_selector = published_number_selector

  @property
  def draft_selector(self) -> Optional['DraftSelector']:
    return self._draft_selector or None

  @draft_selector.setter
  def draft_selector(self, draft_selector: Optional['DraftSelector']):
    if draft_selector is None:
      del self.draft_selector
      return
    if not isinstance(draft_selector, DraftSelector):
      raise TypeError('draft_selector must be of type DraftSelector')
    del self.version_id_selector
    del self.published_latest_selector
    del self.published_number_selector
    del self.benchmark_slug_selector
    self._draft_selector = draft_selector

  @property
  def benchmark_slug_selector(self) -> Optional['BenchmarkSlugSelector']:
    return self._benchmark_slug_selector or None

  @benchmark_slug_selector.setter
  def benchmark_slug_selector(self, benchmark_slug_selector: Optional['BenchmarkSlugSelector']):
    if benchmark_slug_selector is None:
      del self.benchmark_slug_selector
      return
    if not isinstance(benchmark_slug_selector, BenchmarkSlugSelector):
      raise TypeError('benchmark_slug_selector must be of type BenchmarkSlugSelector')
    del self.version_id_selector
    del self.published_latest_selector
    del self.published_number_selector
    del self.draft_selector
    self._benchmark_slug_selector = benchmark_slug_selector


class DraftSelector(KaggleObject):
  r"""
  Select by the parent benchmark's single draft version (always exists).

  Attributes:
    parent_benchmark_identifier (BenchmarkIdentifier)
  """

  def __init__(self):
    self._parent_benchmark_identifier = None
    self._freeze()

  @property
  def parent_benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    return self._parent_benchmark_identifier

  @parent_benchmark_identifier.setter
  def parent_benchmark_identifier(self, parent_benchmark_identifier: Optional['BenchmarkIdentifier']):
    if parent_benchmark_identifier is None:
      del self.parent_benchmark_identifier
      return
    if not isinstance(parent_benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('parent_benchmark_identifier must be of type BenchmarkIdentifier')
    self._parent_benchmark_identifier = parent_benchmark_identifier


class PublishedLatestSelector(KaggleObject):
  r"""
  Select by the parent benchmark's latest published version, defaults to NULL.

  Attributes:
    parent_benchmark_identifier (BenchmarkIdentifier)
  """

  def __init__(self):
    self._parent_benchmark_identifier = None
    self._freeze()

  @property
  def parent_benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    return self._parent_benchmark_identifier

  @parent_benchmark_identifier.setter
  def parent_benchmark_identifier(self, parent_benchmark_identifier: Optional['BenchmarkIdentifier']):
    if parent_benchmark_identifier is None:
      del self.parent_benchmark_identifier
      return
    if not isinstance(parent_benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('parent_benchmark_identifier must be of type BenchmarkIdentifier')
    self._parent_benchmark_identifier = parent_benchmark_identifier


class PublishedNumberSelector(KaggleObject):
  r"""
  Select by the parent benchmark's published version at a particular version
  number. Defaults to NULL.

  Attributes:
    parent_benchmark_identifier (BenchmarkIdentifier)
    version_number (int)
  """

  def __init__(self):
    self._parent_benchmark_identifier = None
    self._version_number = 0
    self._freeze()

  @property
  def parent_benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    return self._parent_benchmark_identifier

  @parent_benchmark_identifier.setter
  def parent_benchmark_identifier(self, parent_benchmark_identifier: Optional['BenchmarkIdentifier']):
    if parent_benchmark_identifier is None:
      del self.parent_benchmark_identifier
      return
    if not isinstance(parent_benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('parent_benchmark_identifier must be of type BenchmarkIdentifier')
    self._parent_benchmark_identifier = parent_benchmark_identifier

  @property
  def version_number(self) -> int:
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number


class VersionIdSelector(KaggleObject):
  r"""
  Select by the benchmark version id. Optional parent benchmark id.

  Attributes:
    parent_benchmark_identifier (BenchmarkIdentifier)
    id (int)
  """

  def __init__(self):
    self._parent_benchmark_identifier = None
    self._id = 0
    self._freeze()

  @property
  def parent_benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    return self._parent_benchmark_identifier or None

  @parent_benchmark_identifier.setter
  def parent_benchmark_identifier(self, parent_benchmark_identifier: Optional[Optional['BenchmarkIdentifier']]):
    if parent_benchmark_identifier is None:
      del self.parent_benchmark_identifier
      return
    if not isinstance(parent_benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('parent_benchmark_identifier must be of type BenchmarkIdentifier')
    self._parent_benchmark_identifier = parent_benchmark_identifier

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id


class BenchmarkIdentifier(KaggleObject):
  r"""
  Identifier for selecting a specific benchmark.

  Attributes:
    id (int)
    slug (str)
  """

  def __init__(self):
    self._id = None
    self._slug = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    del self.slug
    self._id = id

  @property
  def slug(self) -> str:
    return self._slug or ""

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    del self.id
    self._slug = slug


class BenchmarkResult(KaggleObject):
  r"""
  TODO(bml): Integrate this proto with personal benchmarks trials.
  Represents the outcome of a benchmark run. All fields are immutable.

  Attributes:
    task_version_id (int)
      Convenience fields for this result (for the frontend):
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
  """

  def __init__(self):
    self._task_version_id = None
    self._numeric_result = None
    self._boolean_result = None
    self._custom_additional_results = []
    self._numeric_result_private = None
    self._numeric_result_public = None
    self._evaluation_date = None
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


class BenchmarkSlugSelector(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    benchmark_slug (str)
    version_number (int)
  """

  def __init__(self):
    self._owner_slug = ""
    self._benchmark_slug = ""
    self._version_number = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def benchmark_slug(self) -> str:
    return self._benchmark_slug

  @benchmark_slug.setter
  def benchmark_slug(self, benchmark_slug: str):
    if benchmark_slug is None:
      del self.benchmark_slug
      return
    if not isinstance(benchmark_slug, str):
      raise TypeError('benchmark_slug must be of type str')
    self._benchmark_slug = benchmark_slug

  @property
  def version_number(self) -> int:
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number


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


BenchmarkVersionIdentifier._fields = [
  FieldMetadata("versionIdSelector", "version_id_selector", "_version_id_selector", VersionIdSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("publishedLatestSelector", "published_latest_selector", "_published_latest_selector", PublishedLatestSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("publishedNumberSelector", "published_number_selector", "_published_number_selector", PublishedNumberSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("draftSelector", "draft_selector", "_draft_selector", DraftSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("benchmarkSlugSelector", "benchmark_slug_selector", "_benchmark_slug_selector", BenchmarkSlugSelector, None, KaggleObjectSerializer(), optional=True),
]

DraftSelector._fields = [
  FieldMetadata("parentBenchmarkIdentifier", "parent_benchmark_identifier", "_parent_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer()),
]

PublishedLatestSelector._fields = [
  FieldMetadata("parentBenchmarkIdentifier", "parent_benchmark_identifier", "_parent_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer()),
]

PublishedNumberSelector._fields = [
  FieldMetadata("parentBenchmarkIdentifier", "parent_benchmark_identifier", "_parent_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
]

VersionIdSelector._fields = [
  FieldMetadata("parentBenchmarkIdentifier", "parent_benchmark_identifier", "_parent_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

BenchmarkIdentifier._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
]

BenchmarkResult._fields = [
  FieldMetadata("taskVersionId", "task_version_id", "_task_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("numericResult", "numeric_result", "_numeric_result", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("booleanResult", "boolean_result", "_boolean_result", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("customAdditionalResults", "custom_additional_results", "_custom_additional_results", CustomResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("numericResultPrivate", "numeric_result_private", "_numeric_result_private", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("numericResultPublic", "numeric_result_public", "_numeric_result_public", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("evaluationDate", "evaluation_date", "_evaluation_date", datetime, None, DateTimeSerializer(), optional=True),
]

BenchmarkSlugSelector._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("benchmarkSlug", "benchmark_slug", "_benchmark_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
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

