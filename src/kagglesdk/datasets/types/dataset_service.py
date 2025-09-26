from datetime import datetime
from kagglesdk.datasets.types.dataset_enums import DatabundleVersionStatus
from kagglesdk.kaggle_object import *
from typing import Optional

class DatabundleVersionCreationStatus(KaggleObject):
  r"""
  Attributes:
    status (DatabundleVersionStatus)
    creation_percent_complete (float)
    creation_exception (str)
    creation_last_update (datetime)
    creation_step (str)
    creation_start (datetime)
    user_message (str)
    version_number (int)
  """

  def __init__(self):
    self._status = DatabundleVersionStatus.NOT_YET_PERSISTED
    self._creation_percent_complete = 0.0
    self._creation_exception = None
    self._creation_last_update = None
    self._creation_step = None
    self._creation_start = None
    self._user_message = None
    self._version_number = None
    self._freeze()

  @property
  def status(self) -> 'DatabundleVersionStatus':
    return self._status

  @status.setter
  def status(self, status: 'DatabundleVersionStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, DatabundleVersionStatus):
      raise TypeError('status must be of type DatabundleVersionStatus')
    self._status = status

  @property
  def creation_percent_complete(self) -> float:
    return self._creation_percent_complete

  @creation_percent_complete.setter
  def creation_percent_complete(self, creation_percent_complete: float):
    if creation_percent_complete is None:
      del self.creation_percent_complete
      return
    if not isinstance(creation_percent_complete, float):
      raise TypeError('creation_percent_complete must be of type float')
    self._creation_percent_complete = creation_percent_complete

  @property
  def creation_exception(self) -> str:
    return self._creation_exception or ""

  @creation_exception.setter
  def creation_exception(self, creation_exception: Optional[str]):
    if creation_exception is None:
      del self.creation_exception
      return
    if not isinstance(creation_exception, str):
      raise TypeError('creation_exception must be of type str')
    self._creation_exception = creation_exception

  @property
  def creation_last_update(self) -> datetime:
    return self._creation_last_update

  @creation_last_update.setter
  def creation_last_update(self, creation_last_update: datetime):
    if creation_last_update is None:
      del self.creation_last_update
      return
    if not isinstance(creation_last_update, datetime):
      raise TypeError('creation_last_update must be of type datetime')
    self._creation_last_update = creation_last_update

  @property
  def creation_step(self) -> str:
    return self._creation_step or ""

  @creation_step.setter
  def creation_step(self, creation_step: Optional[str]):
    if creation_step is None:
      del self.creation_step
      return
    if not isinstance(creation_step, str):
      raise TypeError('creation_step must be of type str')
    self._creation_step = creation_step

  @property
  def creation_start(self) -> datetime:
    return self._creation_start

  @creation_start.setter
  def creation_start(self, creation_start: datetime):
    if creation_start is None:
      del self.creation_start
      return
    if not isinstance(creation_start, datetime):
      raise TypeError('creation_start must be of type datetime')
    self._creation_start = creation_start

  @property
  def user_message(self) -> str:
    return self._user_message or ""

  @user_message.setter
  def user_message(self, user_message: Optional[str]):
    if user_message is None:
      del self.user_message
      return
    if not isinstance(user_message, str):
      raise TypeError('user_message must be of type str')
    self._user_message = user_message

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


DatabundleVersionCreationStatus._fields = [
  FieldMetadata("status", "status", "_status", DatabundleVersionStatus, DatabundleVersionStatus.NOT_YET_PERSISTED, EnumSerializer()),
  FieldMetadata("creationPercentComplete", "creation_percent_complete", "_creation_percent_complete", float, 0.0, PredefinedSerializer()),
  FieldMetadata("creationException", "creation_exception", "_creation_exception", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creationLastUpdate", "creation_last_update", "_creation_last_update", datetime, None, DateTimeSerializer()),
  FieldMetadata("creationStep", "creation_step", "_creation_step", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creationStart", "creation_start", "_creation_start", datetime, None, DateTimeSerializer()),
  FieldMetadata("userMessage", "user_message", "_user_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
]

