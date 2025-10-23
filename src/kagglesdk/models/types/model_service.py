from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.models.types.model_enums import ModelFramework
from typing import Optional, List

class GetModelMetricsRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    start_time (datetime)
      Optional start time for the time series. A year ago by default.
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._start_time = None
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
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def start_time(self) -> datetime:
    """Optional start time for the time series. A year ago by default."""
    return self._start_time or None

  @start_time.setter
  def start_time(self, start_time: Optional[datetime]):
    if start_time is None:
      del self.start_time
      return
    if not isinstance(start_time, datetime):
      raise TypeError('start_time must be of type datetime')
    self._start_time = start_time

  def endpoint(self):
    path = '/api/v1/models/{owner_slug}/{model_slug}/metrics'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/models/{owner_slug}/{model_slug}/metrics'


class GetModelMetricsResponse(KaggleObject):
  r"""
  Attributes:
    metrics (ModelMetric)
  """

  def __init__(self):
    self._metrics = []
    self._freeze()

  @property
  def metrics(self) -> Optional[List[Optional['ModelMetric']]]:
    return self._metrics

  @metrics.setter
  def metrics(self, metrics: Optional[List[Optional['ModelMetric']]]):
    if metrics is None:
      del self.metrics
      return
    if not isinstance(metrics, list):
      raise TypeError('metrics must be of type list')
    if not all([isinstance(t, ModelMetric) for t in metrics]):
      raise TypeError('metrics must contain only items of type ModelMetric')
    self._metrics = metrics


class ModelInstanceMetric(KaggleObject):
  r"""
  Attributes:
    variation (str)
    framework (ModelFramework)
    downloads (int)
    notebooks (int)
  """

  def __init__(self):
    self._variation = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._downloads = 0
    self._notebooks = 0
    self._freeze()

  @property
  def variation(self) -> str:
    return self._variation

  @variation.setter
  def variation(self, variation: str):
    if variation is None:
      del self.variation
      return
    if not isinstance(variation, str):
      raise TypeError('variation must be of type str')
    self._variation = variation

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def downloads(self) -> int:
    return self._downloads

  @downloads.setter
  def downloads(self, downloads: int):
    if downloads is None:
      del self.downloads
      return
    if not isinstance(downloads, int):
      raise TypeError('downloads must be of type int')
    self._downloads = downloads

  @property
  def notebooks(self) -> int:
    return self._notebooks

  @notebooks.setter
  def notebooks(self, notebooks: int):
    if notebooks is None:
      del self.notebooks
      return
    if not isinstance(notebooks, int):
      raise TypeError('notebooks must be of type int')
    self._notebooks = notebooks


class ModelMetric(KaggleObject):
  r"""
  Attributes:
    date (str)
    views (int)
    downloads (int)
    notebooks (int)
    instances (ModelInstanceMetric)
  """

  def __init__(self):
    self._date = ""
    self._views = 0
    self._downloads = 0
    self._notebooks = 0
    self._instances = []
    self._freeze()

  @property
  def date(self) -> str:
    return self._date

  @date.setter
  def date(self, date: str):
    if date is None:
      del self.date
      return
    if not isinstance(date, str):
      raise TypeError('date must be of type str')
    self._date = date

  @property
  def views(self) -> int:
    return self._views

  @views.setter
  def views(self, views: int):
    if views is None:
      del self.views
      return
    if not isinstance(views, int):
      raise TypeError('views must be of type int')
    self._views = views

  @property
  def downloads(self) -> int:
    return self._downloads

  @downloads.setter
  def downloads(self, downloads: int):
    if downloads is None:
      del self.downloads
      return
    if not isinstance(downloads, int):
      raise TypeError('downloads must be of type int')
    self._downloads = downloads

  @property
  def notebooks(self) -> int:
    return self._notebooks

  @notebooks.setter
  def notebooks(self, notebooks: int):
    if notebooks is None:
      del self.notebooks
      return
    if not isinstance(notebooks, int):
      raise TypeError('notebooks must be of type int')
    self._notebooks = notebooks

  @property
  def instances(self) -> Optional[List[Optional['ModelInstanceMetric']]]:
    return self._instances

  @instances.setter
  def instances(self, instances: Optional[List[Optional['ModelInstanceMetric']]]):
    if instances is None:
      del self.instances
      return
    if not isinstance(instances, list):
      raise TypeError('instances must be of type list')
    if not all([isinstance(t, ModelInstanceMetric) for t in instances]):
      raise TypeError('instances must contain only items of type ModelInstanceMetric')
    self._instances = instances


GetModelMetricsRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("startTime", "start_time", "_start_time", datetime, None, DateTimeSerializer(), optional=True),
]

GetModelMetricsResponse._fields = [
  FieldMetadata("metrics", "metrics", "_metrics", ModelMetric, [], ListSerializer(KaggleObjectSerializer())),
]

ModelInstanceMetric._fields = [
  FieldMetadata("variation", "variation", "_variation", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("downloads", "downloads", "_downloads", int, 0, PredefinedSerializer()),
  FieldMetadata("notebooks", "notebooks", "_notebooks", int, 0, PredefinedSerializer()),
]

ModelMetric._fields = [
  FieldMetadata("date", "date", "_date", str, "", PredefinedSerializer()),
  FieldMetadata("views", "views", "_views", int, 0, PredefinedSerializer()),
  FieldMetadata("downloads", "downloads", "_downloads", int, 0, PredefinedSerializer()),
  FieldMetadata("notebooks", "notebooks", "_notebooks", int, 0, PredefinedSerializer()),
  FieldMetadata("instances", "instances", "_instances", ModelInstanceMetric, [], ListSerializer(KaggleObjectSerializer())),
]

