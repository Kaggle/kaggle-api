from __future__ import print_function
from .kaggle_api import KaggleApi
from ..api_client import ApiClient
from ..models.kaggle_models_extended import Competition, SubmitResult, Submission, Dataset, File, FileUploadInfo, DatasetNewVersionResponse, DatasetNewResponse
from ..models.dataset_new_version_request import DatasetNewVersionRequest
from ..models.dataset_new_request import DatasetNewRequest
from ..models.dataset_upload_file import DatasetUploadFile
from kaggle.configuration import Configuration
import os, json, sys, csv, zipfile, urllib3
from os.path import expanduser, isfile
from datetime import datetime

try:
    unicode        # Python 2
except NameError:
    unicode = str  # Python 3


class KaggleApi(KaggleApi):
    __version__ = "1.1.0"

    CONFIG_NAME_PROXY = "proxy"
    CONFIG_NAME_COMPETITION = "competition"
    CONFIG_NAME_PATH = "path"
    CONFIG_NAME_USER = "username"
    CONFIG_NAME_KEY = "key"
    
    HEADER_API_VERSION = "X-Kaggle-ApiVersion"
    METADATA_FILE = "datapackage.json"
    
    configPath = os.path.join(expanduser("~"),".kaggle")
    if not os.path.exists(configPath):
      os.makedirs(configPath)
    configFile = 'kaggle.json'
    config = os.path.join(configPath, configFile)
    configValues = {}
    alreadyPrintedVersionWarning = False

    def authenticate(self):
      try:
        configuration = Configuration()
        if os.name != 'nt':
          permissions = os.stat(self.config).st_mode
          if (permissions & 4) or (permissions & 32):
            print("Warning: Your Kaggle API key is readable by other users on this system! To fix this, you can run 'chmod 600 {}'".format(self.config))
        with open(self.config, 'r') as f:
          configData = json.load(f)

        self.copyConfigValue(self.CONFIG_NAME_PROXY, configData)
        self.copyConfigValue(self.CONFIG_NAME_PATH, configData)
        self.copyConfigValue(self.CONFIG_NAME_COMPETITION, configData)
        self.copyConfigValue(self.CONFIG_NAME_USER, configData)

        configuration.username = configData[self.CONFIG_NAME_USER]
        configuration.password = configData[self.CONFIG_NAME_KEY]
        if self.CONFIG_NAME_PROXY in configData:
          configuration.proxy = configData[self.CONFIG_NAME_PROXY]
        self.api_client = ApiClient(configuration)

      except Exception as error:
        if 'Proxy' in type(error).__name__:
          sys.exit('The specified proxy ' + configData[self.CONFIG_NAME_PROXY] + ' is not valid, please check your proxy settings')
        else:
          sys.exit('Unauthorized: you must download an API key from https://www.kaggle.com/<username>/account\nThen put ' + self.configFile + ' in the folder ' + self.configPath)


    def setConfigValue(self, name, value, quiet = False):
      try: 
        with open(self.config, 'r') as f:
          configData = json.load(f)
        if value is not None:
          configData[name] = value
          with open(self.config, 'w') as f:
            json.dump(configData, f)
        if name in configData:
          self.configValues[name] = configData[name]
      except:
        pass
      if not quiet:
        self.printConfigValue(name, separator = ' is now set to: ')


    def unsetConfigValue(self, name, quiet = False):
      try: 
        with open(self.config, 'r') as f:
          configData = json.load(f)
        configData[name] = None
        with open(self.config, 'w') as f:
          json.dump(configData, f)
        self.configValues[name] = None
      except:
        pass
      if not quiet:
        self.printConfigValue(name, separator = ' is now set to: ')


    def copyConfigValue(self, name, values):
      if name in values:
        self.configValues[name] = values[name]


    def getConfigValue(self, name):
      if name in self.configValues:
        return self.configValues[name]
      return None


    def getConfigPath(self):
      path = self.getConfigValue(self.CONFIG_NAME_PATH)
      if path is None:
        return self.configPath
      return path


    def printConfigValue(self, name, prefix = '', separator = ': '):
      valueOut = 'None'
      if name in self.configValues and self.configValues[name] is not None: 
        valueOut = self.configValues[name]
      print(prefix + name + separator + valueOut)


    def printConfigValues(self):
      print("Configuration values from " + self.getConfigPath())
      self.printConfigValue(self.CONFIG_NAME_USER, prefix = '- ')
      self.printConfigValue(self.CONFIG_NAME_PATH, prefix = '- ')
      self.printConfigValue(self.CONFIG_NAME_PROXY, prefix = '- ')
      self.printConfigValue(self.CONFIG_NAME_COMPETITION, prefix = '- ')
          
      
    def competitionsList(self, page = 1, search = ''):
      if search is None:
        search = ''
      competitionsListResult = self.process_response(self.competitions_list_with_http_info(page = page, search = search))
      return [Competition(c) for c in competitionsListResult]


    def competitionsListCli(self, page = 1, search = '', csv = False):
      competitions = self.competitionsList(page, search)
      fields = ['ref', 'deadline', 'category', 'reward', 'teamCount', 'userHasEntered']
      if competitions:
        if csv:
           self.printCsv(competitions, fields)
        else:
           self.printTable(competitions, fields)
      else:
        print('No competitions found')


    def competitionSubmit(self, file, message, competition, quiet = False):
      if (competition is None):
        competition = self.getConfigValue(self.CONFIG_NAME_COMPETITION)
        if (competition is not None and not quiet):
          print('Using competition: ' + competition)

      if (competition is None):
        sys.exit('No competition specified')
      else: 
        urlResult = self.process_response(self.competitions_submissions_url_with_http_info(file_name = os.path.basename(file), content_length = os.path.getsize(file), last_modified_date_utc = int(os.path.getmtime(file) * 1000)))
        urlResultList = urlResult['createUrl'].split('/')
        uploadResult = self.process_response(self.competitions_submissions_upload_with_http_info(file = file, guid = urlResultList[-3], content_length = urlResultList[-2], last_modified_date_utc = urlResultList[-1]))
        uploadResultToken = uploadResult['token']
        submitResult = self.process_response(self.competitions_submissions_submit_with_http_info(id = competition, blob_file_tokens = uploadResultToken, submission_description = message))
        return SubmitResult(submitResult)


    def competitionSubmissions(self, competition):
      submissionsResult = self.process_response(self.competitions_submissions_list_with_http_info(id = competition))
      return [Submission(s) for s in submissionsResult]

    
    def competitionSubmissionsCli(self, competition = None, csv = False, quiet = False):
      if (competition is None):
        competition = self.getConfigValue(self.CONFIG_NAME_COMPETITION)
        if (competition is not None and not quiet):
          print('Using competition: ' + competition)

      if (competition is None):
        sys.exit('No competition specified')
      else: 
        submissions = self.competitionSubmissions(competition)
        fields = ['fileName', 'date', 'description', 'status', 'publicScore', 'privateScore']
        if submissions:
          if csv:
            self.printCsv(submissions, fields)
          else:
            self.printTable(submissions, fields)
        else:
          print('No submissions found')


    def competitionListFiles(self, competition):
      competitionListFilesResult = self.process_response(self.competitions_data_list_files_with_http_info(id = competition))
      return [File(f) for f in competitionListFilesResult]


    def competitionListFilesCli(self, competition, csv = False, quiet = False):
      if (competition is None):
        competition = self.getConfigValue(self.CONFIG_NAME_COMPETITION)
        if (competition is not None and not quiet):
          print('Using competition: ' + competition)

      if (competition is None):
        sys.exit('No competition specified')
      else: 
        files = self.competitionListFiles(competition)
        fields = ['name', 'size', 'creationDate']
        if files:
          if csv:
            self.printCsv(files, fields)
          else:
            self.printTable(files, fields)
        else:
          print('No files found')


    def competitionDownloadFile(self, competition, file, path = None, force = False, quiet = False):
      if path is None:
        effective_path = os.path.join(self.getConfigPath(), 'competitions', competition)
      else:
        effective_path = path
      
      response = self.process_response(self.competitions_data_download_file_with_http_info(id = competition, file_name = file, _preload_content = False))
      url = response.retries.history[0].redirect_location.split('?')[0]
      outfile = os.path.join(effective_path, url.split('/')[-1])
      
      if force or self.downloadNeeded(response, outfile, quiet):
        self.downloadFile(response, outfile, quiet)


    def competitionDownloadFiles(self, competition, path = None, force = False, quiet = True):
      files = self.competitionListFiles(competition)
      for file in files:
        self.competitionDownloadFile(competition, file.ref, path, force, quiet)


    def competitionDownloadCli(self, competition, file = None, path = None, force = False, quiet = False):
      if (competition is None):
        competition = self.getConfigValue(self.CONFIG_NAME_COMPETITION)
        if (competition is not None and not quiet):
          print('Using competition: ' + competition)

      if (competition is None):
        sys.exit('No competition specified')
      else: 
        if file is None:
          self.competitionDownloadFiles(competition, path, force, quiet)
        else:
          self.competitionDownloadFile(competition, file, path, force, quiet)


    def datasetsList(self, page = 1, search = ''):
      if search is None:
        search = ''
      datasetsListResult = self.process_response(self.datasets_list_with_http_info(page = page, search = search))
      return [Dataset(d) for d in datasetsListResult]


    def datasetsListCli(self, page = 1, search = '', csv = False):
      datasets = self.datasetsList(page, search)
      fields = ['ref', 'title', 'size', 'lastUpdated', 'downloadCount']
      if datasets:
        if csv:
          self.printCsv(datasets, fields)
        else:
          self.printTable(datasets, fields)
      else:
        print('No datasets found')


    def datasetListFiles(self, dataset):
      datasetUrlList = dataset.split('/')
      ownerSlug = datasetUrlList[0]
      datasetSlug = datasetUrlList[1]
      datasetListFilesResult = self.process_response(self.datasets_list_files_with_http_info(owner_slug = ownerSlug, dataset_slug = datasetSlug))
      return [File(f) for f in datasetListFilesResult]


    def datasetListFilesCli(self, dataset, csv = False):
      files = self.datasetListFiles(dataset)
      fields = ['name', 'size', 'creationDate']
      if files:
        if csv:
          self.printCsv(files, fields)
        else:
          self.printTable(files, fields)
      else:
        print('No files found')


    def datasetDownloadFile(self, dataset, file, path = None, force = False, quiet = True):
      datasetUrlList = dataset.split('/')
      ownerSlug = datasetUrlList[0]
      datasetSlug = datasetUrlList[1]
      
      if path is None:
        effective_path = os.path.join(self.getConfigPath(), 'datasets', ownerSlug, datasetSlug)
      else:
        effective_path = path

      response = self.process_response(self.datasets_download_file_with_http_info(owner_slug = ownerSlug, dataset_slug = datasetSlug, file_name = file, _preload_content = False))
      url = response.retries.history[0].redirect_location.split('?')[0]
      outfile = os.path.join(effective_path, url.split('/')[-1])
      if force or self.downloadNeeded(response, outfile, quiet):
        self.downloadFile(response, outfile, quiet)
        return True
      else:
        return False


    def datasetDownloadFiles(self, dataset, path = None, force = False, quiet = True):
      datasetUrlList = dataset.split('/')
      ownerSlug = datasetUrlList[0]
      datasetSlug = datasetUrlList[1]
      
      if path is None:
        effective_path = os.path.join(self.getConfigPath(), 'datasets', ownerSlug, datasetSlug)
      else:
        effective_path = path

      downloaded = self.datasetDownloadFile(dataset, datasetSlug + '.zip', path, force, quiet)
      if downloaded:
        outfile = os.path.join(effective_path, datasetSlug + '.zip')
        with zipfile.ZipFile(outfile, 'r') as z:
          z.extractall(effective_path)


    def datasetDownloadCli(self, dataset, file = None, path = None, force = False, quiet = False):
      if file is None:
        self.datasetDownloadFiles(dataset, path, force, quiet)
      else:
        self.datasetDownloadFile(dataset, file, path, force, quiet)


    def datasetUploadFile(self, file):
      file_name = os.path.basename(file)
      content_length = os.path.getsize(file)
      last_modified_date_utc = int(os.path.getmtime(file))
      result = FileUploadInfo(self.process_response(self.datasets_upload_file_with_http_info(file_name, content_length, last_modified_date_utc)))

      success = self.upload_complete(file, result.createUrl)
      
      if success: 
        return result.token
      return None

    def datasetCreateVersion(self, folder,version_notes, quiet = False):
      if not os.path.isdir(folder):
        sys.exit("Invalid folder: " + folder)

      meta_file = os.path.join(folder, self.METADATA_FILE)
      if not os.path.isfile(meta_file):
        sys.exit("Metadata file not found: " + self.METADATA_FILE)
        return

      # read json
      with open(meta_file, 'r') as f:
        meta_data = json.load(f)
      ref = self.get_or_exit(meta_data, "id")
      ref_list = ref.split('/')
      owner_slug = ref_list[0]
      dataset_slug = ref_list[1]

      # validations
      if ref == self.configValues[self.CONFIG_NAME_USER] + "/INSERT_SLUG_HERE":
        sys.exit("Default slug detected, please change values before uploading")

      request = DatasetNewVersionRequest(version_notes, [])

      for file in os.listdir(folder):
        full_path = os.path.join(folder, file)
        
        if file == self.METADATA_FILE:
          continue

        if os.path.isfile(full_path):
          content_length = os.path.getsize(full_path)
          token = self.datasetUploadFile(full_path)
          if token is None:
            print("Upload unsuccessful: " + file)
            return
          
          if not quiet:
            print("Upload successful: " + file + " (" + File.getSize(content_length) + ")")
          
          upload_file = DatasetUploadFile()
          upload_file.token = token
          request.files.append(upload_file)
        else: 
          if not quiet:
            print("Skipping: " + file)

      result = DatasetNewVersionResponse(self.process_response(self.datasets_create_version_with_http_info(owner_slug, dataset_slug, request)))
      return result


    def datasetCreateVersionCli(self, folder, version_notes, quiet = False):
      result = self.datasetCreateVersion(folder, version_notes, quiet)
      
      if result is None:
        print("Dataset version creation error: See previous output")
      elif result.status == 'ok':
        print("Dataset version is being created. Please check progress at " + result.url)
      else:
        print("Dataset version creation error: " + result.error)


    def datasetInitialize(self, folder):
      if not os.path.isdir(folder):
        sys.exit("Invalid folder: " + folder)

      ref = self.configValues[self.CONFIG_NAME_USER] + "/INSERT_SLUG_HERE"
      licenses = []
      license = {}
      license["name"] = "CC0-1.0"
      licenses.append(license)
      
      meta_data = {}
      meta_data["title"] = "INSERT_TITLE_HERE"
      meta_data["id"] = ref
      meta_data["licenses"] = licenses
      meta_file = os.path.join(folder, self.METADATA_FILE)
      with open(meta_file, 'w') as f:
        json.dump(meta_data, f)

      print("Data package template written to: " + meta_file)


    def datasetCreateNew(self, folder, public = False, quiet = False):
      if not os.path.isdir(folder):
        sys.exit("Invalid folder: " + folder)

      meta_file = os.path.join(folder, self.METADATA_FILE)
      if not os.path.isfile(meta_file):
        sys.exit("Metadata file not found: " + self.METADATA_FILE)
        return

      # read json
      with open(meta_file, 'r') as f:
        meta_data = json.load(f)
      ref = self.get_or_exit(meta_data, "id")
      title = self.get_or_exit(meta_data, "title")
      licenses = self.get_or_exit(meta_data, "licenses")
      ref_list = ref.split('/')
      owner_slug = ref_list[0]
      dataset_slug = ref_list[1]

      # validations
      if ref == self.configValues[self.CONFIG_NAME_USER] + "/INSERT_SLUG_HERE":
        sys.exit("Default slug detected, please change values before uploading")
      if title == "INSERT_TITLE_HERE":
        sys.exit("Default title detected, please change values before uploading")
      if len(licenses) != 1:
        sys.exit("Please specify exactly one license")

      licenseName = self.get_or_exit(licenses[0], "name")

      request = DatasetNewRequest(title, dataset_slug, owner_slug, licenseName, [], not public)

      for file in os.listdir(folder):
        if file == self.METADATA_FILE:
          continue
        full_path = os.path.join(folder, file)

        if os.path.isfile(full_path):
          content_length = os.path.getsize(full_path)
          token = self.datasetUploadFile(full_path)
          if token is None:
            print("Upload unsuccessful: " + file)
            return
          
          if not quiet:
            print("Upload successful: " + file + " (" + File.getSize(content_length) + ")")
          
          upload_file = DatasetUploadFile()
          upload_file.token = token
          request.files.append(upload_file)
        else: 
          if not quiet:
            print("Skipping: " + file)

      result = DatasetNewResponse(self.process_response(self.datasets_create_new_with_http_info(request)))
      return result


    def datasetCreateNewCli(self, folder, public = False, quiet = False):
      result = self.datasetCreateNew(folder, public, quiet)
      if result.status == 'ok':
        if public:
          print("Your public Dataset is being created. Please check progress at " + result.url)
        else:
          print("Your private Dataset is being created. Please check progress at " + result.url)
      else:
        print("Dataset creation error: " + result.error)


    def downloadFile(self, response, outfile, quiet = True, chunkSize = 1048576):
      outpath = os.path.dirname(outfile)
      if not os.path.exists(outpath):
        os.makedirs(outpath)
      size = int(response.headers['Content-Length'])
      sizeRead = 0
      with open(outfile, 'wb') as out:
        while True:
          data = response.read(chunkSize)
          if not data:
            break
          out.write(data)
          sizeRead = min(size, sizeRead + chunkSize) 
          if not quiet:
            print(os.path.basename(outfile) + ': Downloaded ' + File.getSize(sizeRead) + ' of ' + File.getSize(size), end = '\r')
      if not quiet:
        print('\n', end = '')


    def downloadNeeded(self, response, outfile, quiet = True):
      try:
        remoteDate = datetime.strptime(response.headers['Last-Modified'], "%a, %d %b %Y %X %Z")
        if isfile(outfile):
          localDate = datetime.fromtimestamp(os.path.getmtime(outfile))
          if remoteDate <= localDate:
            if not quiet:
              print(os.path.basename(outfile) + ': Skipping, found more recently modified local copy (use --force to force download)')
            return False
      except:
         pass
      return True


    def printTable(self, items, fields):
      formats = []
      borders = []
      for f in fields:
        length = max(len(f),max([len(self.string(getattr(i,f))) for i in items]))
        justify = '>' if isinstance(getattr(items[0],f), int) or f == 'size' or f == 'reward' else '<'
        formats.append('{:' + justify + self.string(length + 2) + '}')
        borders.append('-' * length + '  ')
      row_format = u''.join(formats)
      headers = [f + '  ' for f in fields]
      print(row_format.format(*headers))
      print(row_format.format(*borders))
      for i in items:
        i_fields = [self.string(getattr(i,f)) + '  ' for f in fields]
        print(row_format.format(*i_fields))


    def printCsv(self, items, fields):
      writer = csv.writer(sys.stdout)
      writer.writerow(fields)
      for i in items:
        i_fields = [self.string(getattr(i,f)) for f in fields]
        writer.writerow(i_fields)


    def string(self, item):
      return item if isinstance(item, unicode) else str(item)


    def get_or_exit(self, data, key):
      if key in data:
        return data[key]
      sys.exit("Key " + key + " not found in data")


    def process_response(self, result):
      if len(result) == 3:
        data = result[0]
        code = result[1]
        headers = result[2]
        if self.HEADER_API_VERSION in headers:
          api_version = headers[self.HEADER_API_VERSION]
          if not self.alreadyPrintedVersionWarning and self.__version__ < api_version: 
            print("Warning: Looks like you're using an outdated API Version, please consider updating (server " + api_version + " / client " + self.__version__ + ")")
            self.alreadyPrintedVersionWarning = True
        return data
      return result


    def upload_complete(self, file, url):
      urllib3.disable_warnings()
      proxyUrl = self.getConfigValue(self.CONFIG_NAME_PROXY)
      if proxyUrl is None:
        http = urllib3.PoolManager()
      else:
        http = urllib3.ProxyManager(proxyUrl)

      content_length = os.path.getsize(file)
      with open(file, 'rb') as fp:
        data = fp.read()
        try: 
          response = http.request('PUT', url, body=data)
        except Exception as error:
          print(error)
          return False
      return True
      

    def dataset_data(self, dataset, file_path = None, force = False, quiet = True):
      datasetUrlList = dataset.split('/')
      ownerSlug = datasetUrlList[0]
      datasetSlug = datasetUrlList[1]
      effective_path = os.path.join(self.getConfigPath(), 'datasets', ownerSlug, datasetSlug)

      # complete folders
      if file_path is None:
        if os.path.exists(effective_path) and not force:
          return effective_path

        if not quiet:
          print("Downloading Dataset " + dataset + "...")
        self.datasetDownloadFiles(dataset, path=None, force=force, quiet=quiet)
        return effective_path

      # individual files
      effective_path = os.path.join(effective_path, file_path)
      if os.path.exists(effective_path) and not force:
        return effective_path

      if not quiet:
        print("Downloading file " + file_path + " from Dataset " + dataset)

      self.datasetDownloadFile(dataset, file_path, path=None, force=force, quiet=quiet)
      return effective_path


    def competition_data(self, competition, file_path = None, force = False, quiet = True):
      effective_path = os.path.join(self.getConfigPath(), 'competitions', competition)

      # complete folders
      if file_path is None:
        if os.path.exists(effective_path) and not force:
          return effective_path

        if not quiet:
          print("Downloading Competition " + competition + "...")
        self.competitionDownloadFiles(competition, path=None, force=force, quiet=quiet)
        return effective_path

      # individual files
      effective_path = os.path.join(effective_path, file_path)
      if os.path.exists(effective_path) and not force:
        return effective_path

      if not quiet:
        print("Downloading file " + file_path + " from Competition " + competition)

      self.competitionDownloadFile(competition, file_path, path=None, force=force, quiet=quiet)
      return effective_path


    def upload_in_chunks(self, file, url, chunk_size = 1048576):
      urllib3.disable_warnings()
      proxyUrl = self.getConfigValue(self.CONFIG_NAME_PROXY)
      if proxyUrl is None:
        http = urllib3.PoolManager()
      else:
        http = urllib3.ProxyManager(proxyUrl)

      file_name = os.path.basename(file)
      content_length = os.path.getsize(file)
      index = 0
      offset = 0
      headers = {}
      with open(file, 'rb') as fp:
        for chunk in self.read_in_chunks(fp, chunk_size=chunk_size):

          offset = index + len(chunk)
          headers['Content-Length'] = content_length
          headers['Content-Range'] = 'bytes %s-%s/%s' % (index, offset, content_length)
          index = offset
          try:
            response = http.request('PUT', url, body=chunk, headers=headers)
            print(file_name + ': Uploaded ' + File.getSize(index) + ' of ' + File.getSize(content_length))

          except Exception as error:
            print(error)
            return False
      return True


    def read_in_chunks(self, file_object, chunk_size):
      while True:
        data = file_object.read(chunk_size)
        if not data:
          break
        yield data
