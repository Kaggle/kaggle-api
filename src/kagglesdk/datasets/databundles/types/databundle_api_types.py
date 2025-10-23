from datetime import datetime
from kagglesdk.kaggle_object import *
from typing import List, Optional

class ApiColumnSummaryInfo(KaggleObject):
  r"""
  Attributes:
    total_column_count (int)
    column_types (ApiColumnTypeSummaryInfo)
  """

  def __init__(self):
    self._total_column_count = 0
    self._column_types = []
    self._freeze()

  @property
  def total_column_count(self) -> int:
    return self._total_column_count

  @total_column_count.setter
  def total_column_count(self, total_column_count: int):
    if total_column_count is None:
      del self.total_column_count
      return
    if not isinstance(total_column_count, int):
      raise TypeError('total_column_count must be of type int')
    self._total_column_count = total_column_count

  @property
  def column_types(self) -> Optional[List[Optional['ApiColumnTypeSummaryInfo']]]:
    return self._column_types

  @column_types.setter
  def column_types(self, column_types: Optional[List[Optional['ApiColumnTypeSummaryInfo']]]):
    if column_types is None:
      del self.column_types
      return
    if not isinstance(column_types, list):
      raise TypeError('column_types must be of type list')
    if not all([isinstance(t, ApiColumnTypeSummaryInfo) for t in column_types]):
      raise TypeError('column_types must contain only items of type ApiColumnTypeSummaryInfo')
    self._column_types = column_types


class ApiColumnTypeSummaryInfo(KaggleObject):
  r"""
  Attributes:
    column_type (str)
    column_count (int)
  """

  def __init__(self):
    self._column_type = None
    self._column_count = 0
    self._freeze()

  @property
  def column_type(self) -> str:
    return self._column_type or ""

  @column_type.setter
  def column_type(self, column_type: Optional[str]):
    if column_type is None:
      del self.column_type
      return
    if not isinstance(column_type, str):
      raise TypeError('column_type must be of type str')
    self._column_type = column_type

  @property
  def column_count(self) -> int:
    return self._column_count

  @column_count.setter
  def column_count(self, column_count: int):
    if column_count is None:
      del self.column_count
      return
    if not isinstance(column_count, int):
      raise TypeError('column_count must be of type int')
    self._column_count = column_count


class ApiDirectory(KaggleObject):
  r"""
  Attributes:
    name (str)
    relative_url (str)
    total_directories (int)
    total_files (int)
    total_children (int)
  """

  def __init__(self):
    self._name = None
    self._relative_url = None
    self._total_directories = 0
    self._total_files = 0
    self._total_children = 0
    self._freeze()

  @property
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def relative_url(self) -> str:
    return self._relative_url or ""

  @relative_url.setter
  def relative_url(self, relative_url: Optional[str]):
    if relative_url is None:
      del self.relative_url
      return
    if not isinstance(relative_url, str):
      raise TypeError('relative_url must be of type str')
    self._relative_url = relative_url

  @property
  def total_directories(self) -> int:
    return self._total_directories

  @total_directories.setter
  def total_directories(self, total_directories: int):
    if total_directories is None:
      del self.total_directories
      return
    if not isinstance(total_directories, int):
      raise TypeError('total_directories must be of type int')
    self._total_directories = total_directories

  @property
  def total_files(self) -> int:
    return self._total_files

  @total_files.setter
  def total_files(self, total_files: int):
    if total_files is None:
      del self.total_files
      return
    if not isinstance(total_files, int):
      raise TypeError('total_files must be of type int')
    self._total_files = total_files

  @property
  def total_children(self) -> int:
    return self._total_children

  @total_children.setter
  def total_children(self, total_children: int):
    if total_children is None:
      del self.total_children
      return
    if not isinstance(total_children, int):
      raise TypeError('total_children must be of type int')
    self._total_children = total_children


class ApiDirectoryContent(KaggleObject):
  r"""
  Attributes:
    directories (ApiDirectory)
    files (ApiFile)
    total_children (int)
    total_directories (int)
    total_files (int)
    next_page_token (str)
  """

  def __init__(self):
    self._directories = []
    self._files = []
    self._total_children = 0
    self._total_directories = 0
    self._total_files = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def directories(self) -> Optional[List[Optional['ApiDirectory']]]:
    return self._directories

  @directories.setter
  def directories(self, directories: Optional[List[Optional['ApiDirectory']]]):
    if directories is None:
      del self.directories
      return
    if not isinstance(directories, list):
      raise TypeError('directories must be of type list')
    if not all([isinstance(t, ApiDirectory) for t in directories]):
      raise TypeError('directories must contain only items of type ApiDirectory')
    self._directories = directories

  @property
  def files(self) -> Optional[List[Optional['ApiFile']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiFile) for t in files]):
      raise TypeError('files must contain only items of type ApiFile')
    self._files = files

  @property
  def total_children(self) -> int:
    return self._total_children

  @total_children.setter
  def total_children(self, total_children: int):
    if total_children is None:
      del self.total_children
      return
    if not isinstance(total_children, int):
      raise TypeError('total_children must be of type int')
    self._total_children = total_children

  @property
  def total_directories(self) -> int:
    return self._total_directories

  @total_directories.setter
  def total_directories(self, total_directories: int):
    if total_directories is None:
      del self.total_directories
      return
    if not isinstance(total_directories, int):
      raise TypeError('total_directories must be of type int')
    self._total_directories = total_directories

  @property
  def total_files(self) -> int:
    return self._total_files

  @total_files.setter
  def total_files(self, total_files: int):
    if total_files is None:
      del self.total_files
      return
    if not isinstance(total_files, int):
      raise TypeError('total_files must be of type int')
    self._total_files = total_files

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


class ApiFile(KaggleObject):
  r"""
  Attributes:
    name (str)
    creation_date (datetime)
    total_bytes (int)
    relative_url (str)
    description (str)
  """

  def __init__(self):
    self._name = None
    self._creation_date = None
    self._total_bytes = 0
    self._relative_url = None
    self._description = None
    self._freeze()

  @property
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
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
  def relative_url(self) -> str:
    return self._relative_url or ""

  @relative_url.setter
  def relative_url(self, relative_url: Optional[str]):
    if relative_url is None:
      del self.relative_url
      return
    if not isinstance(relative_url, str):
      raise TypeError('relative_url must be of type str')
    self._relative_url = relative_url

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description


class ApiFileExtensionSummaryInfo(KaggleObject):
  r"""
  Attributes:
    extension (str)
    file_count (int)
    total_size (int)
  """

  def __init__(self):
    self._extension = ""
    self._file_count = 0
    self._total_size = 0
    self._freeze()

  @property
  def extension(self) -> str:
    return self._extension

  @extension.setter
  def extension(self, extension: str):
    if extension is None:
      del self.extension
      return
    if not isinstance(extension, str):
      raise TypeError('extension must be of type str')
    self._extension = extension

  @property
  def file_count(self) -> int:
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
  def total_size(self) -> int:
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size


class ApiFilesSummary(KaggleObject):
  r"""
  Attributes:
    file_summary_info (ApiFileSummaryInfo)
    column_summary_info (ApiColumnSummaryInfo)
  """

  def __init__(self):
    self._file_summary_info = None
    self._column_summary_info = None
    self._freeze()

  @property
  def file_summary_info(self) -> Optional['ApiFileSummaryInfo']:
    return self._file_summary_info

  @file_summary_info.setter
  def file_summary_info(self, file_summary_info: Optional['ApiFileSummaryInfo']):
    if file_summary_info is None:
      del self.file_summary_info
      return
    if not isinstance(file_summary_info, ApiFileSummaryInfo):
      raise TypeError('file_summary_info must be of type ApiFileSummaryInfo')
    self._file_summary_info = file_summary_info

  @property
  def column_summary_info(self) -> Optional['ApiColumnSummaryInfo']:
    return self._column_summary_info

  @column_summary_info.setter
  def column_summary_info(self, column_summary_info: Optional['ApiColumnSummaryInfo']):
    if column_summary_info is None:
      del self.column_summary_info
      return
    if not isinstance(column_summary_info, ApiColumnSummaryInfo):
      raise TypeError('column_summary_info must be of type ApiColumnSummaryInfo')
    self._column_summary_info = column_summary_info


class ApiFileSummaryInfo(KaggleObject):
  r"""
  Attributes:
    total_file_count (int)
    file_types (ApiFileExtensionSummaryInfo)
  """

  def __init__(self):
    self._total_file_count = 0
    self._file_types = []
    self._freeze()

  @property
  def total_file_count(self) -> int:
    return self._total_file_count

  @total_file_count.setter
  def total_file_count(self, total_file_count: int):
    if total_file_count is None:
      del self.total_file_count
      return
    if not isinstance(total_file_count, int):
      raise TypeError('total_file_count must be of type int')
    self._total_file_count = total_file_count

  @property
  def file_types(self) -> Optional[List[Optional['ApiFileExtensionSummaryInfo']]]:
    return self._file_types

  @file_types.setter
  def file_types(self, file_types: Optional[List[Optional['ApiFileExtensionSummaryInfo']]]):
    if file_types is None:
      del self.file_types
      return
    if not isinstance(file_types, list):
      raise TypeError('file_types must be of type list')
    if not all([isinstance(t, ApiFileExtensionSummaryInfo) for t in file_types]):
      raise TypeError('file_types must contain only items of type ApiFileExtensionSummaryInfo')
    self._file_types = file_types


ApiColumnSummaryInfo._fields = [
  FieldMetadata("totalColumnCount", "total_column_count", "_total_column_count", int, 0, PredefinedSerializer()),
  FieldMetadata("columnTypes", "column_types", "_column_types", ApiColumnTypeSummaryInfo, [], ListSerializer(KaggleObjectSerializer())),
]

ApiColumnTypeSummaryInfo._fields = [
  FieldMetadata("columnType", "column_type", "_column_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("columnCount", "column_count", "_column_count", int, 0, PredefinedSerializer()),
]

ApiDirectory._fields = [
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("relativeUrl", "relative_url", "_relative_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalDirectories", "total_directories", "_total_directories", int, 0, PredefinedSerializer()),
  FieldMetadata("totalFiles", "total_files", "_total_files", int, 0, PredefinedSerializer()),
  FieldMetadata("totalChildren", "total_children", "_total_children", int, 0, PredefinedSerializer()),
]

ApiDirectoryContent._fields = [
  FieldMetadata("directories", "directories", "_directories", ApiDirectory, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("files", "files", "_files", ApiFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalChildren", "total_children", "_total_children", int, 0, PredefinedSerializer()),
  FieldMetadata("totalDirectories", "total_directories", "_total_directories", int, 0, PredefinedSerializer()),
  FieldMetadata("totalFiles", "total_files", "_total_files", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ApiFile._fields = [
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creationDate", "creation_date", "_creation_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("totalBytes", "total_bytes", "_total_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("relativeUrl", "relative_url", "_relative_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
]

ApiFileExtensionSummaryInfo._fields = [
  FieldMetadata("extension", "extension", "_extension", str, "", PredefinedSerializer()),
  FieldMetadata("fileCount", "file_count", "_file_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
]

ApiFilesSummary._fields = [
  FieldMetadata("fileSummaryInfo", "file_summary_info", "_file_summary_info", ApiFileSummaryInfo, None, KaggleObjectSerializer()),
  FieldMetadata("columnSummaryInfo", "column_summary_info", "_column_summary_info", ApiColumnSummaryInfo, None, KaggleObjectSerializer()),
]

ApiFileSummaryInfo._fields = [
  FieldMetadata("totalFileCount", "total_file_count", "_total_file_count", int, 0, PredefinedSerializer()),
  FieldMetadata("fileTypes", "file_types", "_file_types", ApiFileExtensionSummaryInfo, [], ListSerializer(KaggleObjectSerializer())),
]

