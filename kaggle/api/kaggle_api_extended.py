from __future__ import print_function
from .kaggle_api import KaggleApi
from ..models.kaggle_models_extended import Competition, SubmitResult, Submission, Dataset, File
from kaggle.configuration import Configuration
import os, json, sys, csv, zipfile
from os.path import expanduser, isfile
from datetime import datetime


class KaggleApi(KaggleApi):
    configPath = os.path.join(expanduser("~"),".kaggle")
    if not os.path.exists(configPath):
      os.makedirs(configPath)
    configFile = 'kaggle.json'
    config = os.path.join(configPath, configFile)
    path = configPath

    def authenticate(self):
      try:
        configuration = Configuration()
        if os.name != 'nt':
          permissions = os.stat(self.config).st_mode
          if (permissions & 4) or (permissions & 32):
            print("Warning: Your Kaggle API key is readable by other users on this system! To fix this, you can run 'chmod 600 {}'".format(self.config))
        with open(self.config, 'r') as f:
          configData = json.load(f)
        configuration.username = configData['username']
        configuration.password = configData['key']
        self.api_client.configuration = configuration
      except: 
        sys.exit('Unauthorized: you must download an API key from https://www.kaggle.com/<username>/account\nThen put ' + self.configFile + ' in the folder ' + self.configPath)

    def downloadPath(self, path = None, quiet = False):
      try: 
        with open(self.config, 'r') as f:
          configData = json.load(f)
        if path is not None:
          configData['path'] = path
          with open(self.config, 'w') as f:
            json.dump(configData, f)
        if 'path' in configData:
          self.path = configData['path']
      except:
        pass
      if not quiet:
        print('Your files will be downloaded to ' + self.path)
   
    def competitionsList(self, page = 1, search = ''):
      if search is None:
        search = ''
      competitionsListResult = self.competitions_list(page = page, search = search)
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

    def competitionSubmit(self, file, message, competition):
      urlResult = self.competitions_submissions_url(file_name = os.path.basename(file), content_length = os.path.getsize(file), last_modified_date_utc = int(os.path.getmtime(file) * 1000))
      urlResultList = urlResult['createUrl'].split('/')
      uploadResult = self.competitions_submissions_upload(file = file, guid = urlResultList[-3], content_length = urlResultList[-2], last_modified_date_utc = urlResultList[-1])
      uploadResultToken = uploadResult['token']
      submitResult = self.competitions_submissions_submit(id = competition, blob_file_tokens = uploadResultToken, submission_description = message)
      return SubmitResult(submitResult)

    def competitionSubmissions(self, competition):
      submissionsResult = self.competitions_submissions_list(id = competition)
      return [Submission(s) for s in submissionsResult]

    
    def competitionSubmissionsCli(self, competition, csv = False):
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
      competitionListFilesResult = self.competitions_data_list_files(id = competition)
      return [File(f) for f in competitionListFilesResult]

    def competitionListFilesCli(self, competition, csv = False):
      files = self.competitionListFiles(competition)
      fields = ['name', 'size', 'creationDate']
      if files:
        if csv:
          self.printCsv(fiels, fields)
        else:
          self.printTable(files, fields)
      else:
        print('No files found')

    def competitionDownloadFile(self, competition, file, path = None, force = False, quiet = True):
      if path is None:
        path = os.path.join(self.path, 'competitions')
      response = self.competitions_data_download_file(id = competition, file_name = file, _preload_content = False)
      url = response.retries.history[0].redirect_location.split('?')[0]
      outfile = os.path.join(path, competition, url.split('/')[-1])
      if force or self.downloadNeeded(response, outfile, quiet):
        self.downloadFile(response, outfile, quiet)

    def competitionDownloadFiles(self, competition, path = None, force = False, quiet = True):
      files = self.competitionListFiles(competition)
      for file in files:
        self.competitionDownloadFile(competition, file.ref, path, force, quiet)

    def competitionDownloadCli(self, competition, file = None, path = None, force = False, quiet = False):
      if file is None:
        self.competitionDownloadFiles(competition, path, force, quiet)
      else:
        self.competitionDownloadFile(competition, file, path, force, quiet)

    def datasetsList(self, page = 1, search = ''):
      if search is None:
        search = ''
      datasetsListResult = self.datasets_list(page = page, search = search)
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
      datasetListFilesResult = self.datasets_list_files(owner_slug = ownerSlug, dataset_slug = datasetSlug)
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
      if path is None:
        path = os.path.join(self.path, 'datasets')
      datasetUrlList = dataset.split('/')
      ownerSlug = datasetUrlList[0]
      datasetSlug = datasetUrlList[1]
      response = self.datasets_download_file(owner_slug = ownerSlug, dataset_slug = datasetSlug, file_name = file, _preload_content = False)
      url = response.retries.history[0].redirect_location.split('?')[0]
      outfile = os.path.join(path, ownerSlug, datasetSlug, url.split('/')[-1])
      if force or self.downloadNeeded(response, outfile, quiet):
        self.downloadFile(response, outfile, quiet)
        return True
      else:
        return False

    def datasetDownloadFiles(self, dataset, path = None, force = False, quiet = True):
      if path is None:
        path = os.path.join(self.path, 'datasets')
      datasetUrlList = dataset.split('/')
      ownerSlug = datasetUrlList[0]
      datasetSlug = datasetUrlList[1]
      downloaded = self.datasetDownloadFile(dataset, datasetSlug + '.zip', path, force, quiet)
      if downloaded:
        outpath = os.path.join(path, ownerSlug, datasetSlug)
        outfile = os.path.join(outpath, datasetSlug + '.zip')
        with zipfile.ZipFile(outfile, 'r') as z:
          z.extractall(outpath)

    def datasetDownloadCli(self, dataset, file = None, path = None, force = False, quiet = False):
      if file is None:
        self.datasetDownloadFiles(dataset, path, force, quiet)
      else:
        self.datasetDownloadFile(dataset, file, path, force, quiet)

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
      try:
        if isinstance(item, unicode):
          return item
      except:
        return str(item)
