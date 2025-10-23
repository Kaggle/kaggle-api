import enum

class ListSearchContentOrderBy(enum.Enum):
  LIST_SEARCH_CONTENT_ORDER_BY_UNSPECIFIED = 0
  LIST_SEARCH_CONTENT_ORDER_BY_DATE_CREATED = 1
  LIST_SEARCH_CONTENT_ORDER_BY_DATE_UPDATED = 2
  LIST_SEARCH_CONTENT_ORDER_BY_HOTNESS = 3
  LIST_SEARCH_CONTENT_ORDER_BY_LAST_VIEWED = 4
  LIST_SEARCH_CONTENT_ORDER_BY_TOTAL_COMMENTS = 5
  LIST_SEARCH_CONTENT_ORDER_BY_VOTES = 6

class DocumentType(enum.Enum):
  DOCUMENT_TYPE_UNSPECIFIED = 0
  BLOG = 1
  COMPETITION = 2
  DATASET = 3
  KERNEL = 5
  COMMENT = 6
  TOPIC = 8
  USER = 9
  COURSE = 10
  TUTORIAL = 11
  MODEL = 12
  RESOURCEREFERENCE = 13
  BENCHMARKTASK = 14
  BENCHMARK = 15

class OwnerType(enum.Enum):
  OWNER_TYPE_UNSPECIFIED = 0
  """ownerUserId is sole owner of content or is in read/writeGroupId"""
  OWNER_TYPE_OWNS = 1
  """ownerUserId is sole owner of content"""
  OWNER_TYPE_COLLABORATIONS = 2
  """ownerUserId is in read/writeGroupId, but not owner [Profiles only]"""
  OWNER_TYPE_SHARED_WITH_CURRENT_USER = 3
  """ownerUserId is sole owner of content, currentUser is in read/writeGroupId"""

class PrivacyFilter(enum.Enum):
  ALL = 0
  """Return all search results (private and public)."""
  PRIVATE = 1
  """Return only private search results (if caller has access, of course)."""
  PUBLIC = 2
  """Return only public search results."""

