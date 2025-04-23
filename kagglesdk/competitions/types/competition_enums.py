import enum

class CompetitionListTab(enum.Enum):
  COMPETITION_LIST_TAB_GENERAL = 0
  """TODO(aip.dev/126): (-- api-linter: core::0126::unspecified=disabled --)"""
  COMPETITION_LIST_TAB_ENTERED = 1
  COMPETITION_LIST_TAB_COMMUNITY = 2
  COMPETITION_LIST_TAB_HOSTED = 3
  COMPETITION_LIST_TAB_UNLAUNCHED = 4
  COMPETITION_LIST_TAB_UNLAUNCHED_COMMUNITY = 5
  COMPETITION_LIST_TAB_EVERYTHING = 6

class CompetitionSortBy(enum.Enum):
  COMPETITION_SORT_BY_GROUPED = 0
  """TODO(aip.dev/126): (-- api-linter: core::0126::unspecified=disabled --)"""
  COMPETITION_SORT_BY_BEST = 1
  COMPETITION_SORT_BY_PRIZE = 2
  COMPETITION_SORT_BY_EARLIEST_DEADLINE = 3
  COMPETITION_SORT_BY_LATEST_DEADLINE = 4
  COMPETITION_SORT_BY_NUMBER_OF_TEAMS = 5
  COMPETITION_SORT_BY_RELEVANCE = 6
  COMPETITION_SORT_BY_RECENTLY_CREATED = 7

class HostSegment(enum.Enum):
  r"""
  NOTE: Keep in Sync with Kaggle.Entities.HostSegment until migrated! Also keep
  the comment in
  competition_service.ListCompetitionsRequest.Selector.host_segment_id_filter
  up to date
  """
  HOST_SEGMENT_UNSPECIFIED = 0
  HOST_SEGMENT_FEATURED = 1
  HOST_SEGMENT_GETTING_STARTED = 5
  HOST_SEGMENT_MASTERS = 6
  HOST_SEGMENT_PLAYGROUND = 8
  HOST_SEGMENT_RECRUITMENT = 3
  HOST_SEGMENT_RESEARCH = 2
  HOST_SEGMENT_COMMUNITY = 10
  HOST_SEGMENT_ANALYTICS = 11

class SubmissionGroup(enum.Enum):
  SUBMISSION_GROUP_ALL = 0
  """TODO(aip.dev/126): (-- api-linter: core::0126::unspecified=disabled --)"""
  SUBMISSION_GROUP_SUCCESSFUL = 1
  SUBMISSION_GROUP_SELECTED = 2

class SubmissionSortBy(enum.Enum):
  SUBMISSION_SORT_BY_DATE = 0
  """TODO(aip.dev/126): (-- api-linter: core::0126::unspecified=disabled --)"""
  SUBMISSION_SORT_BY_NAME = 1
  SUBMISSION_SORT_BY_PRIVATE_SCORE = 2
  SUBMISSION_SORT_BY_PUBLIC_SCORE = 3

