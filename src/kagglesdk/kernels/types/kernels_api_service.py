from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.kernels_enums import KernelsListSortType, KernelsListViewType, KernelWorkerStatus
from typing import Optional, List

class ApiDownloadKernelOutputRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    kernel_slug (str)
    file_path (str)
      Relative path to a specific file inside the databundle.
    version_number (int)
  """

  def __init__(self):
    self._owner_slug = ""
    self._kernel_slug = ""
    self._file_path = None
    self._version_number = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

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
  def file_path(self) -> str:
    """Relative path to a specific file inside the databundle."""
    return self._file_path or ""

  @file_path.setter
  def file_path(self, file_path: str):
    if file_path is None:
      del self.file_path
      return
    if not isinstance(file_path, str):
      raise TypeError('file_path must be of type str')
    self._file_path = file_path

  @property
  def version_number(self) -> int:
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  def endpoint(self):
    if self.file_path:
      path = '/api/v1/kernels/output/download/{owner_slug}/{kernel_slug}/{file_path}'
    else:
      path = '/api/v1/kernels/output/download/{owner_slug}/{kernel_slug}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/kernels/output/download/{owner_slug}/{kernel_slug}'


class ApiDownloadKernelOutputZipRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._freeze()

  @property
  def kernel_session_id(self) -> int:
    return self._kernel_session_id

  @kernel_session_id.setter
  def kernel_session_id(self, kernel_session_id: int):
    if kernel_session_id is None:
      del self.kernel_session_id
      return
    if not isinstance(kernel_session_id, int):
      raise TypeError('kernel_session_id must be of type int')
    self._kernel_session_id = kernel_session_id

  def endpoint(self):
    path = '/api/v1/kernels/output/download_zip/{kernel_session_id}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/kernels/output/download_zip/{kernel_session_id}'


class ApiGetKernelRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
    kernel_slug (str)
  """

  def __init__(self):
    self._user_name = ""
    self._kernel_slug = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

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

  def endpoint(self):
    path = '/api/v1/kernels/pull'
    return path.format_map(self.to_field_map(self))


class ApiGetKernelResponse(KaggleObject):
  r"""
  Attributes:
    metadata (ApiKernelMetadata)
    blob (ApiKernelBlob)
  """

  def __init__(self):
    self._metadata = None
    self._blob = None
    self._freeze()

  @property
  def metadata(self) -> Optional['ApiKernelMetadata']:
    return self._metadata

  @metadata.setter
  def metadata(self, metadata: Optional['ApiKernelMetadata']):
    if metadata is None:
      del self.metadata
      return
    if not isinstance(metadata, ApiKernelMetadata):
      raise TypeError('metadata must be of type ApiKernelMetadata')
    self._metadata = metadata

  @property
  def blob(self) -> Optional['ApiKernelBlob']:
    return self._blob

  @blob.setter
  def blob(self, blob: Optional['ApiKernelBlob']):
    if blob is None:
      del self.blob
      return
    if not isinstance(blob, ApiKernelBlob):
      raise TypeError('blob must be of type ApiKernelBlob')
    self._blob = blob


class ApiGetKernelSessionStatusRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
    kernel_slug (str)
  """

  def __init__(self):
    self._user_name = ""
    self._kernel_slug = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

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

  def endpoint(self):
    path = '/api/v1/kernels/status'
    return path.format_map(self.to_field_map(self))


class ApiGetKernelSessionStatusResponse(KaggleObject):
  r"""
  Attributes:
    status (KernelWorkerStatus)
    failure_message (str)
  """

  def __init__(self):
    self._status = KernelWorkerStatus.QUEUED
    self._failure_message = None
    self._freeze()

  @property
  def status(self) -> 'KernelWorkerStatus':
    return self._status

  @status.setter
  def status(self, status: 'KernelWorkerStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, KernelWorkerStatus):
      raise TypeError('status must be of type KernelWorkerStatus')
    self._status = status

  @property
  def failure_message(self) -> str:
    return self._failure_message or ""

  @failure_message.setter
  def failure_message(self, failure_message: str):
    if failure_message is None:
      del self.failure_message
      return
    if not isinstance(failure_message, str):
      raise TypeError('failure_message must be of type str')
    self._failure_message = failure_message

  @property
  def failureMessage(self):
    return self.failure_message


class ApiKernelBlob(KaggleObject):
  r"""
  Attributes:
    source (str)
    language (str)
    kernel_type (str)
    slug (str)
  """

  def __init__(self):
    self._source = None
    self._language = None
    self._kernel_type = None
    self._slug = None
    self._freeze()

  @property
  def source(self) -> str:
    return self._source or ""

  @source.setter
  def source(self, source: str):
    if source is None:
      del self.source
      return
    if not isinstance(source, str):
      raise TypeError('source must be of type str')
    self._source = source

  @property
  def language(self) -> str:
    return self._language or ""

  @language.setter
  def language(self, language: str):
    if language is None:
      del self.language
      return
    if not isinstance(language, str):
      raise TypeError('language must be of type str')
    self._language = language

  @property
  def kernel_type(self) -> str:
    return self._kernel_type or ""

  @kernel_type.setter
  def kernel_type(self, kernel_type: str):
    if kernel_type is None:
      del self.kernel_type
      return
    if not isinstance(kernel_type, str):
      raise TypeError('kernel_type must be of type str')
    self._kernel_type = kernel_type

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
    self._slug = slug


class ApiKernelMetadata(KaggleObject):
  r"""
  Attributes:
    id (int)
    ref (str)
    title (str)
    author (str)
    slug (str)
    last_run_time (datetime)
    language (str)
    kernel_type (str)
    is_private (bool)
    enable_gpu (bool)
    enable_tpu (bool)
    enable_internet (bool)
    category_ids (str)
    dataset_data_sources (str)
    kernel_data_sources (str)
    competition_data_sources (str)
    model_data_sources (str)
    total_votes (int)
    current_version_number (int)
  """

  def __init__(self):
    self._id = 0
    self._ref = ""
    self._title = ""
    self._author = ""
    self._slug = ""
    self._last_run_time = None
    self._language = None
    self._kernel_type = None
    self._is_private = None
    self._enable_gpu = None
    self._enable_tpu = None
    self._enable_internet = None
    self._category_ids = []
    self._dataset_data_sources = []
    self._kernel_data_sources = []
    self._competition_data_sources = []
    self._model_data_sources = []
    self._total_votes = 0
    self._current_version_number = None
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
  def author(self) -> str:
    return self._author

  @author.setter
  def author(self, author: str):
    if author is None:
      del self.author
      return
    if not isinstance(author, str):
      raise TypeError('author must be of type str')
    self._author = author

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

  @property
  def last_run_time(self) -> datetime:
    return self._last_run_time

  @last_run_time.setter
  def last_run_time(self, last_run_time: datetime):
    if last_run_time is None:
      del self.last_run_time
      return
    if not isinstance(last_run_time, datetime):
      raise TypeError('last_run_time must be of type datetime')
    self._last_run_time = last_run_time

  @property
  def language(self) -> str:
    return self._language or ""

  @language.setter
  def language(self, language: str):
    if language is None:
      del self.language
      return
    if not isinstance(language, str):
      raise TypeError('language must be of type str')
    self._language = language

  @property
  def kernel_type(self) -> str:
    return self._kernel_type or ""

  @kernel_type.setter
  def kernel_type(self, kernel_type: str):
    if kernel_type is None:
      del self.kernel_type
      return
    if not isinstance(kernel_type, str):
      raise TypeError('kernel_type must be of type str')
    self._kernel_type = kernel_type

  @property
  def is_private(self) -> bool:
    return self._is_private or False

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def enable_gpu(self) -> bool:
    return self._enable_gpu or False

  @enable_gpu.setter
  def enable_gpu(self, enable_gpu: bool):
    if enable_gpu is None:
      del self.enable_gpu
      return
    if not isinstance(enable_gpu, bool):
      raise TypeError('enable_gpu must be of type bool')
    self._enable_gpu = enable_gpu

  @property
  def enable_tpu(self) -> bool:
    return self._enable_tpu or False

  @enable_tpu.setter
  def enable_tpu(self, enable_tpu: bool):
    if enable_tpu is None:
      del self.enable_tpu
      return
    if not isinstance(enable_tpu, bool):
      raise TypeError('enable_tpu must be of type bool')
    self._enable_tpu = enable_tpu

  @property
  def enable_internet(self) -> bool:
    return self._enable_internet or False

  @enable_internet.setter
  def enable_internet(self, enable_internet: bool):
    if enable_internet is None:
      del self.enable_internet
      return
    if not isinstance(enable_internet, bool):
      raise TypeError('enable_internet must be of type bool')
    self._enable_internet = enable_internet

  @property
  def category_ids(self) -> Optional[List[str]]:
    return self._category_ids

  @category_ids.setter
  def category_ids(self, category_ids: Optional[List[str]]):
    if category_ids is None:
      del self.category_ids
      return
    if not isinstance(category_ids, list):
      raise TypeError('category_ids must be of type list')
    if not all([isinstance(t, str) for t in category_ids]):
      raise TypeError('category_ids must contain only items of type str')
    self._category_ids = category_ids

  @property
  def dataset_data_sources(self) -> Optional[List[str]]:
    return self._dataset_data_sources

  @dataset_data_sources.setter
  def dataset_data_sources(self, dataset_data_sources: Optional[List[str]]):
    if dataset_data_sources is None:
      del self.dataset_data_sources
      return
    if not isinstance(dataset_data_sources, list):
      raise TypeError('dataset_data_sources must be of type list')
    if not all([isinstance(t, str) for t in dataset_data_sources]):
      raise TypeError('dataset_data_sources must contain only items of type str')
    self._dataset_data_sources = dataset_data_sources

  @property
  def kernel_data_sources(self) -> Optional[List[str]]:
    return self._kernel_data_sources

  @kernel_data_sources.setter
  def kernel_data_sources(self, kernel_data_sources: Optional[List[str]]):
    if kernel_data_sources is None:
      del self.kernel_data_sources
      return
    if not isinstance(kernel_data_sources, list):
      raise TypeError('kernel_data_sources must be of type list')
    if not all([isinstance(t, str) for t in kernel_data_sources]):
      raise TypeError('kernel_data_sources must contain only items of type str')
    self._kernel_data_sources = kernel_data_sources

  @property
  def competition_data_sources(self) -> Optional[List[str]]:
    return self._competition_data_sources

  @competition_data_sources.setter
  def competition_data_sources(self, competition_data_sources: Optional[List[str]]):
    if competition_data_sources is None:
      del self.competition_data_sources
      return
    if not isinstance(competition_data_sources, list):
      raise TypeError('competition_data_sources must be of type list')
    if not all([isinstance(t, str) for t in competition_data_sources]):
      raise TypeError('competition_data_sources must contain only items of type str')
    self._competition_data_sources = competition_data_sources

  @property
  def model_data_sources(self) -> Optional[List[str]]:
    return self._model_data_sources

  @model_data_sources.setter
  def model_data_sources(self, model_data_sources: Optional[List[str]]):
    if model_data_sources is None:
      del self.model_data_sources
      return
    if not isinstance(model_data_sources, list):
      raise TypeError('model_data_sources must be of type list')
    if not all([isinstance(t, str) for t in model_data_sources]):
      raise TypeError('model_data_sources must contain only items of type str')
    self._model_data_sources = model_data_sources

  @property
  def total_votes(self) -> int:
    return self._total_votes

  @total_votes.setter
  def total_votes(self, total_votes: int):
    if total_votes is None:
      del self.total_votes
      return
    if not isinstance(total_votes, int):
      raise TypeError('total_votes must be of type int')
    self._total_votes = total_votes

  @property
  def current_version_number(self) -> int:
    return self._current_version_number or 0

  @current_version_number.setter
  def current_version_number(self, current_version_number: int):
    if current_version_number is None:
      del self.current_version_number
      return
    if not isinstance(current_version_number, int):
      raise TypeError('current_version_number must be of type int')
    self._current_version_number = current_version_number


class ApiListKernelFilesRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
    kernel_slug (str)
    page_size (int)
    page_token (str)
  """

  def __init__(self):
    self._user_name = ""
    self._kernel_slug = ""
    self._page_size = None
    self._page_token = None
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

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
    path = '/api/v1/kernels/files'
    return path.format_map(self.to_field_map(self))


class ApiListKernelFilesResponse(KaggleObject):
  r"""
  Attributes:
    files (ApiListKernelFilesItem)
    next_page_token (str)
  """

  def __init__(self):
    self._files = []
    self._next_page_token = None
    self._freeze()

  @property
  def files(self) -> Optional[List[Optional['ApiListKernelFilesItem']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiListKernelFilesItem']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiListKernelFilesItem) for t in files]):
      raise TypeError('files must contain only items of type ApiListKernelFilesItem')
    self._files = files

  @property
  def next_page_token(self) -> str:
    return self._next_page_token or ""

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


class ApiListKernelSessionOutputRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
    kernel_slug (str)
    page_size (int)
    page_token (str)
  """

  def __init__(self):
    self._user_name = ""
    self._kernel_slug = ""
    self._page_size = None
    self._page_token = None
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

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
    path = '/api/v1/kernels/output'
    return path.format_map(self.to_field_map(self))


class ApiListKernelSessionOutputResponse(KaggleObject):
  r"""
  Attributes:
    files (ApiKernelSessionOutputFile)
    log (str)
    next_page_token (str)
  """

  def __init__(self):
    self._files = []
    self._log = None
    self._next_page_token = None
    self._freeze()

  @property
  def files(self) -> Optional[List[Optional['ApiKernelSessionOutputFile']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiKernelSessionOutputFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiKernelSessionOutputFile) for t in files]):
      raise TypeError('files must contain only items of type ApiKernelSessionOutputFile')
    self._files = files

  @property
  def log(self) -> str:
    return self._log or ""

  @log.setter
  def log(self, log: str):
    if log is None:
      del self.log
      return
    if not isinstance(log, str):
      raise TypeError('log must be of type str')
    self._log = log

  @property
  def next_page_token(self) -> str:
    return self._next_page_token or ""

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


class ApiListKernelsRequest(KaggleObject):
  r"""
  Attributes:
    competition (str)
      Display kernels using the specified competition.
    dataset (str)
      Display kernels using the specified dataset.
    parent_kernel (str)
      Display kernels that have forked the specified kernel.
    group (KernelsListViewType)
      Display your kernels, collaborated, bookmarked or upvoted kernels.
    kernel_type (str)
      Display kernels of a specific type.
    language (str)
      Display kernels in a specific language. One of 'all', 'python', 'r',
      'sqlite' and 'julia'.
    output_type (str)
      Display kernels with a specific output type. One of 'all', 'visualization'
      and 'notebook'.
    search (str)
      Display kernels matching the specified search terms.
    sort_by (KernelsListSortType)
      Sort the results (default is 'hotness'). 'relevance' only works if there is
      a search query.
    user (str)
      Display kernels by a particular user or group.
    page (int)
      Page number (default is 1).
    page_size (int)
      Page size, i.e., maximum number of results to return.
  """

  def __init__(self):
    self._competition = None
    self._dataset = None
    self._parent_kernel = None
    self._group = KernelsListViewType.KERNELS_LIST_VIEW_TYPE_UNSPECIFIED
    self._kernel_type = None
    self._language = None
    self._output_type = None
    self._search = None
    self._sort_by = KernelsListSortType.HOTNESS
    self._user = None
    self._page = None
    self._page_size = None
    self._freeze()

  @property
  def competition(self) -> str:
    """Display kernels using the specified competition."""
    return self._competition or ""

  @competition.setter
  def competition(self, competition: str):
    if competition is None:
      del self.competition
      return
    if not isinstance(competition, str):
      raise TypeError('competition must be of type str')
    self._competition = competition

  @property
  def dataset(self) -> str:
    """Display kernels using the specified dataset."""
    return self._dataset or ""

  @dataset.setter
  def dataset(self, dataset: str):
    if dataset is None:
      del self.dataset
      return
    if not isinstance(dataset, str):
      raise TypeError('dataset must be of type str')
    self._dataset = dataset

  @property
  def parent_kernel(self) -> str:
    """Display kernels that have forked the specified kernel."""
    return self._parent_kernel or ""

  @parent_kernel.setter
  def parent_kernel(self, parent_kernel: str):
    if parent_kernel is None:
      del self.parent_kernel
      return
    if not isinstance(parent_kernel, str):
      raise TypeError('parent_kernel must be of type str')
    self._parent_kernel = parent_kernel

  @property
  def group(self) -> 'KernelsListViewType':
    """Display your kernels, collaborated, bookmarked or upvoted kernels."""
    return self._group

  @group.setter
  def group(self, group: 'KernelsListViewType'):
    if group is None:
      del self.group
      return
    if not isinstance(group, KernelsListViewType):
      raise TypeError('group must be of type KernelsListViewType')
    self._group = group

  @property
  def kernel_type(self) -> str:
    """Display kernels of a specific type."""
    return self._kernel_type or ""

  @kernel_type.setter
  def kernel_type(self, kernel_type: str):
    if kernel_type is None:
      del self.kernel_type
      return
    if not isinstance(kernel_type, str):
      raise TypeError('kernel_type must be of type str')
    self._kernel_type = kernel_type

  @property
  def language(self) -> str:
    r"""
    Display kernels in a specific language. One of 'all', 'python', 'r',
    'sqlite' and 'julia'.
    """
    return self._language or ""

  @language.setter
  def language(self, language: str):
    if language is None:
      del self.language
      return
    if not isinstance(language, str):
      raise TypeError('language must be of type str')
    self._language = language

  @property
  def output_type(self) -> str:
    r"""
    Display kernels with a specific output type. One of 'all', 'visualization'
    and 'notebook'.
    """
    return self._output_type or ""

  @output_type.setter
  def output_type(self, output_type: str):
    if output_type is None:
      del self.output_type
      return
    if not isinstance(output_type, str):
      raise TypeError('output_type must be of type str')
    self._output_type = output_type

  @property
  def search(self) -> str:
    """Display kernels matching the specified search terms."""
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
  def sort_by(self) -> 'KernelsListSortType':
    r"""
    Sort the results (default is 'hotness'). 'relevance' only works if there is
    a search query.
    """
    return self._sort_by

  @sort_by.setter
  def sort_by(self, sort_by: 'KernelsListSortType'):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, KernelsListSortType):
      raise TypeError('sort_by must be of type KernelsListSortType')
    self._sort_by = sort_by

  @property
  def user(self) -> str:
    """Display kernels by a particular user or group."""
    return self._user or ""

  @user.setter
  def user(self, user: str):
    if user is None:
      del self.user
      return
    if not isinstance(user, str):
      raise TypeError('user must be of type str')
    self._user = user

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

  @property
  def page_size(self) -> int:
    """Page size, i.e., maximum number of results to return."""
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  def endpoint(self):
    path = '/api/v1/kernels/list'
    return path.format_map(self.to_field_map(self))


class ApiListKernelsResponse(KaggleObject):
  r"""
  Attributes:
    kernels (ApiKernelMetadata)
  """

  def __init__(self):
    self._kernels = []
    self._freeze()

  @property
  def kernels(self) -> Optional[List[Optional['ApiKernelMetadata']]]:
    return self._kernels

  @kernels.setter
  def kernels(self, kernels: Optional[List[Optional['ApiKernelMetadata']]]):
    if kernels is None:
      del self.kernels
      return
    if not isinstance(kernels, list):
      raise TypeError('kernels must be of type list')
    if not all([isinstance(t, ApiKernelMetadata) for t in kernels]):
      raise TypeError('kernels must contain only items of type ApiKernelMetadata')
    self._kernels = kernels

  @classmethod
  def prepare_from(cls, http_response):
    return cls.from_dict({'kernels': json.loads(http_response.text)})


class ApiSaveKernelRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
      The kernel's unique ID number. One of `id` and `slug` are required. If both
      are specified, `id` will be preferred.
    slug (str)
      The full slug of the kernel to push to, in the format
      `{username}/{kernel-slug}`. The kernel slug must be the title lowercased
      with dashes (`-`) replacing spaces. One of `id` and `slug` are required. If
      both are specified, `id` will be preferred.
    new_title (str)
      The title to be set on the kernel.
    text (str)
      The kernel's source code.
    language (str)
      The language that the kernel is written in. One of 'python', 'r' and
      'rmarkdown'.
    kernel_type (str)
      The type of kernel. Cannot be changed once the kernel has been created.
    dataset_data_sources (str)
      A list of dataset data sources that the kernel should use. Each dataset is
      specified as
      `{username}/{dataset-slug}`.
    kernel_data_sources (str)
      A list of kernel data sources that the kernel should use. Each dataset is
      specified as
      `{username}/{kernel-slug}`.
    competition_data_sources (str)
      A list of competition data sources that the kernel should use
    category_ids (str)
      A list of tag IDs to associated with the kernel.
    is_private (bool)
      Whether or not the kernel should be private.
    enable_gpu (bool)
      Whether or not the kernel should run on a GPU.
    enable_tpu (bool)
      Whether or not the kernel should run on a TPU.
    enable_internet (bool)
      Whether or not the kernel should be able to access the internet.
    docker_image_pinning_type (str)
      Which docker image to use for executing new versions going forward.
    model_data_sources (str)
      A list of model data sources that the kernel should use.
      Each model is specified as (for the latest version):
      `{username}/{model-slug}/{framework}/{variation-slug}`
      Or versioned:
      `{username}/{model-slug}/{framework}/{variation-slug}/{version-number}`
    session_timeout_seconds (int)
      If specified, terminate the kernel session after this many seconds of
      runtime, which must be lower than the global maximum.
  """

  def __init__(self):
    self._id = None
    self._slug = None
    self._new_title = None
    self._text = None
    self._language = None
    self._kernel_type = None
    self._dataset_data_sources = []
    self._kernel_data_sources = []
    self._competition_data_sources = []
    self._category_ids = []
    self._is_private = None
    self._enable_gpu = None
    self._enable_tpu = None
    self._enable_internet = None
    self._docker_image_pinning_type = None
    self._model_data_sources = []
    self._session_timeout_seconds = None
    self._freeze()

  @property
  def id(self) -> int:
    r"""
    The kernel's unique ID number. One of `id` and `slug` are required. If both
    are specified, `id` will be preferred.
    """
    return self._id or 0

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
    r"""
    The full slug of the kernel to push to, in the format
    `{username}/{kernel-slug}`. The kernel slug must be the title lowercased
    with dashes (`-`) replacing spaces. One of `id` and `slug` are required. If
    both are specified, `id` will be preferred.
    """
    return self._slug or ""

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def new_title(self) -> str:
    """The title to be set on the kernel."""
    return self._new_title or ""

  @new_title.setter
  def new_title(self, new_title: str):
    if new_title is None:
      del self.new_title
      return
    if not isinstance(new_title, str):
      raise TypeError('new_title must be of type str')
    self._new_title = new_title

  @property
  def text(self) -> str:
    """The kernel's source code."""
    return self._text or ""

  @text.setter
  def text(self, text: str):
    if text is None:
      del self.text
      return
    if not isinstance(text, str):
      raise TypeError('text must be of type str')
    self._text = text

  @property
  def language(self) -> str:
    r"""
    The language that the kernel is written in. One of 'python', 'r' and
    'rmarkdown'.
    """
    return self._language or ""

  @language.setter
  def language(self, language: str):
    if language is None:
      del self.language
      return
    if not isinstance(language, str):
      raise TypeError('language must be of type str')
    self._language = language

  @property
  def kernel_type(self) -> str:
    """The type of kernel. Cannot be changed once the kernel has been created."""
    return self._kernel_type or ""

  @kernel_type.setter
  def kernel_type(self, kernel_type: str):
    if kernel_type is None:
      del self.kernel_type
      return
    if not isinstance(kernel_type, str):
      raise TypeError('kernel_type must be of type str')
    self._kernel_type = kernel_type

  @property
  def dataset_data_sources(self) -> Optional[List[str]]:
    r"""
    A list of dataset data sources that the kernel should use. Each dataset is
    specified as
    `{username}/{dataset-slug}`.
    """
    return self._dataset_data_sources

  @dataset_data_sources.setter
  def dataset_data_sources(self, dataset_data_sources: Optional[List[str]]):
    if dataset_data_sources is None:
      del self.dataset_data_sources
      return
    if not isinstance(dataset_data_sources, list):
      raise TypeError('dataset_data_sources must be of type list')
    if not all([isinstance(t, str) for t in dataset_data_sources]):
      raise TypeError('dataset_data_sources must contain only items of type str')
    self._dataset_data_sources = dataset_data_sources

  @property
  def kernel_data_sources(self) -> Optional[List[str]]:
    r"""
    A list of kernel data sources that the kernel should use. Each dataset is
    specified as
    `{username}/{kernel-slug}`.
    """
    return self._kernel_data_sources

  @kernel_data_sources.setter
  def kernel_data_sources(self, kernel_data_sources: Optional[List[str]]):
    if kernel_data_sources is None:
      del self.kernel_data_sources
      return
    if not isinstance(kernel_data_sources, list):
      raise TypeError('kernel_data_sources must be of type list')
    if not all([isinstance(t, str) for t in kernel_data_sources]):
      raise TypeError('kernel_data_sources must contain only items of type str')
    self._kernel_data_sources = kernel_data_sources

  @property
  def competition_data_sources(self) -> Optional[List[str]]:
    """A list of competition data sources that the kernel should use"""
    return self._competition_data_sources

  @competition_data_sources.setter
  def competition_data_sources(self, competition_data_sources: Optional[List[str]]):
    if competition_data_sources is None:
      del self.competition_data_sources
      return
    if not isinstance(competition_data_sources, list):
      raise TypeError('competition_data_sources must be of type list')
    if not all([isinstance(t, str) for t in competition_data_sources]):
      raise TypeError('competition_data_sources must contain only items of type str')
    self._competition_data_sources = competition_data_sources

  @property
  def category_ids(self) -> Optional[List[str]]:
    """A list of tag IDs to associated with the kernel."""
    return self._category_ids

  @category_ids.setter
  def category_ids(self, category_ids: Optional[List[str]]):
    if category_ids is None:
      del self.category_ids
      return
    if not isinstance(category_ids, list):
      raise TypeError('category_ids must be of type list')
    if not all([isinstance(t, str) for t in category_ids]):
      raise TypeError('category_ids must contain only items of type str')
    self._category_ids = category_ids

  @property
  def is_private(self) -> bool:
    """Whether or not the kernel should be private."""
    return self._is_private or False

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def enable_gpu(self) -> bool:
    """Whether or not the kernel should run on a GPU."""
    return self._enable_gpu or False

  @enable_gpu.setter
  def enable_gpu(self, enable_gpu: bool):
    if enable_gpu is None:
      del self.enable_gpu
      return
    if not isinstance(enable_gpu, bool):
      raise TypeError('enable_gpu must be of type bool')
    self._enable_gpu = enable_gpu

  @property
  def enable_tpu(self) -> bool:
    """Whether or not the kernel should run on a TPU."""
    return self._enable_tpu or False

  @enable_tpu.setter
  def enable_tpu(self, enable_tpu: bool):
    if enable_tpu is None:
      del self.enable_tpu
      return
    if not isinstance(enable_tpu, bool):
      raise TypeError('enable_tpu must be of type bool')
    self._enable_tpu = enable_tpu

  @property
  def enable_internet(self) -> bool:
    """Whether or not the kernel should be able to access the internet."""
    return self._enable_internet or False

  @enable_internet.setter
  def enable_internet(self, enable_internet: bool):
    if enable_internet is None:
      del self.enable_internet
      return
    if not isinstance(enable_internet, bool):
      raise TypeError('enable_internet must be of type bool')
    self._enable_internet = enable_internet

  @property
  def docker_image_pinning_type(self) -> str:
    """Which docker image to use for executing new versions going forward."""
    return self._docker_image_pinning_type or ""

  @docker_image_pinning_type.setter
  def docker_image_pinning_type(self, docker_image_pinning_type: str):
    if docker_image_pinning_type is None:
      del self.docker_image_pinning_type
      return
    if not isinstance(docker_image_pinning_type, str):
      raise TypeError('docker_image_pinning_type must be of type str')
    self._docker_image_pinning_type = docker_image_pinning_type

  @property
  def model_data_sources(self) -> Optional[List[str]]:
    r"""
    A list of model data sources that the kernel should use.
    Each model is specified as (for the latest version):
    `{username}/{model-slug}/{framework}/{variation-slug}`
    Or versioned:
    `{username}/{model-slug}/{framework}/{variation-slug}/{version-number}`
    """
    return self._model_data_sources

  @model_data_sources.setter
  def model_data_sources(self, model_data_sources: Optional[List[str]]):
    if model_data_sources is None:
      del self.model_data_sources
      return
    if not isinstance(model_data_sources, list):
      raise TypeError('model_data_sources must be of type list')
    if not all([isinstance(t, str) for t in model_data_sources]):
      raise TypeError('model_data_sources must contain only items of type str')
    self._model_data_sources = model_data_sources

  @property
  def session_timeout_seconds(self) -> int:
    r"""
    If specified, terminate the kernel session after this many seconds of
    runtime, which must be lower than the global maximum.
    """
    return self._session_timeout_seconds or 0

  @session_timeout_seconds.setter
  def session_timeout_seconds(self, session_timeout_seconds: int):
    if session_timeout_seconds is None:
      del self.session_timeout_seconds
      return
    if not isinstance(session_timeout_seconds, int):
      raise TypeError('session_timeout_seconds must be of type int')
    self._session_timeout_seconds = session_timeout_seconds

  def endpoint(self):
    path = '/api/v1/kernels/push'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiSaveKernelResponse(KaggleObject):
  r"""
  Attributes:
    ref (str)
    url (str)
    version_number (int)
    error (str)
    invalid_tags (str)
    invalid_dataset_sources (str)
    invalid_competition_sources (str)
    invalid_kernel_sources (str)
    invalid_model_sources (str)
  """

  def __init__(self):
    self._ref = ""
    self._url = ""
    self._version_number = None
    self._error = None
    self._invalid_tags = []
    self._invalid_dataset_sources = []
    self._invalid_competition_sources = []
    self._invalid_kernel_sources = []
    self._invalid_model_sources = []
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
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def version_number(self) -> int:
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def error(self) -> str:
    return self._error or ""

  @error.setter
  def error(self, error: str):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error

  @property
  def invalid_tags(self) -> Optional[List[str]]:
    return self._invalid_tags

  @invalid_tags.setter
  def invalid_tags(self, invalid_tags: Optional[List[str]]):
    if invalid_tags is None:
      del self.invalid_tags
      return
    if not isinstance(invalid_tags, list):
      raise TypeError('invalid_tags must be of type list')
    if not all([isinstance(t, str) for t in invalid_tags]):
      raise TypeError('invalid_tags must contain only items of type str')
    self._invalid_tags = invalid_tags

  @property
  def invalid_dataset_sources(self) -> Optional[List[str]]:
    return self._invalid_dataset_sources

  @invalid_dataset_sources.setter
  def invalid_dataset_sources(self, invalid_dataset_sources: Optional[List[str]]):
    if invalid_dataset_sources is None:
      del self.invalid_dataset_sources
      return
    if not isinstance(invalid_dataset_sources, list):
      raise TypeError('invalid_dataset_sources must be of type list')
    if not all([isinstance(t, str) for t in invalid_dataset_sources]):
      raise TypeError('invalid_dataset_sources must contain only items of type str')
    self._invalid_dataset_sources = invalid_dataset_sources

  @property
  def invalid_competition_sources(self) -> Optional[List[str]]:
    return self._invalid_competition_sources

  @invalid_competition_sources.setter
  def invalid_competition_sources(self, invalid_competition_sources: Optional[List[str]]):
    if invalid_competition_sources is None:
      del self.invalid_competition_sources
      return
    if not isinstance(invalid_competition_sources, list):
      raise TypeError('invalid_competition_sources must be of type list')
    if not all([isinstance(t, str) for t in invalid_competition_sources]):
      raise TypeError('invalid_competition_sources must contain only items of type str')
    self._invalid_competition_sources = invalid_competition_sources

  @property
  def invalid_kernel_sources(self) -> Optional[List[str]]:
    return self._invalid_kernel_sources

  @invalid_kernel_sources.setter
  def invalid_kernel_sources(self, invalid_kernel_sources: Optional[List[str]]):
    if invalid_kernel_sources is None:
      del self.invalid_kernel_sources
      return
    if not isinstance(invalid_kernel_sources, list):
      raise TypeError('invalid_kernel_sources must be of type list')
    if not all([isinstance(t, str) for t in invalid_kernel_sources]):
      raise TypeError('invalid_kernel_sources must contain only items of type str')
    self._invalid_kernel_sources = invalid_kernel_sources

  @property
  def invalid_model_sources(self) -> Optional[List[str]]:
    return self._invalid_model_sources

  @invalid_model_sources.setter
  def invalid_model_sources(self, invalid_model_sources: Optional[List[str]]):
    if invalid_model_sources is None:
      del self.invalid_model_sources
      return
    if not isinstance(invalid_model_sources, list):
      raise TypeError('invalid_model_sources must be of type list')
    if not all([isinstance(t, str) for t in invalid_model_sources]):
      raise TypeError('invalid_model_sources must contain only items of type str')
    self._invalid_model_sources = invalid_model_sources

  @property
  def versionNumber(self):
    return self.version_number

  @property
  def invalidTags(self):
    return self.invalid_tags

  @property
  def invalidDatasetSources(self):
    return self.invalid_dataset_sources

  @property
  def invalidCompetitionSources(self):
    return self.invalid_competition_sources

  @property
  def invalidKernelSources(self):
    return self.invalid_kernel_sources

  @property
  def invalidModelSources(self):
    return self.invalid_model_sources


class ApiKernelSessionOutputFile(KaggleObject):
  r"""
  Attributes:
    url (str)
    file_name (str)
  """

  def __init__(self):
    self._url = None
    self._file_name = None
    self._freeze()

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


class ApiListKernelFilesItem(KaggleObject):
  r"""
  Attributes:
    name (str)
    size (int)
    creation_date (str)
  """

  def __init__(self):
    self._name = ""
    self._size = 0
    self._creation_date = ""
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
  def size(self) -> int:
    return self._size

  @size.setter
  def size(self, size: int):
    if size is None:
      del self.size
      return
    if not isinstance(size, int):
      raise TypeError('size must be of type int')
    self._size = size

  @property
  def creation_date(self) -> str:
    return self._creation_date

  @creation_date.setter
  def creation_date(self, creation_date: str):
    if creation_date is None:
      del self.creation_date
      return
    if not isinstance(creation_date, str):
      raise TypeError('creation_date must be of type str')
    self._creation_date = creation_date


ApiDownloadKernelOutputRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("kernelSlug", "kernel_slug", "_kernel_slug", str, "", PredefinedSerializer()),
  FieldMetadata("filePath", "file_path", "_file_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
]

ApiDownloadKernelOutputZipRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
]

ApiGetKernelRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("kernelSlug", "kernel_slug", "_kernel_slug", str, "", PredefinedSerializer()),
]

ApiGetKernelResponse._fields = [
  FieldMetadata("metadata", "metadata", "_metadata", ApiKernelMetadata, None, KaggleObjectSerializer()),
  FieldMetadata("blob", "blob", "_blob", ApiKernelBlob, None, KaggleObjectSerializer()),
]

ApiGetKernelSessionStatusRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("kernelSlug", "kernel_slug", "_kernel_slug", str, "", PredefinedSerializer()),
]

ApiGetKernelSessionStatusResponse._fields = [
  FieldMetadata("status", "status", "_status", KernelWorkerStatus, KernelWorkerStatus.QUEUED, EnumSerializer()),
  FieldMetadata("failureMessage", "failure_message", "_failure_message", str, None, PredefinedSerializer(), optional=True),
]

ApiKernelBlob._fields = [
  FieldMetadata("source", "source", "_source", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("language", "language", "_language", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelType", "kernel_type", "_kernel_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
]

ApiKernelMetadata._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("ref", "ref", "_ref", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("author", "author", "_author", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("lastRunTime", "last_run_time", "_last_run_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("language", "language", "_language", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelType", "kernel_type", "_kernel_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableGpu", "enable_gpu", "_enable_gpu", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableTpu", "enable_tpu", "_enable_tpu", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableInternet", "enable_internet", "_enable_internet", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("categoryIds", "category_ids", "_category_ids", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("datasetDataSources", "dataset_data_sources", "_dataset_data_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("kernelDataSources", "kernel_data_sources", "_kernel_data_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("competitionDataSources", "competition_data_sources", "_competition_data_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("modelDataSources", "model_data_sources", "_model_data_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("totalVotes", "total_votes", "_total_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("currentVersionNumber", "current_version_number", "_current_version_number", int, None, PredefinedSerializer(), optional=True),
]

ApiListKernelFilesRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("kernelSlug", "kernel_slug", "_kernel_slug", str, "", PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListKernelFilesResponse._fields = [
  FieldMetadata("files", "files", "_files", ApiListKernelFilesItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListKernelSessionOutputRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("kernelSlug", "kernel_slug", "_kernel_slug", str, "", PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListKernelSessionOutputResponse._fields = [
  FieldMetadata("files", "files", "_files", ApiKernelSessionOutputFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("log", "log", "_log", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListKernelsRequest._fields = [
  FieldMetadata("competition", "competition", "_competition", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dataset", "dataset", "_dataset", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parentKernel", "parent_kernel", "_parent_kernel", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("group", "group", "_group", KernelsListViewType, KernelsListViewType.KERNELS_LIST_VIEW_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("kernelType", "kernel_type", "_kernel_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("language", "language", "_language", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("outputType", "output_type", "_output_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("search", "search", "_search", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sortBy", "sort_by", "_sort_by", KernelsListSortType, KernelsListSortType.HOTNESS, EnumSerializer()),
  FieldMetadata("user", "user", "_user", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("page", "page", "_page", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
]

ApiListKernelsResponse._fields = [
  FieldMetadata("kernels", "kernels", "_kernels", ApiKernelMetadata, [], ListSerializer(KaggleObjectSerializer())),
]

ApiSaveKernelRequest._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("newTitle", "new_title", "_new_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("text", "text", "_text", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("language", "language", "_language", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelType", "kernel_type", "_kernel_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetDataSources", "dataset_data_sources", "_dataset_data_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("kernelDataSources", "kernel_data_sources", "_kernel_data_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("competitionDataSources", "competition_data_sources", "_competition_data_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("categoryIds", "category_ids", "_category_ids", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableGpu", "enable_gpu", "_enable_gpu", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableTpu", "enable_tpu", "_enable_tpu", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableInternet", "enable_internet", "_enable_internet", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerImagePinningType", "docker_image_pinning_type", "_docker_image_pinning_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelDataSources", "model_data_sources", "_model_data_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("sessionTimeoutSeconds", "session_timeout_seconds", "_session_timeout_seconds", int, None, PredefinedSerializer(), optional=True),
]

ApiSaveKernelResponse._fields = [
  FieldMetadata("ref", "ref", "_ref", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("invalidTags", "invalid_tags", "_invalid_tags", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("invalidDatasetSources", "invalid_dataset_sources", "_invalid_dataset_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("invalidCompetitionSources", "invalid_competition_sources", "_invalid_competition_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("invalidKernelSources", "invalid_kernel_sources", "_invalid_kernel_sources", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("invalidModelSources", "invalid_model_sources", "_invalid_model_sources", str, [], ListSerializer(PredefinedSerializer())),
]

ApiKernelSessionOutputFile._fields = [
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fileName", "file_name", "_file_name", str, None, PredefinedSerializer(), optional=True),
]

ApiListKernelFilesItem._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("size", "size", "_size", int, 0, PredefinedSerializer()),
  FieldMetadata("creationDate", "creation_date", "_creation_date", str, "", PredefinedSerializer()),
]

