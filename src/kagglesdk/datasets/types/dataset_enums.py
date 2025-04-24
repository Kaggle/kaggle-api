import enum

class DatabundleVersionStatus(enum.Enum):
  NOT_YET_PERSISTED = 0
  BLOBS_RECEIVED = 1
  BLOBS_DECOMPRESSED = 2
  BLOBS_COPIED_TO_SDS = 3
  INDIVIDUAL_BLOBS_COMPRESSED = 4
  READY = 5
  FAILED = 6
  DELETED = 7
  REPROCESSING = 8

class DatasetFileTypeGroup(enum.Enum):
  r"""
  This enum drives acceptable values from the python API, so avoid changing
  enum member names if possible
  """
  DATASET_FILE_TYPE_GROUP_ALL = 0
  DATASET_FILE_TYPE_GROUP_CSV = 1
  DATASET_FILE_TYPE_GROUP_SQLITE = 2
  DATASET_FILE_TYPE_GROUP_JSON = 3
  DATASET_FILE_TYPE_GROUP_BIG_QUERY = 4

class DatasetLicenseGroup(enum.Enum):
  r"""
  This enum drives acceptable values from the python API, so avoid changing
  enum member names if possible
  """
  DATASET_LICENSE_GROUP_ALL = 0
  DATASET_LICENSE_GROUP_CC = 1
  DATASET_LICENSE_GROUP_GPL = 2
  DATASET_LICENSE_GROUP_ODB = 3
  DATASET_LICENSE_GROUP_OTHER = 4

class DatasetSelectionGroup(enum.Enum):
  DATASET_SELECTION_GROUP_PUBLIC = 0
  DATASET_SELECTION_GROUP_MY = 1
  DATASET_SELECTION_GROUP_USER = 2
  DATASET_SELECTION_GROUP_USER_SHARED_WITH_ME = 3
  DATASET_SELECTION_GROUP_UPVOTED = 4
  DATASET_SELECTION_GROUP_MY_PRIVATE = 5
  DATASET_SELECTION_GROUP_MY_PUBLIC = 10
  DATASET_SELECTION_GROUP_ORGANIZATION = 6
  DATASET_SELECTION_GROUP_BOOKMARKED = 11
  DATASET_SELECTION_GROUP_COLLABORATION = 12
  DATASET_SELECTION_GROUP_SHARED_WITH_USER = 13
  DATASET_SELECTION_GROUP_FEATURED = 7
  """Old"""
  DATASET_SELECTION_GROUP_ALL = 8
  DATASET_SELECTION_GROUP_UNFEATURED = 9

class DatasetSizeGroup(enum.Enum):
  r"""
  This enum drives acceptable values from the python API, so avoid changing
  enum member names if possible
  """
  DATASET_SIZE_GROUP_ALL = 0
  DATASET_SIZE_GROUP_SMALL = 1
  DATASET_SIZE_GROUP_MEDIUM = 2
  DATASET_SIZE_GROUP_LARGE = 3

class DatasetSortBy(enum.Enum):
  r"""
  This enum drives acceptable values from the python API, so avoid changing
  enum member names if possible
  """
  DATASET_SORT_BY_HOTTEST = 0
  DATASET_SORT_BY_VOTES = 1
  DATASET_SORT_BY_UPDATED = 2
  DATASET_SORT_BY_ACTIVE = 3
  """Deprecated"""
  DATASET_SORT_BY_PUBLISHED = 4
  DATASET_SORT_BY_RELEVANCE = 5
  """Old world"""
  DATASET_SORT_BY_LAST_VIEWED = 6
  DATASET_SORT_BY_USABILITY = 7

class DatasetViewedGroup(enum.Enum):
  DATASET_VIEWED_GROUP_UNSPECIFIED = 0
  DATASET_VIEWED_GROUP_VIEWED = 1

