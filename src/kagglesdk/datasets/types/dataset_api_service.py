from datetime import datetime
from kagglesdk.datasets.types.dataset_enums import DatabundleVersionStatus, DatasetFileTypeGroup, DatasetLicenseGroup, DatasetSelectionGroup, DatasetSizeGroup, DatasetSortBy, DatasetViewedGroup
from kagglesdk.datasets.types.dataset_types import DatasetInfo, DatasetSettings
from kagglesdk.kaggle_object import *
from typing import Optional, List

class ApiCreateDatasetRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
    owner_slug (str)
    slug (str)
    title (str)
    license_name (str)
    is_private (bool)
    files (ApiDatasetNewFile)
    subtitle (str)
    description (str)
    category_ids (str)
  """

  def __init__(self):
    self._id = None
    self._owner_slug = None
    self._slug = None
    self._title = None
    self._license_name = None
    self._is_private = False
    self._files = []
    self._subtitle = None
    self._description = None
    self._category_ids = []
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
    self._id = id

  @property
  def owner_slug(self) -> str:
    return self._owner_slug or ""

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

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
  def license_name(self) -> str:
    return self._license_name or ""

  @license_name.setter
  def license_name(self, license_name: str):
    if license_name is None:
      del self.license_name
      return
    if not isinstance(license_name, str):
      raise TypeError('license_name must be of type str')
    self._license_name = license_name

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def files(self) -> Optional[List[Optional['ApiDatasetNewFile']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiDatasetNewFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiDatasetNewFile) for t in files]):
      raise TypeError('files must contain only items of type ApiDatasetNewFile')
    self._files = files

  @property
  def subtitle(self) -> str:
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: str):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

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

  def endpoint(self):
    path = '/api/v1/datasets/create/new'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiCreateDatasetResponse(KaggleObject):
  r"""
  Attributes:
    ref (str)
    url (str)
    status (str)
    error (str)
    invalid_tags (str)
  """

  def __init__(self):
    self._ref = None
    self._url = None
    self._status = None
    self._error = None
    self._invalid_tags = []
    self._freeze()

  @property
  def ref(self) -> str:
    return self._ref or ""

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
  def status(self) -> str:
    return self._status or ""

  @status.setter
  def status(self, status: str):
    if status is None:
      del self.status
      return
    if not isinstance(status, str):
      raise TypeError('status must be of type str')
    self._status = status

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
  def invalidTags(self):
    return self.invalid_tags


class ApiCreateDatasetVersionByIdRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
    body (ApiCreateDatasetVersionRequestBody)
  """

  def __init__(self):
    self._id = 0
    self._body = None
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
  def body(self) -> Optional['ApiCreateDatasetVersionRequestBody']:
    return self._body

  @body.setter
  def body(self, body: Optional['ApiCreateDatasetVersionRequestBody']):
    if body is None:
      del self.body
      return
    if not isinstance(body, ApiCreateDatasetVersionRequestBody):
      raise TypeError('body must be of type ApiCreateDatasetVersionRequestBody')
    self._body = body

  def endpoint(self):
    path = '/api/v1/datasets/create/version/{id}'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return 'body'


class ApiCreateDatasetVersionRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    dataset_slug (str)
    body (ApiCreateDatasetVersionRequestBody)
  """

  def __init__(self):
    self._owner_slug = ""
    self._dataset_slug = ""
    self._body = None
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
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  @property
  def body(self) -> Optional['ApiCreateDatasetVersionRequestBody']:
    return self._body

  @body.setter
  def body(self, body: Optional['ApiCreateDatasetVersionRequestBody']):
    if body is None:
      del self.body
      return
    if not isinstance(body, ApiCreateDatasetVersionRequestBody):
      raise TypeError('body must be of type ApiCreateDatasetVersionRequestBody')
    self._body = body

  def endpoint(self):
    path = '/api/v1/datasets/create/version/{owner_slug}/{dataset_slug}'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return 'body'


class ApiCreateDatasetVersionRequestBody(KaggleObject):
  r"""
  Attributes:
    version_notes (str)
    delete_old_versions (bool)
    files (ApiDatasetNewFile)
    subtitle (str)
    description (str)
    category_ids (str)
  """

  def __init__(self):
    self._version_notes = None
    self._delete_old_versions = False
    self._files = []
    self._subtitle = None
    self._description = None
    self._category_ids = []
    self._freeze()

  @property
  def version_notes(self) -> str:
    return self._version_notes or ""

  @version_notes.setter
  def version_notes(self, version_notes: str):
    if version_notes is None:
      del self.version_notes
      return
    if not isinstance(version_notes, str):
      raise TypeError('version_notes must be of type str')
    self._version_notes = version_notes

  @property
  def delete_old_versions(self) -> bool:
    return self._delete_old_versions

  @delete_old_versions.setter
  def delete_old_versions(self, delete_old_versions: bool):
    if delete_old_versions is None:
      del self.delete_old_versions
      return
    if not isinstance(delete_old_versions, bool):
      raise TypeError('delete_old_versions must be of type bool')
    self._delete_old_versions = delete_old_versions

  @property
  def files(self) -> Optional[List[Optional['ApiDatasetNewFile']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiDatasetNewFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiDatasetNewFile) for t in files]):
      raise TypeError('files must contain only items of type ApiDatasetNewFile')
    self._files = files

  @property
  def subtitle(self) -> str:
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: str):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

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


class ApiDataset(KaggleObject):
  r"""
  Attributes:
    id (int)
    ref (str)
    subtitle (str)
    creator_name (str)
    creator_url (str)
    total_bytes (int)
    url (str)
    last_updated (datetime)
    download_count (int)
    is_private (bool)
    is_featured (bool)
    license_name (str)
    description (str)
    owner_name (str)
    owner_ref (str)
    kernel_count (int)
    title (str)
    topic_count (int)
    view_count (int)
    vote_count (int)
    current_version_number (int)
    usability_rating (float)
    tags (ApiCategory)
    files (ApiDatasetFile)
    versions (ApiDatasetVersion)
  """

  def __init__(self):
    self._id = 0
    self._ref = ""
    self._subtitle = None
    self._creator_name = None
    self._creator_url = None
    self._total_bytes = None
    self._url = None
    self._last_updated = None
    self._download_count = 0
    self._is_private = False
    self._is_featured = False
    self._license_name = None
    self._description = None
    self._owner_name = None
    self._owner_ref = None
    self._kernel_count = 0
    self._title = None
    self._topic_count = 0
    self._view_count = 0
    self._vote_count = 0
    self._current_version_number = None
    self._usability_rating = None
    self._tags = []
    self._files = []
    self._versions = []
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
  def subtitle(self) -> str:
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: str):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def creator_name(self) -> str:
    return self._creator_name or ""

  @creator_name.setter
  def creator_name(self, creator_name: str):
    if creator_name is None:
      del self.creator_name
      return
    if not isinstance(creator_name, str):
      raise TypeError('creator_name must be of type str')
    self._creator_name = creator_name

  @property
  def creator_url(self) -> str:
    return self._creator_url or ""

  @creator_url.setter
  def creator_url(self, creator_url: str):
    if creator_url is None:
      del self.creator_url
      return
    if not isinstance(creator_url, str):
      raise TypeError('creator_url must be of type str')
    self._creator_url = creator_url

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
  def last_updated(self) -> datetime:
    return self._last_updated

  @last_updated.setter
  def last_updated(self, last_updated: datetime):
    if last_updated is None:
      del self.last_updated
      return
    if not isinstance(last_updated, datetime):
      raise TypeError('last_updated must be of type datetime')
    self._last_updated = last_updated

  @property
  def download_count(self) -> int:
    return self._download_count

  @download_count.setter
  def download_count(self, download_count: int):
    if download_count is None:
      del self.download_count
      return
    if not isinstance(download_count, int):
      raise TypeError('download_count must be of type int')
    self._download_count = download_count

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def is_featured(self) -> bool:
    return self._is_featured

  @is_featured.setter
  def is_featured(self, is_featured: bool):
    if is_featured is None:
      del self.is_featured
      return
    if not isinstance(is_featured, bool):
      raise TypeError('is_featured must be of type bool')
    self._is_featured = is_featured

  @property
  def license_name(self) -> str:
    return self._license_name or ""

  @license_name.setter
  def license_name(self, license_name: str):
    if license_name is None:
      del self.license_name
      return
    if not isinstance(license_name, str):
      raise TypeError('license_name must be of type str')
    self._license_name = license_name

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
  def owner_name(self) -> str:
    return self._owner_name or ""

  @owner_name.setter
  def owner_name(self, owner_name: str):
    if owner_name is None:
      del self.owner_name
      return
    if not isinstance(owner_name, str):
      raise TypeError('owner_name must be of type str')
    self._owner_name = owner_name

  @property
  def owner_ref(self) -> str:
    return self._owner_ref or ""

  @owner_ref.setter
  def owner_ref(self, owner_ref: str):
    if owner_ref is None:
      del self.owner_ref
      return
    if not isinstance(owner_ref, str):
      raise TypeError('owner_ref must be of type str')
    self._owner_ref = owner_ref

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
  def topic_count(self) -> int:
    return self._topic_count

  @topic_count.setter
  def topic_count(self, topic_count: int):
    if topic_count is None:
      del self.topic_count
      return
    if not isinstance(topic_count, int):
      raise TypeError('topic_count must be of type int')
    self._topic_count = topic_count

  @property
  def view_count(self) -> int:
    return self._view_count

  @view_count.setter
  def view_count(self, view_count: int):
    if view_count is None:
      del self.view_count
      return
    if not isinstance(view_count, int):
      raise TypeError('view_count must be of type int')
    self._view_count = view_count

  @property
  def vote_count(self) -> int:
    return self._vote_count

  @vote_count.setter
  def vote_count(self, vote_count: int):
    if vote_count is None:
      del self.vote_count
      return
    if not isinstance(vote_count, int):
      raise TypeError('vote_count must be of type int')
    self._vote_count = vote_count

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

  @property
  def usability_rating(self) -> float:
    return self._usability_rating or 0.0

  @usability_rating.setter
  def usability_rating(self, usability_rating: float):
    if usability_rating is None:
      del self.usability_rating
      return
    if not isinstance(usability_rating, float):
      raise TypeError('usability_rating must be of type float')
    self._usability_rating = usability_rating

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
  def files(self) -> Optional[List[Optional['ApiDatasetFile']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiDatasetFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiDatasetFile) for t in files]):
      raise TypeError('files must contain only items of type ApiDatasetFile')
    self._files = files

  @property
  def versions(self) -> Optional[List[Optional['ApiDatasetVersion']]]:
    return self._versions

  @versions.setter
  def versions(self, versions: Optional[List[Optional['ApiDatasetVersion']]]):
    if versions is None:
      del self.versions
      return
    if not isinstance(versions, list):
      raise TypeError('versions must be of type list')
    if not all([isinstance(t, ApiDatasetVersion) for t in versions]):
      raise TypeError('versions must contain only items of type ApiDatasetVersion')
    self._versions = versions


class ApiDatasetFile(KaggleObject):
  r"""
  Attributes:
    ref (str)
    dataset_ref (str)
    owner_ref (str)
    name (str)
    creation_date (datetime)
    description (str)
    file_type (str)
    url (str)
    total_bytes (int)
    columns (ApiDatasetColumn)
  """

  def __init__(self):
    self._ref = ""
    self._dataset_ref = None
    self._owner_ref = None
    self._name = None
    self._creation_date = None
    self._description = None
    self._file_type = None
    self._url = None
    self._total_bytes = 0
    self._columns = []
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
  def dataset_ref(self) -> str:
    return self._dataset_ref or ""

  @dataset_ref.setter
  def dataset_ref(self, dataset_ref: str):
    if dataset_ref is None:
      del self.dataset_ref
      return
    if not isinstance(dataset_ref, str):
      raise TypeError('dataset_ref must be of type str')
    self._dataset_ref = dataset_ref

  @property
  def owner_ref(self) -> str:
    return self._owner_ref or ""

  @owner_ref.setter
  def owner_ref(self, owner_ref: str):
    if owner_ref is None:
      del self.owner_ref
      return
    if not isinstance(owner_ref, str):
      raise TypeError('owner_ref must be of type str')
    self._owner_ref = owner_ref

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
  def file_type(self) -> str:
    return self._file_type or ""

  @file_type.setter
  def file_type(self, file_type: str):
    if file_type is None:
      del self.file_type
      return
    if not isinstance(file_type, str):
      raise TypeError('file_type must be of type str')
    self._file_type = file_type

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
  def columns(self) -> Optional[List[Optional['ApiDatasetColumn']]]:
    return self._columns

  @columns.setter
  def columns(self, columns: Optional[List[Optional['ApiDatasetColumn']]]):
    if columns is None:
      del self.columns
      return
    if not isinstance(columns, list):
      raise TypeError('columns must be of type list')
    if not all([isinstance(t, ApiDatasetColumn) for t in columns]):
      raise TypeError('columns must contain only items of type ApiDatasetColumn')
    self._columns = columns


class ApiDatasetNewFile(KaggleObject):
  r"""
  Attributes:
    token (str)
    description (str)
    columns (ApiDatasetColumn)
  """

  def __init__(self):
    self._token = None
    self._description = None
    self._columns = []
    self._freeze()

  @property
  def token(self) -> str:
    return self._token or ""

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token

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
  def columns(self) -> Optional[List[Optional['ApiDatasetColumn']]]:
    return self._columns

  @columns.setter
  def columns(self, columns: Optional[List[Optional['ApiDatasetColumn']]]):
    if columns is None:
      del self.columns
      return
    if not isinstance(columns, list):
      raise TypeError('columns must be of type list')
    if not all([isinstance(t, ApiDatasetColumn) for t in columns]):
      raise TypeError('columns must contain only items of type ApiDatasetColumn')
    self._columns = columns


class ApiDatasetVersion(KaggleObject):
  r"""
  Attributes:
    version_number (int)
    creation_date (datetime)
    creator_name (str)
    creator_ref (str)
    version_notes (str)
    status (str)
  """

  def __init__(self):
    self._version_number = 0
    self._creation_date = None
    self._creator_name = None
    self._creator_ref = None
    self._version_notes = None
    self._status = None
    self._freeze()

  @property
  def version_number(self) -> int:
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

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

  @property
  def creator_name(self) -> str:
    return self._creator_name or ""

  @creator_name.setter
  def creator_name(self, creator_name: str):
    if creator_name is None:
      del self.creator_name
      return
    if not isinstance(creator_name, str):
      raise TypeError('creator_name must be of type str')
    self._creator_name = creator_name

  @property
  def creator_ref(self) -> str:
    return self._creator_ref or ""

  @creator_ref.setter
  def creator_ref(self, creator_ref: str):
    if creator_ref is None:
      del self.creator_ref
      return
    if not isinstance(creator_ref, str):
      raise TypeError('creator_ref must be of type str')
    self._creator_ref = creator_ref

  @property
  def version_notes(self) -> str:
    return self._version_notes or ""

  @version_notes.setter
  def version_notes(self, version_notes: str):
    if version_notes is None:
      del self.version_notes
      return
    if not isinstance(version_notes, str):
      raise TypeError('version_notes must be of type str')
    self._version_notes = version_notes

  @property
  def status(self) -> str:
    return self._status or ""

  @status.setter
  def status(self, status: str):
    if status is None:
      del self.status
      return
    if not isinstance(status, str):
      raise TypeError('status must be of type str')
    self._status = status


class ApiDeleteDatasetRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    dataset_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._dataset_slug = ""
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
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  def endpoint(self):
    path = '/api/v1/dataset/{owner_slug}/{dataset_slug}/delete'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'


class ApiDeleteDatasetResponse(KaggleObject):
  r"""
  Attributes:
    error (str)
  """

  def __init__(self):
    self._error = None
    self._freeze()

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


class ApiDownloadDatasetRawRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    dataset_slug (str)
    file_name (str)
    dataset_version_number (int)
  """

  def __init__(self):
    self._owner_slug = ""
    self._dataset_slug = ""
    self._file_name = None
    self._dataset_version_number = None
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
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

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
  def dataset_version_number(self) -> int:
    return self._dataset_version_number or 0

  @dataset_version_number.setter
  def dataset_version_number(self, dataset_version_number: int):
    if dataset_version_number is None:
      del self.dataset_version_number
      return
    if not isinstance(dataset_version_number, int):
      raise TypeError('dataset_version_number must be of type int')
    self._dataset_version_number = dataset_version_number

  def endpoint(self):
    path = '/api/v1/datasets/download-raw/{owner_slug}/{dataset_slug}/{file_name}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/datasets/download-raw/{owner_slug}/{dataset_slug}/{file_name}'


class ApiDownloadDatasetRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    dataset_slug (str)
    file_name (str)
    dataset_version_number (int)
    raw (bool)
    hash_link (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._dataset_slug = ""
    self._file_name = None
    self._dataset_version_number = None
    self._raw = False
    self._hash_link = None
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
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

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
  def dataset_version_number(self) -> int:
    return self._dataset_version_number or 0

  @dataset_version_number.setter
  def dataset_version_number(self, dataset_version_number: int):
    if dataset_version_number is None:
      del self.dataset_version_number
      return
    if not isinstance(dataset_version_number, int):
      raise TypeError('dataset_version_number must be of type int')
    self._dataset_version_number = dataset_version_number

  @property
  def raw(self) -> bool:
    return self._raw

  @raw.setter
  def raw(self, raw: bool):
    if raw is None:
      del self.raw
      return
    if not isinstance(raw, bool):
      raise TypeError('raw must be of type bool')
    self._raw = raw

  @property
  def hash_link(self) -> str:
    return self._hash_link or ""

  @hash_link.setter
  def hash_link(self, hash_link: str):
    if hash_link is None:
      del self.hash_link
      return
    if not isinstance(hash_link, str):
      raise TypeError('hash_link must be of type str')
    self._hash_link = hash_link

  def endpoint(self):
    if self.file_name:
      path = '/api/v1/datasets/download/{owner_slug}/{dataset_slug}/{file_name}'
    else:
      path = '/api/v1/datasets/download/{owner_slug}/{dataset_slug}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/datasets/download/{owner_slug}/{dataset_slug}'


class ApiGetDatasetMetadataRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    dataset_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._dataset_slug = ""
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
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  def endpoint(self):
    path = '/api/v1/datasets/metadata/{owner_slug}/{dataset_slug}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/datasets/metadata/{owner_slug}/{dataset_slug}'


class ApiGetDatasetMetadataResponse(KaggleObject):
  r"""
  Attributes:
    info (DatasetInfo)
    error_message (str)
      Required for backwards-compatibility. See
      https://github.com/Kaggle/kaggle-api/issues/235
  """

  def __init__(self):
    self._info = None
    self._error_message = None
    self._freeze()

  @property
  def info(self) -> Optional['DatasetInfo']:
    return self._info

  @info.setter
  def info(self, info: Optional['DatasetInfo']):
    if info is None:
      del self.info
      return
    if not isinstance(info, DatasetInfo):
      raise TypeError('info must be of type DatasetInfo')
    self._info = info

  @property
  def error_message(self) -> str:
    r"""
    Required for backwards-compatibility. See
    https://github.com/Kaggle/kaggle-api/issues/235
    """
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: str):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message

  @property
  def errorMessage(self):
    return self.error_message


class ApiGetDatasetRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    dataset_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._dataset_slug = ""
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
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  def endpoint(self):
    path = '/api/v1/datasets/view/{owner_slug}/{dataset_slug}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/datasets/view/{owner_slug}/{dataset_slug}'


class ApiGetDatasetStatusRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    dataset_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._dataset_slug = ""
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
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  def endpoint(self):
    path = '/api/v1/datasets/status/{owner_slug}/{dataset_slug}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/datasets/status/{owner_slug}/{dataset_slug}'


class ApiGetDatasetStatusResponse(KaggleObject):
  r"""
  Attributes:
    status (DatabundleVersionStatus)
  """

  def __init__(self):
    self._status = DatabundleVersionStatus.NOT_YET_PERSISTED
    self._freeze()

  @property
  def status(self) -> 'DatabundleVersionStatus':
    return self._status

  @status.setter
  def status(self, status: 'DatabundleVersionStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, DatabundleVersionStatus):
      raise TypeError('status must be of type DatabundleVersionStatus')
    self._status = status

  @classmethod
  def prepare_from(cls, http_response):
    return cls.from_dict({'status': json.loads(http_response.text)})


class ApiListDatasetFilesRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    dataset_slug (str)
    dataset_version_number (int)
    page_token (str)
    page_size (int)
  """

  def __init__(self):
    self._owner_slug = ""
    self._dataset_slug = ""
    self._dataset_version_number = None
    self._page_token = None
    self._page_size = None
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
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  @property
  def dataset_version_number(self) -> int:
    return self._dataset_version_number or 0

  @dataset_version_number.setter
  def dataset_version_number(self, dataset_version_number: int):
    if dataset_version_number is None:
      del self.dataset_version_number
      return
    if not isinstance(dataset_version_number, int):
      raise TypeError('dataset_version_number must be of type int')
    self._dataset_version_number = dataset_version_number

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

  def endpoint(self):
    path = '/api/v1/datasets/list/{owner_slug}/{dataset_slug}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/datasets/list/{owner_slug}/{dataset_slug}'


class ApiListDatasetFilesResponse(KaggleObject):
  r"""
  Attributes:
    dataset_files (ApiDatasetFile)
    error_message (str)
    next_page_token (str)
  """

  def __init__(self):
    self._dataset_files = []
    self._error_message = None
    self._next_page_token = None
    self._freeze()

  @property
  def dataset_files(self) -> Optional[List[Optional['ApiDatasetFile']]]:
    return self._dataset_files

  @dataset_files.setter
  def dataset_files(self, dataset_files: Optional[List[Optional['ApiDatasetFile']]]):
    if dataset_files is None:
      del self.dataset_files
      return
    if not isinstance(dataset_files, list):
      raise TypeError('dataset_files must be of type list')
    if not all([isinstance(t, ApiDatasetFile) for t in dataset_files]):
      raise TypeError('dataset_files must contain only items of type ApiDatasetFile')
    self._dataset_files = dataset_files

  @property
  def error_message(self) -> str:
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: str):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message

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
  def files(self):
    return self.dataset_files

  @property
  def errorMessage(self):
    return self.error_message

  @property
  def nextPageToken(self):
    return self.next_page_token


class ApiListDatasetsRequest(KaggleObject):
  r"""
  Attributes:
    group (DatasetSelectionGroup)
    sort_by (DatasetSortBy)
    size (DatasetSizeGroup)
    file_type (DatasetFileTypeGroup)
    license (DatasetLicenseGroup)
    viewed (DatasetViewedGroup)
    tag_ids (str)
    search (str)
    user (str)
    min_size (int)
    max_size (int)
    page (int)
    page_token (str)
    page_size (int)
  """

  def __init__(self):
    self._group = DatasetSelectionGroup.DATASET_SELECTION_GROUP_PUBLIC
    self._sort_by = DatasetSortBy.DATASET_SORT_BY_HOTTEST
    self._size = DatasetSizeGroup.DATASET_SIZE_GROUP_ALL
    self._file_type = DatasetFileTypeGroup.DATASET_FILE_TYPE_GROUP_ALL
    self._license = DatasetLicenseGroup.DATASET_LICENSE_GROUP_ALL
    self._viewed = DatasetViewedGroup.DATASET_VIEWED_GROUP_UNSPECIFIED
    self._tag_ids = None
    self._search = None
    self._user = None
    self._min_size = None
    self._max_size = None
    self._page = None
    self._page_token = None
    self._page_size = None
    self._freeze()

  @property
  def group(self) -> 'DatasetSelectionGroup':
    return self._group

  @group.setter
  def group(self, group: 'DatasetSelectionGroup'):
    if group is None:
      del self.group
      return
    if not isinstance(group, DatasetSelectionGroup):
      raise TypeError('group must be of type DatasetSelectionGroup')
    self._group = group

  @property
  def sort_by(self) -> 'DatasetSortBy':
    return self._sort_by

  @sort_by.setter
  def sort_by(self, sort_by: 'DatasetSortBy'):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, DatasetSortBy):
      raise TypeError('sort_by must be of type DatasetSortBy')
    self._sort_by = sort_by

  @property
  def size(self) -> 'DatasetSizeGroup':
    return self._size

  @size.setter
  def size(self, size: 'DatasetSizeGroup'):
    if size is None:
      del self.size
      return
    if not isinstance(size, DatasetSizeGroup):
      raise TypeError('size must be of type DatasetSizeGroup')
    self._size = size

  @property
  def file_type(self) -> 'DatasetFileTypeGroup':
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
  def license(self) -> 'DatasetLicenseGroup':
    return self._license

  @license.setter
  def license(self, license: 'DatasetLicenseGroup'):
    if license is None:
      del self.license
      return
    if not isinstance(license, DatasetLicenseGroup):
      raise TypeError('license must be of type DatasetLicenseGroup')
    self._license = license

  @property
  def viewed(self) -> 'DatasetViewedGroup':
    return self._viewed

  @viewed.setter
  def viewed(self, viewed: 'DatasetViewedGroup'):
    if viewed is None:
      del self.viewed
      return
    if not isinstance(viewed, DatasetViewedGroup):
      raise TypeError('viewed must be of type DatasetViewedGroup')
    self._viewed = viewed

  @property
  def tag_ids(self) -> str:
    return self._tag_ids or ""

  @tag_ids.setter
  def tag_ids(self, tag_ids: str):
    if tag_ids is None:
      del self.tag_ids
      return
    if not isinstance(tag_ids, str):
      raise TypeError('tag_ids must be of type str')
    self._tag_ids = tag_ids

  @property
  def search(self) -> str:
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
  def user(self) -> str:
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
  def min_size(self) -> int:
    return self._min_size or 0

  @min_size.setter
  def min_size(self, min_size: int):
    if min_size is None:
      del self.min_size
      return
    if not isinstance(min_size, int):
      raise TypeError('min_size must be of type int')
    self._min_size = min_size

  @property
  def max_size(self) -> int:
    return self._max_size or 0

  @max_size.setter
  def max_size(self, max_size: int):
    if max_size is None:
      del self.max_size
      return
    if not isinstance(max_size, int):
      raise TypeError('max_size must be of type int')
    self._max_size = max_size

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

  def endpoint(self):
    path = '/api/v1/datasets/list'
    return path.format_map(self.to_field_map(self))


class ApiListDatasetsResponse(KaggleObject):
  r"""
  Attributes:
    datasets (ApiDataset)
  """

  def __init__(self):
    self._datasets = []
    self._freeze()

  @property
  def datasets(self) -> Optional[List[Optional['ApiDataset']]]:
    return self._datasets

  @datasets.setter
  def datasets(self, datasets: Optional[List[Optional['ApiDataset']]]):
    if datasets is None:
      del self.datasets
      return
    if not isinstance(datasets, list):
      raise TypeError('datasets must be of type list')
    if not all([isinstance(t, ApiDataset) for t in datasets]):
      raise TypeError('datasets must contain only items of type ApiDataset')
    self._datasets = datasets

  @classmethod
  def prepare_from(cls, http_response):
    return cls.from_dict({'datasets': json.loads(http_response.text)})


class ApiUpdateDatasetMetadataRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    dataset_slug (str)
    settings (DatasetSettings)
  """

  def __init__(self):
    self._owner_slug = ""
    self._dataset_slug = ""
    self._settings = None
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
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  @property
  def settings(self) -> Optional['DatasetSettings']:
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['DatasetSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, DatasetSettings):
      raise TypeError('settings must be of type DatasetSettings')
    self._settings = settings

  def endpoint(self):
    path = '/api/v1/datasets/metadata/{owner_slug}/{dataset_slug}'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return 'settings'


class ApiUpdateDatasetMetadataResponse(KaggleObject):
  r"""
  Attributes:
    errors (str)
      Required for backwards-compatibility.
  """

  def __init__(self):
    self._errors = []
    self._freeze()

  @property
  def errors(self) -> Optional[List[str]]:
    """Required for backwards-compatibility."""
    return self._errors

  @errors.setter
  def errors(self, errors: Optional[List[str]]):
    if errors is None:
      del self.errors
      return
    if not isinstance(errors, list):
      raise TypeError('errors must be of type list')
    if not all([isinstance(t, str) for t in errors]):
      raise TypeError('errors must contain only items of type str')
    self._errors = errors


class ApiUploadDatasetFileRequest(KaggleObject):
  r"""
  Attributes:
    file_name (str)
    content_length (int)
    last_modified_epoch_seconds (int)
  """

  def __init__(self):
    self._file_name = ""
    self._content_length = 0
    self._last_modified_epoch_seconds = 0
    self._freeze()

  @property
  def file_name(self) -> str:
    return self._file_name

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

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

  def endpoint(self):
    path = '/api/v1/datasets/upload/file/{content_length}/{last_modified_epoch_seconds}'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'


class ApiUploadDatasetFileResponse(KaggleObject):
  r"""
  Attributes:
    token (str)
      Opaque string token used to reference the new BlobFile.
    create_url (str)
      URL to use to start the upload
  """

  def __init__(self):
    self._token = ""
    self._create_url = ""
    self._freeze()

  @property
  def token(self) -> str:
    """Opaque string token used to reference the new BlobFile."""
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
    """URL to use to start the upload"""
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


class ApiCategory(KaggleObject):
  r"""
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


class ApiDatasetColumn(KaggleObject):
  r"""
  Attributes:
    order (int)
    name (str)
    type (str)
    original_type (str)
    description (str)
  """

  def __init__(self):
    self._order = None
    self._name = None
    self._type = None
    self._original_type = None
    self._description = None
    self._freeze()

  @property
  def order(self) -> int:
    return self._order or 0

  @order.setter
  def order(self, order: int):
    if order is None:
      del self.order
      return
    if not isinstance(order, int):
      raise TypeError('order must be of type int')
    self._order = order

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
  def type(self) -> str:
    return self._type or ""

  @type.setter
  def type(self, type: str):
    if type is None:
      del self.type
      return
    if not isinstance(type, str):
      raise TypeError('type must be of type str')
    self._type = type

  @property
  def original_type(self) -> str:
    return self._original_type or ""

  @original_type.setter
  def original_type(self, original_type: str):
    if original_type is None:
      del self.original_type
      return
    if not isinstance(original_type, str):
      raise TypeError('original_type must be of type str')
    self._original_type = original_type

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


class ApiUploadDirectoryInfo(KaggleObject):
  r"""
  Attributes:
    name (str)
    directories (ApiUploadDirectoryInfo)
    files (ApiDatasetNewFile)
  """

  def __init__(self):
    self._name = ""
    self._directories = []
    self._files = []
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
  def directories(self) -> Optional[List[Optional['ApiUploadDirectoryInfo']]]:
    return self._directories

  @directories.setter
  def directories(self, directories: Optional[List[Optional['ApiUploadDirectoryInfo']]]):
    if directories is None:
      del self.directories
      return
    if not isinstance(directories, list):
      raise TypeError('directories must be of type list')
    if not all([isinstance(t, ApiUploadDirectoryInfo) for t in directories]):
      raise TypeError('directories must contain only items of type ApiUploadDirectoryInfo')
    self._directories = directories

  @property
  def files(self) -> Optional[List[Optional['ApiDatasetNewFile']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiDatasetNewFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiDatasetNewFile) for t in files]):
      raise TypeError('files must contain only items of type ApiDatasetNewFile')
    self._files = files


ApiCreateDatasetRequest._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licenseName", "license_name", "_license_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("files", "files", "_files", ApiDatasetNewFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("categoryIds", "category_ids", "_category_ids", str, [], ListSerializer(PredefinedSerializer())),
]

ApiCreateDatasetResponse._fields = [
  FieldMetadata("ref", "ref", "_ref", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("status", "status", "_status", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("invalidTags", "invalid_tags", "_invalid_tags", str, [], ListSerializer(PredefinedSerializer())),
]

ApiCreateDatasetVersionByIdRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("body", "body", "_body", ApiCreateDatasetVersionRequestBody, None, KaggleObjectSerializer()),
]

ApiCreateDatasetVersionRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
  FieldMetadata("body", "body", "_body", ApiCreateDatasetVersionRequestBody, None, KaggleObjectSerializer()),
]

ApiCreateDatasetVersionRequestBody._fields = [
  FieldMetadata("versionNotes", "version_notes", "_version_notes", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("deleteOldVersions", "delete_old_versions", "_delete_old_versions", bool, False, PredefinedSerializer()),
  FieldMetadata("files", "files", "_files", ApiDatasetNewFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("categoryIds", "category_ids", "_category_ids", str, [], ListSerializer(PredefinedSerializer())),
]

ApiDataset._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("ref", "ref", "_ref", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creatorName", "creator_name", "_creator_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creatorUrl", "creator_url", "_creator_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalBytes", "total_bytes", "_total_bytes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastUpdated", "last_updated", "_last_updated", datetime, None, DateTimeSerializer()),
  FieldMetadata("downloadCount", "download_count", "_download_count", int, 0, PredefinedSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("isFeatured", "is_featured", "_is_featured", bool, False, PredefinedSerializer()),
  FieldMetadata("licenseName", "license_name", "_license_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerName", "owner_name", "_owner_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerRef", "owner_ref", "_owner_ref", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelCount", "kernel_count", "_kernel_count", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("topicCount", "topic_count", "_topic_count", int, 0, PredefinedSerializer()),
  FieldMetadata("viewCount", "view_count", "_view_count", int, 0, PredefinedSerializer()),
  FieldMetadata("voteCount", "vote_count", "_vote_count", int, 0, PredefinedSerializer()),
  FieldMetadata("currentVersionNumber", "current_version_number", "_current_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("usabilityRating", "usability_rating", "_usability_rating", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tags", "tags", "_tags", ApiCategory, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("files", "files", "_files", ApiDatasetFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("versions", "versions", "_versions", ApiDatasetVersion, [], ListSerializer(KaggleObjectSerializer())),
]

ApiDatasetFile._fields = [
  FieldMetadata("ref", "ref", "_ref", str, "", PredefinedSerializer()),
  FieldMetadata("datasetRef", "dataset_ref", "_dataset_ref", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerRef", "owner_ref", "_owner_ref", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creationDate", "creation_date", "_creation_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fileType", "file_type", "_file_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalBytes", "total_bytes", "_total_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("columns", "columns", "_columns", ApiDatasetColumn, [], ListSerializer(KaggleObjectSerializer())),
]

ApiDatasetNewFile._fields = [
  FieldMetadata("token", "token", "_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("columns", "columns", "_columns", ApiDatasetColumn, [], ListSerializer(KaggleObjectSerializer())),
]

ApiDatasetVersion._fields = [
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("creationDate", "creation_date", "_creation_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("creatorName", "creator_name", "_creator_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creatorRef", "creator_ref", "_creator_ref", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionNotes", "version_notes", "_version_notes", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("status", "status", "_status", str, None, PredefinedSerializer(), optional=True),
]

ApiDeleteDatasetRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
]

ApiDeleteDatasetResponse._fields = [
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
]

ApiDownloadDatasetRawRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetVersionNumber", "dataset_version_number", "_dataset_version_number", int, None, PredefinedSerializer(), optional=True),
]

ApiDownloadDatasetRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetVersionNumber", "dataset_version_number", "_dataset_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("raw", "raw", "_raw", bool, False, PredefinedSerializer()),
  FieldMetadata("hashLink", "hash_link", "_hash_link", str, None, PredefinedSerializer(), optional=True),
]

ApiGetDatasetMetadataRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
]

ApiGetDatasetMetadataResponse._fields = [
  FieldMetadata("info", "info", "_info", DatasetInfo, None, KaggleObjectSerializer()),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
]

ApiGetDatasetRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
]

ApiGetDatasetStatusRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
]

ApiGetDatasetStatusResponse._fields = [
  FieldMetadata("status", "status", "_status", DatabundleVersionStatus, DatabundleVersionStatus.NOT_YET_PERSISTED, EnumSerializer()),
]

ApiListDatasetFilesRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetVersionNumber", "dataset_version_number", "_dataset_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
]

ApiListDatasetFilesResponse._fields = [
  FieldMetadata("datasetFiles", "dataset_files", "_dataset_files", ApiDatasetFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListDatasetsRequest._fields = [
  FieldMetadata("group", "group", "_group", DatasetSelectionGroup, DatasetSelectionGroup.DATASET_SELECTION_GROUP_PUBLIC, EnumSerializer()),
  FieldMetadata("sortBy", "sort_by", "_sort_by", DatasetSortBy, DatasetSortBy.DATASET_SORT_BY_HOTTEST, EnumSerializer()),
  FieldMetadata("size", "size", "_size", DatasetSizeGroup, DatasetSizeGroup.DATASET_SIZE_GROUP_ALL, EnumSerializer()),
  FieldMetadata("fileType", "file_type", "_file_type", DatasetFileTypeGroup, DatasetFileTypeGroup.DATASET_FILE_TYPE_GROUP_ALL, EnumSerializer()),
  FieldMetadata("license", "license", "_license", DatasetLicenseGroup, DatasetLicenseGroup.DATASET_LICENSE_GROUP_ALL, EnumSerializer()),
  FieldMetadata("viewed", "viewed", "_viewed", DatasetViewedGroup, DatasetViewedGroup.DATASET_VIEWED_GROUP_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("search", "search", "_search", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("user", "user", "_user", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("minSize", "min_size", "_min_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxSize", "max_size", "_max_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("page", "page", "_page", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
]

ApiListDatasetsResponse._fields = [
  FieldMetadata("datasets", "datasets", "_datasets", ApiDataset, [], ListSerializer(KaggleObjectSerializer())),
]

ApiUpdateDatasetMetadataRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", DatasetSettings, None, KaggleObjectSerializer()),
]

ApiUpdateDatasetMetadataResponse._fields = [
  FieldMetadata("errors", "errors", "_errors", str, [], ListSerializer(PredefinedSerializer())),
]

ApiUploadDatasetFileRequest._fields = [
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("lastModifiedEpochSeconds", "last_modified_epoch_seconds", "_last_modified_epoch_seconds", int, 0, PredefinedSerializer()),
]

ApiUploadDatasetFileResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
  FieldMetadata("createUrl", "create_url", "_create_url", str, "", PredefinedSerializer()),
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

ApiDatasetColumn._fields = [
  FieldMetadata("order", "order", "_order", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("originalType", "original_type", "_original_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
]

ApiUploadDirectoryInfo._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("directories", "directories", "_directories", ApiUploadDirectoryInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("files", "files", "_files", ApiDatasetNewFile, [], ListSerializer(KaggleObjectSerializer())),
]

