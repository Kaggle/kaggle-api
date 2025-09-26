from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class UserLicenseAgreementStatus(enum.Enum):
  r"""
  This enum tracks the state of a user's agreement with respect to any
  license that requires it. For Llama 2, users will consent and after some
  time, Meta will indicate to us that they're approved.
  """
  USER_LICENSE_AGREEMENT_STATUS_UNSPECIFIED = 0
  """Default, unspecified."""
  USER_LICENSE_AGREEMENT_STATUS_PENDING = 1
  r"""
  Users in this status are waiting for review from the 3rd-party. Users in
  any specified status implicitly have consented to this review. The presence
  of a ConsentTime value in the UserLicenseAgreements table explicitly
  denotes if and when the user consented.
  """
  USER_LICENSE_AGREEMENT_STATUS_ACCEPTED = 2
  """3rd-party has approved the user's license agreement."""
  USER_LICENSE_AGREEMENT_STATUS_REJECTED = 3
  """3rd-party has rejected the user's license agreement."""
  USER_LICENSE_AGREEMENT_STATUS_EXPIRED = 4
  r"""
  Too much time has passed from when the user submitted the consent form and
  the license owner reviewed it
  """

class License(KaggleObject):
  r"""
  This proto is a subset of LicenseOption representing the currently selected
  License. It excludes any metadata needed to organize a selection of options
  (like display_sequence, etc.)

  Attributes:
    id (int)
    name (str)
    url (str)
    agreement_required (bool)
      Indicates whether this license requires agreement to its terms (e.g. Llama
      2, other custom license, etc.)
    agreement_status (UserLicenseAgreementStatus)
      Represents the status of the current user's agreement regarding this
      specific license. Only applicable when requires_agreement is true
    consent_time (datetime)
      If applicable, this is the time when the current user consented to the
      license agreement
    current_revision_number (int)
      If applicable, the current license revision number we want users to be
      accepting.
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._url = None
    self._agreement_required = None
    self._agreement_status = None
    self._consent_time = None
    self._current_revision_number = None
    self._freeze()

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

  @property
  def name(self) -> str:
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
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def agreement_required(self) -> bool:
    r"""
    Indicates whether this license requires agreement to its terms (e.g. Llama
    2, other custom license, etc.)
    """
    return self._agreement_required or False

  @agreement_required.setter
  def agreement_required(self, agreement_required: Optional[bool]):
    if agreement_required is None:
      del self.agreement_required
      return
    if not isinstance(agreement_required, bool):
      raise TypeError('agreement_required must be of type bool')
    self._agreement_required = agreement_required

  @property
  def agreement_status(self) -> 'UserLicenseAgreementStatus':
    r"""
    Represents the status of the current user's agreement regarding this
    specific license. Only applicable when requires_agreement is true
    """
    return self._agreement_status or UserLicenseAgreementStatus.USER_LICENSE_AGREEMENT_STATUS_UNSPECIFIED

  @agreement_status.setter
  def agreement_status(self, agreement_status: Optional['UserLicenseAgreementStatus']):
    if agreement_status is None:
      del self.agreement_status
      return
    if not isinstance(agreement_status, UserLicenseAgreementStatus):
      raise TypeError('agreement_status must be of type UserLicenseAgreementStatus')
    self._agreement_status = agreement_status

  @property
  def consent_time(self) -> datetime:
    r"""
    If applicable, this is the time when the current user consented to the
    license agreement
    """
    return self._consent_time or None

  @consent_time.setter
  def consent_time(self, consent_time: Optional[datetime]):
    if consent_time is None:
      del self.consent_time
      return
    if not isinstance(consent_time, datetime):
      raise TypeError('consent_time must be of type datetime')
    self._consent_time = consent_time

  @property
  def current_revision_number(self) -> int:
    r"""
    If applicable, the current license revision number we want users to be
    accepting.
    """
    return self._current_revision_number or 0

  @current_revision_number.setter
  def current_revision_number(self, current_revision_number: Optional[int]):
    if current_revision_number is None:
      del self.current_revision_number
      return
    if not isinstance(current_revision_number, int):
      raise TypeError('current_revision_number must be of type int')
    self._current_revision_number = current_revision_number


License._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agreementRequired", "agreement_required", "_agreement_required", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agreementStatus", "agreement_status", "_agreement_status", UserLicenseAgreementStatus, None, EnumSerializer(), optional=True),
  FieldMetadata("consentTime", "consent_time", "_consent_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("currentRevisionNumber", "current_revision_number", "_current_revision_number", int, None, PredefinedSerializer(), optional=True),
]

