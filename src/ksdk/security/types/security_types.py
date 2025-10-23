import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class KaggleResourceType(enum.Enum):
  r"""
  Types of Kaggle resources on which permissions can be defined. Each entry in
  this proto must correspond to a permission block in the Permission enum in
  'permissions.proto'. For example COMPETITIONS_GET permission
  applies to resource of type COMPETITIONS and thus has value of 300 because
  COMPETITIONS_X permissions block start at 3000. The formula
  ValueOfFirstCanonicalPermission / 10. (COMPETITIONS_GET = 3001) / 10 =>
  (COMPETITIONS = 300).
  Please see the documentation of the Permission enum to understand permission
  blocks better.
  """
  KAGGLE_RESOURCE_TYPE_UNSPECIFIED = 0
  KAGGLE_RESOURCE_TYPE_WILDCARD_ALL = -1
  KAGGLE_RESOURCE_TYPE_USERS = 100
  """---------- Shared ----------"""
  KAGGLE_RESOURCE_TYPE_USER_ATTRIBUTES = 102
  KAGGLE_RESOURCE_TYPE_ATTRIBUTES = 104
  KAGGLE_RESOURCE_TYPE_ACCESS_TOKENS = 106
  KAGGLE_RESOURCE_TYPE_API_TOKENS = 108
  KAGGLE_RESOURCE_TYPE_SYNCHRONIZED_GROUPS = 110
  KAGGLE_RESOURCE_TYPE_BLOBS = 112
  KAGGLE_RESOURCE_TYPE_LICENSES = 114
  KAGGLE_RESOURCE_TYPE_LICENSE_USER_AGREEMENTS = 116
  KAGGLE_RESOURCE_TYPE_SEARCH_PROXY = 118
  KAGGLE_RESOURCE_TYPE_SECRETS = 120
  KAGGLE_RESOURCE_TYPE_SECRET_ATTACHMENTS = 122
  KAGGLE_RESOURCE_TYPE_TAGS = 124
  KAGGLE_RESOURCE_TYPE_RESOURCES = 130
  KAGGLE_RESOURCE_TYPE_USER_MANAGED_GROUPS = 132
  KAGGLE_RESOURCE_TYPE_USER_MANAGED_GROUP_INVITES = 134
  KAGGLE_RESOURCE_TYPE_USER_MANAGED_GROUP_MEMBERSHIPS = 136
  KAGGLE_RESOURCE_TYPE_OAUTH_CLIENTS = 138
  KAGGLE_RESOURCE_TYPE_RESOURCE_ACCESS_GROUPS = 140
  KAGGLE_RESOURCE_TYPE_OPERATIONS = 142
  KAGGLE_RESOURCE_TYPE_FORUMS = 200
  """---------- Community ----------"""
  KAGGLE_RESOURCE_TYPE_FORUM_TOPICS = 202
  KAGGLE_RESOURCE_TYPE_FORUM_MESSAGES = 204
  KAGGLE_RESOURCE_TYPE_FORUM_MESSAGE_ATTACHMENTS = 208
  KAGGLE_RESOURCE_TYPE_BADGES = 210
  KAGGLE_RESOURCE_TYPE_USER_BADGES = 212
  KAGGLE_RESOURCE_TYPE_BOOKMARKS = 214
  KAGGLE_RESOURCE_TYPE_COLLECTIONS = 216
  KAGGLE_RESOURCE_TYPE_NUDGES = 218
  KAGGLE_RESOURCE_TYPE_ORGANIZATIONS = 220
  KAGGLE_RESOURCE_TYPE_ORGANIZATION_MEMBERS = 224
  KAGGLE_RESOURCE_TYPE_SUGGESTED_ITEMS = 226
  KAGGLE_RESOURCE_TYPE_WRITE_UPS = 228
  KAGGLE_RESOURCE_TYPE_VOTES = 230
  KAGGLE_RESOURCE_TYPE_OPEN_GRAPH_IMAGE_METADATUM = 232
  KAGGLE_RESOURCE_TYPE_COMPETITIONS = 300
  """---------- Competitions ----------"""
  KAGGLE_RESOURCE_TYPE_COMPETITION_LEADERBOARDS = 304
  KAGGLE_RESOURCE_TYPE_EPISODES = 306
  KAGGLE_RESOURCE_TYPE_EPISODE_AGENTS = 308
  KAGGLE_RESOURCE_TYPE_EVALUATION_ALGORITHMS = 310
  KAGGLE_RESOURCE_TYPE_HOST_SEGMENTS = 312
  KAGGLE_RESOURCE_TYPE_PAGES = 314
  KAGGLE_RESOURCE_TYPE_SUBMISSIONS = 316
  KAGGLE_RESOURCE_TYPE_SUBMISSION_RESCORES = 318
  KAGGLE_RESOURCE_TYPE_TEAMS = 320
  KAGGLE_RESOURCE_TYPE_TEAM_MERGE_REQUESTS = 322
  KAGGLE_RESOURCE_TYPE_HACKATHON_WRITE_UPS = 324
  KAGGLE_RESOURCE_TYPE_COMPETITION_METRIC_VERSIONS = 326
  KAGGLE_RESOURCE_TYPE_DATASETS = 400
  """---------- Datasets ----------"""
  KAGGLE_RESOURCE_TYPE_DATASET_VERSIONS = 404
  KAGGLE_RESOURCE_TYPE_DATASET_SUGGESTION_BUNDLES = 406
  KAGGLE_RESOURCE_TYPE_DATABUNDLES = 408
  KAGGLE_RESOURCE_TYPE_DATABUNDLE_VERSIONS = 410
  KAGGLE_RESOURCE_TYPE_DATA_VIEWS = 412
  KAGGLE_RESOURCE_TYPE_KERNELS = 500
  """---------- Kernels ----------"""
  KAGGLE_RESOURCE_TYPE_KERNEL_SESSIONS = 504
  KAGGLE_RESOURCE_TYPE_KERNEL_SNIPPETS = 508
  KAGGLE_RESOURCE_TYPE_KERNEL_SOURCE_REFERENCES = 510
  KAGGLE_RESOURCE_TYPE_KERNEL_VERSIONS = 512
  KAGGLE_RESOURCE_TYPE_RESOURCE_REFERENCES = 520
  KAGGLE_RESOURCE_TYPE_MODELS = 600
  """---------- Models ----------"""
  KAGGLE_RESOURCE_TYPE_MODEL_INSTANCES = 608
  KAGGLE_RESOURCE_TYPE_MODEL_INSTANCE_VERSIONS = 610
  KAGGLE_RESOURCE_TYPE_MODEL_VERSIONS = 612
  KAGGLE_RESOURCE_TYPE_GATING_AGREEMENTS = 614
  KAGGLE_RESOURCE_TYPE_GATING_AGREEMENTS_USER_CONSENTS = 616
  KAGGLE_RESOURCE_TYPE_BENCHMARKS = 700
  """---------- Benchmarks ----------"""
  KAGGLE_RESOURCE_TYPE_BENCHMARK_VERSIONS = 704
  KAGGLE_RESOURCE_TYPE_BENCHMARK_MODELS = 706
  KAGGLE_RESOURCE_TYPE_BENCHMARK_MODEL_VERSIONS = 708
  KAGGLE_RESOURCE_TYPE_BENCHMARK_TASKS = 710
  KAGGLE_RESOURCE_TYPE_BENCHMARK_TASK_VERSIONS = 712
  KAGGLE_RESOURCE_TYPE_BENCHMARK_TASK_RUNS = 714

class KaggleResourceId(KaggleObject):
  r"""
  Attributes:
    type (KaggleResourceType)
    id (int)
    hash_link (str)
  """

  def __init__(self):
    self._type = KaggleResourceType.KAGGLE_RESOURCE_TYPE_UNSPECIFIED
    self._id = 0
    self._hash_link = None
    self._freeze()

  @property
  def type(self) -> 'KaggleResourceType':
    return self._type

  @type.setter
  def type(self, type: 'KaggleResourceType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, KaggleResourceType):
      raise TypeError('type must be of type KaggleResourceType')
    self._type = type

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
  def hash_link(self) -> str:
    return self._hash_link or ""

  @hash_link.setter
  def hash_link(self, hash_link: Optional[str]):
    if hash_link is None:
      del self.hash_link
      return
    if not isinstance(hash_link, str):
      raise TypeError('hash_link must be of type str')
    self._hash_link = hash_link


KaggleResourceId._fields = [
  FieldMetadata("type", "type", "_type", KaggleResourceType, KaggleResourceType.KAGGLE_RESOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hashLink", "hash_link", "_hash_link", str, None, PredefinedSerializer(), optional=True),
]

