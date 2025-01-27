from kagglesdk.kaggle_object import *
from kagglesdk.users.types.users_enums import CollaboratorType
from typing import Optional, List

class DatasetInfo(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    dataset_slug (str)
    owner_user (str)
    usability_rating (float)
    total_views (int)
    total_votes (int)
    total_downloads (int)
    title (str)
      Copy/paste from DatasetSettings below. Can't use composition because
      that'd be a backwards-incompatible change for the Python Api.
    subtitle (str)
    description (str)
    is_private (bool)
    keywords (str)
    licenses (SettingsLicense)
    collaborators (DatasetCollaborator)
    data (DatasetSettingsFile)
  """

  def __init__(self):
    self._dataset_id = 0
    self._dataset_slug = None
    self._owner_user = None
    self._usability_rating = None
    self._total_views = 0
    self._total_votes = 0
    self._total_downloads = 0
    self._title = None
    self._subtitle = None
    self._description = None
    self._is_private = False
    self._keywords = []
    self._licenses = []
    self._collaborators = []
    self._data = []
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def dataset_slug(self) -> str:
    return self._dataset_slug or ""

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  @property
  def owner_user(self) -> str:
    return self._owner_user or ""

  @owner_user.setter
  def owner_user(self, owner_user: str):
    if owner_user is None:
      del self.owner_user
      return
    if not isinstance(owner_user, str):
      raise TypeError('owner_user must be of type str')
    self._owner_user = owner_user

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
  def total_views(self) -> int:
    return self._total_views

  @total_views.setter
  def total_views(self, total_views: int):
    if total_views is None:
      del self.total_views
      return
    if not isinstance(total_views, int):
      raise TypeError('total_views must be of type int')
    self._total_views = total_views

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
  def total_downloads(self) -> int:
    return self._total_downloads

  @total_downloads.setter
  def total_downloads(self, total_downloads: int):
    if total_downloads is None:
      del self.total_downloads
      return
    if not isinstance(total_downloads, int):
      raise TypeError('total_downloads must be of type int')
    self._total_downloads = total_downloads

  @property
  def title(self) -> str:
    r"""
    Copy/paste from DatasetSettings below. Can't use composition because
    that'd be a backwards-incompatible change for the Python Api.
    """
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
  def keywords(self) -> Optional[List[str]]:
    return self._keywords

  @keywords.setter
  def keywords(self, keywords: Optional[List[str]]):
    if keywords is None:
      del self.keywords
      return
    if not isinstance(keywords, list):
      raise TypeError('keywords must be of type list')
    if not all([isinstance(t, str) for t in keywords]):
      raise TypeError('keywords must contain only items of type str')
    self._keywords = keywords

  @property
  def licenses(self) -> Optional[List[Optional['SettingsLicense']]]:
    return self._licenses

  @licenses.setter
  def licenses(self, licenses: Optional[List[Optional['SettingsLicense']]]):
    if licenses is None:
      del self.licenses
      return
    if not isinstance(licenses, list):
      raise TypeError('licenses must be of type list')
    if not all([isinstance(t, SettingsLicense) for t in licenses]):
      raise TypeError('licenses must contain only items of type SettingsLicense')
    self._licenses = licenses

  @property
  def collaborators(self) -> Optional[List[Optional['DatasetCollaborator']]]:
    return self._collaborators

  @collaborators.setter
  def collaborators(self, collaborators: Optional[List[Optional['DatasetCollaborator']]]):
    if collaborators is None:
      del self.collaborators
      return
    if not isinstance(collaborators, list):
      raise TypeError('collaborators must be of type list')
    if not all([isinstance(t, DatasetCollaborator) for t in collaborators]):
      raise TypeError('collaborators must contain only items of type DatasetCollaborator')
    self._collaborators = collaborators

  @property
  def data(self) -> Optional[List[Optional['DatasetSettingsFile']]]:
    return self._data

  @data.setter
  def data(self, data: Optional[List[Optional['DatasetSettingsFile']]]):
    if data is None:
      del self.data
      return
    if not isinstance(data, list):
      raise TypeError('data must be of type list')
    if not all([isinstance(t, DatasetSettingsFile) for t in data]):
      raise TypeError('data must contain only items of type DatasetSettingsFile')
    self._data = data


class DatasetSettings(KaggleObject):
  r"""
  Attributes:
    title (str)
    subtitle (str)
    description (str)
    is_private (bool)
    keywords (str)
    licenses (SettingsLicense)
    collaborators (DatasetCollaborator)
    data (DatasetSettingsFile)
  """

  def __init__(self):
    self._title = None
    self._subtitle = None
    self._description = None
    self._is_private = False
    self._keywords = []
    self._licenses = []
    self._collaborators = []
    self._data = []
    self._freeze()

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
  def keywords(self) -> Optional[List[str]]:
    return self._keywords

  @keywords.setter
  def keywords(self, keywords: Optional[List[str]]):
    if keywords is None:
      del self.keywords
      return
    if not isinstance(keywords, list):
      raise TypeError('keywords must be of type list')
    if not all([isinstance(t, str) for t in keywords]):
      raise TypeError('keywords must contain only items of type str')
    self._keywords = keywords

  @property
  def licenses(self) -> Optional[List[Optional['SettingsLicense']]]:
    return self._licenses

  @licenses.setter
  def licenses(self, licenses: Optional[List[Optional['SettingsLicense']]]):
    if licenses is None:
      del self.licenses
      return
    if not isinstance(licenses, list):
      raise TypeError('licenses must be of type list')
    if not all([isinstance(t, SettingsLicense) for t in licenses]):
      raise TypeError('licenses must contain only items of type SettingsLicense')
    self._licenses = licenses

  @property
  def collaborators(self) -> Optional[List[Optional['DatasetCollaborator']]]:
    return self._collaborators

  @collaborators.setter
  def collaborators(self, collaborators: Optional[List[Optional['DatasetCollaborator']]]):
    if collaborators is None:
      del self.collaborators
      return
    if not isinstance(collaborators, list):
      raise TypeError('collaborators must be of type list')
    if not all([isinstance(t, DatasetCollaborator) for t in collaborators]):
      raise TypeError('collaborators must contain only items of type DatasetCollaborator')
    self._collaborators = collaborators

  @property
  def data(self) -> Optional[List[Optional['DatasetSettingsFile']]]:
    return self._data

  @data.setter
  def data(self, data: Optional[List[Optional['DatasetSettingsFile']]]):
    if data is None:
      del self.data
      return
    if not isinstance(data, list):
      raise TypeError('data must be of type list')
    if not all([isinstance(t, DatasetSettingsFile) for t in data]):
      raise TypeError('data must contain only items of type DatasetSettingsFile')
    self._data = data


class DatasetSettingsFile(KaggleObject):
  r"""
  Attributes:
    name (str)
    description (str)
    total_bytes (int)
    columns (DatasetSettingsFileColumn)
  """

  def __init__(self):
    self._name = ""
    self._description = None
    self._total_bytes = 0
    self._columns = []
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
  def columns(self) -> Optional[List[Optional['DatasetSettingsFileColumn']]]:
    return self._columns

  @columns.setter
  def columns(self, columns: Optional[List[Optional['DatasetSettingsFileColumn']]]):
    if columns is None:
      del self.columns
      return
    if not isinstance(columns, list):
      raise TypeError('columns must be of type list')
    if not all([isinstance(t, DatasetSettingsFileColumn) for t in columns]):
      raise TypeError('columns must contain only items of type DatasetSettingsFileColumn')
    self._columns = columns


class DatasetSettingsFileColumn(KaggleObject):
  r"""
  Attributes:
    name (str)
    description (str)
    type (str)
  """

  def __init__(self):
    self._name = ""
    self._description = None
    self._type = None
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


class SettingsLicense(KaggleObject):
  r"""
  Attributes:
    name (str)
  """

  def __init__(self):
    self._name = None
    self._freeze()

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


class DatasetCollaborator(KaggleObject):
  r"""
  Attributes:
    username (str)
    group_slug (str)
    role (CollaboratorType)
  """

  def __init__(self):
    self._username = None
    self._group_slug = None
    self._role = CollaboratorType.COLLABORATOR_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def username(self) -> str:
    return self._username or ""

  @username.setter
  def username(self, username: str):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    del self.group_slug
    self._username = username

  @property
  def group_slug(self) -> str:
    return self._group_slug or ""

  @group_slug.setter
  def group_slug(self, group_slug: str):
    if group_slug is None:
      del self.group_slug
      return
    if not isinstance(group_slug, str):
      raise TypeError('group_slug must be of type str')
    del self.username
    self._group_slug = group_slug

  @property
  def role(self) -> 'CollaboratorType':
    return self._role

  @role.setter
  def role(self, role: 'CollaboratorType'):
    if role is None:
      del self.role
      return
    if not isinstance(role, CollaboratorType):
      raise TypeError('role must be of type CollaboratorType')
    self._role = role


DatasetInfo._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("usabilityRating", "usability_rating", "_usability_rating", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalViews", "total_views", "_total_views", int, 0, PredefinedSerializer()),
  FieldMetadata("totalVotes", "total_votes", "_total_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("totalDownloads", "total_downloads", "_total_downloads", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("keywords", "keywords", "_keywords", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("licenses", "licenses", "_licenses", SettingsLicense, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("collaborators", "collaborators", "_collaborators", DatasetCollaborator, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("data", "data", "_data", DatasetSettingsFile, [], ListSerializer(KaggleObjectSerializer())),
]

DatasetSettings._fields = [
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("keywords", "keywords", "_keywords", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("licenses", "licenses", "_licenses", SettingsLicense, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("collaborators", "collaborators", "_collaborators", DatasetCollaborator, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("data", "data", "_data", DatasetSettingsFile, [], ListSerializer(KaggleObjectSerializer())),
]

DatasetSettingsFile._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalBytes", "total_bytes", "_total_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("columns", "columns", "_columns", DatasetSettingsFileColumn, [], ListSerializer(KaggleObjectSerializer())),
]

DatasetSettingsFileColumn._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", str, None, PredefinedSerializer(), optional=True),
]

SettingsLicense._fields = [
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
]

DatasetCollaborator._fields = [
  FieldMetadata("username", "username", "_username", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("role", "role", "_role", CollaboratorType, CollaboratorType.COLLABORATOR_TYPE_UNSPECIFIED, EnumSerializer()),
]

