from datetime import datetime
from kagglesdk.competitions.types.competition_enums import CompetitionListTab, CompetitionSortBy, HostSegment, SubmissionGroup, SubmissionSortBy
from kagglesdk.competitions.types.submission_status import SubmissionStatus
from kagglesdk.kaggle_object import *
from typing import Optional, List

class ApiCreateCodeSubmissionRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
    kernel_owner (str)
    kernel_slug (str)
    kernel_version (int)
    file_name (str)
    submission_description (str)
  """

  def __init__(self):
    self._competition_name = ""
    self._kernel_owner = ""
    self._kernel_slug = ""
    self._kernel_version = None
    self._file_name = None
    self._submission_description = None
    self._freeze()

  @property
  def competition_name(self) -> str:
    return self._competition_name

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  @property
  def kernel_owner(self) -> str:
    return self._kernel_owner

  @kernel_owner.setter
  def kernel_owner(self, kernel_owner: str):
    if kernel_owner is None:
      del self.kernel_owner
      return
    if not isinstance(kernel_owner, str):
      raise TypeError('kernel_owner must be of type str')
    self._kernel_owner = kernel_owner

  @property
  def kernel_slug(self) -> str:
    return self._kernel_slug

  @kernel_slug.setter
  def kernel_slug(self, kernel_slug: str):
    if kernel_slug is None:
      del self.kernel_slug
      return
    if not isinstance(kernel_slug, str):
      raise TypeError('kernel_slug must be of type str')
    self._kernel_slug = kernel_slug

  @property
  def kernel_version(self) -> int:
    return self._kernel_version or 0

  @kernel_version.setter
  def kernel_version(self, kernel_version: int):
    if kernel_version is None:
      del self.kernel_version
      return
    if not isinstance(kernel_version, int):
      raise TypeError('kernel_version must be of type int')
    self._kernel_version = kernel_version

  @property
  def file_name(self) -> str:
    return self._file_name or ""

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

  @property
  def submission_description(self) -> str:
    return self._submission_description or ""

  @submission_description.setter
  def submission_description(self, submission_description: str):
    if submission_description is None:
      del self.submission_description
      return
    if not isinstance(submission_description, str):
      raise TypeError('submission_description must be of type str')
    self._submission_description = submission_description

  def endpoint(self):
    path = '/api/v1/competitions/submissions/submit-notebook/{competition_name}'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'


class ApiCreateCodeSubmissionResponse(KaggleObject):
  r"""
  Attributes:
    message (str)
    ref (int)
  """

  def __init__(self):
    self._message = ""
    self._ref = 0
    self._freeze()

  @property
  def message(self) -> str:
    return self._message

  @message.setter
  def message(self, message: str):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message

  @property
  def ref(self) -> int:
    return self._ref

  @ref.setter
  def ref(self, ref: int):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, int):
      raise TypeError('ref must be of type int')
    self._ref = ref


class ApiCreateSubmissionRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
      Competition name. Example: 'titanic'.
    blob_file_tokens (str)
      Token identifying location of uploaded submission file.
    submission_description (str)
      Description of competition submission.
  """

  def __init__(self):
    self._competition_name = ""
    self._blob_file_tokens = ""
    self._submission_description = None
    self._freeze()

  @property
  def competition_name(self) -> str:
    """Competition name. Example: 'titanic'."""
    return self._competition_name

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  @property
  def blob_file_tokens(self) -> str:
    """Token identifying location of uploaded submission file."""
    return self._blob_file_tokens

  @blob_file_tokens.setter
  def blob_file_tokens(self, blob_file_tokens: str):
    if blob_file_tokens is None:
      del self.blob_file_tokens
      return
    if not isinstance(blob_file_tokens, str):
      raise TypeError('blob_file_tokens must be of type str')
    self._blob_file_tokens = blob_file_tokens

  @property
  def submission_description(self) -> str:
    """Description of competition submission."""
    return self._submission_description or ""

  @submission_description.setter
  def submission_description(self, submission_description: str):
    if submission_description is None:
      del self.submission_description
      return
    if not isinstance(submission_description, str):
      raise TypeError('submission_description must be of type str')
    self._submission_description = submission_description

  def endpoint(self):
    path = '/api/v1/competitions/submissions/submit/{competition_name}'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'


class ApiCreateSubmissionResponse(KaggleObject):
  r"""
  Attributes:
    message (str)
    ref (int)
  """

  def __init__(self):
    self._message = ""
    self._ref = 0
    self._freeze()

  @property
  def message(self) -> str:
    return self._message

  @message.setter
  def message(self, message: str):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message

  @property
  def ref(self) -> int:
    return self._ref

  @ref.setter
  def ref(self, ref: int):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, int):
      raise TypeError('ref must be of type int')
    self._ref = ref


class ApiDownloadDataFileRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
      Competition name. Example: 'titanic'.
    file_name (str)
      Name of the file to download. Example: 'train/foo/bar.png'.
  """

  def __init__(self):
    self._competition_name = ""
    self._file_name = ""
    self._freeze()

  @property
  def competition_name(self) -> str:
    """Competition name. Example: 'titanic'."""
    return self._competition_name

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  @property
  def file_name(self) -> str:
    """Name of the file to download. Example: 'train/foo/bar.png'."""
    return self._file_name

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

  def endpoint(self):
    path = '/api/v1/competitions/data/download/{competition_name}/{file_name}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/data/download/{competition_name}/{file_name}'


class ApiDownloadDataFilesRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
      Competition name. Example: 'titanic'.
  """

  def __init__(self):
    self._competition_name = ""
    self._freeze()

  @property
  def competition_name(self) -> str:
    """Competition name. Example: 'titanic'."""
    return self._competition_name

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  def endpoint(self):
    path = '/api/v1/competitions/data/download-all/{competition_name}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/data/download-all/{competition_name}'


class ApiDownloadLeaderboardRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
  """

  def __init__(self):
    self._competition_name = ""
    self._freeze()

  @property
  def competition_name(self) -> str:
    return self._competition_name

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  def endpoint(self):
    path = '/api/v1/competitions/{competition_name}/leaderboard/download'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/{competition_name}/leaderboard/download'


class ApiGetLeaderboardRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
      Competition name. Example: 'titanic'.
    override_public (bool)
      By default we return the private leaderboard if it's available, otherwise
      the public LB. This flag lets you override to get public even if private
      is available.
  """

  def __init__(self):
    self._competition_name = ""
    self._override_public = None
    self._freeze()

  @property
  def competition_name(self) -> str:
    """Competition name. Example: 'titanic'."""
    return self._competition_name

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  @property
  def override_public(self) -> bool:
    r"""
    By default we return the private leaderboard if it's available, otherwise
    the public LB. This flag lets you override to get public even if private
    is available.
    """
    return self._override_public or False

  @override_public.setter
  def override_public(self, override_public: bool):
    if override_public is None:
      del self.override_public
      return
    if not isinstance(override_public, bool):
      raise TypeError('override_public must be of type bool')
    self._override_public = override_public

  def endpoint(self):
    path = '/api/v1/competitions/{competition_name}/leaderboard/view'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/{competition_name}/leaderboard/view'


class ApiGetLeaderboardResponse(KaggleObject):
  r"""
  Attributes:
    submissions (ApiLeaderboardSubmission)
  """

  def __init__(self):
    self._submissions = []
    self._freeze()

  @property
  def submissions(self) -> Optional[List[Optional['ApiLeaderboardSubmission']]]:
    return self._submissions

  @submissions.setter
  def submissions(self, submissions: Optional[List[Optional['ApiLeaderboardSubmission']]]):
    if submissions is None:
      del self.submissions
      return
    if not isinstance(submissions, list):
      raise TypeError('submissions must be of type list')
    if not all([isinstance(t, ApiLeaderboardSubmission) for t in submissions]):
      raise TypeError('submissions must contain only items of type ApiLeaderboardSubmission')
    self._submissions = submissions


class ApiGetSubmissionRequest(KaggleObject):
  r"""
  Attributes:
    ref (int)
      SubmissionId.
  """

  def __init__(self):
    self._ref = 0
    self._freeze()

  @property
  def ref(self) -> int:
    """SubmissionId."""
    return self._ref

  @ref.setter
  def ref(self, ref: int):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, int):
      raise TypeError('ref must be of type int')
    self._ref = ref

  def endpoint(self):
    path = '/api/v1/competitions/submissions/get/{ref}'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'


class ApiLeaderboardSubmission(KaggleObject):
  r"""
  Attributes:
    team_id (int)
    team_name (str)
    submission_date (datetime)
    score (str)
  """

  def __init__(self):
    self._team_id = 0
    self._team_name = None
    self._submission_date = None
    self._score = None
    self._freeze()

  @property
  def team_id(self) -> int:
    return self._team_id

  @team_id.setter
  def team_id(self, team_id: int):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id

  @property
  def team_name(self) -> str:
    return self._team_name or ""

  @team_name.setter
  def team_name(self, team_name: str):
    if team_name is None:
      del self.team_name
      return
    if not isinstance(team_name, str):
      raise TypeError('team_name must be of type str')
    self._team_name = team_name

  @property
  def submission_date(self) -> datetime:
    return self._submission_date

  @submission_date.setter
  def submission_date(self, submission_date: datetime):
    if submission_date is None:
      del self.submission_date
      return
    if not isinstance(submission_date, datetime):
      raise TypeError('submission_date must be of type datetime')
    self._submission_date = submission_date

  @property
  def score(self) -> str:
    return self._score or ""

  @score.setter
  def score(self, score: str):
    if score is None:
      del self.score
      return
    if not isinstance(score, str):
      raise TypeError('score must be of type str')
    self._score = score


class ApiListCompetitionsRequest(KaggleObject):
  r"""
  Attributes:
    group (CompetitionListTab)
      Filter competitions by a particular group (default is 'general').
      One of 'general', 'entered' and 'inClass'.
    category (HostSegment)
      Filter competitions by a particular category (default is 'all').
      One of 'all', 'featured', 'research', 'recruitment', 'gettingStarted',
      'masters', 'playground'.
    sort_by (CompetitionSortBy)
      Sort the results (default is 'latestDeadline').
      One of 'grouped', 'prize', 'earliestDeadline', 'latestDeadline',
      'numberOfTeams', 'recentlyCreated'.
    search (str)
      Filter competitions by search terms.
    page (int)
      Page number (default is 1).
  """

  def __init__(self):
    self._group = None
    self._category = None
    self._sort_by = None
    self._search = None
    self._page = None
    self._freeze()

  @property
  def group(self) -> 'CompetitionListTab':
    r"""
    Filter competitions by a particular group (default is 'general').
    One of 'general', 'entered' and 'inClass'.
    """
    return self._group or CompetitionListTab.COMPETITION_LIST_TAB_GENERAL

  @group.setter
  def group(self, group: 'CompetitionListTab'):
    if group is None:
      del self.group
      return
    if not isinstance(group, CompetitionListTab):
      raise TypeError('group must be of type CompetitionListTab')
    self._group = group

  @property
  def category(self) -> 'HostSegment':
    r"""
    Filter competitions by a particular category (default is 'all').
    One of 'all', 'featured', 'research', 'recruitment', 'gettingStarted',
    'masters', 'playground'.
    """
    return self._category or HostSegment.HOST_SEGMENT_UNSPECIFIED

  @category.setter
  def category(self, category: 'HostSegment'):
    if category is None:
      del self.category
      return
    if not isinstance(category, HostSegment):
      raise TypeError('category must be of type HostSegment')
    self._category = category

  @property
  def sort_by(self) -> 'CompetitionSortBy':
    r"""
    Sort the results (default is 'latestDeadline').
    One of 'grouped', 'prize', 'earliestDeadline', 'latestDeadline',
    'numberOfTeams', 'recentlyCreated'.
    """
    return self._sort_by or CompetitionSortBy.COMPETITION_SORT_BY_GROUPED

  @sort_by.setter
  def sort_by(self, sort_by: 'CompetitionSortBy'):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, CompetitionSortBy):
      raise TypeError('sort_by must be of type CompetitionSortBy')
    self._sort_by = sort_by

  @property
  def search(self) -> str:
    """Filter competitions by search terms."""
    return self._search or ""

  @search.setter
  def search(self, search: str):
    if search is None:
      del self.search
      return
    if not isinstance(search, str):
      raise TypeError('search must be of type str')
    self._search = search

  @property
  def page(self) -> int:
    """Page number (default is 1)."""
    return self._page or 0

  @page.setter
  def page(self, page: int):
    if page is None:
      del self.page
      return
    if not isinstance(page, int):
      raise TypeError('page must be of type int')
    self._page = page

  def endpoint(self):
    path = '/api/v1/competitions/list'
    return path.format_map(self.to_field_map(self))


class ApiListCompetitionsResponse(KaggleObject):
  r"""
  Attributes:
    competitions (ApiCompetition)
  """

  def __init__(self):
    self._competitions = []
    self._freeze()

  @property
  def competitions(self) -> Optional[List[Optional['ApiCompetition']]]:
    return self._competitions

  @competitions.setter
  def competitions(self, competitions: Optional[List[Optional['ApiCompetition']]]):
    if competitions is None:
      del self.competitions
      return
    if not isinstance(competitions, list):
      raise TypeError('competitions must be of type list')
    if not all([isinstance(t, ApiCompetition) for t in competitions]):
      raise TypeError('competitions must contain only items of type ApiCompetition')
    self._competitions = competitions

  @classmethod
  def prepare_from(cls, http_response):
    return cls.from_dict({'competitions': json.loads(http_response.text)})


class ApiListDataFilesRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
      Competition name. Example: 'titanic'.
    page_size (int)
    page_token (str)
  """

  def __init__(self):
    self._competition_name = ""
    self._page_size = None
    self._page_token = None
    self._freeze()

  @property
  def competition_name(self) -> str:
    """Competition name. Example: 'titanic'."""
    return self._competition_name

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  @property
  def page_size(self) -> int:
    return self._page_size or 0

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
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  def endpoint(self):
    path = '/api/v1/competitions/data/list/{competition_name}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/data/list/{competition_name}'


class ApiListDataFilesResponse(KaggleObject):
  r"""
  Attributes:
    files (ApiDataFile)
    next_page_token (str)
  """

  def __init__(self):
    self._files = []
    self._next_page_token = ""
    self._freeze()

  @property
  def files(self) -> Optional[List[Optional['ApiDataFile']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiDataFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiDataFile) for t in files]):
      raise TypeError('files must contain only items of type ApiDataFile')
    self._files = files

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


class ApiListSubmissionsRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
    sort_by (SubmissionSortBy)
    group (SubmissionGroup)
    page (int)
  """

  def __init__(self):
    self._competition_name = ""
    self._sort_by = SubmissionSortBy.SUBMISSION_SORT_BY_DATE
    self._group = SubmissionGroup.SUBMISSION_GROUP_ALL
    self._page = None
    self._freeze()

  @property
  def competition_name(self) -> str:
    return self._competition_name

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  @property
  def sort_by(self) -> 'SubmissionSortBy':
    return self._sort_by

  @sort_by.setter
  def sort_by(self, sort_by: 'SubmissionSortBy'):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, SubmissionSortBy):
      raise TypeError('sort_by must be of type SubmissionSortBy')
    self._sort_by = sort_by

  @property
  def group(self) -> 'SubmissionGroup':
    return self._group

  @group.setter
  def group(self, group: 'SubmissionGroup'):
    if group is None:
      del self.group
      return
    if not isinstance(group, SubmissionGroup):
      raise TypeError('group must be of type SubmissionGroup')
    self._group = group

  @property
  def page(self) -> int:
    return self._page or 0

  @page.setter
  def page(self, page: int):
    if page is None:
      del self.page
      return
    if not isinstance(page, int):
      raise TypeError('page must be of type int')
    self._page = page

  def endpoint(self):
    path = '/api/v1/competitions/submissions/list/{competition_name}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/submissions/list/{competition_name}'


class ApiListSubmissionsResponse(KaggleObject):
  r"""
  Attributes:
    submissions (ApiSubmission)
  """

  def __init__(self):
    self._submissions = []
    self._freeze()

  @property
  def submissions(self) -> Optional[List[Optional['ApiSubmission']]]:
    return self._submissions

  @submissions.setter
  def submissions(self, submissions: Optional[List[Optional['ApiSubmission']]]):
    if submissions is None:
      del self.submissions
      return
    if not isinstance(submissions, list):
      raise TypeError('submissions must be of type list')
    if not all([isinstance(t, ApiSubmission) for t in submissions]):
      raise TypeError('submissions must contain only items of type ApiSubmission')
    self._submissions = submissions

  @classmethod
  def prepare_from(cls, http_response):
    return cls.from_dict({'submissions': json.loads(http_response.text)})


class ApiStartSubmissionUploadRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
    content_length (int)
    last_modified_epoch_seconds (int)
    file_name (str)
      Comes from form upload
  """

  def __init__(self):
    self._competition_name = None
    self._content_length = 0
    self._last_modified_epoch_seconds = 0
    self._file_name = ""
    self._freeze()

  @property
  def competition_name(self) -> str:
    return self._competition_name or ""

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  @property
  def content_length(self) -> int:
    return self._content_length

  @content_length.setter
  def content_length(self, content_length: int):
    if content_length is None:
      del self.content_length
      return
    if not isinstance(content_length, int):
      raise TypeError('content_length must be of type int')
    self._content_length = content_length

  @property
  def last_modified_epoch_seconds(self) -> int:
    return self._last_modified_epoch_seconds

  @last_modified_epoch_seconds.setter
  def last_modified_epoch_seconds(self, last_modified_epoch_seconds: int):
    if last_modified_epoch_seconds is None:
      del self.last_modified_epoch_seconds
      return
    if not isinstance(last_modified_epoch_seconds, int):
      raise TypeError('last_modified_epoch_seconds must be of type int')
    self._last_modified_epoch_seconds = last_modified_epoch_seconds

  @property
  def file_name(self) -> str:
    """Comes from form upload"""
    return self._file_name

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

  def endpoint(self):
    path = '/api/v1/competitions/submission-url'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'


class ApiStartSubmissionUploadResponse(KaggleObject):
  r"""
  Currently identical to StartBlobUploadResponse, but keeping separate since
  they could change independently and this is a legacy V1 type.

  Attributes:
    token (str)
    create_url (str)
  """

  def __init__(self):
    self._token = ""
    self._create_url = ""
    self._freeze()

  @property
  def token(self) -> str:
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token

  @property
  def create_url(self) -> str:
    return self._create_url

  @create_url.setter
  def create_url(self, create_url: str):
    if create_url is None:
      del self.create_url
      return
    if not isinstance(create_url, str):
      raise TypeError('create_url must be of type str')
    self._create_url = create_url

  @property
  def createUrl(self):
    return self.create_url


class ApiSubmission(KaggleObject):
  r"""
  Attributes:
    ref (int)
    total_bytes (int)
    date (datetime)
    description (str)
    error_description (str)
    file_name (str)
    public_score (str)
    private_score (str)
    status (SubmissionStatus)
    submitted_by (str)
    submitted_by_ref (str)
    team_name (str)
    url (str)
      Minor note: ListSubmissions and GetSubmission may differ in setting this
      field.
  """

  def __init__(self):
    self._ref = 0
    self._total_bytes = None
    self._date = None
    self._description = None
    self._error_description = None
    self._file_name = None
    self._public_score = None
    self._private_score = None
    self._status = SubmissionStatus.PENDING
    self._submitted_by = None
    self._submitted_by_ref = None
    self._team_name = None
    self._url = None
    self._freeze()

  @property
  def ref(self) -> int:
    return self._ref

  @ref.setter
  def ref(self, ref: int):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, int):
      raise TypeError('ref must be of type int')
    self._ref = ref

  @property
  def total_bytes(self) -> int:
    return self._total_bytes or 0

  @total_bytes.setter
  def total_bytes(self, total_bytes: int):
    if total_bytes is None:
      del self.total_bytes
      return
    if not isinstance(total_bytes, int):
      raise TypeError('total_bytes must be of type int')
    self._total_bytes = total_bytes

  @property
  def date(self) -> datetime:
    return self._date

  @date.setter
  def date(self, date: datetime):
    if date is None:
      del self.date
      return
    if not isinstance(date, datetime):
      raise TypeError('date must be of type datetime')
    self._date = date

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
  def error_description(self) -> str:
    return self._error_description or ""

  @error_description.setter
  def error_description(self, error_description: str):
    if error_description is None:
      del self.error_description
      return
    if not isinstance(error_description, str):
      raise TypeError('error_description must be of type str')
    self._error_description = error_description

  @property
  def file_name(self) -> str:
    return self._file_name or ""

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

  @property
  def public_score(self) -> str:
    return self._public_score or ""

  @public_score.setter
  def public_score(self, public_score: str):
    if public_score is None:
      del self.public_score
      return
    if not isinstance(public_score, str):
      raise TypeError('public_score must be of type str')
    self._public_score = public_score

  @property
  def private_score(self) -> str:
    return self._private_score or ""

  @private_score.setter
  def private_score(self, private_score: str):
    if private_score is None:
      del self.private_score
      return
    if not isinstance(private_score, str):
      raise TypeError('private_score must be of type str')
    self._private_score = private_score

  @property
  def status(self) -> 'SubmissionStatus':
    return self._status

  @status.setter
  def status(self, status: 'SubmissionStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, SubmissionStatus):
      raise TypeError('status must be of type SubmissionStatus')
    self._status = status

  @property
  def submitted_by(self) -> str:
    return self._submitted_by or ""

  @submitted_by.setter
  def submitted_by(self, submitted_by: str):
    if submitted_by is None:
      del self.submitted_by
      return
    if not isinstance(submitted_by, str):
      raise TypeError('submitted_by must be of type str')
    self._submitted_by = submitted_by

  @property
  def submitted_by_ref(self) -> str:
    return self._submitted_by_ref or ""

  @submitted_by_ref.setter
  def submitted_by_ref(self, submitted_by_ref: str):
    if submitted_by_ref is None:
      del self.submitted_by_ref
      return
    if not isinstance(submitted_by_ref, str):
      raise TypeError('submitted_by_ref must be of type str')
    self._submitted_by_ref = submitted_by_ref

  @property
  def team_name(self) -> str:
    return self._team_name or ""

  @team_name.setter
  def team_name(self, team_name: str):
    if team_name is None:
      del self.team_name
      return
    if not isinstance(team_name, str):
      raise TypeError('team_name must be of type str')
    self._team_name = team_name

  @property
  def url(self) -> str:
    r"""
    Minor note: ListSubmissions and GetSubmission may differ in setting this
    field.
    """
    return self._url or ""

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class ApiCompetition(KaggleObject):
  r"""
  Attributes:
    id (int)
    ref (str)
    title (str)
    url (str)
    description (str)
    organization_name (str)
    organization_ref (str)
    category (str)
    reward (str)
    tags (ApiCategory)
    deadline (datetime)
    kernel_count (int)
    team_count (int)
    user_has_entered (bool)
    user_rank (int)
    merger_deadline (datetime)
    new_entrant_deadline (datetime)
    enabled_date (datetime)
    max_daily_submissions (int)
    max_team_size (int)
    evaluation_metric (str)
    awards_points (bool)
    is_kernels_submissions_only (bool)
    submissions_disabled (bool)
  """

  def __init__(self):
    self._id = 0
    self._ref = ""
    self._title = None
    self._url = None
    self._description = None
    self._organization_name = None
    self._organization_ref = None
    self._category = None
    self._reward = None
    self._tags = []
    self._deadline = None
    self._kernel_count = 0
    self._team_count = 0
    self._user_has_entered = False
    self._user_rank = None
    self._merger_deadline = None
    self._new_entrant_deadline = None
    self._enabled_date = None
    self._max_daily_submissions = 0
    self._max_team_size = None
    self._evaluation_metric = None
    self._awards_points = False
    self._is_kernels_submissions_only = False
    self._submissions_disabled = False
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
  def ref(self) -> str:
    return self._ref

  @ref.setter
  def ref(self, ref: str):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, str):
      raise TypeError('ref must be of type str')
    self._ref = ref

  @property
  def title(self) -> str:
    return self._title or ""

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

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
  def organization_name(self) -> str:
    return self._organization_name or ""

  @organization_name.setter
  def organization_name(self, organization_name: str):
    if organization_name is None:
      del self.organization_name
      return
    if not isinstance(organization_name, str):
      raise TypeError('organization_name must be of type str')
    self._organization_name = organization_name

  @property
  def organization_ref(self) -> str:
    return self._organization_ref or ""

  @organization_ref.setter
  def organization_ref(self, organization_ref: str):
    if organization_ref is None:
      del self.organization_ref
      return
    if not isinstance(organization_ref, str):
      raise TypeError('organization_ref must be of type str')
    self._organization_ref = organization_ref

  @property
  def category(self) -> str:
    return self._category or ""

  @category.setter
  def category(self, category: str):
    if category is None:
      del self.category
      return
    if not isinstance(category, str):
      raise TypeError('category must be of type str')
    self._category = category

  @property
  def reward(self) -> str:
    return self._reward or ""

  @reward.setter
  def reward(self, reward: str):
    if reward is None:
      del self.reward
      return
    if not isinstance(reward, str):
      raise TypeError('reward must be of type str')
    self._reward = reward

  @property
  def tags(self) -> Optional[List[Optional['ApiCategory']]]:
    return self._tags

  @tags.setter
  def tags(self, tags: Optional[List[Optional['ApiCategory']]]):
    if tags is None:
      del self.tags
      return
    if not isinstance(tags, list):
      raise TypeError('tags must be of type list')
    if not all([isinstance(t, ApiCategory) for t in tags]):
      raise TypeError('tags must contain only items of type ApiCategory')
    self._tags = tags

  @property
  def deadline(self) -> datetime:
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
  def kernel_count(self) -> int:
    return self._kernel_count

  @kernel_count.setter
  def kernel_count(self, kernel_count: int):
    if kernel_count is None:
      del self.kernel_count
      return
    if not isinstance(kernel_count, int):
      raise TypeError('kernel_count must be of type int')
    self._kernel_count = kernel_count

  @property
  def team_count(self) -> int:
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
  def user_has_entered(self) -> bool:
    return self._user_has_entered

  @user_has_entered.setter
  def user_has_entered(self, user_has_entered: bool):
    if user_has_entered is None:
      del self.user_has_entered
      return
    if not isinstance(user_has_entered, bool):
      raise TypeError('user_has_entered must be of type bool')
    self._user_has_entered = user_has_entered

  @property
  def user_rank(self) -> int:
    return self._user_rank or 0

  @user_rank.setter
  def user_rank(self, user_rank: int):
    if user_rank is None:
      del self.user_rank
      return
    if not isinstance(user_rank, int):
      raise TypeError('user_rank must be of type int')
    self._user_rank = user_rank

  @property
  def merger_deadline(self) -> datetime:
    return self._merger_deadline

  @merger_deadline.setter
  def merger_deadline(self, merger_deadline: datetime):
    if merger_deadline is None:
      del self.merger_deadline
      return
    if not isinstance(merger_deadline, datetime):
      raise TypeError('merger_deadline must be of type datetime')
    self._merger_deadline = merger_deadline

  @property
  def new_entrant_deadline(self) -> datetime:
    return self._new_entrant_deadline

  @new_entrant_deadline.setter
  def new_entrant_deadline(self, new_entrant_deadline: datetime):
    if new_entrant_deadline is None:
      del self.new_entrant_deadline
      return
    if not isinstance(new_entrant_deadline, datetime):
      raise TypeError('new_entrant_deadline must be of type datetime')
    self._new_entrant_deadline = new_entrant_deadline

  @property
  def enabled_date(self) -> datetime:
    return self._enabled_date

  @enabled_date.setter
  def enabled_date(self, enabled_date: datetime):
    if enabled_date is None:
      del self.enabled_date
      return
    if not isinstance(enabled_date, datetime):
      raise TypeError('enabled_date must be of type datetime')
    self._enabled_date = enabled_date

  @property
  def max_daily_submissions(self) -> int:
    return self._max_daily_submissions

  @max_daily_submissions.setter
  def max_daily_submissions(self, max_daily_submissions: int):
    if max_daily_submissions is None:
      del self.max_daily_submissions
      return
    if not isinstance(max_daily_submissions, int):
      raise TypeError('max_daily_submissions must be of type int')
    self._max_daily_submissions = max_daily_submissions

  @property
  def max_team_size(self) -> int:
    return self._max_team_size or 0

  @max_team_size.setter
  def max_team_size(self, max_team_size: int):
    if max_team_size is None:
      del self.max_team_size
      return
    if not isinstance(max_team_size, int):
      raise TypeError('max_team_size must be of type int')
    self._max_team_size = max_team_size

  @property
  def evaluation_metric(self) -> str:
    return self._evaluation_metric or ""

  @evaluation_metric.setter
  def evaluation_metric(self, evaluation_metric: str):
    if evaluation_metric is None:
      del self.evaluation_metric
      return
    if not isinstance(evaluation_metric, str):
      raise TypeError('evaluation_metric must be of type str')
    self._evaluation_metric = evaluation_metric

  @property
  def awards_points(self) -> bool:
    return self._awards_points

  @awards_points.setter
  def awards_points(self, awards_points: bool):
    if awards_points is None:
      del self.awards_points
      return
    if not isinstance(awards_points, bool):
      raise TypeError('awards_points must be of type bool')
    self._awards_points = awards_points

  @property
  def is_kernels_submissions_only(self) -> bool:
    return self._is_kernels_submissions_only

  @is_kernels_submissions_only.setter
  def is_kernels_submissions_only(self, is_kernels_submissions_only: bool):
    if is_kernels_submissions_only is None:
      del self.is_kernels_submissions_only
      return
    if not isinstance(is_kernels_submissions_only, bool):
      raise TypeError('is_kernels_submissions_only must be of type bool')
    self._is_kernels_submissions_only = is_kernels_submissions_only

  @property
  def submissions_disabled(self) -> bool:
    return self._submissions_disabled

  @submissions_disabled.setter
  def submissions_disabled(self, submissions_disabled: bool):
    if submissions_disabled is None:
      del self.submissions_disabled
      return
    if not isinstance(submissions_disabled, bool):
      raise TypeError('submissions_disabled must be of type bool')
    self._submissions_disabled = submissions_disabled


class ApiDataFile(KaggleObject):
  r"""
  Attributes:
    ref (str)
    name (str)
    description (str)
    total_bytes (int)
    url (str)
    creation_date (datetime)
  """

  def __init__(self):
    self._ref = ""
    self._name = None
    self._description = None
    self._total_bytes = 0
    self._url = None
    self._creation_date = None
    self._freeze()

  @property
  def ref(self) -> str:
    return self._ref

  @ref.setter
  def ref(self, ref: str):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, str):
      raise TypeError('ref must be of type str')
    self._ref = ref

  @property
  def name(self) -> str:
    return self._name or ""

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
  def total_bytes(self) -> int:
    return self._total_bytes

  @total_bytes.setter
  def total_bytes(self, total_bytes: int):
    if total_bytes is None:
      del self.total_bytes
      return
    if not isinstance(total_bytes, int):
      raise TypeError('total_bytes must be of type int')
    self._total_bytes = total_bytes

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def creation_date(self) -> datetime:
    return self._creation_date

  @creation_date.setter
  def creation_date(self, creation_date: datetime):
    if creation_date is None:
      del self.creation_date
      return
    if not isinstance(creation_date, datetime):
      raise TypeError('creation_date must be of type datetime')
    self._creation_date = creation_date


class ApiCategory(KaggleObject):
  r"""
  TODO(erdalsivri): Consider reusing with Kaggle.Sdk.Datasets.ApiCategory.

  Attributes:
    ref (str)
    name (str)
    description (str)
    full_path (str)
    competition_count (int)
    dataset_count (int)
    script_count (int)
    total_count (int)
  """

  def __init__(self):
    self._ref = ""
    self._name = None
    self._description = None
    self._full_path = None
    self._competition_count = 0
    self._dataset_count = 0
    self._script_count = 0
    self._total_count = 0
    self._freeze()

  @property
  def ref(self) -> str:
    return self._ref

  @ref.setter
  def ref(self, ref: str):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, str):
      raise TypeError('ref must be of type str')
    self._ref = ref

  @property
  def name(self) -> str:
    return self._name or ""

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
  def full_path(self) -> str:
    return self._full_path or ""

  @full_path.setter
  def full_path(self, full_path: str):
    if full_path is None:
      del self.full_path
      return
    if not isinstance(full_path, str):
      raise TypeError('full_path must be of type str')
    self._full_path = full_path

  @property
  def competition_count(self) -> int:
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
  def dataset_count(self) -> int:
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
  def script_count(self) -> int:
    return self._script_count

  @script_count.setter
  def script_count(self, script_count: int):
    if script_count is None:
      del self.script_count
      return
    if not isinstance(script_count, int):
      raise TypeError('script_count must be of type int')
    self._script_count = script_count

  @property
  def total_count(self) -> int:
    return self._total_count

  @total_count.setter
  def total_count(self, total_count: int):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count


ApiCreateCodeSubmissionRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("kernelOwner", "kernel_owner", "_kernel_owner", str, "", PredefinedSerializer()),
  FieldMetadata("kernelSlug", "kernel_slug", "_kernel_slug", str, "", PredefinedSerializer()),
  FieldMetadata("kernelVersion", "kernel_version", "_kernel_version", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fileName", "file_name", "_file_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submissionDescription", "submission_description", "_submission_description", str, None, PredefinedSerializer(), optional=True),
]

ApiCreateCodeSubmissionResponse._fields = [
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
  FieldMetadata("ref", "ref", "_ref", int, 0, PredefinedSerializer()),
]

ApiCreateSubmissionRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("blobFileTokens", "blob_file_tokens", "_blob_file_tokens", str, "", PredefinedSerializer()),
  FieldMetadata("submissionDescription", "submission_description", "_submission_description", str, None, PredefinedSerializer(), optional=True),
]

ApiCreateSubmissionResponse._fields = [
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
  FieldMetadata("ref", "ref", "_ref", int, 0, PredefinedSerializer()),
]

ApiDownloadDataFileRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
]

ApiDownloadDataFilesRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
]

ApiDownloadLeaderboardRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
]

ApiGetLeaderboardRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("overridePublic", "override_public", "_override_public", bool, None, PredefinedSerializer(), optional=True),
]

ApiGetLeaderboardResponse._fields = [
  FieldMetadata("submissions", "submissions", "_submissions", ApiLeaderboardSubmission, [], ListSerializer(KaggleObjectSerializer())),
]

ApiGetSubmissionRequest._fields = [
  FieldMetadata("ref", "ref", "_ref", int, 0, PredefinedSerializer()),
]

ApiLeaderboardSubmission._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamName", "team_name", "_team_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submissionDate", "submission_date", "_submission_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("score", "score", "_score", str, None, PredefinedSerializer(), optional=True),
]

ApiListCompetitionsRequest._fields = [
  FieldMetadata("group", "group", "_group", CompetitionListTab, None, EnumSerializer(), optional=True),
  FieldMetadata("category", "category", "_category", HostSegment, None, EnumSerializer(), optional=True),
  FieldMetadata("sortBy", "sort_by", "_sort_by", CompetitionSortBy, None, EnumSerializer(), optional=True),
  FieldMetadata("search", "search", "_search", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("page", "page", "_page", int, None, PredefinedSerializer(), optional=True),
]

ApiListCompetitionsResponse._fields = [
  FieldMetadata("competitions", "competitions", "_competitions", ApiCompetition, [], ListSerializer(KaggleObjectSerializer())),
]

ApiListDataFilesRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListDataFilesResponse._fields = [
  FieldMetadata("files", "files", "_files", ApiDataFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ApiListSubmissionsRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("sortBy", "sort_by", "_sort_by", SubmissionSortBy, SubmissionSortBy.SUBMISSION_SORT_BY_DATE, EnumSerializer()),
  FieldMetadata("group", "group", "_group", SubmissionGroup, SubmissionGroup.SUBMISSION_GROUP_ALL, EnumSerializer()),
  FieldMetadata("page", "page", "_page", int, None, PredefinedSerializer(), optional=True),
]

ApiListSubmissionsResponse._fields = [
  FieldMetadata("submissions", "submissions", "_submissions", ApiSubmission, [], ListSerializer(KaggleObjectSerializer())),
]

ApiStartSubmissionUploadRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("lastModifiedEpochSeconds", "last_modified_epoch_seconds", "_last_modified_epoch_seconds", int, 0, PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
]

ApiStartSubmissionUploadResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
  FieldMetadata("createUrl", "create_url", "_create_url", str, "", PredefinedSerializer()),
]

ApiSubmission._fields = [
  FieldMetadata("ref", "ref", "_ref", int, 0, PredefinedSerializer()),
  FieldMetadata("totalBytes", "total_bytes", "_total_bytes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("date", "date", "_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("errorDescription", "error_description", "_error_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fileName", "file_name", "_file_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("publicScore", "public_score", "_public_score", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateScore", "private_score", "_private_score", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("status", "status", "_status", SubmissionStatus, SubmissionStatus.PENDING, EnumSerializer()),
  FieldMetadata("submittedBy", "submitted_by", "_submitted_by", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submittedByRef", "submitted_by_ref", "_submitted_by_ref", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teamName", "team_name", "_team_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
]

ApiCompetition._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("ref", "ref", "_ref", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organizationName", "organization_name", "_organization_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organizationRef", "organization_ref", "_organization_ref", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("category", "category", "_category", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reward", "reward", "_reward", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tags", "tags", "_tags", ApiCategory, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("kernelCount", "kernel_count", "_kernel_count", int, 0, PredefinedSerializer()),
  FieldMetadata("teamCount", "team_count", "_team_count", int, 0, PredefinedSerializer()),
  FieldMetadata("userHasEntered", "user_has_entered", "_user_has_entered", bool, False, PredefinedSerializer()),
  FieldMetadata("userRank", "user_rank", "_user_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("mergerDeadline", "merger_deadline", "_merger_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("newEntrantDeadline", "new_entrant_deadline", "_new_entrant_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("enabledDate", "enabled_date", "_enabled_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("maxDailySubmissions", "max_daily_submissions", "_max_daily_submissions", int, 0, PredefinedSerializer()),
  FieldMetadata("maxTeamSize", "max_team_size", "_max_team_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("evaluationMetric", "evaluation_metric", "_evaluation_metric", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("awardsPoints", "awards_points", "_awards_points", bool, False, PredefinedSerializer()),
  FieldMetadata("isKernelsSubmissionsOnly", "is_kernels_submissions_only", "_is_kernels_submissions_only", bool, False, PredefinedSerializer()),
  FieldMetadata("submissionsDisabled", "submissions_disabled", "_submissions_disabled", bool, False, PredefinedSerializer()),
]

ApiDataFile._fields = [
  FieldMetadata("ref", "ref", "_ref", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalBytes", "total_bytes", "_total_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creationDate", "creation_date", "_creation_date", datetime, None, DateTimeSerializer()),
]

ApiCategory._fields = [
  FieldMetadata("ref", "ref", "_ref", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fullPath", "full_path", "_full_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionCount", "competition_count", "_competition_count", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetCount", "dataset_count", "_dataset_count", int, 0, PredefinedSerializer()),
  FieldMetadata("scriptCount", "script_count", "_script_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
]

