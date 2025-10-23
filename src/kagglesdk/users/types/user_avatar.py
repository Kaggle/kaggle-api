from kagglesdk.kaggle_object import *
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional

class UserAvatar(KaggleObject):
  r"""
  Attributes:
    display_name (str)
      Display name for the given user
    thumbnail_url (str)
      Thumbnail URL for the given user
    url (str)
      Profile URL for the given user
    user_name (str)
      User name for the given user
    tier (UserAchievementTier)
      Tier for the given user
    id (int)
      ID for the given user
    profile_url (str)
      Alternate name for 'url', to aid in refactoring both are provided.
      TODO(http://b/402224065) remove once clients have migrated from this.
    performance_tier (UserAchievementTier)
      Alternate name for `tier`, to aid in refactoring both are provided.
      TODO(http://b/402224065) remove once clients have migrated from this.
    user_id (int)
      Alternate name for `id`, to aid in refactoring both are provided.
      TODO(http://b/402224065) remove once clients have migrated from this.
    progression_opt_out (bool)
      True if the user is opted out of the progression system.
    is_phone_verified (bool)
      True if the user is phone verified
  """

  def __init__(self):
    self._display_name = None
    self._thumbnail_url = None
    self._url = None
    self._user_name = None
    self._tier = UserAchievementTier.NOVICE
    self._id = 0
    self._profile_url = None
    self._performance_tier = None
    self._user_id = None
    self._progression_opt_out = None
    self._is_phone_verified = None
    self._freeze()

  @property
  def display_name(self) -> str:
    """Display name for the given user"""
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def thumbnail_url(self) -> str:
    """Thumbnail URL for the given user"""
    return self._thumbnail_url or ""

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: Optional[str]):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

  @property
  def url(self) -> str:
    """Profile URL for the given user"""
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
  def profile_url(self) -> str:
    r"""
    Alternate name for 'url', to aid in refactoring both are provided.
    TODO(http://b/402224065) remove once clients have migrated from this.
    """
    return self._profile_url or ""

  @profile_url.setter
  def profile_url(self, profile_url: Optional[str]):
    if profile_url is None:
      del self.profile_url
      return
    if not isinstance(profile_url, str):
      raise TypeError('profile_url must be of type str')
    self._profile_url = profile_url

  @property
  def user_name(self) -> str:
    """User name for the given user"""
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: Optional[str]):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def tier(self) -> 'UserAchievementTier':
    """Tier for the given user"""
    return self._tier

  @tier.setter
  def tier(self, tier: 'UserAchievementTier'):
    if tier is None:
      del self.tier
      return
    if not isinstance(tier, UserAchievementTier):
      raise TypeError('tier must be of type UserAchievementTier')
    self._tier = tier

  @property
  def performance_tier(self) -> 'UserAchievementTier':
    r"""
    Alternate name for `tier`, to aid in refactoring both are provided.
    TODO(http://b/402224065) remove once clients have migrated from this.
    """
    return self._performance_tier or UserAchievementTier.NOVICE

  @performance_tier.setter
  def performance_tier(self, performance_tier: Optional['UserAchievementTier']):
    if performance_tier is None:
      del self.performance_tier
      return
    if not isinstance(performance_tier, UserAchievementTier):
      raise TypeError('performance_tier must be of type UserAchievementTier')
    self._performance_tier = performance_tier

  @property
  def id(self) -> int:
    """ID for the given user"""
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
  def user_id(self) -> int:
    r"""
    Alternate name for `id`, to aid in refactoring both are provided.
    TODO(http://b/402224065) remove once clients have migrated from this.
    """
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def progression_opt_out(self) -> bool:
    """True if the user is opted out of the progression system."""
    return self._progression_opt_out or False

  @progression_opt_out.setter
  def progression_opt_out(self, progression_opt_out: Optional[bool]):
    if progression_opt_out is None:
      del self.progression_opt_out
      return
    if not isinstance(progression_opt_out, bool):
      raise TypeError('progression_opt_out must be of type bool')
    self._progression_opt_out = progression_opt_out

  @property
  def is_phone_verified(self) -> bool:
    """True if the user is phone verified"""
    return self._is_phone_verified or False

  @is_phone_verified.setter
  def is_phone_verified(self, is_phone_verified: Optional[bool]):
    if is_phone_verified is None:
      del self.is_phone_verified
      return
    if not isinstance(is_phone_verified, bool):
      raise TypeError('is_phone_verified must be of type bool')
    self._is_phone_verified = is_phone_verified


UserAvatar._fields = [
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("profileUrl", "profile_url", "_profile_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("performanceTier", "performance_tier", "_performance_tier", UserAchievementTier, None, EnumSerializer(), optional=True),
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("progressionOptOut", "progression_opt_out", "_progression_opt_out", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPhoneVerified", "is_phone_verified", "_is_phone_verified", bool, None, PredefinedSerializer(), optional=True),
]

