from kagglesdk.kaggle_object import *
from kagglesdk.models.types.model_enums import ModelFramework, ModelVersionLinkType
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
    allow_model_gating (bool)
  """

  def __init__(self):
    self._id = 0
    self._image_url = None
    self._is_organization = False
    self._name = ""
    self._profile_url = None
    self._slug = ""
    self._user_tier = UserAchievementTier.NOVICE
    self._allow_model_gating = None
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

  @property
  def allow_model_gating(self) -> bool:
    return self._allow_model_gating or False

  @allow_model_gating.setter
  def allow_model_gating(self, allow_model_gating: bool):
    if allow_model_gating is None:
      del self.allow_model_gating
      return
    if not isinstance(allow_model_gating, bool):
      raise TypeError('allow_model_gating must be of type bool')
    self._allow_model_gating = allow_model_gating


BaseModelInstanceInformation._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("owner", "owner", "_owner", Owner, None, KaggleObjectSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
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
  FieldMetadata("allowModelGating", "allow_model_gating", "_allow_model_gating", bool, None, PredefinedSerializer(), optional=True),
]

