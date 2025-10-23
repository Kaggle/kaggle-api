from kagglesdk.kaggle_object import *
from kagglesdk.users.types.groups_enum import GroupMembershipRole
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class UserManagedGroup(KaggleObject):
  r"""
  Attributes:
    id (int)
    name (str)
    slug (str)
    description (str)
    owner (UserAvatar)
    member_count (int)
    current_user_role (GroupMembershipRole)
    avatar_infos (UserAvatar)
      List of up to three avatars sorted by join date.
    share_token (str)
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._slug = ""
    self._description = None
    self._owner = None
    self._member_count = None
    self._current_user_role = None
    self._avatar_infos = []
    self._share_token = None
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
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def owner(self) -> Optional['UserAvatar']:
    return self._owner or None

  @owner.setter
  def owner(self, owner: Optional[Optional['UserAvatar']]):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, UserAvatar):
      raise TypeError('owner must be of type UserAvatar')
    self._owner = owner

  @property
  def member_count(self) -> int:
    return self._member_count or 0

  @member_count.setter
  def member_count(self, member_count: Optional[int]):
    if member_count is None:
      del self.member_count
      return
    if not isinstance(member_count, int):
      raise TypeError('member_count must be of type int')
    self._member_count = member_count

  @property
  def current_user_role(self) -> 'GroupMembershipRole':
    return self._current_user_role or GroupMembershipRole.GROUP_MEMBERSHIP_ROLE_UNSPECIFIED

  @current_user_role.setter
  def current_user_role(self, current_user_role: Optional['GroupMembershipRole']):
    if current_user_role is None:
      del self.current_user_role
      return
    if not isinstance(current_user_role, GroupMembershipRole):
      raise TypeError('current_user_role must be of type GroupMembershipRole')
    self._current_user_role = current_user_role

  @property
  def avatar_infos(self) -> Optional[List[Optional['UserAvatar']]]:
    """List of up to three avatars sorted by join date."""
    return self._avatar_infos

  @avatar_infos.setter
  def avatar_infos(self, avatar_infos: Optional[List[Optional['UserAvatar']]]):
    if avatar_infos is None:
      del self.avatar_infos
      return
    if not isinstance(avatar_infos, list):
      raise TypeError('avatar_infos must be of type list')
    if not all([isinstance(t, UserAvatar) for t in avatar_infos]):
      raise TypeError('avatar_infos must contain only items of type UserAvatar')
    self._avatar_infos = avatar_infos

  @property
  def share_token(self) -> str:
    return self._share_token or ""

  @share_token.setter
  def share_token(self, share_token: Optional[str]):
    if share_token is None:
      del self.share_token
      return
    if not isinstance(share_token, str):
      raise TypeError('share_token must be of type str')
    self._share_token = share_token


UserManagedGroup._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("owner", "owner", "_owner", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("memberCount", "member_count", "_member_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("currentUserRole", "current_user_role", "_current_user_role", GroupMembershipRole, None, EnumSerializer(), optional=True),
  FieldMetadata("avatarInfos", "avatar_infos", "_avatar_infos", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("shareToken", "share_token", "_share_token", str, None, PredefinedSerializer(), optional=True),
]

