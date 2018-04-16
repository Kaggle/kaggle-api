from __future__ import print_function
import csv
from datetime import datetime
import json
import os
from os.path import expanduser
from os.path import isfile
import sys
import zipfile
from ..api_client import ApiClient
from kaggle.configuration import Configuration
from .kaggle_api import KaggleApi
from ..models.dataset_new_request import DatasetNewRequest
from ..models.dataset_new_version_request import DatasetNewVersionRequest
from ..models.dataset_upload_file import DatasetUploadFile
from ..models.kaggle_models_extended import Competition
from ..models.kaggle_models_extended import Dataset
from ..models.kaggle_models_extended import DatasetNewResponse
from ..models.kaggle_models_extended import DatasetNewVersionResponse
from ..models.kaggle_models_extended import File
from ..models.kaggle_models_extended import FileUploadInfo
from ..models.kaggle_models_extended import Submission
from ..models.kaggle_models_extended import SubmitResult
import urllib3

try:
  unicode  # Python 2
except NameError:
  unicode = str  # Python 3


class KaggleApi(KaggleApi):
  __version__ = '1.1.0'

  CONFIG_NAME_PROXY = 'proxy'
  CONFIG_NAME_COMPETITION = 'competition'
  CONFIG_NAME_PATH = 'path'
  CONFIG_NAME_USER = 'username'
  CONFIG_NAME_KEY = 'key'

  HEADER_API_VERSION = 'X-Kaggle-ApiVersion'
  METADATA_FILE = 'datapackage.json'

  config_path = os.path.join(expanduser('~'), '.kaggle')
  if not os.path.exists(config_path):
    os.makedirs(config_path)
  config_file = 'kaggle.json'
  config = os.path.join(config_path, config_file)
  config_values = {}
  already_printed_version_warning = False

  def authenticate(self):
    try:
      configuration = Configuration()
      if os.name != 'nt':
        permissions = os.stat(self.config).st_mode
        if (permissions & 4) or (permissions & 32):
          print('Warning: Your Kaggle API key is readable by other users on ' +
                'this system! To fix this, you can run \'chmod 600 {}\''.format(
                    self.config))
      with open(self.config, 'r') as f:
        config_data = json.load(f)

      self.copy_config_value(self.CONFIG_NAME_PROXY, config_data)
      self.copy_config_value(self.CONFIG_NAME_PATH, config_data)
      self.copy_config_value(self.CONFIG_NAME_COMPETITION, config_data)
      self.copy_config_value(self.CONFIG_NAME_USER, config_data)

      configuration.username = config_data[self.CONFIG_NAME_USER]
      configuration.password = config_data[self.CONFIG_NAME_KEY]
      if self.CONFIG_NAME_PROXY in config_data:
        configuration.proxy = config_data[self.CONFIG_NAME_PROXY]
      self.api_client = ApiClient(configuration)

    except Exception as error:
      if 'Proxy' in type(error).__name__:
        sys.exit('The specified proxy ' + config_data[self.CONFIG_NAME_PROXY] +
                 ' is not valid, please check your proxy settings')
      else:
        sys.exit('Unauthorized: you must download an API key from ' +
                 'https://www.kaggle.com/<username>/account\nThen put ' +
                 self.config_file + ' in the folder ' + self.config_path)

  def set_config_value(self, name, value, quiet=False):
    try:
      with open(self.config, 'r') as f:
        config_data = json.load(f)
      if value is not None:
        config_data[name] = value
        with open(self.config, 'w') as f:
          json.dump(config_data, f)
      if name in config_data:
        self.config_values[name] = config_data[name]
    except:
      pass
    if not quiet:
      self.print_config_value(name, separator=' is now set to: ')

  def unset_config_value(self, name, quiet=False):
    try:
      with open(self.config, 'r') as f:
        config_data = json.load(f)
      config_data[name] = None
      with open(self.config, 'w') as f:
        json.dump(config_data, f)
      self.config_values[name] = None
    except:
      pass
    if not quiet:
      self.print_config_value(name, separator=' is now set to: ')

  def copy_config_value(self, name, values):
    if name in values:
      self.config_values[name] = values[name]

  def get_config_value(self, name):
    if name in self.config_values:
      return self.config_values[name]
    return None

  def get_config_path(self):
    path = self.get_config_value(self.CONFIG_NAME_PATH)
    if path is None:
      return self.config_path
    return path

  def print_config_value(self, name, prefix='', separator=': '):
    value_out = 'None'
    if name in self.config_values and self.config_values[name] is not None:
      value_out = self.config_values[name]
    print(prefix + name + separator + value_out)

  def print_config_values(self):
    print('Configuration values from ' + self.get_config_path())
    self.print_config_value(self.CONFIG_NAME_USER, prefix='- ')
    self.print_config_value(self.CONFIG_NAME_PATH, prefix='- ')
    self.print_config_value(self.CONFIG_NAME_PROXY, prefix='- ')
    self.print_config_value(self.CONFIG_NAME_COMPETITION, prefix='- ')

  def competitions_list(self, page=1, search=''):
    if search is None:
      search = ''
    competitions_list_result = self.process_response(
        self.competitions_list_with_http_info(page=page, search=search))
    return [Competition(c) for c in competitions_list_result]

  def competitions_list_cli(self, page=1, search='', csv=False):
    competitions = self.competitions_list(page, search)
    fields = [
        'ref', 'deadline', 'category', 'reward', 'teamCount', 'userHasEntered'
    ]
    if competitions:
      if csv:
        self.print_csv(competitions, fields)
      else:
        self.print_table(competitions, fields)
    else:
      print('No competitions found')

  def competition_submit(self, file, message, competition, quiet=False):
    if competition is None:
      competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
      if competition is not None and not quiet:
        print('Using competition: ' + competition)

    if competition is None:
      sys.exit('No competition specified')
    else:
      url_result = self.process_response(
          self.competitions_submissions_url_with_http_info(
              file_name=os.path.basename(file),
              content_length=os.path.getsize(file),
              last_modified_date_utc=int(os.path.getmtime(file) * 1000)))
      url_result_list = url_result['createUrl'].split('/')
      upload_result = self.process_response(
          self.competitions_submissions_upload_with_http_info(
              file=file,
              guid=url_result_list[-3],
              content_length=url_result_list[-2],
              last_modified_date_utc=url_result_list[-1]))
      upload_result_token = upload_result['token']
      submit_result = self.process_response(
          self.competitions_submissions_submit_with_http_info(
              id=competition,
              blob_file_tokens=upload_result_token,
              submission_descriptio=message))
      return SubmitResult(submit_result)

  def competition_submissions(self, competition):
    submissions_result = self.process_response(
        self.competitions_submissions_list_with_http_info(id=competition))
    return [Submission(s) for s in submissions_result]

  def competition_submissions_cli(self,
                                  competition=None,
                                  csv=False,
                                  quiet=False):
    if competition is None:
      competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
      if competition is not None and not quiet:
        print('Using competition: ' + competition)

    if competition is None:
      sys.exit('No competition specified')
    else:
      submissions = self.competition_submissions(competition)
      fields = [
          'fileName', 'date', 'description', 'status', 'publicScore',
          'privateScore'
      ]
      if submissions:
        if csv:
          self.print_csv(submissions, fields)
        else:
          self.print_table(submissions, fields)
      else:
        print('No submissions found')

  def competition_list_files(self, competition):
    competition_list_files_result = self.process_response(
        self.competitions_data_list_files_with_http_info(id=competition))
    return [File(f) for f in competition_list_files_result]

  def competition_list_files_cli(self, competition, csv=False, quiet=False):
    if competition is None:
      competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
      if competition is not None and not quiet:
        print('Using competition: ' + competition)

    if competition is None:
      sys.exit('No competition specified')
    else:
      files = self.competition_list_files(competition)
      fields = ['name', 'size', 'creationDate']
      if files:
        if csv:
          self.print_csv(files, fields)
        else:
          self.print_table(files, fields)
      else:
        print('No files found')

  def competition_download_file(self,
                                competition,
                                file,
                                path=None,
                                force=False,
                                quiet=False):
    if path is None:
      effective_path = os.path.join(self.get_config_path(), 'competitions',
                                    competition)
    else:
      effective_path = path

    response = self.process_response(
        self.competitions_data_download_file_with_http_info(
            id=competition, file_name=file, _preload_content=False))
    url = response.retries.history[0].redirect_location.split('?')[0]
    outfile = os.path.join(effective_path, url.split('/')[-1])

    if force or self.download_needed(response, outfile, quiet):
      self.download_file(response, outfile, quiet)

  def competition_download_files(self,
                                 competition,
                                 path=None,
                                 force=False,
                                 quiet=True):
    files = self.competition_list_files(competition)
    for file in files:
      self.competition_download_file(competition, file.ref, path, force, quiet)

  def competition_download_cli(self,
                               competition,
                               file=None,
                               path=None,
                               force=False,
                               quiet=False):
    if competition is None:
      competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
      if competition is not None and not quiet:
        print('Using competition: ' + competition)

    if competition is None:
      sys.exit('No competition specified')
    else:
      if file is None:
        self.competition_download_files(competition, path, force, quiet)
      else:
        self.competition_download_file(competition, file, path, force, quiet)

  def datasets_list(self, page=1, search=''):
    if search is None:
      search = ''
    datasets_list_result = self.process_response(
        self.datasets_list_with_http_info(page=page, search=search))
    return [Dataset(d) for d in datasets_list_result]

  def datasets_view(self, dataset):
    dataset_urls = dataset.split('/')
    owner_slug = dataset_urls[0]
    dataset_slug = dataset_urls[1]

    result = self.process_response(
        self.datasets_view_with_http_info(owner_slug, dataset_slug))
    return Dataset(result)

  def datasets_list_cli(self, page=1, search='', csv=False):
    datasets = self.datasets_list(page, search)
    fields = ['ref', 'title', 'size', 'lastUpdated', 'downloadCount']
    if datasets:
      if csv:
        self.print_csv(datasets, fields)
      else:
        self.print_table(datasets, fields)
    else:
      print('No datasets found')

  def dataset_list_files(self, dataset):
    dataset_url_list = dataset.split('/')
    owner_slug = dataset_url_list[0]
    dataset_slug = dataset_url_list[1]
    dataset_list_files_result = self.process_response(
        self.datasets_list_files_with_http_info(
            owner_slug=owner_slug, dataset_slug=dataset_slug))
    return [File(f) for f in dataset_list_files_result]

  def dataset_list_files_cli(self, dataset, csv=False):
    files = self.dataset_list_files(dataset)
    fields = ['name', 'size', 'creationDate']
    if files:
      if csv:
        self.print_csv(files, fields)
      else:
        self.print_table(files, fields)
    else:
      print('No files found')

  def dataset_download_file(self,
                            dataset,
                            file,
                            path=None,
                            force=False,
                            quiet=True):
    dataset_url_list = dataset.split('/')
    owner_slug = dataset_url_list[0]
    dataset_slug = dataset_url_list[1]

    if path is None:
      effective_path = os.path.join(self.get_config_path(), 'datasets',
                                    owner_slug, dataset_slug)
    else:
      effective_path = path

    response = self.process_response(
        self.datasets_download_file_with_http_info(
            owner_slug=owner_slug,
            dataset_slug=dataset_slug,
            file_name=file,
            _preload_content=False))
    url = response.retries.history[0].redirect_location.split('?')[0]
    outfile = os.path.join(effective_path, url.split('/')[-1])
    if force or self.download_needed(response, outfile, quiet):
      self.download_file(response, outfile, quiet)
      return True
    else:
      return False

  def dataset_download_files(self, dataset, path=None, force=False, quiet=True):
    dataset_url_list = dataset.split('/')
    owner_slug = dataset_url_list[0]
    dataset_slug = dataset_url_list[1]

    if path is None:
      effective_path = os.path.join(self.get_config_path(), 'datasets',
                                    owner_slug, dataset_slug)
    else:
      effective_path = path

    downloaded = self.dataset_download_file(dataset, dataset_slug + '.zip',
                                            path, force, quiet)
    if downloaded:
      outfile = os.path.join(effective_path, dataset_slug + '.zip')
      with zipfile.ZipFile(outfile, 'r') as z:
        z.extractall(effective_path)

  def dataset_download_cli(self,
                           dataset,
                           file=None,
                           path=None,
                           force=False,
                           quiet=False):
    if file is None:
      self.dataset_download_files(dataset, path, force, quiet)
    else:
      self.dataset_download_file(dataset, file, path, force, quiet)

  def dataset_upload_file(self, file):
    file_name = os.path.basename(file)
    content_length = os.path.getsize(file)
    last_modified_date_utc = int(os.path.getmtime(file))
    result = FileUploadInfo(
        self.process_response(
            self.datasets_upload_file_with_http_info(file_name, content_length,
                                                     last_modified_date_utc)))

    success = self.upload_complete(file, result.createUrl)

    if success:
      return result.token
    return None

  def dataset_create_version(self, folder, version_notes, quiet=False):
    if not os.path.isdir(folder):
      sys.exit('Invalid folder: ' + folder)

    meta_file = os.path.join(folder, self.METADATA_FILE)
    if not os.path.isfile(meta_file):
      sys.exit('Metadata file not found: ' + self.METADATA_FILE)
      return

    # read json
    with open(meta_file, 'r') as f:
      meta_data = json.load(f)
    ref = self.get_or_exit(meta_data, 'id')
    ref_list = ref.split('/')
    owner_slug = ref_list[0]
    dataset_slug = ref_list[1]

    # validations
    if ref == self.config_values[self.CONFIG_NAME_USER] + '/INSERT_SLUG_HERE':
      sys.exit('Default slug detected, please change values before uploading')

    request = DatasetNewVersionRequest(version_notes, [])

    for file in os.listdir(folder):
      full_path = os.path.join(folder, file)

      if file == self.METADATA_FILE:
        continue

      if os.path.isfile(full_path):
        content_length = os.path.getsize(full_path)
        token = self.dataset_upload_file(full_path)
        if token is None:
          print('Upload unsuccessful: ' + file)
          return

        if not quiet:
          print('Upload successful: ' + file + ' (' +
                File.get_size(content_length) + ')')

        upload_file = DatasetUploadFile()
        upload_file.token = token
        request.files.append(upload_file)
      else:
        if not quiet:
          print('Skipping: ' + file)

    result = DatasetNewVersionResponse(
        self.process_response(
            self.datasets_create_version_with_http_info(owner_slug,
                                                        dataset_slug, request)))
    return result

  def dataset_create_version_cli(self, folder, version_notes, quiet=False):
    result = self.dataset_create_version(folder, version_notes, quiet)

    if result is None:
      print('Dataset version creation error: See previous output')
    elif result.status == 'ok':
      print('Dataset version is being created. Please check progress at ' +
            result.url)
    else:
      print('Dataset version creation error: ' + result.error)

  def dataset_initialize(self, folder):
    if not os.path.isdir(folder):
      sys.exit('Invalid folder: ' + folder)

    ref = self.config_values[self.CONFIG_NAME_USER] + '/INSERT_SLUG_HERE'
    licenses = []
    license = {}
    license['name'] = 'CC0-1.0'
    licenses.append(license)

    meta_data = {}
    meta_data['title'] = 'INSERT_TITLE_HERE'
    meta_data['id'] = ref
    meta_data['licenses'] = licenses
    meta_file = os.path.join(folder, self.METADATA_FILE)
    with open(meta_file, 'w') as f:
      json.dump(meta_data, f)

    print('Data package template written to: ' + meta_file)

  def dataset_create_new(self, folder, public=False, quiet=False):
    if not os.path.isdir(folder):
      sys.exit('Invalid folder: ' + folder)

    meta_file = os.path.join(folder, self.METADATA_FILE)
    if not os.path.isfile(meta_file):
      sys.exit('Metadata file not found: ' + self.METADATA_FILE)
      return

    # read json
    with open(meta_file, 'r') as f:
      meta_data = json.load(f)
    ref = self.get_or_exit(meta_data, 'id')
    title = self.get_or_exit(meta_data, 'title')
    licenses = self.get_or_exit(meta_data, 'licenses')
    ref_list = ref.split('/')
    owner_slug = ref_list[0]
    dataset_slug = ref_list[1]

    # validations
    if ref == self.config_values[self.CONFIG_NAME_USER] + '/INSERT_SLUG_HERE':
      sys.exit('Default slug detected, please change values before uploading')
    if title == 'INSERT_TITLE_HERE':
      sys.exit('Default title detected, please change values before uploading')
    if len(licenses) != 1:
      sys.exit('Please specify exactly one license')

    license_name = self.get_or_exit(licenses[0], 'name')

    request = DatasetNewRequest(title, dataset_slug, owner_slug, license_name,
                                [], not public)

    for file in os.listdir(folder):
      if file == self.METADATA_FILE:
        continue
      full_path = os.path.join(folder, file)

      if os.path.isfile(full_path):
        content_length = os.path.getsize(full_path)
        token = self.dataset_upload_file(full_path)
        if token is None:
          print('Upload unsuccessful: ' + file)
          return

        if not quiet:
          print('Upload successful: ' + file + ' (' +
                File.get_size(content_length) + ')')

        upload_file = DatasetUploadFile()
        upload_file.token = token
        request.files.append(upload_file)
      else:
        if not quiet:
          print('Skipping: ' + file)

    result = DatasetNewResponse(
        self.process_response(self.datasets_create_new_with_http_info(request)))
    return result

  def dataset_create_new_cli(self, folder, public=False, quiet=False):
    result = self.dataset_create_new(folder, public, quiet)
    if result.status == 'ok':
      if public:
        print('Your public Dataset is being created. Please check progress at '
              + result.url)
      else:
        print('Your private Dataset is being created. Please check progress at '
              + result.url)
    else:
      print('Dataset creation error: ' + result.error)

  def download_file(self, response, outfile, quiet=True, chunk_size=1048576):
    outpath = os.path.dirname(outfile)
    if not os.path.exists(outpath):
      os.makedirs(outpath)
    size = int(response.headers['Content-Length'])
    size_read = 0
    with open(outfile, 'wb') as out:
      while True:
        data = response.read(chunk_size)
        if not data:
          break
        out.write(data)
        size_read = min(size, size_read + chunk_size)
        if not quiet:
          print(
              os.path.basename(outfile) + ': Downloaded ' +
              File.get_size(size_read) + ' of ' + File.get_size(size),
              end='\r')
    if not quiet:
      print('\n', end='')

  def download_needed(self, response, outfile, quiet=True):
    try:
      remote_date = datetime.strptime(response.headers['Last-Modified'],
                                      '%a, %d %b %Y %X %Z')
      if isfile(outfile):
        local_date = datetime.fromtimestamp(os.path.getmtime(outfile))
        if remote_date <= local_date:
          if not quiet:
            print(os.path.basename(outfile) +
                  ': Skipping, found more recently modified local copy ' +
                  '(use --force to force download)')
          return False
    except:
      pass
    return True

  def print_table(self, items, fields):
    formats = []
    borders = []
    for f in fields:
      length = max(
          len(f), max([len(self.string(getattr(i, f))) for i in items]))
      justify = '>' if isinstance(getattr(items[0], f),
                                  int) or f == 'size' or f == 'reward' else '<'
      formats.append('{:' + justify + self.string(length + 2) + '}')
      borders.append('-' * length + '  ')
    row_format = u''.join(formats)
    headers = [f + '  ' for f in fields]
    print(row_format.format(*headers))
    print(row_format.format(*borders))
    for i in items:
      i_fields = [self.string(getattr(i, f)) + '  ' for f in fields]
      print(row_format.format(*i_fields))

  def print_csv(self, items, fields):
    writer = csv.writer(sys.stdout)
    writer.writerow(fields)
    for i in items:
      i_fields = [self.string(getattr(i, f)) for f in fields]
      writer.writerow(i_fields)

  def string(self, item):
    return item if isinstance(item, unicode) else str(item)

  def get_or_exit(self, data, key):
    if key in data:
      return data[key]
    sys.exit('Key ' + key + ' not found in data')

  def process_response(self, result):
    if len(result) == 3:
      data = result[0]
      code = result[1]
      headers = result[2]
      if self.HEADER_API_VERSION in headers:
        api_version = headers[self.HEADER_API_VERSION]
        if not self.already_printed_version_warning and self.__version__ < api_version:
          print('Warning: Looks like you\'re using an outdated API Version, ' +
                'please consider updating (server ' + api_version +
                ' / client ' + self.__version__ + ')')
          self.already_printed_version_warning = True
      return data
    return result

  def upload_complete(self, file, url):
    urllib3.disable_warnings()
    proxy_url = self.get_config_value(self.CONFIG_NAME_PROXY)
    if proxy_url is None:
      http = urllib3.PoolManager()
    else:
      http = urllib3.ProxyManager(proxy_url)

    content_length = os.path.getsize(file)
    with open(file, 'rb') as fp:
      data = fp.read()
      try:
        response = http.request('PUT', url, body=data)
      except Exception as error:
        print(error)
        return False
    return True

  def dataset_data(self, dataset, file_path=None, force=False, quiet=True):
    dataset_url_list = dataset.split('/')
    owner_slug = dataset_url_list[0]
    dataset_slug = dataset_url_list[1]
    effective_path = os.path.join(self.get_config_path(), 'datasets',
                                  owner_slug, dataset_slug)

    # complete folders
    if file_path is None:
      if os.path.exists(effective_path) and not force:
        return effective_path

      if not quiet:
        print('Downloading Dataset ' + dataset + '...')
      self.dataset_download_files(dataset, path=None, force=force, quiet=quiet)
      return effective_path

    # individual files
    effective_path = os.path.join(effective_path, file_path)
    if os.path.exists(effective_path) and not force:
      return effective_path

    if not quiet:
      print('Downloading file ' + file_path + ' from Dataset ' + dataset)

    self.dataset_download_file(
        dataset, file_path, path=None, force=force, quiet=quiet)
    return effective_path

  def competition_data(self,
                       competition,
                       file_path=None,
                       force=False,
                       quiet=True):
    effective_path = os.path.join(self.get_config_path(), 'competitions',
                                  competition)

    # complete folders
    if file_path is None:
      if os.path.exists(effective_path) and not force:
        return effective_path

      if not quiet:
        print('Downloading Competition ' + competition + '...')
      self.competitionDownloadFiles(
          competition, path=None, force=force, quiet=quiet)
      return effective_path

    # individual files
    effective_path = os.path.join(effective_path, file_path)
    if os.path.exists(effective_path) and not force:
      return effective_path

    if not quiet:
      print('Downloading file ' + file_path + ' from Competition ' +
            competition)

    self.competition_download_file(
        competition, file_path, path=None, force=force, quiet=quiet)
    return effective_path

  def upload_in_chunks(self, file, url, chunk_size=1048576):
    urllib3.disable_warnings()
    proxy_url = self.get_config_value(self.CONFIG_NAME_PROXY)
    if proxy_url is None:
      http = urllib3.PoolManager()
    else:
      http = urllib3.ProxyManager(proxy_url)

    file_name = os.path.basename(file)
    content_length = os.path.getsize(file)
    index = 0
    offset = 0
    headers = {}
    with open(file, 'rb') as fp:
      for chunk in self.read_in_chunks(fp, chunk_size=chunk_size):

        offset = index + len(chunk)
        headers['Content-Length'] = content_length
        headers['Content-Range'] = 'bytes %s-%s/%s' % (index, offset,
                                                       content_length)
        index = offset
        try:
          response = http.request('PUT', url, body=chunk, headers=headers)
          print(file_name + ': Uploaded ' + File.get_size(index) + ' of ' +
                File.get_size(content_length))

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
