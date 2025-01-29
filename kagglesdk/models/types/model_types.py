from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.models.types.model_enums import GatingAgreementRequestsExpiryStatus, GatingAgreementRequestsReviewStatus, ModelFramework, ModelVersionLinkType
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional

class BaseModelInstanceInformation(KaggleObject):
  r"""
  Attributes:
    id (int)
    owner (Owner)
    model_slug (str)
    instance_slug (str)
    framework (ModelFramework)
  """

  def __init__(self):
    self._id = 0
    self._owner = None
    self._model_slug = ""
    self._instance_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
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
  def owner(self) -> Optional['Owner']:
    return self._owner

  @owner.setter
  def owner(self, owner: Optional['Owner']):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, Owner):
      raise TypeError('owner must be of type Owner')
    self._owner = owner

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
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

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


class GatingUserConsent(KaggleObject):
  r"""
  Attributes:
    id (int)
    agreement_id (int)
    user_id (int)
    request_data (str)
    request_time (datetime)
    review_time (datetime)
    review_status (GatingAgreementRequestsReviewStatus)
    expiry_status (GatingAgreementRequestsExpiryStatus)
    expiry_time (datetime)
    publisher_notes (str)
  """

  def __init__(self):
    self._id = 0
    self._agreement_id = 0
    self._user_id = 0
    self._request_data = None
    self._request_time = None
    self._review_time = None
    self._review_status = GatingAgreementRequestsReviewStatus.GATING_AGREEMENT_REQUESTS_REVIEW_STATUS_UNSPECIFIED
    self._expiry_status = GatingAgreementRequestsExpiryStatus.GATING_AGREEMENT_REQUESTS_EXPIRY_STATUS_UNSPECIFIED
    self._expiry_time = None
    self._publisher_notes = None
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
  def agreement_id(self) -> int:
    return self._agreement_id

  @agreement_id.setter
  def agreement_id(self, agreement_id: int):
    if agreement_id is None:
      del self.agreement_id
      return
    if not isinstance(agreement_id, int):
      raise TypeError('agreement_id must be of type int')
    self._agreement_id = agreement_id

  @property
  def user_id(self) -> int:
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def request_data(self) -> str:
    return self._request_data or ""

  @request_data.setter
  def request_data(self, request_data: str):
    if request_data is None:
      del self.request_data
      return
    if not isinstance(request_data, str):
      raise TypeError('request_data must be of type str')
    self._request_data = request_data

  @property
  def request_time(self) -> datetime:
    return self._request_time

  @request_time.setter
  def request_time(self, request_time: datetime):
    if request_time is None:
      del self.request_time
      return
    if not isinstance(request_time, datetime):
      raise TypeError('request_time must be of type datetime')
    self._request_time = request_time

  @property
  def review_time(self) -> datetime:
    return self._review_time or None

  @review_time.setter
  def review_time(self, review_time: datetime):
    if review_time is None:
      del self.review_time
      return
    if not isinstance(review_time, datetime):
      raise TypeError('review_time must be of type datetime')
    self._review_time = review_time

  @property
  def review_status(self) -> 'GatingAgreementRequestsReviewStatus':
    return self._review_status

  @review_status.setter
  def review_status(self, review_status: 'GatingAgreementRequestsReviewStatus'):
    if review_status is None:
      del self.review_status
      return
    if not isinstance(review_status, GatingAgreementRequestsReviewStatus):
      raise TypeError('review_status must be of type GatingAgreementRequestsReviewStatus')
    self._review_status = review_status

  @property
  def expiry_status(self) -> 'GatingAgreementRequestsExpiryStatus':
    return self._expiry_status

  @expiry_status.setter
  def expiry_status(self, expiry_status: 'GatingAgreementRequestsExpiryStatus'):
    if expiry_status is None:
      del self.expiry_status
      return
    if not isinstance(expiry_status, GatingAgreementRequestsExpiryStatus):
      raise TypeError('expiry_status must be of type GatingAgreementRequestsExpiryStatus')
    self._expiry_status = expiry_status

  @property
  def expiry_time(self) -> datetime:
    return self._expiry_time or None

  @expiry_time.setter
  def expiry_time(self, expiry_time: datetime):
    if expiry_time is None:
      del self.expiry_time
      return
    if not isinstance(expiry_time, datetime):
      raise TypeError('expiry_time must be of type datetime')
    self._expiry_time = expiry_time

  @property
  def publisher_notes(self) -> str:
    return self._publisher_notes or ""

  @publisher_notes.setter
  def publisher_notes(self, publisher_notes: str):
    if publisher_notes is None:
      del self.publisher_notes
      return
    if not isinstance(publisher_notes, str):
      raise TypeError('publisher_notes must be of type str')
    self._publisher_notes = publisher_notes


class ModelLink(KaggleObject):
  r"""
  Attributes:
    type (ModelVersionLinkType)
    url (str)
  """

  def __init__(self):
    self._type = ModelVersionLinkType.MODEL_VERSION_LINK_TYPE_UNSPECIFIED
    self._url = ""
    self._freeze()

  @property
  def type(self) -> 'ModelVersionLinkType':
    return self._type

  @type.setter
  def type(self, type: 'ModelVersionLinkType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ModelVersionLinkType):
      raise TypeError('type must be of type ModelVersionLinkType')
    self._type = type

  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class Owner(KaggleObject):
  r"""
  Based off Datasets OwnerDto as the permission model is the same
  Separate message since Models don't have max_file_size_bytes.
  Consider renaming more generically to apply to Users/Orgs
  interchangeably without a strict concept of ownership

  Attributes:
    id (int)
    image_url (str)
    is_organization (bool)
    name (str)
    profile_url (str)
    slug (str)
    user_tier (UserAchievementTier)
  """

  def __init__(self):
    self._id = 0
    self._image_url = None
    self._is_organization = False
    self._name = ""
    self._profile_url = None
    self._slug = ""
    self._user_tier = UserAchievementTier.NOVICE
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
  def image_url(self) -> str:
    return self._image_url or ""

  @image_url.setter
  def image_url(self, image_url: str):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def is_organization(self) -> bool:
    return self._is_organization

  @is_organization.setter
  def is_organization(self, is_organization: bool):
    if is_organization is None:
      del self.is_organization
      return
    if not isinstance(is_organization, bool):
      raise TypeError('is_organization must be of type bool')
    self._is_organization = is_organization

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
  def profile_url(self) -> str:
    return self._profile_url or ""

  @profile_url.setter
  def profile_url(self, profile_url: str):
    if profile_url is None:
      del self.profile_url
      return
    if not isinstance(profile_url, str):
      raise TypeError('profile_url must be of type str')
    self._profile_url = profile_url

  @property
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def user_tier(self) -> 'UserAchievementTier':
    return self._user_tier

  @user_tier.setter
  def user_tier(self, user_tier: 'UserAchievementTier'):
    if user_tier is None:
      del self.user_tier
      return
    if not isinstance(user_tier, UserAchievementTier):
      raise TypeError('user_tier must be of type UserAchievementTier')
    self._user_tier = user_tier


BaseModelInstanceInformation._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("owner", "owner", "_owner", Owner, None, KaggleObjectSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
]

GatingUserConsent._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("agreementId", "agreement_id", "_agreement_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("requestData", "request_data", "_request_data", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("requestTime", "request_time", "_request_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("reviewTime", "review_time", "_review_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("reviewStatus", "review_status", "_review_status", GatingAgreementRequestsReviewStatus, GatingAgreementRequestsReviewStatus.GATING_AGREEMENT_REQUESTS_REVIEW_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("expiryStatus", "expiry_status", "_expiry_status", GatingAgreementRequestsExpiryStatus, GatingAgreementRequestsExpiryStatus.GATING_AGREEMENT_REQUESTS_EXPIRY_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("expiryTime", "expiry_time", "_expiry_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("publisherNotes", "publisher_notes", "_publisher_notes", str, None, PredefinedSerializer(), optional=True),
]

ModelLink._fields = [
  FieldMetadata("type", "type", "_type", ModelVersionLinkType, ModelVersionLinkType.MODEL_VERSION_LINK_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
]

Owner._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isOrganization", "is_organization", "_is_organization", bool, False, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("profileUrl", "profile_url", "_profile_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("userTier", "user_tier", "_user_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
]

