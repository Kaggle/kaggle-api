from datetime import datetime
import enum
from kagglesdk.competitions.types.competition import RewardTypeId
from kagglesdk.competitions.types.competition_enums import HostSegment
from kagglesdk.competitions.types.search_competitions import SearchCompetitionsOrderBy, SearchCompetitionsProfileVisibility, SearchCompetitionsRole, SearchCompetitionsStatus
from kagglesdk.datasets.types.dataset_enums import DatasetFileType, DatasetFileTypeGroup, DatasetLicenseGroup, DatasetSizeGroup
from kagglesdk.datasets.types.search_datasets import SearchDatasetsOrderBy
from kagglesdk.discussions.types.search_discussions import SearchDiscussionsDocumentType, SearchDiscussionsOrderBy, SearchDiscussionsSourceType, SearchDiscussionsTopicType, WriteUpInclusionType
from kagglesdk.discussions.types.writeup_enums import WriteUpType
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.search_kernels import SearchKernelsOrderBy
from kagglesdk.models.types.search_models import SearchModelsOrderBy
from kagglesdk.search.types.search_content_shared import ListSearchContentRangeFilter
from kagglesdk.search.types.search_enums import DocumentType, ListSearchContentOrderBy, OwnerType, PrivacyFilter
from kagglesdk.search.types.search_service import WriteUpItemInfo
from kagglesdk.users.types.progression_service import UserAchievementType
from kagglesdk.users.types.search_users import SearchUsersOrderBy
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional, List

class ApiListType(enum.Enum):
  """Based on kaggle.search.ListType"""
  API_LIST_TYPE_UNSPECIFIED = 0
  API_LIST_TYPE_YOUR_WORK = 1

class ApiOrganizationCard(KaggleObject):
  r"""
  Based on kaggle.users.OrganizationCard

  Attributes:
    name (str)
    id (int)
    thumbnail_image_url (str)
    slug (str)
  """

  def __init__(self):
    self._name = ""
    self._id = 0
    self._thumbnail_image_url = ""
    self._slug = ""
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
  def thumbnail_image_url(self) -> str:
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


class ApiSearchCompetitionsDocument(KaggleObject):
  r"""
  Based on kaggle.competitions.SearchCompetitionsDocument

  Attributes:
    host_segment (HostSegment)
      The host segment of the Competition
    deadline (datetime)
      The deadline of the Competition
    team_count (int)
      The total number of teams participating in the Competition
    team_rank (int)
      The rank of the current user's team on the Competition
    is_environment_evaluation (bool)
      Whether the Competition has an environment evaluation
    prize_type (RewardTypeId)
      The prize/award type of the Competition
    prize_value (float)
      The prize/award value of the Competition
    is_launched (bool)
      Whether the competition has launched (even if it's ended)
    owner_user_has_joined (bool)
      Whether the owner user (profile user, then current user) has joined the
      competition
    is_limited_participation (bool)
      Whether the competition is a limited participation competition
    only_allow_kernel_submissions (bool)
      Whether only kernel submissions are allowed
  """

  def __init__(self):
    self._host_segment = HostSegment.HOST_SEGMENT_UNSPECIFIED
    self._deadline = None
    self._team_count = 0
    self._team_rank = None
    self._is_environment_evaluation = False
    self._prize_type = RewardTypeId.REWARD_TYPE_ID_UNSPECIFIED
    self._prize_value = None
    self._is_launched = False
    self._owner_user_has_joined = False
    self._is_limited_participation = False
    self._only_allow_kernel_submissions = False
    self._freeze()

  @property
  def host_segment(self) -> 'HostSegment':
    """The host segment of the Competition"""
    return self._host_segment

  @host_segment.setter
  def host_segment(self, host_segment: 'HostSegment'):
    if host_segment is None:
      del self.host_segment
      return
    if not isinstance(host_segment, HostSegment):
      raise TypeError('host_segment must be of type HostSegment')
    self._host_segment = host_segment

  @property
  def deadline(self) -> datetime:
    """The deadline of the Competition"""
    return self._deadline

  @deadline.setter
  def deadline(self, deadline: datetime):
    if deadline is None:
      del self.deadline
      return
    if not isinstance(deadline, datetime):
      raise TypeError('deadline must be of type datetime')
    self._deadline = deadline

  @property
  def team_count(self) -> int:
    """The total number of teams participating in the Competition"""
    return self._team_count

  @team_count.setter
  def team_count(self, team_count: int):
    if team_count is None:
      del self.team_count
      return
    if not isinstance(team_count, int):
      raise TypeError('team_count must be of type int')
    self._team_count = team_count

  @property
  def team_rank(self) -> int:
    """The rank of the current user's team on the Competition"""
    return self._team_rank or 0

  @team_rank.setter
  def team_rank(self, team_rank: Optional[int]):
    if team_rank is None:
      del self.team_rank
      return
    if not isinstance(team_rank, int):
      raise TypeError('team_rank must be of type int')
    self._team_rank = team_rank

  @property
  def is_environment_evaluation(self) -> bool:
    """Whether the Competition has an environment evaluation"""
    return self._is_environment_evaluation

  @is_environment_evaluation.setter
  def is_environment_evaluation(self, is_environment_evaluation: bool):
    if is_environment_evaluation is None:
      del self.is_environment_evaluation
      return
    if not isinstance(is_environment_evaluation, bool):
      raise TypeError('is_environment_evaluation must be of type bool')
    self._is_environment_evaluation = is_environment_evaluation

  @property
  def prize_type(self) -> 'RewardTypeId':
    """The prize/award type of the Competition"""
    return self._prize_type

  @prize_type.setter
  def prize_type(self, prize_type: 'RewardTypeId'):
    if prize_type is None:
      del self.prize_type
      return
    if not isinstance(prize_type, RewardTypeId):
      raise TypeError('prize_type must be of type RewardTypeId')
    self._prize_type = prize_type

  @property
  def prize_value(self) -> float:
    """The prize/award value of the Competition"""
    return self._prize_value or 0.0

  @prize_value.setter
  def prize_value(self, prize_value: Optional[float]):
    if prize_value is None:
      del self.prize_value
      return
    if not isinstance(prize_value, float):
      raise TypeError('prize_value must be of type float')
    self._prize_value = prize_value

  @property
  def is_launched(self) -> bool:
    """Whether the competition has launched (even if it's ended)"""
    return self._is_launched

  @is_launched.setter
  def is_launched(self, is_launched: bool):
    if is_launched is None:
      del self.is_launched
      return
    if not isinstance(is_launched, bool):
      raise TypeError('is_launched must be of type bool')
    self._is_launched = is_launched

  @property
  def owner_user_has_joined(self) -> bool:
    r"""
    Whether the owner user (profile user, then current user) has joined the
    competition
    """
    return self._owner_user_has_joined

  @owner_user_has_joined.setter
  def owner_user_has_joined(self, owner_user_has_joined: bool):
    if owner_user_has_joined is None:
      del self.owner_user_has_joined
      return
    if not isinstance(owner_user_has_joined, bool):
      raise TypeError('owner_user_has_joined must be of type bool')
    self._owner_user_has_joined = owner_user_has_joined

  @property
  def is_limited_participation(self) -> bool:
    """Whether the competition is a limited participation competition"""
    return self._is_limited_participation

  @is_limited_participation.setter
  def is_limited_participation(self, is_limited_participation: bool):
    if is_limited_participation is None:
      del self.is_limited_participation
      return
    if not isinstance(is_limited_participation, bool):
      raise TypeError('is_limited_participation must be of type bool')
    self._is_limited_participation = is_limited_participation

  @property
  def only_allow_kernel_submissions(self) -> bool:
    """Whether only kernel submissions are allowed"""
    return self._only_allow_kernel_submissions

  @only_allow_kernel_submissions.setter
  def only_allow_kernel_submissions(self, only_allow_kernel_submissions: bool):
    if only_allow_kernel_submissions is None:
      del self.only_allow_kernel_submissions
      return
    if not isinstance(only_allow_kernel_submissions, bool):
      raise TypeError('only_allow_kernel_submissions must be of type bool')
    self._only_allow_kernel_submissions = only_allow_kernel_submissions


class ApiSearchCompetitionsFilters(KaggleObject):
  r"""
  Based on kaggle.competitions.SearchCompetitionsFilters

  Attributes:
    role (SearchCompetitionsRole)
      The Competition role used to filter the documents
    status (SearchCompetitionsStatus)
      The Competition status used to filter the documents
    profile_visibility (SearchCompetitionsProfileVisibility)
      Competition visibility status on user profile
    earned_medal (bool)
      Whether to return documents that the owner_user_id earned a medal for.
  """

  def __init__(self):
    self._role = SearchCompetitionsRole.SEARCH_COMPETITIONS_ROLE_ANY
    self._status = SearchCompetitionsStatus.SEARCH_COMPETITIONS_STATUS_ANY
    self._profile_visibility = SearchCompetitionsProfileVisibility.SEARCH_COMPETITIONS_PROFILE_VISIBILITY_ANY
    self._earned_medal = None
    self._freeze()

  @property
  def role(self) -> 'SearchCompetitionsRole':
    """The Competition role used to filter the documents"""
    return self._role

  @role.setter
  def role(self, role: 'SearchCompetitionsRole'):
    if role is None:
      del self.role
      return
    if not isinstance(role, SearchCompetitionsRole):
      raise TypeError('role must be of type SearchCompetitionsRole')
    self._role = role

  @property
  def status(self) -> 'SearchCompetitionsStatus':
    """The Competition status used to filter the documents"""
    return self._status

  @status.setter
  def status(self, status: 'SearchCompetitionsStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, SearchCompetitionsStatus):
      raise TypeError('status must be of type SearchCompetitionsStatus')
    self._status = status

  @property
  def profile_visibility(self) -> 'SearchCompetitionsProfileVisibility':
    """Competition visibility status on user profile"""
    return self._profile_visibility

  @profile_visibility.setter
  def profile_visibility(self, profile_visibility: 'SearchCompetitionsProfileVisibility'):
    if profile_visibility is None:
      del self.profile_visibility
      return
    if not isinstance(profile_visibility, SearchCompetitionsProfileVisibility):
      raise TypeError('profile_visibility must be of type SearchCompetitionsProfileVisibility')
    self._profile_visibility = profile_visibility

  @property
  def earned_medal(self) -> bool:
    """Whether to return documents that the owner_user_id earned a medal for."""
    return self._earned_medal or False

  @earned_medal.setter
  def earned_medal(self, earned_medal: Optional[bool]):
    if earned_medal is None:
      del self.earned_medal
      return
    if not isinstance(earned_medal, bool):
      raise TypeError('earned_medal must be of type bool')
    self._earned_medal = earned_medal


class ApiSearchDatasetsDocument(KaggleObject):
  r"""
  Based on kaggle.datasets.SearchDatasetsDocument

  Attributes:
    usability_rating (float)
      The usability rating of the Dataset
    file_count (int)
      How many files the Dataset has
    file_types (DatasetFileType)
      The file types of all the files in the Dataset
    size (int)
      The size of the Dataset
  """

  def __init__(self):
    self._usability_rating = 0.0
    self._file_count = 0
    self._file_types = []
    self._size = 0
    self._freeze()

  @property
  def usability_rating(self) -> float:
    """The usability rating of the Dataset"""
    return self._usability_rating

  @usability_rating.setter
  def usability_rating(self, usability_rating: float):
    if usability_rating is None:
      del self.usability_rating
      return
    if not isinstance(usability_rating, float):
      raise TypeError('usability_rating must be of type float')
    self._usability_rating = usability_rating

  @property
  def file_count(self) -> int:
    """How many files the Dataset has"""
    return self._file_count

  @file_count.setter
  def file_count(self, file_count: int):
    if file_count is None:
      del self.file_count
      return
    if not isinstance(file_count, int):
      raise TypeError('file_count must be of type int')
    self._file_count = file_count

  @property
  def file_types(self) -> Optional[List['DatasetFileType']]:
    """The file types of all the files in the Dataset"""
    return self._file_types

  @file_types.setter
  def file_types(self, file_types: Optional[List['DatasetFileType']]):
    if file_types is None:
      del self.file_types
      return
    if not isinstance(file_types, list):
      raise TypeError('file_types must be of type list')
    if not all([isinstance(t, DatasetFileType) for t in file_types]):
      raise TypeError('file_types must contain only items of type DatasetFileType')
    self._file_types = file_types

  @property
  def size(self) -> int:
    """The size of the Dataset"""
    return self._size

  @size.setter
  def size(self, size: int):
    if size is None:
      del self.size
      return
    if not isinstance(size, int):
      raise TypeError('size must be of type int')
    self._size = size


class ApiSearchDatasetsFilters(KaggleObject):
  r"""
  Based on kaggle.datasets.SearchDiscussionsFilters

  Attributes:
    file_type (DatasetFileTypeGroup)
      The file types used to filter the documents
    license_group (DatasetLicenseGroup)
      The license groups used to filter the documents
    size (DatasetSizeGroup)
      The dataset size range used to filter the documents
    earned_medal (bool)
      Whether to return documents that the owner_user_id earned a medal for.
  """

  def __init__(self):
    self._file_type = DatasetFileTypeGroup.DATASET_FILE_TYPE_GROUP_ALL
    self._license_group = None
    self._size = None
    self._earned_medal = None
    self._freeze()

  @property
  def file_type(self) -> 'DatasetFileTypeGroup':
    """The file types used to filter the documents"""
    return self._file_type

  @file_type.setter
  def file_type(self, file_type: 'DatasetFileTypeGroup'):
    if file_type is None:
      del self.file_type
      return
    if not isinstance(file_type, DatasetFileTypeGroup):
      raise TypeError('file_type must be of type DatasetFileTypeGroup')
    self._file_type = file_type

  @property
  def license_group(self) -> 'DatasetLicenseGroup':
    """The license groups used to filter the documents"""
    return self._license_group or DatasetLicenseGroup.DATASET_LICENSE_GROUP_ALL

  @license_group.setter
  def license_group(self, license_group: Optional['DatasetLicenseGroup']):
    if license_group is None:
      del self.license_group
      return
    if not isinstance(license_group, DatasetLicenseGroup):
      raise TypeError('license_group must be of type DatasetLicenseGroup')
    self._license_group = license_group

  @property
  def size(self) -> 'DatasetSizeGroup':
    """The dataset size range used to filter the documents"""
    return self._size or DatasetSizeGroup.DATASET_SIZE_GROUP_ALL

  @size.setter
  def size(self, size: Optional['DatasetSizeGroup']):
    if size is None:
      del self.size
      return
    if not isinstance(size, DatasetSizeGroup):
      raise TypeError('size must be of type DatasetSizeGroup')
    self._size = size

  @property
  def earned_medal(self) -> bool:
    """Whether to return documents that the owner_user_id earned a medal for."""
    return self._earned_medal or False

  @earned_medal.setter
  def earned_medal(self, earned_medal: Optional[bool]):
    if earned_medal is None:
      del self.earned_medal
      return
    if not isinstance(earned_medal, bool):
      raise TypeError('earned_medal must be of type bool')
    self._earned_medal = earned_medal


class ApiSearchDiscussionsDocument(KaggleObject):
  r"""
  Based on kaggle.discussions.SearchDiscussionsDocument

  Attributes:
    new_comment_url (str)
    message_stripped (str)
      The message of the topic/comment, stripped of HTML (at time of index)
    message_markdown (str)
      The markdown for the message of the topic/comment
    forum_name (str)
      The name of the parent forum
    forum_url (str)
      The URL for the parent forum
    source_type (SearchDiscussionsSourceType)
      The source type of the comment
    topic_type (SearchDiscussionsTopicType)
      The type of topic returned
    type (SearchDiscussionsDocumentType)
      The type of document returned
    write_up_metadata (WriteUpItemInfo)
      If the document is a WriteUp, extra WriteUp-specific data
      is provided
  """

  def __init__(self):
    self._new_comment_url = None
    self._message_stripped = ""
    self._message_markdown = None
    self._forum_name = ""
    self._forum_url = None
    self._source_type = SearchDiscussionsSourceType.SEARCH_DISCUSSIONS_SOURCE_TYPE_UNSPECIFIED
    self._topic_type = SearchDiscussionsTopicType.SEARCH_DISCUSSIONS_TOPIC_TYPE_UNSPECIFIED
    self._type = SearchDiscussionsDocumentType.SEARCH_DISCUSSIONS_DOCUMENT_TYPE_UNSPECIFIED
    self._write_up_metadata = None
    self._freeze()

  @property
  def new_comment_url(self) -> str:
    return self._new_comment_url or ""

  @new_comment_url.setter
  def new_comment_url(self, new_comment_url: Optional[str]):
    if new_comment_url is None:
      del self.new_comment_url
      return
    if not isinstance(new_comment_url, str):
      raise TypeError('new_comment_url must be of type str')
    self._new_comment_url = new_comment_url

  @property
  def message_stripped(self) -> str:
    """The message of the topic/comment, stripped of HTML (at time of index)"""
    return self._message_stripped

  @message_stripped.setter
  def message_stripped(self, message_stripped: str):
    if message_stripped is None:
      del self.message_stripped
      return
    if not isinstance(message_stripped, str):
      raise TypeError('message_stripped must be of type str')
    self._message_stripped = message_stripped

  @property
  def message_markdown(self) -> str:
    """The markdown for the message of the topic/comment"""
    return self._message_markdown or ""

  @message_markdown.setter
  def message_markdown(self, message_markdown: Optional[str]):
    if message_markdown is None:
      del self.message_markdown
      return
    if not isinstance(message_markdown, str):
      raise TypeError('message_markdown must be of type str')
    self._message_markdown = message_markdown

  @property
  def forum_name(self) -> str:
    """The name of the parent forum"""
    return self._forum_name

  @forum_name.setter
  def forum_name(self, forum_name: str):
    if forum_name is None:
      del self.forum_name
      return
    if not isinstance(forum_name, str):
      raise TypeError('forum_name must be of type str')
    self._forum_name = forum_name

  @property
  def forum_url(self) -> str:
    """The URL for the parent forum"""
    return self._forum_url or ""

  @forum_url.setter
  def forum_url(self, forum_url: Optional[str]):
    if forum_url is None:
      del self.forum_url
      return
    if not isinstance(forum_url, str):
      raise TypeError('forum_url must be of type str')
    self._forum_url = forum_url

  @property
  def source_type(self) -> 'SearchDiscussionsSourceType':
    """The source type of the comment"""
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'SearchDiscussionsSourceType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, SearchDiscussionsSourceType):
      raise TypeError('source_type must be of type SearchDiscussionsSourceType')
    self._source_type = source_type

  @property
  def topic_type(self) -> 'SearchDiscussionsTopicType':
    """The type of topic returned"""
    return self._topic_type

  @topic_type.setter
  def topic_type(self, topic_type: 'SearchDiscussionsTopicType'):
    if topic_type is None:
      del self.topic_type
      return
    if not isinstance(topic_type, SearchDiscussionsTopicType):
      raise TypeError('topic_type must be of type SearchDiscussionsTopicType')
    self._topic_type = topic_type

  @property
  def type(self) -> 'SearchDiscussionsDocumentType':
    """The type of document returned"""
    return self._type

  @type.setter
  def type(self, type: 'SearchDiscussionsDocumentType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, SearchDiscussionsDocumentType):
      raise TypeError('type must be of type SearchDiscussionsDocumentType')
    self._type = type

  @property
  def write_up_metadata(self) -> Optional['WriteUpItemInfo']:
    r"""
    If the document is a WriteUp, extra WriteUp-specific data
    is provided
    """
    return self._write_up_metadata or None

  @write_up_metadata.setter
  def write_up_metadata(self, write_up_metadata: Optional[Optional['WriteUpItemInfo']]):
    if write_up_metadata is None:
      del self.write_up_metadata
      return
    if not isinstance(write_up_metadata, WriteUpItemInfo):
      raise TypeError('write_up_metadata must be of type WriteUpItemInfo')
    self._write_up_metadata = write_up_metadata


class ApiSearchDiscussionsFilters(KaggleObject):
  r"""
  Based on kaggle.discussions.SearchDiscussionsFilters

  Attributes:
    source_type (SearchDiscussionsSourceType)
      The discussion source type used to filter the documents
    only_new_comments (bool)
      Show only topics with new comments
    write_up_inclusion_type (WriteUpInclusionType)
      Determines whether or not WriteUps should be included
    write_up_types (WriteUpType)
      Filters on WriteUp type
  """

  def __init__(self):
    self._source_type = SearchDiscussionsSourceType.SEARCH_DISCUSSIONS_SOURCE_TYPE_UNSPECIFIED
    self._only_new_comments = False
    self._write_up_inclusion_type = WriteUpInclusionType.WRITE_UP_INCLUSION_TYPE_UNSPECIFIED
    self._write_up_types = []
    self._freeze()

  @property
  def source_type(self) -> 'SearchDiscussionsSourceType':
    """The discussion source type used to filter the documents"""
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'SearchDiscussionsSourceType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, SearchDiscussionsSourceType):
      raise TypeError('source_type must be of type SearchDiscussionsSourceType')
    self._source_type = source_type

  @property
  def only_new_comments(self) -> bool:
    """Show only topics with new comments"""
    return self._only_new_comments

  @only_new_comments.setter
  def only_new_comments(self, only_new_comments: bool):
    if only_new_comments is None:
      del self.only_new_comments
      return
    if not isinstance(only_new_comments, bool):
      raise TypeError('only_new_comments must be of type bool')
    self._only_new_comments = only_new_comments

  @property
  def write_up_inclusion_type(self) -> 'WriteUpInclusionType':
    """Determines whether or not WriteUps should be included"""
    return self._write_up_inclusion_type

  @write_up_inclusion_type.setter
  def write_up_inclusion_type(self, write_up_inclusion_type: 'WriteUpInclusionType'):
    if write_up_inclusion_type is None:
      del self.write_up_inclusion_type
      return
    if not isinstance(write_up_inclusion_type, WriteUpInclusionType):
      raise TypeError('write_up_inclusion_type must be of type WriteUpInclusionType')
    self._write_up_inclusion_type = write_up_inclusion_type

  @property
  def write_up_types(self) -> Optional[List['WriteUpType']]:
    """Filters on WriteUp type"""
    return self._write_up_types

  @write_up_types.setter
  def write_up_types(self, write_up_types: Optional[List['WriteUpType']]):
    if write_up_types is None:
      del self.write_up_types
      return
    if not isinstance(write_up_types, list):
      raise TypeError('write_up_types must be of type list')
    if not all([isinstance(t, WriteUpType) for t in write_up_types]):
      raise TypeError('write_up_types must contain only items of type WriteUpType')
    self._write_up_types = write_up_types


class ApiSearchKernelsDocument(KaggleObject):
  r"""
  Based on kaggle.kernels.SearchKernelsDocument

  Attributes:
    session_id (int)
      The session ID of the Kernel
    has_linked_submission (bool)
      Whether the Kernel has a linked submission
    datasource_is_private (bool)
      Whether the datasource is private
    best_public_score (float)
      The best public score of the Kernel's submission
    is_draft (bool)
      Whether the Kernel is a draft
  """

  def __init__(self):
    self._session_id = None
    self._has_linked_submission = False
    self._datasource_is_private = False
    self._best_public_score = 0.0
    self._is_draft = False
    self._freeze()

  @property
  def session_id(self) -> int:
    """The session ID of the Kernel"""
    return self._session_id or 0

  @session_id.setter
  def session_id(self, session_id: Optional[int]):
    if session_id is None:
      del self.session_id
      return
    if not isinstance(session_id, int):
      raise TypeError('session_id must be of type int')
    self._session_id = session_id

  @property
  def has_linked_submission(self) -> bool:
    """Whether the Kernel has a linked submission"""
    return self._has_linked_submission

  @has_linked_submission.setter
  def has_linked_submission(self, has_linked_submission: bool):
    if has_linked_submission is None:
      del self.has_linked_submission
      return
    if not isinstance(has_linked_submission, bool):
      raise TypeError('has_linked_submission must be of type bool')
    self._has_linked_submission = has_linked_submission

  @property
  def datasource_is_private(self) -> bool:
    """Whether the datasource is private"""
    return self._datasource_is_private

  @datasource_is_private.setter
  def datasource_is_private(self, datasource_is_private: bool):
    if datasource_is_private is None:
      del self.datasource_is_private
      return
    if not isinstance(datasource_is_private, bool):
      raise TypeError('datasource_is_private must be of type bool')
    self._datasource_is_private = datasource_is_private

  @property
  def best_public_score(self) -> float:
    """The best public score of the Kernel's submission"""
    return self._best_public_score

  @best_public_score.setter
  def best_public_score(self, best_public_score: float):
    if best_public_score is None:
      del self.best_public_score
      return
    if not isinstance(best_public_score, float):
      raise TypeError('best_public_score must be of type float')
    self._best_public_score = best_public_score

  @property
  def is_draft(self) -> bool:
    """Whether the Kernel is a draft"""
    return self._is_draft

  @is_draft.setter
  def is_draft(self, is_draft: bool):
    if is_draft is None:
      del self.is_draft
      return
    if not isinstance(is_draft, bool):
      raise TypeError('is_draft must be of type bool')
    self._is_draft = is_draft


class ApiSearchKernelsFilters(KaggleObject):
  r"""
  Based on kaggle.kernels.SearchKernelsFilters

  Attributes:
    language (str)
      The Kernel language used to filter documents
    earned_medal (bool)
      Whether to return documents that the owner_user_id earned a medal for.
  """

  def __init__(self):
    self._language = None
    self._earned_medal = None
    self._freeze()

  @property
  def language(self) -> str:
    """The Kernel language used to filter documents"""
    return self._language or ""

  @language.setter
  def language(self, language: Optional[str]):
    if language is None:
      del self.language
      return
    if not isinstance(language, str):
      raise TypeError('language must be of type str')
    self._language = language

  @property
  def earned_medal(self) -> bool:
    """Whether to return documents that the owner_user_id earned a medal for."""
    return self._earned_medal or False

  @earned_medal.setter
  def earned_medal(self, earned_medal: Optional[bool]):
    if earned_medal is None:
      del self.earned_medal
      return
    if not isinstance(earned_medal, bool):
      raise TypeError('earned_medal must be of type bool')
    self._earned_medal = earned_medal


class ApiSearchModelsDocument(KaggleObject):
  r"""
  Based on kaggle.models.SearchModelsDocument

  Attributes:
    instance_count (int)
      The total number of instances in the Model
    notebook_count (int)
      The total number of notebooks in the Model
  """

  def __init__(self):
    self._instance_count = 0
    self._notebook_count = 0
    self._freeze()

  @property
  def instance_count(self) -> int:
    """The total number of instances in the Model"""
    return self._instance_count

  @instance_count.setter
  def instance_count(self, instance_count: int):
    if instance_count is None:
      del self.instance_count
      return
    if not isinstance(instance_count, int):
      raise TypeError('instance_count must be of type int')
    self._instance_count = instance_count

  @property
  def notebook_count(self) -> int:
    """The total number of notebooks in the Model"""
    return self._notebook_count

  @notebook_count.setter
  def notebook_count(self, notebook_count: int):
    if notebook_count is None:
      del self.notebook_count
      return
    if not isinstance(notebook_count, int):
      raise TypeError('notebook_count must be of type int')
    self._notebook_count = notebook_count


class ApiSearchModelsFilters(KaggleObject):
  r"""
  Based on kaggle.models.SearchModelsFilters

  Attributes:
    size (ListSearchContentRangeFilter)
      The size of the Model used to filter the documents
  """

  def __init__(self):
    self._size = None
    self._freeze()

  @property
  def size(self) -> Optional['ListSearchContentRangeFilter']:
    """The size of the Model used to filter the documents"""
    return self._size

  @size.setter
  def size(self, size: Optional['ListSearchContentRangeFilter']):
    if size is None:
      del self.size
      return
    if not isinstance(size, ListSearchContentRangeFilter):
      raise TypeError('size must be of type ListSearchContentRangeFilter')
    self._size = size


class ApiSearchUsersDocument(KaggleObject):
  r"""
  Based on kaggle.users.SearchUsersDocument

  Attributes:
    grandmaster_tier_level (int)
      User's GM tier level. Tier levels are awarded starting at GM. All
      users who are not GM will have a tier level of 0.
    user_location (str)
      User location string, if location sharing is opted-in. In the format:
      'city, region, country'.
    occupation_organization_name (str)
      Occupation organization name as indicated on the user's profile.
    competition_ranking (int)
      Current ranking for the user in the competition achievement type.
    competition_points (int)
      Current points for the user in the competition achievement type.
    kernel_ranking (int)
      Current ranking for the user in the kernel achievement type.
    kernel_points (int)
      Current points for the user in the kernel achievement type.
    dataset_ranking (int)
      Current ranking for the user in dataset achievement type.
    dataset_points (int)
      Current points for the user in the dataset achievement type.
  """

  def __init__(self):
    self._grandmaster_tier_level = 0
    self._user_location = None
    self._occupation_organization_name = None
    self._competition_ranking = None
    self._competition_points = None
    self._kernel_ranking = None
    self._kernel_points = None
    self._dataset_ranking = None
    self._dataset_points = None
    self._freeze()

  @property
  def grandmaster_tier_level(self) -> int:
    r"""
    User's GM tier level. Tier levels are awarded starting at GM. All
    users who are not GM will have a tier level of 0.
    """
    return self._grandmaster_tier_level

  @grandmaster_tier_level.setter
  def grandmaster_tier_level(self, grandmaster_tier_level: int):
    if grandmaster_tier_level is None:
      del self.grandmaster_tier_level
      return
    if not isinstance(grandmaster_tier_level, int):
      raise TypeError('grandmaster_tier_level must be of type int')
    self._grandmaster_tier_level = grandmaster_tier_level

  @property
  def user_location(self) -> str:
    r"""
    User location string, if location sharing is opted-in. In the format:
    'city, region, country'.
    """
    return self._user_location or ""

  @user_location.setter
  def user_location(self, user_location: Optional[str]):
    if user_location is None:
      del self.user_location
      return
    if not isinstance(user_location, str):
      raise TypeError('user_location must be of type str')
    self._user_location = user_location

  @property
  def occupation_organization_name(self) -> str:
    """Occupation organization name as indicated on the user's profile."""
    return self._occupation_organization_name or ""

  @occupation_organization_name.setter
  def occupation_organization_name(self, occupation_organization_name: Optional[str]):
    if occupation_organization_name is None:
      del self.occupation_organization_name
      return
    if not isinstance(occupation_organization_name, str):
      raise TypeError('occupation_organization_name must be of type str')
    self._occupation_organization_name = occupation_organization_name

  @property
  def competition_ranking(self) -> int:
    """Current ranking for the user in the competition achievement type."""
    return self._competition_ranking or 0

  @competition_ranking.setter
  def competition_ranking(self, competition_ranking: Optional[int]):
    if competition_ranking is None:
      del self.competition_ranking
      return
    if not isinstance(competition_ranking, int):
      raise TypeError('competition_ranking must be of type int')
    self._competition_ranking = competition_ranking

  @property
  def competition_points(self) -> int:
    """Current points for the user in the competition achievement type."""
    return self._competition_points or 0

  @competition_points.setter
  def competition_points(self, competition_points: Optional[int]):
    if competition_points is None:
      del self.competition_points
      return
    if not isinstance(competition_points, int):
      raise TypeError('competition_points must be of type int')
    self._competition_points = competition_points

  @property
  def kernel_ranking(self) -> int:
    """Current ranking for the user in the kernel achievement type."""
    return self._kernel_ranking or 0

  @kernel_ranking.setter
  def kernel_ranking(self, kernel_ranking: Optional[int]):
    if kernel_ranking is None:
      del self.kernel_ranking
      return
    if not isinstance(kernel_ranking, int):
      raise TypeError('kernel_ranking must be of type int')
    self._kernel_ranking = kernel_ranking

  @property
  def kernel_points(self) -> int:
    """Current points for the user in the kernel achievement type."""
    return self._kernel_points or 0

  @kernel_points.setter
  def kernel_points(self, kernel_points: Optional[int]):
    if kernel_points is None:
      del self.kernel_points
      return
    if not isinstance(kernel_points, int):
      raise TypeError('kernel_points must be of type int')
    self._kernel_points = kernel_points

  @property
  def dataset_ranking(self) -> int:
    """Current ranking for the user in dataset achievement type."""
    return self._dataset_ranking or 0

  @dataset_ranking.setter
  def dataset_ranking(self, dataset_ranking: Optional[int]):
    if dataset_ranking is None:
      del self.dataset_ranking
      return
    if not isinstance(dataset_ranking, int):
      raise TypeError('dataset_ranking must be of type int')
    self._dataset_ranking = dataset_ranking

  @property
  def dataset_points(self) -> int:
    """Current points for the user in the dataset achievement type."""
    return self._dataset_points or 0

  @dataset_points.setter
  def dataset_points(self, dataset_points: Optional[int]):
    if dataset_points is None:
      del self.dataset_points
      return
    if not isinstance(dataset_points, int):
      raise TypeError('dataset_points must be of type int')
    self._dataset_points = dataset_points


class ApiSearchUsersFilters(KaggleObject):
  r"""
  Based on kaggle.users.SearchUsersFilters

  Attributes:
    user_locations (str)
      Filter to users that have one of the the specified locations. Expects the
      format: 'city, region, country' for each.
    tier (UserAchievementTier)
      Filter to users that have the specified performance tier.
    user_ids (int)
      Filter to users based on the provided user ids.
    require_ranking_for_type (UserAchievementType)
      Filter to users that have points for the specified type.
    occupation_organization_names (str)
      Filter to users that have one of the provided occupation organization names
      indicated on their user profile, i.e. http://screen/3N68JKC4hocxWmn. Note:
      This is *not* the same thing as a Kaggle Organization, such as
      kaggle.com/organizations/google.
    grandmaster_level (ListSearchContentRangeFilter)
      Filter to users that have the specified range of Grandmaster tier level.
  """

  def __init__(self):
    self._user_locations = []
    self._tier = None
    self._user_ids = []
    self._require_ranking_for_type = None
    self._occupation_organization_names = []
    self._grandmaster_level = None
    self._freeze()

  @property
  def user_locations(self) -> Optional[List[str]]:
    r"""
    Filter to users that have one of the the specified locations. Expects the
    format: 'city, region, country' for each.
    """
    return self._user_locations

  @user_locations.setter
  def user_locations(self, user_locations: Optional[List[str]]):
    if user_locations is None:
      del self.user_locations
      return
    if not isinstance(user_locations, list):
      raise TypeError('user_locations must be of type list')
    if not all([isinstance(t, str) for t in user_locations]):
      raise TypeError('user_locations must contain only items of type str')
    self._user_locations = user_locations

  @property
  def tier(self) -> 'UserAchievementTier':
    """Filter to users that have the specified performance tier."""
    return self._tier or UserAchievementTier.NOVICE

  @tier.setter
  def tier(self, tier: Optional['UserAchievementTier']):
    if tier is None:
      del self.tier
      return
    if not isinstance(tier, UserAchievementTier):
      raise TypeError('tier must be of type UserAchievementTier')
    self._tier = tier

  @property
  def user_ids(self) -> Optional[List[int]]:
    """Filter to users based on the provided user ids."""
    return self._user_ids

  @user_ids.setter
  def user_ids(self, user_ids: Optional[List[int]]):
    if user_ids is None:
      del self.user_ids
      return
    if not isinstance(user_ids, list):
      raise TypeError('user_ids must be of type list')
    if not all([isinstance(t, int) for t in user_ids]):
      raise TypeError('user_ids must contain only items of type int')
    self._user_ids = user_ids

  @property
  def require_ranking_for_type(self) -> 'UserAchievementType':
    """Filter to users that have points for the specified type."""
    return self._require_ranking_for_type or UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED

  @require_ranking_for_type.setter
  def require_ranking_for_type(self, require_ranking_for_type: Optional['UserAchievementType']):
    if require_ranking_for_type is None:
      del self.require_ranking_for_type
      return
    if not isinstance(require_ranking_for_type, UserAchievementType):
      raise TypeError('require_ranking_for_type must be of type UserAchievementType')
    self._require_ranking_for_type = require_ranking_for_type

  @property
  def occupation_organization_names(self) -> Optional[List[str]]:
    r"""
    Filter to users that have one of the provided occupation organization names
    indicated on their user profile, i.e. http://screen/3N68JKC4hocxWmn. Note:
    This is *not* the same thing as a Kaggle Organization, such as
    kaggle.com/organizations/google.
    """
    return self._occupation_organization_names

  @occupation_organization_names.setter
  def occupation_organization_names(self, occupation_organization_names: Optional[List[str]]):
    if occupation_organization_names is None:
      del self.occupation_organization_names
      return
    if not isinstance(occupation_organization_names, list):
      raise TypeError('occupation_organization_names must be of type list')
    if not all([isinstance(t, str) for t in occupation_organization_names]):
      raise TypeError('occupation_organization_names must contain only items of type str')
    self._occupation_organization_names = occupation_organization_names

  @property
  def grandmaster_level(self) -> Optional['ListSearchContentRangeFilter']:
    """Filter to users that have the specified range of Grandmaster tier level."""
    return self._grandmaster_level

  @grandmaster_level.setter
  def grandmaster_level(self, grandmaster_level: Optional['ListSearchContentRangeFilter']):
    if grandmaster_level is None:
      del self.grandmaster_level
      return
    if not isinstance(grandmaster_level, ListSearchContentRangeFilter):
      raise TypeError('grandmaster_level must be of type ListSearchContentRangeFilter')
    self._grandmaster_level = grandmaster_level


class ApiUserAvatar(KaggleObject):
  r"""
  Based on kaggle.users.UserAvatar

  Attributes:
    id (int)
      ID for the given user
    display_name (str)
      Display name for the given user
    thumbnail_url (str)
      Thumbnail URL for the given user
    url (str)
      Profile URL for the given user
    user_name (str)
      User name for the given user
    progression_opt_out (bool)
      True if the user is opted out of the progression system.
    tier (UserAchievementTier)
      Tier for the given user
  """

  def __init__(self):
    self._id = 0
    self._display_name = None
    self._thumbnail_url = None
    self._url = None
    self._user_name = None
    self._progression_opt_out = None
    self._tier = UserAchievementTier.NOVICE
    self._freeze()

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


class ListEntitiesDocument(KaggleObject):
  r"""
  Based on kaggle.search.ListSearchContentDocument

  Attributes:
    id (int)
      The DB ID (i.e. the PK from the table) of the document
    document_type (DocumentType)
      The type of content of the document
    title (str)
      The canonical title of the document
    image_url (str)
      The thumbnail URL of the document
    create_time (datetime)
      The canonical creation time of the document; May mean different things
      between content types
    update_time (datetime)
      The canonical update time of the document; May be different between content
      types
    is_private (bool)
      Whether the content is marked as private
    votes (int)
      The total votes (or score, if downvotes are supported) for the document
    owner_user (ApiUserAvatar)
    owner_organization (ApiOrganizationCard)
    competition_document (ApiSearchCompetitionsDocument)
    dataset_document (ApiSearchDatasetsDocument)
    kernel_document (ApiSearchKernelsDocument)
    model_document (ApiSearchModelsDocument)
    discussion_document (ApiSearchDiscussionsDocument)
    user_document (ApiSearchUsersDocument)
    slug (str)
      The slug of the document (which may be close to the url)
  """

  def __init__(self):
    self._id = 0
    self._document_type = DocumentType.DOCUMENT_TYPE_UNSPECIFIED
    self._title = ""
    self._image_url = ""
    self._create_time = None
    self._update_time = None
    self._is_private = None
    self._votes = None
    self._owner_user = None
    self._owner_organization = None
    self._competition_document = None
    self._dataset_document = None
    self._kernel_document = None
    self._model_document = None
    self._discussion_document = None
    self._user_document = None
    self._slug = None
    self._freeze()

  @property
  def id(self) -> int:
    """The DB ID (i.e. the PK from the table) of the document"""
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
  def document_type(self) -> 'DocumentType':
    """The type of content of the document"""
    return self._document_type

  @document_type.setter
  def document_type(self, document_type: 'DocumentType'):
    if document_type is None:
      del self.document_type
      return
    if not isinstance(document_type, DocumentType):
      raise TypeError('document_type must be of type DocumentType')
    self._document_type = document_type

  @property
  def title(self) -> str:
    """The canonical title of the document"""
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def image_url(self) -> str:
    """The thumbnail URL of the document"""
    return self._image_url

  @image_url.setter
  def image_url(self, image_url: str):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def create_time(self) -> datetime:
    r"""
    The canonical creation time of the document; May mean different things
    between content types
    """
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
  def update_time(self) -> datetime:
    r"""
    The canonical update time of the document; May be different between content
    types
    """
    return self._update_time or None

  @update_time.setter
  def update_time(self, update_time: Optional[datetime]):
    if update_time is None:
      del self.update_time
      return
    if not isinstance(update_time, datetime):
      raise TypeError('update_time must be of type datetime')
    self._update_time = update_time

  @property
  def is_private(self) -> bool:
    """Whether the content is marked as private"""
    return self._is_private or False

  @is_private.setter
  def is_private(self, is_private: Optional[bool]):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def votes(self) -> int:
    """The total votes (or score, if downvotes are supported) for the document"""
    return self._votes or 0

  @votes.setter
  def votes(self, votes: Optional[int]):
    if votes is None:
      del self.votes
      return
    if not isinstance(votes, int):
      raise TypeError('votes must be of type int')
    self._votes = votes

  @property
  def owner_user(self) -> Optional['ApiUserAvatar']:
    return self._owner_user or None

  @owner_user.setter
  def owner_user(self, owner_user: Optional['ApiUserAvatar']):
    if owner_user is None:
      del self.owner_user
      return
    if not isinstance(owner_user, ApiUserAvatar):
      raise TypeError('owner_user must be of type ApiUserAvatar')
    del self.owner_organization
    self._owner_user = owner_user

  @property
  def owner_organization(self) -> Optional['ApiOrganizationCard']:
    return self._owner_organization or None

  @owner_organization.setter
  def owner_organization(self, owner_organization: Optional['ApiOrganizationCard']):
    if owner_organization is None:
      del self.owner_organization
      return
    if not isinstance(owner_organization, ApiOrganizationCard):
      raise TypeError('owner_organization must be of type ApiOrganizationCard')
    del self.owner_user
    self._owner_organization = owner_organization

  @property
  def competition_document(self) -> Optional['ApiSearchCompetitionsDocument']:
    return self._competition_document or None

  @competition_document.setter
  def competition_document(self, competition_document: Optional['ApiSearchCompetitionsDocument']):
    if competition_document is None:
      del self.competition_document
      return
    if not isinstance(competition_document, ApiSearchCompetitionsDocument):
      raise TypeError('competition_document must be of type ApiSearchCompetitionsDocument')
    del self.dataset_document
    del self.kernel_document
    del self.model_document
    del self.discussion_document
    del self.user_document
    self._competition_document = competition_document

  @property
  def dataset_document(self) -> Optional['ApiSearchDatasetsDocument']:
    return self._dataset_document or None

  @dataset_document.setter
  def dataset_document(self, dataset_document: Optional['ApiSearchDatasetsDocument']):
    if dataset_document is None:
      del self.dataset_document
      return
    if not isinstance(dataset_document, ApiSearchDatasetsDocument):
      raise TypeError('dataset_document must be of type ApiSearchDatasetsDocument')
    del self.competition_document
    del self.kernel_document
    del self.model_document
    del self.discussion_document
    del self.user_document
    self._dataset_document = dataset_document

  @property
  def kernel_document(self) -> Optional['ApiSearchKernelsDocument']:
    return self._kernel_document or None

  @kernel_document.setter
  def kernel_document(self, kernel_document: Optional['ApiSearchKernelsDocument']):
    if kernel_document is None:
      del self.kernel_document
      return
    if not isinstance(kernel_document, ApiSearchKernelsDocument):
      raise TypeError('kernel_document must be of type ApiSearchKernelsDocument')
    del self.competition_document
    del self.dataset_document
    del self.model_document
    del self.discussion_document
    del self.user_document
    self._kernel_document = kernel_document

  @property
  def model_document(self) -> Optional['ApiSearchModelsDocument']:
    return self._model_document or None

  @model_document.setter
  def model_document(self, model_document: Optional['ApiSearchModelsDocument']):
    if model_document is None:
      del self.model_document
      return
    if not isinstance(model_document, ApiSearchModelsDocument):
      raise TypeError('model_document must be of type ApiSearchModelsDocument')
    del self.competition_document
    del self.dataset_document
    del self.kernel_document
    del self.discussion_document
    del self.user_document
    self._model_document = model_document

  @property
  def discussion_document(self) -> Optional['ApiSearchDiscussionsDocument']:
    return self._discussion_document or None

  @discussion_document.setter
  def discussion_document(self, discussion_document: Optional['ApiSearchDiscussionsDocument']):
    if discussion_document is None:
      del self.discussion_document
      return
    if not isinstance(discussion_document, ApiSearchDiscussionsDocument):
      raise TypeError('discussion_document must be of type ApiSearchDiscussionsDocument')
    del self.competition_document
    del self.dataset_document
    del self.kernel_document
    del self.model_document
    del self.user_document
    self._discussion_document = discussion_document

  @property
  def user_document(self) -> Optional['ApiSearchUsersDocument']:
    return self._user_document or None

  @user_document.setter
  def user_document(self, user_document: Optional['ApiSearchUsersDocument']):
    if user_document is None:
      del self.user_document
      return
    if not isinstance(user_document, ApiSearchUsersDocument):
      raise TypeError('user_document must be of type ApiSearchUsersDocument')
    del self.competition_document
    del self.dataset_document
    del self.kernel_document
    del self.model_document
    del self.discussion_document
    self._user_document = user_document

  @property
  def slug(self) -> str:
    """The slug of the document (which may be close to the url)"""
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug


class ListEntitiesFilters(KaggleObject):
  r"""
   Based on kaggle.search.ListSearchContentFilters

  Attributes:
    query (str)
      The free-text query the user entered to filter results
    list_type (ApiListType)
      The type of list being requested
    privacy (PrivacyFilter)
      The privacy filter to apply
    owner_type (OwnerType)
      The owner type filter to apply
    document_types (DocumentType)
      The document type filter to apply
    competition_filters (ApiSearchCompetitionsFilters)
      The set of Competition filters to filter the documents
    dataset_filters (ApiSearchDatasetsFilters)
      The set of Dataset filters to filter the documents
    discussion_filters (ApiSearchDiscussionsFilters)
      The set of Discussion filters to filter the documents
    kernel_filters (ApiSearchKernelsFilters)
      The set of Kernel filters to filter the documents
    model_filters (ApiSearchModelsFilters)
      The set of Model filters to filter the documents
    user_filters (ApiSearchUsersFilters)
      The set of User filters to filter the documents
  """

  def __init__(self):
    self._query = ""
    self._list_type = ApiListType.API_LIST_TYPE_UNSPECIFIED
    self._privacy = PrivacyFilter.ALL
    self._owner_type = OwnerType.OWNER_TYPE_UNSPECIFIED
    self._document_types = []
    self._competition_filters = None
    self._dataset_filters = None
    self._discussion_filters = None
    self._kernel_filters = None
    self._model_filters = None
    self._user_filters = None
    self._freeze()

  @property
  def query(self) -> str:
    """The free-text query the user entered to filter results"""
    return self._query

  @query.setter
  def query(self, query: str):
    if query is None:
      del self.query
      return
    if not isinstance(query, str):
      raise TypeError('query must be of type str')
    self._query = query

  @property
  def list_type(self) -> 'ApiListType':
    """The type of list being requested"""
    return self._list_type

  @list_type.setter
  def list_type(self, list_type: 'ApiListType'):
    if list_type is None:
      del self.list_type
      return
    if not isinstance(list_type, ApiListType):
      raise TypeError('list_type must be of type ApiListType')
    self._list_type = list_type

  @property
  def privacy(self) -> 'PrivacyFilter':
    """The privacy filter to apply"""
    return self._privacy

  @privacy.setter
  def privacy(self, privacy: 'PrivacyFilter'):
    if privacy is None:
      del self.privacy
      return
    if not isinstance(privacy, PrivacyFilter):
      raise TypeError('privacy must be of type PrivacyFilter')
    self._privacy = privacy

  @property
  def owner_type(self) -> 'OwnerType':
    """The owner type filter to apply"""
    return self._owner_type

  @owner_type.setter
  def owner_type(self, owner_type: 'OwnerType'):
    if owner_type is None:
      del self.owner_type
      return
    if not isinstance(owner_type, OwnerType):
      raise TypeError('owner_type must be of type OwnerType')
    self._owner_type = owner_type

  @property
  def document_types(self) -> Optional[List['DocumentType']]:
    """The document type filter to apply"""
    return self._document_types

  @document_types.setter
  def document_types(self, document_types: Optional[List['DocumentType']]):
    if document_types is None:
      del self.document_types
      return
    if not isinstance(document_types, list):
      raise TypeError('document_types must be of type list')
    if not all([isinstance(t, DocumentType) for t in document_types]):
      raise TypeError('document_types must contain only items of type DocumentType')
    self._document_types = document_types

  @property
  def competition_filters(self) -> Optional['ApiSearchCompetitionsFilters']:
    """The set of Competition filters to filter the documents"""
    return self._competition_filters

  @competition_filters.setter
  def competition_filters(self, competition_filters: Optional['ApiSearchCompetitionsFilters']):
    if competition_filters is None:
      del self.competition_filters
      return
    if not isinstance(competition_filters, ApiSearchCompetitionsFilters):
      raise TypeError('competition_filters must be of type ApiSearchCompetitionsFilters')
    self._competition_filters = competition_filters

  @property
  def dataset_filters(self) -> Optional['ApiSearchDatasetsFilters']:
    """The set of Dataset filters to filter the documents"""
    return self._dataset_filters

  @dataset_filters.setter
  def dataset_filters(self, dataset_filters: Optional['ApiSearchDatasetsFilters']):
    if dataset_filters is None:
      del self.dataset_filters
      return
    if not isinstance(dataset_filters, ApiSearchDatasetsFilters):
      raise TypeError('dataset_filters must be of type ApiSearchDatasetsFilters')
    self._dataset_filters = dataset_filters

  @property
  def discussion_filters(self) -> Optional['ApiSearchDiscussionsFilters']:
    """The set of Discussion filters to filter the documents"""
    return self._discussion_filters

  @discussion_filters.setter
  def discussion_filters(self, discussion_filters: Optional['ApiSearchDiscussionsFilters']):
    if discussion_filters is None:
      del self.discussion_filters
      return
    if not isinstance(discussion_filters, ApiSearchDiscussionsFilters):
      raise TypeError('discussion_filters must be of type ApiSearchDiscussionsFilters')
    self._discussion_filters = discussion_filters

  @property
  def kernel_filters(self) -> Optional['ApiSearchKernelsFilters']:
    """The set of Kernel filters to filter the documents"""
    return self._kernel_filters

  @kernel_filters.setter
  def kernel_filters(self, kernel_filters: Optional['ApiSearchKernelsFilters']):
    if kernel_filters is None:
      del self.kernel_filters
      return
    if not isinstance(kernel_filters, ApiSearchKernelsFilters):
      raise TypeError('kernel_filters must be of type ApiSearchKernelsFilters')
    self._kernel_filters = kernel_filters

  @property
  def model_filters(self) -> Optional['ApiSearchModelsFilters']:
    """The set of Model filters to filter the documents"""
    return self._model_filters

  @model_filters.setter
  def model_filters(self, model_filters: Optional['ApiSearchModelsFilters']):
    if model_filters is None:
      del self.model_filters
      return
    if not isinstance(model_filters, ApiSearchModelsFilters):
      raise TypeError('model_filters must be of type ApiSearchModelsFilters')
    self._model_filters = model_filters

  @property
  def user_filters(self) -> Optional['ApiSearchUsersFilters']:
    """The set of User filters to filter the documents"""
    return self._user_filters

  @user_filters.setter
  def user_filters(self, user_filters: Optional['ApiSearchUsersFilters']):
    if user_filters is None:
      del self.user_filters
      return
    if not isinstance(user_filters, ApiSearchUsersFilters):
      raise TypeError('user_filters must be of type ApiSearchUsersFilters')
    self._user_filters = user_filters


class ListEntitiesRequest(KaggleObject):
  r"""
  Attributes:
    filters (ListEntitiesFilters)
      Canonical filters to apply to the search
    canonical_order_by (ListSearchContentOrderBy)
      Canonical order to apply to the results
    competitions_order_by (SearchCompetitionsOrderBy)
      Competitions order to apply to the results
    datasets_order_by (SearchDatasetsOrderBy)
      Datasets order to apply to the results
    kernels_order_by (SearchKernelsOrderBy)
      Kernels order to apply to the results
    models_order_by (SearchModelsOrderBy)
      Models order to apply to the results
    discussions_order_by (SearchDiscussionsOrderBy)
      Discussions order to apply to the results
    users_order_by (SearchUsersOrderBy)
      Users order to apply to the results
    page_token (str)
      Page token for paging (see aip.dev/158)
    page_size (int)
      Number of documents per page to return
    skip (int)
      How many results to skip
  """

  def __init__(self):
    self._filters = None
    self._canonical_order_by = None
    self._competitions_order_by = None
    self._datasets_order_by = None
    self._kernels_order_by = None
    self._models_order_by = None
    self._discussions_order_by = None
    self._users_order_by = None
    self._page_token = ""
    self._page_size = 0
    self._skip = 0
    self._freeze()

  @property
  def filters(self) -> Optional['ListEntitiesFilters']:
    """Canonical filters to apply to the search"""
    return self._filters

  @filters.setter
  def filters(self, filters: Optional['ListEntitiesFilters']):
    if filters is None:
      del self.filters
      return
    if not isinstance(filters, ListEntitiesFilters):
      raise TypeError('filters must be of type ListEntitiesFilters')
    self._filters = filters

  @property
  def canonical_order_by(self) -> 'ListSearchContentOrderBy':
    """Canonical order to apply to the results"""
    return self._canonical_order_by or ListSearchContentOrderBy.LIST_SEARCH_CONTENT_ORDER_BY_UNSPECIFIED

  @canonical_order_by.setter
  def canonical_order_by(self, canonical_order_by: 'ListSearchContentOrderBy'):
    if canonical_order_by is None:
      del self.canonical_order_by
      return
    if not isinstance(canonical_order_by, ListSearchContentOrderBy):
      raise TypeError('canonical_order_by must be of type ListSearchContentOrderBy')
    del self.competitions_order_by
    del self.datasets_order_by
    del self.kernels_order_by
    del self.models_order_by
    del self.discussions_order_by
    del self.users_order_by
    self._canonical_order_by = canonical_order_by

  @property
  def competitions_order_by(self) -> 'SearchCompetitionsOrderBy':
    """Competitions order to apply to the results"""
    return self._competitions_order_by or SearchCompetitionsOrderBy.SEARCH_COMPETITIONS_ORDER_BY_UNSPECIFIED

  @competitions_order_by.setter
  def competitions_order_by(self, competitions_order_by: 'SearchCompetitionsOrderBy'):
    if competitions_order_by is None:
      del self.competitions_order_by
      return
    if not isinstance(competitions_order_by, SearchCompetitionsOrderBy):
      raise TypeError('competitions_order_by must be of type SearchCompetitionsOrderBy')
    del self.canonical_order_by
    del self.datasets_order_by
    del self.kernels_order_by
    del self.models_order_by
    del self.discussions_order_by
    del self.users_order_by
    self._competitions_order_by = competitions_order_by

  @property
  def datasets_order_by(self) -> 'SearchDatasetsOrderBy':
    """Datasets order to apply to the results"""
    return self._datasets_order_by or SearchDatasetsOrderBy.SEARCH_DATASETS_ORDER_BY_UNSPECIFIED

  @datasets_order_by.setter
  def datasets_order_by(self, datasets_order_by: 'SearchDatasetsOrderBy'):
    if datasets_order_by is None:
      del self.datasets_order_by
      return
    if not isinstance(datasets_order_by, SearchDatasetsOrderBy):
      raise TypeError('datasets_order_by must be of type SearchDatasetsOrderBy')
    del self.canonical_order_by
    del self.competitions_order_by
    del self.kernels_order_by
    del self.models_order_by
    del self.discussions_order_by
    del self.users_order_by
    self._datasets_order_by = datasets_order_by

  @property
  def kernels_order_by(self) -> 'SearchKernelsOrderBy':
    """Kernels order to apply to the results"""
    return self._kernels_order_by or SearchKernelsOrderBy.SEARCH_KERNELS_ORDER_BY_UNSPECIFIED

  @kernels_order_by.setter
  def kernels_order_by(self, kernels_order_by: 'SearchKernelsOrderBy'):
    if kernels_order_by is None:
      del self.kernels_order_by
      return
    if not isinstance(kernels_order_by, SearchKernelsOrderBy):
      raise TypeError('kernels_order_by must be of type SearchKernelsOrderBy')
    del self.canonical_order_by
    del self.competitions_order_by
    del self.datasets_order_by
    del self.models_order_by
    del self.discussions_order_by
    del self.users_order_by
    self._kernels_order_by = kernels_order_by

  @property
  def models_order_by(self) -> 'SearchModelsOrderBy':
    """Models order to apply to the results"""
    return self._models_order_by or SearchModelsOrderBy.MODELS_SEARCH_ORDER_BY_UNSPECIFIED

  @models_order_by.setter
  def models_order_by(self, models_order_by: 'SearchModelsOrderBy'):
    if models_order_by is None:
      del self.models_order_by
      return
    if not isinstance(models_order_by, SearchModelsOrderBy):
      raise TypeError('models_order_by must be of type SearchModelsOrderBy')
    del self.canonical_order_by
    del self.competitions_order_by
    del self.datasets_order_by
    del self.kernels_order_by
    del self.discussions_order_by
    del self.users_order_by
    self._models_order_by = models_order_by

  @property
  def discussions_order_by(self) -> 'SearchDiscussionsOrderBy':
    """Discussions order to apply to the results"""
    return self._discussions_order_by or SearchDiscussionsOrderBy.SEARCH_DISCUSSIONS_ORDER_BY_UNSPECIFIED

  @discussions_order_by.setter
  def discussions_order_by(self, discussions_order_by: 'SearchDiscussionsOrderBy'):
    if discussions_order_by is None:
      del self.discussions_order_by
      return
    if not isinstance(discussions_order_by, SearchDiscussionsOrderBy):
      raise TypeError('discussions_order_by must be of type SearchDiscussionsOrderBy')
    del self.canonical_order_by
    del self.competitions_order_by
    del self.datasets_order_by
    del self.kernels_order_by
    del self.models_order_by
    del self.users_order_by
    self._discussions_order_by = discussions_order_by

  @property
  def users_order_by(self) -> 'SearchUsersOrderBy':
    """Users order to apply to the results"""
    return self._users_order_by or SearchUsersOrderBy.SEARCH_USERS_ORDER_BY_UNSPECIFIED

  @users_order_by.setter
  def users_order_by(self, users_order_by: 'SearchUsersOrderBy'):
    if users_order_by is None:
      del self.users_order_by
      return
    if not isinstance(users_order_by, SearchUsersOrderBy):
      raise TypeError('users_order_by must be of type SearchUsersOrderBy')
    del self.canonical_order_by
    del self.competitions_order_by
    del self.datasets_order_by
    del self.kernels_order_by
    del self.models_order_by
    del self.discussions_order_by
    self._users_order_by = users_order_by

  @property
  def page_token(self) -> str:
    """Page token for paging (see aip.dev/158)"""
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def page_size(self) -> int:
    """Number of documents per page to return"""
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
  def skip(self) -> int:
    """How many results to skip"""
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  def endpoint(self):
    path = '/api/v1/search/list-entities'
    return path.format_map(self.to_field_map(self))


class ListEntitiesResponse(KaggleObject):
  r"""
  Attributes:
    documents (ListEntitiesDocument)
      The list of documents returned after filtering
    total_documents (int)
      The total number of documents matching any filters
    next_page_token (str)
      The token to request the next page
  """

  def __init__(self):
    self._documents = []
    self._total_documents = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def documents(self) -> Optional[List[Optional['ListEntitiesDocument']]]:
    """The list of documents returned after filtering"""
    return self._documents

  @documents.setter
  def documents(self, documents: Optional[List[Optional['ListEntitiesDocument']]]):
    if documents is None:
      del self.documents
      return
    if not isinstance(documents, list):
      raise TypeError('documents must be of type list')
    if not all([isinstance(t, ListEntitiesDocument) for t in documents]):
      raise TypeError('documents must contain only items of type ListEntitiesDocument')
    self._documents = documents

  @property
  def total_documents(self) -> int:
    """The total number of documents matching any filters"""
    return self._total_documents

  @total_documents.setter
  def total_documents(self, total_documents: int):
    if total_documents is None:
      del self.total_documents
      return
    if not isinstance(total_documents, int):
      raise TypeError('total_documents must be of type int')
    self._total_documents = total_documents

  @property
  def next_page_token(self) -> str:
    """The token to request the next page"""
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
  def totalDocuments(self):
    return self.total_documents

  @property
  def nextPageToken(self):
    return self.next_page_token


ApiOrganizationCard._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
]

ApiSearchCompetitionsDocument._fields = [
  FieldMetadata("hostSegment", "host_segment", "_host_segment", HostSegment, HostSegment.HOST_SEGMENT_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("teamCount", "team_count", "_team_count", int, 0, PredefinedSerializer()),
  FieldMetadata("teamRank", "team_rank", "_team_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isEnvironmentEvaluation", "is_environment_evaluation", "_is_environment_evaluation", bool, False, PredefinedSerializer()),
  FieldMetadata("prizeType", "prize_type", "_prize_type", RewardTypeId, RewardTypeId.REWARD_TYPE_ID_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("prizeValue", "prize_value", "_prize_value", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isLaunched", "is_launched", "_is_launched", bool, False, PredefinedSerializer()),
  FieldMetadata("ownerUserHasJoined", "owner_user_has_joined", "_owner_user_has_joined", bool, False, PredefinedSerializer()),
  FieldMetadata("isLimitedParticipation", "is_limited_participation", "_is_limited_participation", bool, False, PredefinedSerializer()),
  FieldMetadata("onlyAllowKernelSubmissions", "only_allow_kernel_submissions", "_only_allow_kernel_submissions", bool, False, PredefinedSerializer()),
]

ApiSearchCompetitionsFilters._fields = [
  FieldMetadata("role", "role", "_role", SearchCompetitionsRole, SearchCompetitionsRole.SEARCH_COMPETITIONS_ROLE_ANY, EnumSerializer()),
  FieldMetadata("status", "status", "_status", SearchCompetitionsStatus, SearchCompetitionsStatus.SEARCH_COMPETITIONS_STATUS_ANY, EnumSerializer()),
  FieldMetadata("profileVisibility", "profile_visibility", "_profile_visibility", SearchCompetitionsProfileVisibility, SearchCompetitionsProfileVisibility.SEARCH_COMPETITIONS_PROFILE_VISIBILITY_ANY, EnumSerializer()),
  FieldMetadata("earnedMedal", "earned_medal", "_earned_medal", bool, None, PredefinedSerializer(), optional=True),
]

ApiSearchDatasetsDocument._fields = [
  FieldMetadata("usabilityRating", "usability_rating", "_usability_rating", float, 0.0, PredefinedSerializer()),
  FieldMetadata("fileCount", "file_count", "_file_count", int, 0, PredefinedSerializer()),
  FieldMetadata("fileTypes", "file_types", "_file_types", DatasetFileType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("size", "size", "_size", int, 0, PredefinedSerializer()),
]

ApiSearchDatasetsFilters._fields = [
  FieldMetadata("fileType", "file_type", "_file_type", DatasetFileTypeGroup, DatasetFileTypeGroup.DATASET_FILE_TYPE_GROUP_ALL, EnumSerializer()),
  FieldMetadata("licenseGroup", "license_group", "_license_group", DatasetLicenseGroup, None, EnumSerializer(), optional=True),
  FieldMetadata("size", "size", "_size", DatasetSizeGroup, None, EnumSerializer(), optional=True),
  FieldMetadata("earnedMedal", "earned_medal", "_earned_medal", bool, None, PredefinedSerializer(), optional=True),
]

ApiSearchDiscussionsDocument._fields = [
  FieldMetadata("newCommentUrl", "new_comment_url", "_new_comment_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("messageStripped", "message_stripped", "_message_stripped", str, "", PredefinedSerializer()),
  FieldMetadata("messageMarkdown", "message_markdown", "_message_markdown", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumName", "forum_name", "_forum_name", str, "", PredefinedSerializer()),
  FieldMetadata("forumUrl", "forum_url", "_forum_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceType", "source_type", "_source_type", SearchDiscussionsSourceType, SearchDiscussionsSourceType.SEARCH_DISCUSSIONS_SOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("topicType", "topic_type", "_topic_type", SearchDiscussionsTopicType, SearchDiscussionsTopicType.SEARCH_DISCUSSIONS_TOPIC_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("type", "type", "_type", SearchDiscussionsDocumentType, SearchDiscussionsDocumentType.SEARCH_DISCUSSIONS_DOCUMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("writeUpMetadata", "write_up_metadata", "_write_up_metadata", WriteUpItemInfo, None, KaggleObjectSerializer(), optional=True),
]

ApiSearchDiscussionsFilters._fields = [
  FieldMetadata("sourceType", "source_type", "_source_type", SearchDiscussionsSourceType, SearchDiscussionsSourceType.SEARCH_DISCUSSIONS_SOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("onlyNewComments", "only_new_comments", "_only_new_comments", bool, False, PredefinedSerializer()),
  FieldMetadata("writeUpInclusionType", "write_up_inclusion_type", "_write_up_inclusion_type", WriteUpInclusionType, WriteUpInclusionType.WRITE_UP_INCLUSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("writeUpTypes", "write_up_types", "_write_up_types", WriteUpType, [], ListSerializer(EnumSerializer())),
]

ApiSearchKernelsDocument._fields = [
  FieldMetadata("sessionId", "session_id", "_session_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasLinkedSubmission", "has_linked_submission", "_has_linked_submission", bool, False, PredefinedSerializer()),
  FieldMetadata("datasourceIsPrivate", "datasource_is_private", "_datasource_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("bestPublicScore", "best_public_score", "_best_public_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("isDraft", "is_draft", "_is_draft", bool, False, PredefinedSerializer()),
]

ApiSearchKernelsFilters._fields = [
  FieldMetadata("language", "language", "_language", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("earnedMedal", "earned_medal", "_earned_medal", bool, None, PredefinedSerializer(), optional=True),
]

ApiSearchModelsDocument._fields = [
  FieldMetadata("instanceCount", "instance_count", "_instance_count", int, 0, PredefinedSerializer()),
  FieldMetadata("notebookCount", "notebook_count", "_notebook_count", int, 0, PredefinedSerializer()),
]

ApiSearchModelsFilters._fields = [
  FieldMetadata("size", "size", "_size", ListSearchContentRangeFilter, None, KaggleObjectSerializer()),
]

ApiSearchUsersDocument._fields = [
  FieldMetadata("grandmasterTierLevel", "grandmaster_tier_level", "_grandmaster_tier_level", int, 0, PredefinedSerializer()),
  FieldMetadata("userLocation", "user_location", "_user_location", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("occupationOrganizationName", "occupation_organization_name", "_occupation_organization_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionRanking", "competition_ranking", "_competition_ranking", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionPoints", "competition_points", "_competition_points", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelRanking", "kernel_ranking", "_kernel_ranking", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelPoints", "kernel_points", "_kernel_points", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetRanking", "dataset_ranking", "_dataset_ranking", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetPoints", "dataset_points", "_dataset_points", int, None, PredefinedSerializer(), optional=True),
]

ApiSearchUsersFilters._fields = [
  FieldMetadata("userLocations", "user_locations", "_user_locations", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, None, EnumSerializer(), optional=True),
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("requireRankingForType", "require_ranking_for_type", "_require_ranking_for_type", UserAchievementType, None, EnumSerializer(), optional=True),
  FieldMetadata("occupationOrganizationNames", "occupation_organization_names", "_occupation_organization_names", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("grandmasterLevel", "grandmaster_level", "_grandmaster_level", ListSearchContentRangeFilter, None, KaggleObjectSerializer()),
]

ApiUserAvatar._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("progressionOptOut", "progression_opt_out", "_progression_opt_out", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
]

ListEntitiesDocument._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("documentType", "document_type", "_document_type", DocumentType, DocumentType.DOCUMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("updateTime", "update_time", "_update_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("votes", "votes", "_votes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", ApiUserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("ownerOrganization", "owner_organization", "_owner_organization", ApiOrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("competitionDocument", "competition_document", "_competition_document", ApiSearchCompetitionsDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("datasetDocument", "dataset_document", "_dataset_document", ApiSearchDatasetsDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("kernelDocument", "kernel_document", "_kernel_document", ApiSearchKernelsDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("modelDocument", "model_document", "_model_document", ApiSearchModelsDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("discussionDocument", "discussion_document", "_discussion_document", ApiSearchDiscussionsDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("userDocument", "user_document", "_user_document", ApiSearchUsersDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
]

ListEntitiesFilters._fields = [
  FieldMetadata("query", "query", "_query", str, "", PredefinedSerializer()),
  FieldMetadata("listType", "list_type", "_list_type", ApiListType, ApiListType.API_LIST_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("privacy", "privacy", "_privacy", PrivacyFilter, PrivacyFilter.ALL, EnumSerializer()),
  FieldMetadata("ownerType", "owner_type", "_owner_type", OwnerType, OwnerType.OWNER_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("documentTypes", "document_types", "_document_types", DocumentType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("competitionFilters", "competition_filters", "_competition_filters", ApiSearchCompetitionsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("datasetFilters", "dataset_filters", "_dataset_filters", ApiSearchDatasetsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("discussionFilters", "discussion_filters", "_discussion_filters", ApiSearchDiscussionsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("kernelFilters", "kernel_filters", "_kernel_filters", ApiSearchKernelsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("modelFilters", "model_filters", "_model_filters", ApiSearchModelsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("userFilters", "user_filters", "_user_filters", ApiSearchUsersFilters, None, KaggleObjectSerializer()),
]

ListEntitiesRequest._fields = [
  FieldMetadata("filters", "filters", "_filters", ListEntitiesFilters, None, KaggleObjectSerializer()),
  FieldMetadata("canonicalOrderBy", "canonical_order_by", "_canonical_order_by", ListSearchContentOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("competitionsOrderBy", "competitions_order_by", "_competitions_order_by", SearchCompetitionsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("datasetsOrderBy", "datasets_order_by", "_datasets_order_by", SearchDatasetsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("kernelsOrderBy", "kernels_order_by", "_kernels_order_by", SearchKernelsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("modelsOrderBy", "models_order_by", "_models_order_by", SearchModelsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("discussionsOrderBy", "discussions_order_by", "_discussions_order_by", SearchDiscussionsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("usersOrderBy", "users_order_by", "_users_order_by", SearchUsersOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
]

ListEntitiesResponse._fields = [
  FieldMetadata("documents", "documents", "_documents", ListEntitiesDocument, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalDocuments", "total_documents", "_total_documents", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

