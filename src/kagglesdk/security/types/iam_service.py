from kagglesdk.community.types.organization import Organization
from kagglesdk.kaggle_object import *
from kagglesdk.security.types.roles import CanonicalRole
from kagglesdk.security.types.security_types import KaggleResourceId
from kagglesdk.users.types.group_types import UserManagedGroup
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class GetIamPolicyRequest(KaggleObject):
  r"""
  Request to get the IAM policy for a resource.

  Attributes:
    resource_id (KaggleResourceId)
      ID of the resource for which to pull the policy.
  """

  def __init__(self):
    self._resource_id = None
    self._freeze()

  @property
  def resource_id(self) -> Optional['KaggleResourceId']:
    """ID of the resource for which to pull the policy."""
    return self._resource_id

  @resource_id.setter
  def resource_id(self, resource_id: Optional['KaggleResourceId']):
    if resource_id is None:
      del self.resource_id
      return
    if not isinstance(resource_id, KaggleResourceId):
      raise TypeError('resource_id must be of type KaggleResourceId')
    self._resource_id = resource_id

  def endpoint(self):
    path = '/api/v1/iam/get/{resource_id}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/iam/get/{resource_id}'


class GroupPrincipal(KaggleObject):
  r"""
  Attributes:
    id (int)
    slug (str)
    avatar (UserManagedGroup)
  """

  def __init__(self):
    self._id = None
    self._slug = None
    self._avatar = None
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

  @property
  def avatar(self) -> Optional['UserManagedGroup']:
    return self._avatar

  @avatar.setter
  def avatar(self, avatar: Optional['UserManagedGroup']):
    if avatar is None:
      del self.avatar
      return
    if not isinstance(avatar, UserManagedGroup):
      raise TypeError('avatar must be of type UserManagedGroup')
    self._avatar = avatar


class IamPolicy(KaggleObject):
  r"""
  Defines an Identity and Access Management (IAM) policy. It is used to
  specify access control policies for Kaggle resources.

  Attributes:
    bindings (IamPolicyBinding)
      Associates a list of `principals` with a `role`.
      If no binding is specified for a 'role' (see
      kaggle.security.CanonicalRole), existing bindings for that 'role' are left
      untouched. However, if a binding for a 'role' has no members (see
      IamPolicyBinding.members), all access to that 'role' is revoked.
    owner (Principal)
      Owner of the resource provided for informational purposes. This is an
      output only field, i.e., owner may not be changed even if this is set.
  """

  def __init__(self):
    self._bindings = []
    self._owner = None
    self._freeze()

  @property
  def bindings(self) -> Optional[List[Optional['IamPolicyBinding']]]:
    r"""
    Associates a list of `principals` with a `role`.
    If no binding is specified for a 'role' (see
    kaggle.security.CanonicalRole), existing bindings for that 'role' are left
    untouched. However, if a binding for a 'role' has no members (see
    IamPolicyBinding.members), all access to that 'role' is revoked.
    """
    return self._bindings

  @bindings.setter
  def bindings(self, bindings: Optional[List[Optional['IamPolicyBinding']]]):
    if bindings is None:
      del self.bindings
      return
    if not isinstance(bindings, list):
      raise TypeError('bindings must be of type list')
    if not all([isinstance(t, IamPolicyBinding) for t in bindings]):
      raise TypeError('bindings must contain only items of type IamPolicyBinding')
    self._bindings = bindings

  @property
  def owner(self) -> Optional['Principal']:
    r"""
    Owner of the resource provided for informational purposes. This is an
    output only field, i.e., owner may not be changed even if this is set.
    """
    return self._owner

  @owner.setter
  def owner(self, owner: Optional['Principal']):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, Principal):
      raise TypeError('owner must be of type Principal')
    self._owner = owner


class IamPolicyBinding(KaggleObject):
  r"""
  Associates a list of `principals` with a `role`.

  Attributes:
    role (CanonicalRole)
      Canonical role that is assigned to `members`.
      For example: `Viewer`, `Editor` and `Owner`.
    members (Principal)
      Specifies the principals requesting access for a Kaggle resource.
      If not specified or empty, revokes access to 'role'. Otherwise, sets the
      members to the specified value. In other words, overrides existing members
      are overriden so if you want to add a new member, you need to specify
      existing members as well.
  """

  def __init__(self):
    self._role = CanonicalRole.CANONICAL_ROLE_UNSPECIFIED
    self._members = []
    self._freeze()

  @property
  def role(self) -> 'CanonicalRole':
    r"""
    Canonical role that is assigned to `members`.
    For example: `Viewer`, `Editor` and `Owner`.
    """
    return self._role

  @role.setter
  def role(self, role: 'CanonicalRole'):
    if role is None:
      del self.role
      return
    if not isinstance(role, CanonicalRole):
      raise TypeError('role must be of type CanonicalRole')
    self._role = role

  @property
  def members(self) -> Optional[List[Optional['Principal']]]:
    r"""
    Specifies the principals requesting access for a Kaggle resource.
    If not specified or empty, revokes access to 'role'. Otherwise, sets the
    members to the specified value. In other words, overrides existing members
    are overriden so if you want to add a new member, you need to specify
    existing members as well.
    """
    return self._members

  @members.setter
  def members(self, members: Optional[List[Optional['Principal']]]):
    if members is None:
      del self.members
      return
    if not isinstance(members, list):
      raise TypeError('members must be of type list')
    if not all([isinstance(t, Principal) for t in members]):
      raise TypeError('members must contain only items of type Principal')
    self._members = members


class OrganizationPrincipal(KaggleObject):
  r"""
  Attributes:
    id (int)
    avatar (Organization)
  """

  def __init__(self):
    self._id = 0
    self._avatar = None
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
  def avatar(self) -> Optional['Organization']:
    return self._avatar

  @avatar.setter
  def avatar(self, avatar: Optional['Organization']):
    if avatar is None:
      del self.avatar
      return
    if not isinstance(avatar, Organization):
      raise TypeError('avatar must be of type Organization')
    self._avatar = avatar


class Principal(KaggleObject):
  r"""
  Represents a principal of an IAM policy binding.

  Attributes:
    user (UserPrincipal)
    group (GroupPrincipal)
    organization (OrganizationPrincipal)
    name (str)
  """

  def __init__(self):
    self._user = None
    self._group = None
    self._organization = None
    self._name = ""
    self._freeze()

  @property
  def user(self) -> Optional['UserPrincipal']:
    return self._user or None

  @user.setter
  def user(self, user: Optional['UserPrincipal']):
    if user is None:
      del self.user
      return
    if not isinstance(user, UserPrincipal):
      raise TypeError('user must be of type UserPrincipal')
    del self.group
    del self.organization
    self._user = user

  @property
  def group(self) -> Optional['GroupPrincipal']:
    return self._group or None

  @group.setter
  def group(self, group: Optional['GroupPrincipal']):
    if group is None:
      del self.group
      return
    if not isinstance(group, GroupPrincipal):
      raise TypeError('group must be of type GroupPrincipal')
    del self.user
    del self.organization
    self._group = group

  @property
  def organization(self) -> Optional['OrganizationPrincipal']:
    return self._organization or None

  @organization.setter
  def organization(self, organization: Optional['OrganizationPrincipal']):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationPrincipal):
      raise TypeError('organization must be of type OrganizationPrincipal')
    del self.user
    del self.group
    self._organization = organization

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


class SetIamPolicyRequest(KaggleObject):
  r"""
  Request to set the IAM policy for a resource.

  Attributes:
    resource_id (KaggleResourceId)
      ID of the resource for which the policy is being specified.
    policy (IamPolicy)
      The complete policy to be applied to the resource.
  """

  def __init__(self):
    self._resource_id = None
    self._policy = None
    self._freeze()

  @property
  def resource_id(self) -> Optional['KaggleResourceId']:
    """ID of the resource for which the policy is being specified."""
    return self._resource_id

  @resource_id.setter
  def resource_id(self, resource_id: Optional['KaggleResourceId']):
    if resource_id is None:
      del self.resource_id
      return
    if not isinstance(resource_id, KaggleResourceId):
      raise TypeError('resource_id must be of type KaggleResourceId')
    self._resource_id = resource_id

  @property
  def policy(self) -> Optional['IamPolicy']:
    """The complete policy to be applied to the resource."""
    return self._policy

  @policy.setter
  def policy(self, policy: Optional['IamPolicy']):
    if policy is None:
      del self.policy
      return
    if not isinstance(policy, IamPolicy):
      raise TypeError('policy must be of type IamPolicy')
    self._policy = policy

  def endpoint(self):
    path = '/api/v1/iam/set/{resource_id}/{policy}'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class UserPrincipal(KaggleObject):
  r"""
  Attributes:
    id (int)
    user_name (str)
    avatar (UserAvatar)
  """

  def __init__(self):
    self._id = None
    self._user_name = None
    self._avatar = None
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
    del self.user_name
    self._id = id

  @property
  def user_name(self) -> str:
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    del self.id
    self._user_name = user_name

  @property
  def avatar(self) -> Optional['UserAvatar']:
    return self._avatar

  @avatar.setter
  def avatar(self, avatar: Optional['UserAvatar']):
    if avatar is None:
      del self.avatar
      return
    if not isinstance(avatar, UserAvatar):
      raise TypeError('avatar must be of type UserAvatar')
    self._avatar = avatar


GetIamPolicyRequest._fields = [
  FieldMetadata("resourceId", "resource_id", "_resource_id", KaggleResourceId, None, KaggleObjectSerializer()),
]

GroupPrincipal._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("avatar", "avatar", "_avatar", UserManagedGroup, None, KaggleObjectSerializer()),
]

IamPolicy._fields = [
  FieldMetadata("bindings", "bindings", "_bindings", IamPolicyBinding, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("owner", "owner", "_owner", Principal, None, KaggleObjectSerializer()),
]

IamPolicyBinding._fields = [
  FieldMetadata("role", "role", "_role", CanonicalRole, CanonicalRole.CANONICAL_ROLE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("members", "members", "_members", Principal, [], ListSerializer(KaggleObjectSerializer())),
]

OrganizationPrincipal._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("avatar", "avatar", "_avatar", Organization, None, KaggleObjectSerializer()),
]

Principal._fields = [
  FieldMetadata("user", "user", "_user", UserPrincipal, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("group", "group", "_group", GroupPrincipal, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", OrganizationPrincipal, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
]

SetIamPolicyRequest._fields = [
  FieldMetadata("resourceId", "resource_id", "_resource_id", KaggleResourceId, None, KaggleObjectSerializer()),
  FieldMetadata("policy", "policy", "_policy", IamPolicy, None, KaggleObjectSerializer()),
]

UserPrincipal._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("avatar", "avatar", "_avatar", UserAvatar, None, KaggleObjectSerializer()),
]

