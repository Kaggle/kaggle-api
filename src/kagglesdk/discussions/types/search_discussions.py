import enum
from kagglesdk.community.types.content_enums import ContentState
from kagglesdk.discussions.types.writeup_enums import WriteUpType
from kagglesdk.kaggle_object import *
from typing import Optional

class SearchDiscussionsOrderBy(enum.Enum):
  SEARCH_DISCUSSIONS_ORDER_BY_UNSPECIFIED = 0
  SEARCH_DISCUSSIONS_ORDER_BY_LAST_TOPIC_COMMENT_DATE = 1

class SearchDiscussionsDocumentType(enum.Enum):
  SEARCH_DISCUSSIONS_DOCUMENT_TYPE_UNSPECIFIED = 0
  SEARCH_DISCUSSIONS_DOCUMENT_TYPE_COMMENT = 1
  SEARCH_DISCUSSIONS_DOCUMENT_TYPE_TOPIC = 2
  SEARCH_DISCUSSIONS_DOCUMENT_TYPE_WRITE_UP = 3

class SearchDiscussionsSourceType(enum.Enum):
  SEARCH_DISCUSSIONS_SOURCE_TYPE_UNSPECIFIED = 0
  SEARCH_DISCUSSIONS_SOURCE_TYPE_COMPETITION = 1
  SEARCH_DISCUSSIONS_SOURCE_TYPE_DATASET = 2
  SEARCH_DISCUSSIONS_SOURCE_TYPE_KERNEL = 4
  SEARCH_DISCUSSIONS_SOURCE_TYPE_SITE_FORUM = 5
  SEARCH_DISCUSSIONS_SOURCE_TYPE_COMPETITION_SOLUTION = 6
  SEARCH_DISCUSSIONS_SOURCE_TYPE_MODEL = 7
  SEARCH_DISCUSSIONS_SOURCE_TYPE_WRITE_UP = 8

class SearchDiscussionsTopicType(enum.Enum):
  SEARCH_DISCUSSIONS_TOPIC_TYPE_UNSPECIFIED = 0
  SEARCH_DISCUSSIONS_TOPIC_TYPE_TOPICS = 1
  SEARCH_DISCUSSIONS_TOPIC_TYPE_WRITE_UPS = 2

class WriteUpInclusionType(enum.Enum):
  WRITE_UP_INCLUSION_TYPE_UNSPECIFIED = 0
  WRITE_UP_INCLUSION_TYPE_EXCLUDE = 1
  r"""
  Only ForumTopics will be included, while
  WriteUps will be excluded
  """
  WRITE_UP_INCLUSION_TYPE_INCLUDE = 2
  """WriteUps and ForumTopics will be included"""
  WRITE_UP_INCLUSION_TYPE_ONLY = 3
  r"""
  Only WriteUps will be included, while
  ForumTopics will be excluded
  """

class SearchDiscussionsWriteUpMetadata(KaggleObject):
  r"""
  Attributes:
    type (WriteUpType)
      Type of the WriteUp
    content_state (ContentState)
      Content state of the WriteUp
  """

  def __init__(self):
    self._type = WriteUpType.WRITE_UP_TYPE_UNSPECIFIED
    self._content_state = ContentState.CONTENT_STATE_UNSPECIFIED
    self._freeze()

  @property
  def type(self) -> 'WriteUpType':
    """Type of the WriteUp"""
    return self._type

  @type.setter
  def type(self, type: 'WriteUpType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, WriteUpType):
      raise TypeError('type must be of type WriteUpType')
    self._type = type

  @property
  def content_state(self) -> 'ContentState':
    """Content state of the WriteUp"""
    return self._content_state

  @content_state.setter
  def content_state(self, content_state: 'ContentState'):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state


SearchDiscussionsWriteUpMetadata._fields = [
  FieldMetadata("type", "type", "_type", WriteUpType, WriteUpType.WRITE_UP_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, ContentState.CONTENT_STATE_UNSPECIFIED, EnumSerializer()),
]

