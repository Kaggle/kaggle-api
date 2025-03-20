from kagglesdk.kaggle_object import *
from typing import Optional, List

class AuthorizationScope(KaggleObject):
  r"""
  Attributes:
    resource_id (int)
    permission (AuthorizationPermissionScope)
    role (AuthorizationRoleScope)
  """

  def __init__(self):
    self._resource_id = 0
    self._permission = None
    self._role = None
    self._freeze()

  @property
  def resource_id(self) -> int:
    return self._resource_id

  @resource_id.setter
  def resource_id(self, resource_id: int):
    if resource_id is None:
      del self.resource_id
      return
    if not isinstance(resource_id, int):
      raise TypeError('resource_id must be of type int')
    self._resource_id = resource_id

  @property
  def permission(self) -> Optional['AuthorizationPermissionScope']:
    return self._permission or None

  @permission.setter
  def permission(self, permission: Optional['AuthorizationPermissionScope']):
    if permission is None:
      del self.permission
      return
    if not isinstance(permission, AuthorizationPermissionScope):
      raise TypeError('permission must be of type AuthorizationPermissionScope')
    del self.role
    self._permission = permission

  @property
  def role(self) -> Optional['AuthorizationRoleScope']:
    return self._role or None

  @role.setter
  def role(self, role: Optional['AuthorizationRoleScope']):
    if role is None:
      del self.role
      return
    if not isinstance(role, AuthorizationRoleScope):
      raise TypeError('role must be of type AuthorizationRoleScope')
    del self.permission
    self._role = role


class AuthorizationPermissionScope(KaggleObject):
  r"""
  Attributes:
    name (str)
    description (str)
  """

  def __init__(self):
    self._name = ""
    self._description = None
    self._freeze()

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
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description


class AuthorizationRoleScope(KaggleObject):
  r"""
  Attributes:
    name (str)
    description (str)
    permissions (AuthorizationPermissionScope)
  """

  def __init__(self):
    self._name = ""
    self._description = None
    self._permissions = []
    self._freeze()

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
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def permissions(self) -> Optional[List[Optional['AuthorizationPermissionScope']]]:
    return self._permissions

  @permissions.setter
  def permissions(self, permissions: Optional[List[Optional['AuthorizationPermissionScope']]]):
    if permissions is None:
      del self.permissions
      return
    if not isinstance(permissions, list):
      raise TypeError('permissions must be of type list')
    if not all([isinstance(t, AuthorizationPermissionScope) for t in permissions]):
      raise TypeError('permissions must contain only items of type AuthorizationPermissionScope')
    self._permissions = permissions


AuthorizationScope._fields = [
  FieldMetadata("resourceId", "resource_id", "_resource_id", int, 0, PredefinedSerializer()),
  FieldMetadata("permission", "permission", "_permission", AuthorizationPermissionScope, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("role", "role", "_role", AuthorizationRoleScope, None, KaggleObjectSerializer(), optional=True),
]

AuthorizationPermissionScope._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
]

AuthorizationRoleScope._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("permissions", "permissions", "_permissions", AuthorizationPermissionScope, [], ListSerializer(KaggleObjectSerializer())),
]

