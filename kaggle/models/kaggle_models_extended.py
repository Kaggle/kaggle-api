from datetime import datetime


class Competition:

  def __init__(self, init_dict):
    parsed_dict = {k: parse(v) for k, v in init_dict.items()}
    self.__dict__.update(parsed_dict)
    self.tags = [Tag(t) for t in self.tags]

  def __repr__(self):
    return self.ref


class SubmitResult:

  def __init__(self, init_dict):
    parsed_dict = {k: parse(v) for k, v in init_dict.items()}
    self.__dict__.update(parsed_dict)

  def __repr__(self):
    return self.message


class Submission:

  def __init__(self, init_dict):
    parsed_dict = {k: parse(v) for k, v in init_dict.items()}
    self.__dict__.update(parsed_dict)
    self.size = File.get_size(self.totalBytes)

  def __repr__(self):
    return str(self.ref)


class Dataset:

  def __init__(self, init_dict):
    parsed_dict = {k: parse(v) for k, v in init_dict.items()}
    self.__dict__.update(parsed_dict)
    self.tags = [Tag(t) for t in self.tags]
    self.files = [File(f) for f in self.files]
    self.versions = [DatasetVersion(v) for v in self.versions]
    self.size = File.get_size(self.totalBytes)

  def __repr__(self):
    return self.ref


class DatasetVersion:

  def __init__(self, init_dict):
    parsed_dict = {k: parse(v) for k, v in init_dict.items()}
    self.__dict__.update(parsed_dict)

  def __repr__(self):
    return str(self.version_number)


class File:

  def __init__(self, init_dict):
    parsed_dict = {k: parse(v) for k, v in init_dict.items()}
    self.__dict__.update(parsed_dict)
    self.size = File.get_size(self.totalBytes)

  def __repr__(self):
    return self.ref

  @staticmethod
  def get_size(size, precision=0):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    suffix_index = 0
    while size >= 1024 and suffix_index < 4:
      suffix_index += 1
      size /= 1024.0
    return '%.*f%s' % (precision, size, suffixes[suffix_index])


class Tag:

  def __init__(self, init_dict):
    parsed_dict = {k: parse(v) for k, v in init_dict.items()}
    self.__dict__.update(parsed_dict)

  def __repr__(self):
    return self.ref


class FileUploadInfo:

  def __init__(self, init_dict):
    parsed_dict = {k: parse(v) for k, v in init_dict.items()}
    self.__dict__.update(parsed_dict)

  def __repr__(self):
    return self.token


class DatasetNewVersionResponse:

  def __init__(self, init_dict):
    parsed_dict = {k: parse(v) for k, v in init_dict.items()}
    self.__dict__.update(parsed_dict)

  def __repr__(self):
    return self.url


class DatasetNewResponse:

  def __init__(self, init_dict):
    parsed_dict = {k: parse(v) for k, v in init_dict.items()}
    self.__dict__.update(parsed_dict)

  def __repr__(self):
    return self.url


def parse(string):
  time_formats = [
      '%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%dT%H:%M:%S.%f',
      '%Y-%m-%dT%H:%M:%S.%fZ'
  ]
  for t in time_formats:
    try:
      result = datetime.strptime(string[:26], t).replace(microsecond=0)
      return result
    except:
      pass
  return string
