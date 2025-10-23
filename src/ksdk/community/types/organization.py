from datetime import datetime
import enum
from kagglesdk.community.types.content_enums import ContentState
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class OrganizationCategory(enum.Enum):
  ORGANIZATION_CATEGORY_UNSPECIFIED = 0
  STUDY_GROUP = 1
  """Academic non-organization, e.g. student association"""
  COMPANY_OR_NON_PROFIT_OR_GOVERNMENT = 2
  """Indicates a company, non-profit, or government organization"""
  RESEARCH_LAB = 3
  r"""
  Academic / corporate research-focused organization, e.g. university or
  medical research
  """

class OrganizationMembershipType(enum.Enum):
  ORGANIZATION_MEMBERSHIP_TYPE_UNSPECIFIED = 0
  MEMBER = 1
  """Regular members of an organization"""
  OWNER = 2
  """The current owner of an organization"""
  CREATOR = 3
  """The original creator of an organization"""

class Organization(KaggleObject):
  r"""
  Attributes:
    name (str)
      Display name for an organization
    thumbnail_image_url (str)
      URL for a thumbnail image of an organization
    subtitle (str)
      Subtitle / tagline for an organization
    external_url (str)
      External website for an organization
    id (int)
      The organization's ID
    slug (str)
      Full slug for the organization
    featured_members (UserAvatar)
      A subset of the organization's members for displaying on an organization
      profile
    membership_type (OrganizationMembershipType)
      Membership type for the current user for this organization
    content_state (ContentState)
      The Content State for this Organization, if the current user can view it.
    member_count (int)
      The total count of members in the organization
    dataset_count (int)
      The total count of datasets for the organization
    competition_count (int)
      The total count of competitions for the organization
    model_count (int)
      The total count of models for the organization
    invite_code (str)
      This organization's invite code, if the current user can view it.
    category (OrganizationCategory)
      The category this organization belongs to. Historically organizations did
      not have this field, so not every organization is guaranteed to have it
      now.
    owner_user (UserAvatar)
      The current owner of the organization
    overview (str)
      Organization overview
    create_time (datetime)
      When the organization was created.
    allow_model_gating (bool)
    benchmark_count (int)
      The total count of benchmarks for the organization
  """

  def __init__(self):
    self._name = ""
    self._thumbnail_image_url = ""
    self._subtitle = None
    self._external_url = None
    self._id = 0
    self._slug = ""
    self._featured_members = []
    self._membership_type = None
    self._content_state = None
    self._member_count = 0
    self._dataset_count = 0
    self._competition_count = 0
    self._model_count = 0
    self._invite_code = None
    self._category = None
    self._owner_user = None
    self._overview = None
    self._create_time = None
    self._allow_model_gating = None
    self._benchmark_count = 0
    self._freeze()

  @property
  def name(self) -> str:
    """Display name for an organization"""
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
  def thumbnail_image_url(self) -> str:
    """URL for a thumbnail image of an organization"""
    return self._thumbnail_image_url

  @thumbnail_image_url.setter
  def thumbnail_image_url(self, thumbnail_image_url: str):
    if thumbnail_image_url is None:
      del self.thumbnail_image_url
      return
    if not isinstance(thumbnail_image_url, str):
      raise TypeError('thumbnail_image_url must be of type str')
    self._thumbnail_image_url = thumbnail_image_url

  @property
  def subtitle(self) -> str:
    """Subtitle / tagline for an organization"""
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: Optional[str]):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def external_url(self) -> str:
    """External website for an organization"""
    return self._external_url or ""

  @external_url.setter
  def external_url(self, external_url: Optional[str]):
    if external_url is None:
      del self.external_url
      return
    if not isinstance(external_url, str):
      raise TypeError('external_url must be of type str')
    self._external_url = external_url

  @property
  def id(self) -> int:
    """The organization's ID"""
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
  def slug(self) -> str:
    """Full slug for the organization"""
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
  def featured_members(self) -> Optional[List[Optional['UserAvatar']]]:
    r"""
    A subset of the organization's members for displaying on an organization
    profile
    """
    return self._featured_members

  @featured_members.setter
  def featured_members(self, featured_members: Optional[List[Optional['UserAvatar']]]):
    if featured_members is None:
      del self.featured_members
      return
    if not isinstance(featured_members, list):
      raise TypeError('featured_members must be of type list')
    if not all([isinstance(t, UserAvatar) for t in featured_members]):
      raise TypeError('featured_members must contain only items of type UserAvatar')
    self._featured_members = featured_members

  @property
  def membership_type(self) -> 'OrganizationMembershipType':
    """Membership type for the current user for this organization"""
    return self._membership_type or OrganizationMembershipType.ORGANIZATION_MEMBERSHIP_TYPE_UNSPECIFIED

  @membership_type.setter
  def membership_type(self, membership_type: Optional['OrganizationMembershipType']):
    if membership_type is None:
      del self.membership_type
      return
    if not isinstance(membership_type, OrganizationMembershipType):
      raise TypeError('membership_type must be of type OrganizationMembershipType')
    self._membership_type = membership_type

  @property
  def content_state(self) -> 'ContentState':
    """The Content State for this Organization, if the current user can view it."""
    return self._content_state or ContentState.CONTENT_STATE_UNSPECIFIED

  @content_state.setter
  def content_state(self, content_state: Optional['ContentState']):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state

  @property
  def member_count(self) -> int:
    """The total count of members in the organization"""
    return self._member_count

  @member_count.setter
  def member_count(self, member_count: int):
    if member_count is None:
      del self.member_count
      return
    if not isinstance(member_count, int):
      raise TypeError('member_count must be of type int')
    self._member_count = member_count

  @property
  def dataset_count(self) -> int:
    """The total count of datasets for the organization"""
    return self._dataset_count

  @dataset_count.setter
  def dataset_count(self, dataset_count: int):
    if dataset_count is None:
      del self.dataset_count
      return
    if not isinstance(dataset_count, int):
      raise TypeError('dataset_count must be of type int')
    self._dataset_count = dataset_count

  @property
  def competition_count(self) -> int:
    """The total count of competitions for the organization"""
    return self._competition_count

  @competition_count.setter
  def competition_count(self, competition_count: int):
    if competition_count is None:
      del self.competition_count
      return
    if not isinstance(competition_count, int):
      raise TypeError('competition_count must be of type int')
    self._competition_count = competition_count

  @property
  def model_count(self) -> int:
    """The total count of models for the organization"""
    return self._model_count

  @model_count.setter
  def model_count(self, model_count: int):
    if model_count is None:
      del self.model_count
      return
    if not isinstance(model_count, int):
      raise TypeError('model_count must be of type int')
    self._model_count = model_count

  @property
  def invite_code(self) -> str:
    """This organization's invite code, if the current user can view it."""
    return self._invite_code or ""

  @invite_code.setter
  def invite_code(self, invite_code: Optional[str]):
    if invite_code is None:
      del self.invite_code
      return
    if not isinstance(invite_code, str):
      raise TypeError('invite_code must be of type str')
    self._invite_code = invite_code

  @property
  def category(self) -> 'OrganizationCategory':
    r"""
    The category this organization belongs to. Historically organizations did
    not have this field, so not every organization is guaranteed to have it
    now.
    """
    return self._category or OrganizationCategory.ORGANIZATION_CATEGORY_UNSPECIFIED

  @category.setter
  def category(self, category: Optional['OrganizationCategory']):
    if category is None:
      del self.category
      return
    if not isinstance(category, OrganizationCategory):
      raise TypeError('category must be of type OrganizationCategory')
    self._category = category

  @property
  def owner_user(self) -> Optional['UserAvatar']:
    """The current owner of the organization"""
    return self._owner_user

  @owner_user.setter
  def owner_user(self, owner_user: Optional['UserAvatar']):
    if owner_user is None:
      del self.owner_user
      return
    if not isinstance(owner_user, UserAvatar):
      raise TypeError('owner_user must be of type UserAvatar')
    self._owner_user = owner_user

  @property
  def overview(self) -> str:
    """Organization overview"""
    return self._overview or ""

  @overview.setter
  def overview(self, overview: Optional[str]):
    if overview is None:
      del self.overview
      return
    if not isinstance(overview, str):
      raise TypeError('overview must be of type str')
    self._overview = overview

  @property
  def create_time(self) -> datetime:
    """When the organization was created."""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def allow_model_gating(self) -> bool:
    return self._allow_model_gating or False

  @allow_model_gating.setter
  def allow_model_gating(self, allow_model_gating: Optional[bool]):
    if allow_model_gating is None:
      del self.allow_model_gating
      return
    if not isinstance(allow_model_gating, bool):
      raise TypeError('allow_model_gating must be of type bool')
    self._allow_model_gating = allow_model_gating

  @property
  def benchmark_count(self) -> int:
    """The total count of benchmarks for the organization"""
    return self._benchmark_count

  @benchmark_count.setter
  def benchmark_count(self, benchmark_count: int):
    if benchmark_count is None:
      del self.benchmark_count
      return
    if not isinstance(benchmark_count, int):
      raise TypeError('benchmark_count must be of type int')
    self._benchmark_count = benchmark_count


Organization._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("externalUrl", "external_url", "_external_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("featuredMembers", "featured_members", "_featured_members", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("membershipType", "membership_type", "_membership_type", OrganizationMembershipType, None, EnumSerializer(), optional=True),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, None, EnumSerializer(), optional=True),
  FieldMetadata("memberCount", "member_count", "_member_count", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetCount", "dataset_count", "_dataset_count", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionCount", "competition_count", "_competition_count", int, 0, PredefinedSerializer()),
  FieldMetadata("modelCount", "model_count", "_model_count", int, 0, PredefinedSerializer()),
  FieldMetadata("inviteCode", "invite_code", "_invite_code", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("category", "category", "_category", OrganizationCategory, None, EnumSerializer(), optional=True),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("overview", "overview", "_overview", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("allowModelGating", "allow_model_gating", "_allow_model_gating", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkCount", "benchmark_count", "_benchmark_count", int, 0, PredefinedSerializer()),
]

