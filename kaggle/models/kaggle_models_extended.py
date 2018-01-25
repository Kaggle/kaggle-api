from datetime import datetime

class Competition:
    def __init__(self, initDict):
      parsedDict = {k: parse(v) for k, v in initDict.items()}
      self.__dict__.update(parsedDict)
      self.tags = [Tag(t) for t in self.tags]
    def __repr__(self):
      return self.ref

class SubmitResult:
    def __init__(self, initDict):
      parsedDict = {k: parse(v) for k, v in initDict.items()}
      self.__dict__.update(parsedDict)
    def __repr__(self):
      return self.message

class Submission:
    def __init__(self, initDict):
      parsedDict = {k: parse(v) for k, v in initDict.items()}
      self.__dict__.update(parsedDict)
      self.size = File.getSize(self.totalBytes)
    def __repr__(self):
      return str(self.ref)

class Dataset:
    def __init__(self, initDict):
      parsedDict = {k: parse(v) for k, v in initDict.items()}
      self.__dict__.update(parsedDict)
      self.tags = [Tag(t) for t in self.tags]
      self.size = File.getSize(self.totalBytes)
    def __repr__(self):
      return self.ref

class File:
    def __init__(self, initDict):
      parsedDict = {k: parse(v) for k, v in initDict.items()}
      self.__dict__.update(parsedDict)
      self.size = File.getSize(self.totalBytes)
    def __repr__(self):
      return self.ref
    @staticmethod
    def getSize(size,precision=0):
        suffixes=['B','KB','MB','GB','TB']
        suffixIndex = 0
        while size >= 1024 and suffixIndex < 4:
            suffixIndex += 1
            size = size/1024.0
        return "%.*f%s"%(precision,size,suffixes[suffixIndex])

class Tag:
    def __init__(self, initDict):
      parsedDict = {k: parse(v) for k, v in initDict.items()}
      self.__dict__.update(parsedDict)
    def __repr__(self):
      return self.ref

def parse(string):
  timeFormats = ["%Y-%m-%dT%H:%M:%SZ","%Y-%m-%dT%H:%M:%S.%fZ"]
  for t in timeFormats:
    try:
      result = datetime.strptime(string, t).replace(microsecond=0)
      return result
    except: 
      pass
  return string
