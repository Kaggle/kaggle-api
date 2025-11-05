from kagglesdk.kaggle_object import *
from typing import Optional, List

class ApiGroupMembership(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    username (str)
  """

  def __init__(self):
    self._user_id = 0
    self._username = ""
    self._freeze()

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
  def username(self) -> str:
    return self._username

  @username.setter
  def username(self, username: str):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    self._username = username


class ApiListSynchronizedGroupMembershipsRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    page_token (str)
    skip (int)
    group_slug (str)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = None
    self._skip = None
    self._group_slug = ""
    self._freeze()

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def group_slug(self) -> str:
    return self._group_slug

  @group_slug.setter
  def group_slug(self, group_slug: str):
    if group_slug is None:
      del self.group_slug
      return
    if not isinstance(group_slug, str):
      raise TypeError('group_slug must be of type str')
    self._group_slug = group_slug

  def endpoint(self):
    path = '/api/v1/sync_groups/{group_slug}/members'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/sync_groups/{group_slug}/members'


class ApiListSynchronizedGroupMembershipsResponse(KaggleObject):
  r"""
  Attributes:
    memberships (ApiGroupMembership)
    next_page_token (str)
  """

  def __init__(self):
    self._memberships = []
    self._next_page_token = ""
    self._freeze()

  @property
  def memberships(self) -> Optional[List[Optional['ApiGroupMembership']]]:
    return self._memberships

  @memberships.setter
  def memberships(self, memberships: Optional[List[Optional['ApiGroupMembership']]]):
    if memberships is None:
      del self.memberships
      return
    if not isinstance(memberships, list):
      raise TypeError('memberships must be of type list')
    if not all([isinstance(t, ApiGroupMembership) for t in memberships]):
      raise TypeError('memberships must contain only items of type ApiGroupMembership')
    self._memberships = memberships

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def nextPageToken(self):
    return self.next_page_token


class ApiListUserManagedGroupMembershipsRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    page_token (str)
    skip (int)
    group_slug (str)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = None
    self._skip = None
    self._group_slug = ""
    self._freeze()

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def group_slug(self) -> str:
    return self._group_slug

  @group_slug.setter
  def group_slug(self, group_slug: str):
    if group_slug is None:
      del self.group_slug
      return
    if not isinstance(group_slug, str):
      raise TypeError('group_slug must be of type str')
    self._group_slug = group_slug

  def endpoint(self):
    path = '/api/v1/groups/{group_slug}/members'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/groups/{group_slug}/members'


class ApiListUserManagedGroupMembershipsResponse(KaggleObject):
  r"""
  Attributes:
    memberships (ApiGroupMembership)
    next_page_token (str)
  """

  def __init__(self):
    self._memberships = []
    self._next_page_token = ""
    self._freeze()

  @property
  def memberships(self) -> Optional[List[Optional['ApiGroupMembership']]]:
    return self._memberships

  @memberships.setter
  def memberships(self, memberships: Optional[List[Optional['ApiGroupMembership']]]):
    if memberships is None:
      del self.memberships
      return
    if not isinstance(memberships, list):
      raise TypeError('memberships must be of type list')
    if not all([isinstance(t, ApiGroupMembership) for t in memberships]):
      raise TypeError('memberships must contain only items of type ApiGroupMembership')
    self._memberships = memberships

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def nextPageToken(self):
    return self.next_page_token


ApiGroupMembership._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("username", "username", "_username", str, "", PredefinedSerializer()),
]

ApiListSynchronizedGroupMembershipsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, "", PredefinedSerializer()),
]

ApiListSynchronizedGroupMembershipsResponse._fields = [
  FieldMetadata("memberships", "memberships", "_memberships", ApiGroupMembership, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ApiListUserManagedGroupMembershipsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, "", PredefinedSerializer()),
]

ApiListUserManagedGroupMembershipsResponse._fields = [
  FieldMetadata("memberships", "memberships", "_memberships", ApiGroupMembership, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

