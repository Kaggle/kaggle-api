#!/usr/bin/python
#
# Copyright 2018 Kaggle Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import csv
from datetime import datetime
import io
import json
import os
from os.path import expanduser
from os.path import isfile
import sys
import zipfile
from ..api_client import ApiClient
from kaggle.configuration import Configuration
from .kaggle_api import KaggleApi
from ..models.dataset_column import DatasetColumn
from ..models.dataset_new_request import DatasetNewRequest
from ..models.dataset_new_version_request import DatasetNewVersionRequest
from ..models.dataset_upload_file import DatasetUploadFile
from ..models.kaggle_models_extended import Competition
from ..models.kaggle_models_extended import Dataset
from ..models.kaggle_models_extended import DatasetNewResponse
from ..models.kaggle_models_extended import DatasetNewVersionResponse
from ..models.kaggle_models_extended import File
from ..models.kaggle_models_extended import FileUploadInfo
from ..models.kaggle_models_extended import LeaderboardEntry
from ..models.kaggle_models_extended import ListFilesResult
from ..models.kaggle_models_extended import Submission
from ..models.kaggle_models_extended import SubmitResult
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from ..rest import ApiException
import six
from tqdm import tqdm

try:
    unicode  # Python 2
except NameError:
    unicode = str  # Python 3


class KaggleApi(KaggleApi):
    __version__ = '1.3.10'

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

    # Hack for https://github.com/Kaggle/kaggle-api/issues/22 / b/78194015

    if six.PY2:
        reload(sys)
        sys.setdefaultencoding('latin1')


## Authentication


    def authenticate(self):
        '''authenticate the user with the Kaggle API. This method will generate
           a configuration, first checking the environment for credential
           variables, and falling back to looking for the .kaggle/kaggle.json
           configuration file.
        '''
        config_data = {}

        # Step 1: read in configuration file, if it exists
        if os.path.exists(self.config):
            config_data = self._authenticate_config(config_data)

        # Step 2:, get username/password from environment
        config_data = self._authenticate_environment(config_data)


        # Step 3: load into configuration!
        self._load_config(config_data)


    def _authenticate_environment(self, config_data=None, quiet=False):
        '''autheticate environment is the second effort to get a username
           and key to authenticate to the Kaggle API. The environment keys
           are equivalent to the kaggle.json file, but with "KAGGLE_" prefix
           to define a unique namespace.

           Parameters
           ==========
           configuration: the Configuration object to save a username and
                          password, if defined
           config_data: a partially loaded configuration dictionary (optional)
           quiet: add verbosity

        '''

        if config_data == None:
            config_data = {}

        # Add all variables that start with KAGGLE_ to config data

        for key,val in os.environ.items():
            if key.startswith('KAGGLE_'):
                config_key = key.replace('KAGGLE_','',1).lower()
                config_data[config_key] = val

        return config_data


## Configuration

    def _load_config(self, config_data):
        '''the final step of the authenticate steps, where we load the values
           from config_data into the Configuration object.

           Parameters
           ==========
           config_data: a dictionary with configuration values (keys) to read
                        into self.config_values

        '''
        # Username and password are required.

        for item in [self.CONFIG_NAME_USER, self.CONFIG_NAME_KEY]:
            if item not in config_data:
                print('Error: Missing %s in configuration.' % item)
                sys.exit(1)

        configuration = Configuration()

        # Add to the final configuration (required)

        configuration.username = config_data[self.CONFIG_NAME_USER]
        configuration.password = config_data[self.CONFIG_NAME_KEY]

        # Proxy

        if self.CONFIG_NAME_PROXY in config_data:
            configuration.proxy = config_data[self.CONFIG_NAME_PROXY]

        # Keep config values with class instance, and load api client!

        self.config_values = config_data

        try:
            self.api_client = ApiClient(configuration)

        except Exception as error:

            if 'Proxy' in type(error).__name__:
                sys.exit('The specified proxy ' + 
                         config_data[self.CONFIG_NAME_PROXY] +
                         ' is not valid, please check your proxy settings')
            else:
                sys.exit('Unauthorized: you must download an API key or export '
                         'credentials to the environment. Please see\n ' +
                         'https://github.com/Kaggle/kaggle-api#api-credentials '
                          + 'for instructions.')


    def _authenticate_config(self, quiet=False):
        '''autheticate config is the first effort to get a username
           and key to authenticate to the Kaggle API. Since we can get the
           username and password from the environment, it's not required.

           Parameters
           ==========
           configuration: the Configuration object to save a username and
                          password, if defined
           quiet: add verbosity
        '''
        config_data = {}

        if os.path.exists(self.config):

            try:
                if os.name != 'nt':
                    permissions = os.stat(self.config).st_mode
                    if (permissions & 4) or (permissions & 32):
                        print('Warning: Your Kaggle API key is readable by other' 
                              'users on this system! To fix this, you can run' + 
                              '\'chmod 600 {}\''.format(self.config))

                with open(self.config, 'r') as f:
                    config_data = json.load(f)
            except:
                pass

        else:

            # Warn the user that configuration will be reliant on environment
            if not quiet:
                print('No Kaggle API config file found, will use environment.')

        return config_data

  
    def _read_config(self):
        '''read in the configuration file, a json file defined at self.confi'''
        
        try:
            with open(self.config, 'r') as f:
                config_data = json.load(f)
        except FileNotFoundError:
            config_data = {}

        return config_data


    def _write_config(self, config_data, indent=1):
        '''write config data to file.
        '''
        with open(self.config, 'w') as f:
            json.dump(config_data, f, indent=indent)


    def set_config_value(self, name, value, quiet=False):
        '''a client helper function to set a configuration value, meaning
           reading in the configuration file (if it exists), saving a new
           config value, and then writing back
        '''

        config_data = self._read_config()
   
        # If defined by client, set and save!
        self._write_config(config_data)

        if value is not None:

            # Update the config file with the value
            config_data[name] = value

            # Update the instance with the value
            self.config_values[name] = value

            if not quiet:
                self.print_config_value(name, separator=' is now set to: ')


    def unset_config_value(self, name, quiet=False):
        '''unset a configuration value'''

        config_data = self._read_config()

        # Remove it, if exists, both from loaded file and client

        del self.config_values[name] # is there reason this was None?

        if name in config_data:
            del config_data[name]

            self._write_config(config_data)

            if not quiet:
                self.print_config_value(name, separator=' is now set to: ')

    def get_config_value(self, name):
        ''' return a config value (with key name) if it's in the config_values,
            otherwise return None
 
            Parameters
            ==========
            name: the config value key to get

        '''
        if name in self.config_values:
            return self.config_values[name]

    def get_config_path(self):
        '''get the path configuration value, otherwise return default.
        '''
        path = self.get_config_value(self.CONFIG_NAME_PATH)
        if path is None:
            return self.config_path
        return path

    def print_config_value(self, name, prefix='', separator=': '):
        '''print a single configuration value, based on a prefix and separator

           Parameters
           ==========
           name: the key of the config valur in self.config_values to print
           prefix: the prefix to print
           separator: the separator to use (default is : )
        '''
        value_out = 'None'
        if name in self.config_values and self.config_values[name] is not None:
            value_out = self.config_values[name]
        print(prefix + name + separator + value_out)

    def print_config_values(self):
        '''a wrapper to print_config_value to print all configuration values
        '''
        print('Configuration values from ' + self.get_config_path())
        self.print_config_value(self.CONFIG_NAME_USER, prefix='- ')
        self.print_config_value(self.CONFIG_NAME_PATH, prefix='- ')
        self.print_config_value(self.CONFIG_NAME_PROXY, prefix='- ')
        self.print_config_value(self.CONFIG_NAME_COMPETITION, prefix='- ')


## Competitions

    ## List and Get Competitions

    def competitions_list(self, page=1, search=''):
        '''make call to list competitions, format the response, and return
           a list of Competition instances

           Parameters
           ==========
           page: the page to return (default is 1)
           search: a search term to use (default is empty string)

        '''    

        # Make sure search isn't None

        search = search or ''

        # Get the listing of competitions

        response = self.competitions_list_with_http_info(page=page,
                                                         search=search)
        # Process the response

        competitions_list_result = self.process_response(response)

        return [Competition(c) for c in competitions_list_result]


    def competitions_list_cli(self, page=1, search='', csv_display=False):
        '''a wrapper for competitions_list for the client
        
           Paramters
           =========
           page: the page to return (default is 1)
           search: a default search term
           csv_display: if True, print comma separated values

        '''

        competitions = self.competitions_list(page, search)

        fields = ['ref', 
                  'deadline', 
                  'category', 
                  'reward', 
                  'teamCount', 
                  'userHasEntered']

        self.print_result(competitions, fields, 'competitions', csv_display)


    def _competition_get_or_exit(self, competition):
        '''if a competition is None, look for the name in the config values.
           If it's still None, exit.

           competition: the name of the competition (str)
        '''

        if competition is None:
            competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
        if competition is not None and not quiet:
            print('Using competition: ' + competition)

        if competition is None:
            sys.exit('No competition specified')

        return competition


    ## Submit

    def competition_submit(self, file_name, message, competition, quiet=False):
        '''submit a competition!
      
           Parameters
           ==========
           file_name: the competition metadata file 
           message: the submission description
           competition: the competition name
           
        '''
        if competition is None:
            competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
        elif competition is not None and not quiet:
            print('Using competition: ' + competition)

        # If still None, wasn't obtained in configuration, exit
        if competition is None:
            sys.exit('No competition specified')

        # Calculate the date last modified of the file

        last_modified_date = int(os.path.getmtime(file_name) * 1000)

        # Step 1: Get the URL for the submission
        url_result = self.process_response(
            self.competitions_submissions_url_with_http_info(
                file_name=os.path.basename(file_name),
                content_length=os.path.getsize(file_name),
                last_modified_date_utc=last_modified_date))

        url_result_list = url_result['createUrl'].split('/')

        # Step 2: Upload the result
        upload_result = self.process_response(
            self.competitions_submissions_upload_with_http_info(
                file=file_name,
                guid=url_result_list[-3],
                content_length=url_result_list[-2],
                last_modified_date_utc=url_result_list[-1]))
        upload_result_token = upload_result['token']

        # Step 3: Submit!
        submit_result = self.process_response(
          self.competitions_submissions_submit_with_http_info(
                  id=competition,
                  blob_file_tokens=upload_result_token,
                  submission_description=message))
  
        return SubmitResult(submit_result)


    def competition_submit_cli(self, file_name, message, competition, quiet=False):
        '''submit a competition using the client. Arguments are same as for
           competition_submit
        '''
        try:
            submit_result = self.competition_submit(file_name, message, competition, quiet)
        except ApiException as e:
            if e.status == 404:
                print('Could not find competition - please verify that you ' +
                      'entered the correct competition ID and that the ' +
                      'competition is still accepting submissions.')
                return None
            raise e

        return submit_result

    ## Submissions

    def competition_submissions(self, competition):
        '''get the list of Submission for a particular competition

           Parameters
           ==========
           competition: the name of the competition

        '''
        submissions_result = self.process_response(
            self.competitions_submissions_list_with_http_info(id=competition))
        return [Submission(s) for s in submissions_result]


    def competition_submissions_cli(self,
                                    competition=None,
                                    csv_display=False,
                                    quiet=False):
        '''wrapper to competition_submission, will return either json or csv
           to the user

           Parameters
           ==========
           competition: the name of the competition. If None, look to config
           csv_display: if True, print comma separated values
           
        '''
 
        competition = self._competition_get_or_exit(competition)

        submissions = self.competition_submissions(competition)
        fields = [ 'fileName', 
                   'date', 
                   'description', 
                   'status', 
                   'publicScore',
                   'privateScore']

        self.print_result(submissions, fields, 'submissions', csv_display)


    ## Files

    def competition_list_files(self, competition):
        '''list files for competition

           Parameters
           ==========
           competition: the name of the competition

        '''
        competition_list_files_result = self.process_response(
            self.competitions_data_list_files_with_http_info(id=competition))
        return [File(f) for f in competition_list_files_result]


    def competition_list_files_cli(self,
                                   competition,
                                   csv_display=False,
                                   quiet=False):

        '''List files for a competition, if it exists

           Parameters
           ==========
           competition: the name of the competition. If None, look to config
           csv_display: if True, print comma separated values
        '''

        competition = self._competition_get_or_exit(competition)

        files = self.competition_list_files(competition)
        fields = ['name', 'size', 'creationDate']

        self.print_result(files, fields, 'files', csv_display)


## Download


    def _get_download_path(self, path, subfolders):
        '''Get the download path for a file. If not defined, return default 
           from config.

           Parameters
           ==========
           path: a path defined by the user, doesn't have to be defined
           subfolders: a single (or list of) subfolders under the basepath

        '''
        effective_path = path
        if path is None:
 
            # explode this into os.path.join so it can be arbitrary length
            if not isinstance(subfolders,list):
                subfolders = [subfolders]

            effective_path = os.path.join(self.get_config_path(), *subfolders)

        return effective_path
        

    ## Files

    def competition_download_cli(self,
                                 competition,
                                 file_name=None,
                                 path=None,
                                 force=False,
                                 quiet=False):

        '''a wrapper to competition_download_files, but first will parse input
           from API client.

           Parameters
           =========
           competition: the name of the competition
           file_name: the configuration file name
           path: a path to download the file to

        '''
        competition = self._competition_get_or_exit(competition)

        if file_name is None:
            self.competition_download_files(competition, path, force, quiet)
        else:
            self.competition_download_file(competition, 
                                           file_name=file_name, 
                                           path=path, 
                                           force=force,
                                           quiet=quiet)


    def competition_download_file(self,
                                competition,
                                file_name,
                                path=None,
                                force=False,
                                quiet=False):
        '''download a competition file to a designated location, or use
           a default location

           Paramters
           =========
           competition: the name of the competition
           file_name: the configuration file name
           path: a path to download the file to
          
        '''

        subfolders = [competition, 'competitions']
        effective_path = self._get_download_path(path, subfolders)

        response = self.process_response(
            self.competitions_data_download_file_with_http_info(
                id=competition, 
                file_name=file_name, 
                _preload_content=False))

        url = response.retries.history[0].redirect_location.split('?')[0]
        outfile = os.path.join(effective_path, url.split('/')[-1])

        if force or self.download_needed(response, outfile, quiet):
            self.download_file(response, outfile, quiet)


    def competition_download_files(self,
                                   competition,
                                   path=None,
                                   force=False,
                                   quiet=True):
        '''a wrapper to competition_download_file to download all competition
           files.

           Parameters
           =========
           competition: the name of the competition
           file_name: the configuration file name
           path: a path to download the file to
        '''

        files = self.competition_list_files(competition)
        if not files:
            print('This competition does not have any available data files')
        for file_name in files:
            self.competition_download_file(competition, 
                                           file_name=file_name.ref, 
                                           path=path, 
                                           force=force,
                                           quiet=quiet)


    ## Leaderboards

    def competition_leaderboard_download(self, competition, path, quiet=True):
        ''' Download competition leaderboards
 
            Parameters
            =========
            competition: the name of the competition
            file_name: the configuration file name
            path: a path to download the file to

        '''
        response = self.process_response(
            self.competition_download_leaderboard_with_http_info(
                competition, _preload_content=False))

        subfolders = [competition, 'competitions']
        effective_path = self._get_download_path(path, subfolders)

        file_name = competition + '.zip'
        outfile = os.path.join(effective_path, file_name)
        self.download_file(response, outfile, quiet)


    def competition_leaderboard_view(self, competition):
        '''view a leaderboard based on a competition name
 
           Parameters
           ==========
           competition: the competition name to view leadboard for

        '''
        result = self.process_response(
            self.competition_view_leaderboard_with_http_info(competition))
        return [LeaderboardEntry(e) for e in result['submissions']]


    def competition_leaderboard_cli(self,
                                    competition,
                                    path=None,
                                    view=False,
                                    download=False,
                                    csv_display=False,
                                    quiet=False):

        '''a wrapper for competition_leaderbord_view that will print the
           results as a table or comma separated values

           Parameters
           ==========
           competition: the competition name to view leadboard for
           path: a path to download to, if download is True
           view: if True, show the results in the terminal as csv or table
           csv_display: if True, print comma separated values instead of table

        '''
 
        if not view and not download:
            sys.exit('Either --show or --download must be specified')

        competition = self._competition_get_or_exit(competition)

        if download is True:
            self.competition_leaderboard_download(competition, path, quiet)

        if view is True:
            results = self.competition_leaderboard_view(competition)
            fields = ['teamId', 'teamName', 'submissionDate', 'score']
            self.print_result(results, fields, 'results', csv_display)


## Datasets

    def datasets_list(self, page=1, search=''):
        '''return a list of datasets!

           Parameters
           ==========
           page: the page to return (default is 1)
           search: a search term to use (default is empty string)

        '''
        # Make sure search isn't None
        search = search or ''

        datasets_list_result = self.process_response(
            self.datasets_list_with_http_info(page=page, search=search))
        return [Dataset(d) for d in datasets_list_result]


    def _dataset_get_or_exit(self, dataset):
        '''return the owner (user or organization) of a dataset, or exit
           on error (meaning the user didn't provide the entire URI)

           Parameters
           ==========
           dataset: the string identified of the dataset
                    should be in format [owner]/[dataset-name]   
 
        '''
        try:
            dataset_urls = dataset.split('/')
            owner_slug = dataset_urls[0]
            dataset_slug = dataset_urls[1]

        except IndexError:
            print('%s is an invalid dataset name, should be in format ' +
                  ' [owner]/[dataset-name]' % dataset)
            sys.exit(1)

        return owner_slug, dataset_slug


    def datasets_view(self, dataset):
        '''view metadata for a dataset.
          
           Parameters
           ==========
           dataset: the string identified of the dataset
                    should be in format [owner]/[dataset-name]   
        '''

        owner_slug, dataset_slug = self._dataset_get_or_exit(dataset)

        result = self.process_response(
            self.datasets_view_with_http_info(owner_slug, dataset_slug))
        return Dataset(result)

    def datasets_list_cli(self, page=1, search='', csv_display=False):
        '''a wrapper to datasets_list for the client.

           Parameters
           ==========
           page: the page to return (default is 1)
           search: a search term to use (default is empty string)

        '''
        datasets = self.datasets_list(page, search)
        fields = ['ref', 'title', 'size', 'lastUpdated', 'downloadCount']
        self.print_result(datasets, fields, 'datasets', csv_display)


    ## Files

    def dataset_list_files(self, dataset):
        '''list files for a dataset

           Parameters
           ==========
           dataset: the string identified of the dataset
                    should be in format [owner]/[dataset-name]   

        '''
        owner_slug, dataset_slug = self._dataset_get_or_exit(dataset)

        dataset_list_files_result = self.process_response(
            self.datasets_list_files_with_http_info(
                owner_slug=owner_slug, 
                dataset_slug=dataset_slug))
        return ListFilesResult(dataset_list_files_result)


    def dataset_list_files_cli(self, dataset, csv_display=False):
        '''a wrapper to dataset_list_files for the client 
           (list files for a dataset)

           Parameters
           ==========
           csv_display: if True, print comma separated values instead of table
           dataset: the string identified of the dataset
                    should be in format [owner]/[dataset-name]   

        '''

        result = self.dataset_list_files(dataset)
    
        # There was an error in listing the files.
        if result:
            if result.error_message:
                print(result.error_message)

        # No error, print away!
        else:
            fields = ['name', 'size', 'creationDate']
            self.print_result(result.files, fields, 'files', csv_display)


    ## Download

    def dataset_download_file(self,
                              dataset,
                              file_name,
                              path=None,
                              force=False,
                              quiet=True):
        
        '''download a single file for a dataset

           Parameters
           ==========
           dataset: the string identified of the dataset
                    should be in format [owner]/[dataset-name]   
           file_name: the dataset configuration file
           path: if defined, download to this location
     
        '''

        owner_slug, dataset_slug = self._dataset_get_or_exit(dataset)

        # Get the effective path for the dataset

        subfolders = ['datasets', owner_slug, dataset_slug]
        effective_path = self._get_download_path(path, subfolders)

        response = self.process_response(
            self.datasets_download_file_with_http_info(
                owner_slug=owner_slug,
                dataset_slug=dataset_slug,
                file_name=file_name,
                _preload_content=False))

        url = response.retries.history[0].redirect_location.split('?')[0]
        outfile = os.path.join(effective_path, url.split('/')[-1])

        # Return True if download, False if not

        if force or self.download_needed(response, outfile, quiet):
            self.download_file(response, outfile, quiet)
            return True
        else:
            return False

    def dataset_download_files(self, 
                               dataset, 
                               path=None, 
                               force=False, 
                               quiet=True):
        '''download all files for a dataset
         
           Parameters
           ==========
           dataset: the string identified of the dataset
                    should be in format [owner]/[dataset-name]   
           path: the path to download the dataset to
         
        '''

        owner_slug, dataset_slug = self._dataset_get_or_exit(dataset)

        subfolders = ['datasets', owner_slug, dataset_slug]
        effective_path = self._get_download_path(path, subfolders)

        downloaded = self.dataset_download_file(dataset, dataset_slug + '.zip',
                                                path, force, quiet)
        if downloaded is True:
            outfile = os.path.join(effective_path, dataset_slug + '.zip')
            with zipfile.ZipFile(outfile) as z:
                z.extractall(effective_path)

    def dataset_download_cli(self,
                             dataset,
                             file_name=None,
                             path=None,
                             force=False,
                             quiet=False):
        '''client wrapper for dataset_download_files to download dataset files
         
           Parameters
           ==========
           dataset: the string identified of the dataset
                    should be in format [owner]/[dataset-name]   
           path: the path to download the dataset to
         
        '''

        if file_name is None:
            self.dataset_download_files(dataset, path, force, quiet)
        else:
            self.dataset_download_file(dataset, file_name, path, force, quiet)

    def dataset_upload_file(self, path, quiet):
        '''upload a dataset file

           Parameters
           ==========
           path: the complete path to upload

        '''
 
        file_name = os.path.basename(path)
        content_length = os.path.getsize(path)
        last_modified_date_utc = int(os.path.getmtime(path))

        # Do the upload and get a result
        result = FileUploadInfo(
            self.process_response(
                self.datasets_upload_file_with_http_info(file_name, content_length,
                                                         last_modified_date_utc)))

        # Returns True if successful (otherwise we return None)
        if self.upload_complete(path, result.createUrl, quiet):
            return result.token
    

    def _dataset_prepare_create_request(self, folder):
        '''prepare a dictionary with parameters to create, and also do sanity
           checks for folder and metadata file existence. Return a dictionary
           with values needed for the request.
 
           Parameters
           ==========
           folder: the folder with the expected metadata file

        '''

        # Folder and metadata file are required
        if not os.path.isdir(folder):
            sys.exit('Invalid folder: ' + folder)
        
        meta_file = os.path.join(folder, self.METADATA_FILE)
        if not os.path.isfile(meta_file):
            sys.exit('Metadata file not found: ' + self.METADATA_FILE)
         
        # read metadata json in dataset folder
        with open(meta_file, 'r') as f:
            meta_data = json.load(f)
        ref = self.get_or_exit(meta_data, 'id')

        # Get the owner (organization) and dataset name
        owner_slug, dataset_slug = self._dataset_get_or_exit(ref)
        meta_data['owner_slug'] = owner_slug
        meta_data['dataset_slug'] = dataset_slug

        # validations
        missing_message = 'Default %s detected, please change before uploading'

        # Title and must be defined
        if ref == self.config_values[self.CONFIG_NAME_USER] + '/INSERT_SLUG_HERE':
            sys.exit(missing_message % 'slug')
        if meta_data.get('title') == 'INSERT_TITLE_HERE':
            sys.exit(missing_message % 'title')

        # Only one license allowed
        if len(meta_data.get('licenses')) != 1:
            sys.exit('Please specify exactly one license')

        # Subtitle
        subtitle = meta_data.get('subtitle')
        if subtitle and (len(subtitle) < 20 or len(subtitle) > 80):
            raise ValueError('Subtitle length must be between 20 and 80 characters')

        # Keywords
        meta_data['keywords'] = self.get_or_default(meta_data, 'keywords', [])
        return meta_data


    def dataset_create_version(self,
                               folder,
                               version_notes,
                               quiet=False,
                               convert_to_csv=True,
                               delete_old_versions=False):
         ''' create a version of a dataset

             Parameters
             ==========
             folder: the folder with the dataset configuration / data files
             version_notes: notes to add for the version
             convert_to_csv: on upload, if data should be converted to csv
             delete_old_versions: if True, do that (default False)

         '''
         metadata = self._dataset_prepare_create_request(folder)

         # Make the request
         request = DatasetNewVersionRequest(
             version_notes=version_notes,
             subtitle=metadata.get('subtitle'),
             description=metadata.get('description'),
             files=[],
             convert_to_csv=convert_to_csv,
             category_ids=metadata.get('keywords'),
             delete_old_versions=delete_old_versions)

         # Upload the resources
         resources = metadata.get('resources')
         owner = metadata.get('owner_slug')
         slug = metadata.get('dataset_slug')

         self.upload_files(request, resources, folder, quiet)
         result = DatasetNewVersionResponse(
             self.process_response(
                 self.datasets_create_version_with_http_info(owner,
                                                             slug, 
                                                             request)))
         return result


    def dataset_create_version_cli(self,
                                   folder,
                                   version_notes,
                                   quiet=False,
                                   convert_to_csv=True,
                                   delete_old_versions=False):
        ''' client wrapper for creating a version of a dataset

            Parameters
            ==========
            folder: the folder with the dataset configuration / data files
            version_notes: notes to add for the version
            convert_to_csv: on upload, if data should be converted to csv
            delete_old_versions: if True, do that (default False)

        '''

        result = self.dataset_create_version(
            folder,
            version_notes,
            quiet=quiet,
            convert_to_csv=convert_to_csv,
            delete_old_versions=delete_old_versions)

        if result is None:
            print('Dataset version creation error: See previous output')

        elif result.status == 'ok':
            print('Dataset version is being created. Please check progress at ' +
                  result.url)

            # We only might have invalid tags if the result isn't None

            if result.invalidTags is not None:
                print('The following are not valid tags and could not be added ' +
                      ' to the dataset: ' + str(result.invalidTags))

        # If result isn't None or status isn't ok, something else went wrong!
        else:
            print('Dataset version creation error: ' + result.error)


    def dataset_initialize(self, folder, indent=1):
        '''initialize a folder with a a dataset configuration (metadata) file

            Parameters
            ==========
            folder: the folder to initialize the metadata file in
        '''

        if not os.path.isdir(folder):
            sys.exit('Invalid folder: ' + folder)

        ref = self.config_values[self.CONFIG_NAME_USER] + '/INSERT_SLUG_HERE'

        meta_data = {'title': 'INSERT_TITLE_HERE', 
                     'id': ref, 
                     'licenses': [{'name': 'CC0-1.0'}]}

        meta_file = os.path.join(folder, self.METADATA_FILE)
        with open(meta_file, 'w') as f:
            json.dump(meta_data, f, indent=indent)

        print('Data package template written to: ' + meta_file)
        return meta_file


    def dataset_create_new(self,
                           folder,
                           public=False,
                           quiet=False,
                           convert_to_csv=True):
        '''create a new dataset, meaning the same as creating a version but
           with extra metadata like license and user/owner.

           Parameters
           ==========
           folder: the folder to initialize the metadata file in
           public: should the dataset be public?
           convert_to_csv: if True, convert data to comma separated value

        '''

        meta_data = _dataset_prepare_create_request(folder)
        license_name = self.get_or_exit(metadata['licenses'][0], 'name')

        request = DatasetNewRequest(
            title=meta_data.get('title'),
            slug=meta_data['dataset_slug'],
            owner_slug=meta_data['owner_slug'],
            license_name=license_name,
            subtitle=meta_data.get('subtitle'),
            description=meta_data.get('description'),
            files=[],
            is_private=not public,
            convert_to_csv=convert_to_csv,
            category_ids=meta_data.get('keywords'))
        resources = meta_data.get('resources')

        # Do the upload, return the result
        self.upload_files(request, resources, folder, quiet)
        result = DatasetNewResponse(
           self.process_response(self.datasets_create_new_with_http_info(request)))
        return result

    def dataset_create_new_cli(self,
                               folder,
                               public=False,
                               quiet=False,
                               convert_to_csv=True):
        '''client wrapper for creating a new dataset

           Parameters
           ==========
           folder: the folder to initialize the metadata file in
           public: should the dataset be public?
           convert_to_csv: if True, convert data to comma separated value

        '''
        # Convert to string to print to user

        if public:
            public = 'public'
        else:
            public = 'private'


        result = self.dataset_create_new(folder, public, quiet, convert_to_csv)
        if result.invalidTags is not None:
            print('The following are not valid tags and could not be added ' +
                  'to the dataset: ' + str(result.invalidTags))
        if result.status == 'ok':
            print('Your %s Dataset is being created. Please check ' % public
                  + ' progress at ' + result.url)
        else:
            print('Dataset creation error: ' + result.error)


## Download

    def download_file(self, 
                      response, 
                      outfile, 
                      quiet=True, 
                      chunk_size=1048576):
        '''download a file to an output file based on a chunk size
 
           Parameters
           ==========
           response: the response to download
           outfile: the output file to download to
           chunk_size: the size of the chunk to strema

        '''
        outpath = os.path.dirname(outfile)
        if not os.path.exists(outpath):
            os.makedirs(outpath)

        # Get the total size from the content length of the response
        size = int(response.headers['Content-Length'])
        size_read = 0

        if not quiet:
            print('Downloading ' + os.path.basename(outfile) + ' to ' + outpath)

        with tqdm(total=size, 
                  unit='B', 
                  unit_scale=True, 
                  unit_divisor=1024,
                  disable=quiet) as pbar:

            with open(outfile, 'wb') as out:
                while True:
                    data = response.read(chunk_size)
                    if not data:
                        break
                    out.write(data)
                    size_read = min(size, size_read + chunk_size)
                    pbar.update(len(data))

            if not quiet:
                print('\n', end='')

        # If we downloaded and have file, return it

        if os.path.exists(outfile):
            return outfile

    def download_needed(self, 
                        response, 
                        outfile, 
                        quiet=True):

        '''determine if a download is needed based on timestamp. Return True
           if needed (remote is newer) or False if local is newest.

           Parameters
           ==========
           response: the response from the API
           outfile: the output file to write to

        '''
        try:
            remote_date = datetime.strptime(response.headers['Last-Modified'],
                                            '%a, %d %b %Y %X %Z')
            if isfile(outfile):
                local_date = datetime.fromtimestamp(os.path.getmtime(outfile))

                # The remote date is older, download not needed
                if remote_date <= local_date:
                    if not quiet:
                        print(os.path.basename(outfile) +
                              ': Skipping, found more recently modified local' +
                              ' copy (use --force to force download)')
                    return False
        except:
            pass
        return True

## Helpers

    def string(self, item):
        return item if isinstance(item, unicode) else str(item)

    def get_or_exit(self, data, key):
        if key in data:
            return data[key]
        sys.exit('Key ' + key + ' not found in data')

    def get_or_default(self, data, key, default):
        if key in data:
            return data[key]
        return default

    def process_response(self, result):
        '''process a response from the API. We check the API version against
           the client's to see if it's old, and give them a warning (once)
  
           Parameters
           ==========
           result: the result from the API
        '''
        if len(result) == 3:
            data = result[0]
            headers = result[2]
            if self.HEADER_API_VERSION in headers:
                api_version = headers[self.HEADER_API_VERSION]
                older = self.__version__ < api_version
                if not self.already_printed_version_warning and older:
                    print('Warning: Looks like you\'re using an outdated API ' +
                          'Version, please consider updating (server ' + 
                           api_version + ' / client ' + self.__version__ + ')')
                    self.already_printed_version_warning = True
            return data
        return result

    def upload_files(self,
                     request, 
                     resources, 
                     folder, 
                     quiet=False):
        '''upload files in a folder

           Parameters
           ==========
           request: the prepared request
           resources: the files to upload
           folder: the folder to upload from

        '''

        for file_name in os.listdir(folder):

            # Skip the metadata file
            if file_name == self.METADATA_FILE:
                continue

            full_path = os.path.join(folder, file_name)

            if not quiet:
                print('Starting upload for file ' + file_name)

            # We can only upload with a token

            if os.path.isfile(full_path):
                content_length = os.path.getsize(full_path)
                token = self.dataset_upload_file(full_path, quiet)
                if token is None and not quiet:
                    print('Upload unsuccessful: ' + file_name)
                    return

                if not quiet:
                    print('Upload successful: ' + file_name + ' (' +
                           File.get_size(content_length) + ')')

                upload_file = DatasetUploadFile()
                upload_file.token = token
                if resources:
                    for item in resources:
                        if file_name == item.get('path'):
                            upload_file.description = item.get('description')
                            if 'schema' in item:
                                fields = self.get_or_default(item['schema'], 
                                                                  'fields', [])
                                processed = []
                                count = 0
                                for field in fields:
                                    processed.append(self.process_column(field))
                                    processed[count].order = count
                                    count += 1
                                upload_file.columns = processed

                request.files.append(upload_file)

            # File doesn't exist!
            else:
                if not quiet:
                    print('Skipping: ' + file_name)


        # Return the request, with files added

        return request


    def process_column(self, column):
        '''process a column, check for the type, and return the processed
           column'''

        processed_column = DatasetColumn(
            name=self.get_or_exit(column, 'name'),
            description=self.get_or_default(column, 'description', ''))

        if 'type' in column:
            original_type = column['type']
            processed_column.original_type = original_type
            if (original_type == 'string' or original_type == 'date' or
                original_type == 'time' or original_type == 'yearmonth' or
                original_type == 'duration' or original_type == 'geopoint' or
                original_type == 'geojson'): 
                processed_column.type = 'string'
            elif (original_type == 'numeric' or original_type == 'number' or
                  original_type == 'integer' or original_type == 'year'):
                  processed_column.type = 'numeric'
            elif original_type == 'boolean':
                processed_column.type = 'boolean'
            elif original_type == 'datetime':
                processed_column.type = 'datetime'
            else:
                processed_column.type = 'unknown'
        return processed_column

    def upload_complete(self, path, url, quiet):
        '''finish an upload, return False if an error, or True if status
           is 200 or 201

           Parameters
           ==========
           path: the path of the file uploaded (to get size)
           url: the url to upload complete to
        '''

        file_size = os.path.getsize(path)
        try:
            with tqdm(total=file_size,
                      unit='B',
                      unit_scale=True,
                      unit_divisor=1024,
                      disable=quiet) as progress_bar:
                with open(path, 'rb', buffering=0) as fp:
                    reader = TqdmBufferedReader(fp, progress_bar)
                    session = requests.Session()
                    retries = Retry(total=10, backoff_factor=0.5)
                    adapter = HTTPAdapter(max_retries=retries)
                    session.mount('http://', adapter)
                    session.mount('https://', adapter)
                    response = session.put(url, data=reader)

        except Exception as error:
            print(error)
            return False

        return response.status_code == 200 or response.status_code == 201
  

## Printing

    
    def print_result(self, 
                     listing, 
                     fields, 
                     name, 
                     csv_display=False):

        '''a wrapper to self.print_csv and self.print_table.
           
           Parameters
           ==========
           listing: the result listing to print
           fields: a list of fields to print
           name: the name to "pretty print" as a notification to the user
           csv_display: If True, print comma separated values

        '''
        if listing:
            if csv_display:
                self.print_csv(listing, fields)
            else:
                self.print_table(listing, fields)
        else:
            print('No %s found' % name)


    def print_table(self, items, fields):
        '''print a table of items, for a set of fields defined
   
           Parameters
           ==========
           items: a list of items to print
           fields: a list of fields to select from items

        '''
        formats = []
        borders = []

        # Define formats and borders for table

        for f in fields:
            length = max(
                len(f), max([len(self.string(getattr(i, f))) for i in items]))

            justify = '<'
            if isinstance(getattr(items[0], f)) or f == 'size' or f == 'reward':
                justify = '>'

            formats.append('{:' + justify + self.string(length + 2) + '}')
            borders.append('-' * length + '  ')

        row_format = u''.join(formats)
        headers = [f + '  ' for f in fields]

        # Print the header and table borders

        print(row_format.format(*headers))
        print(row_format.format(*borders))

        # Print the items

        for i in items:
            i_fields = [self.string(getattr(i, f)) + '  ' for f in fields]
            print(row_format.format(*i_fields))


    def print_csv(self, items, fields):
        '''print a set of fields in a set of items using a csv.writer

           Parameters
           ==========
           items: a list of items to print
           fields: a list of fields to select from items
        ''' 
        writer = csv.writer(sys.stdout)
        writer.writerow(fields)
        for i in items:
            i_fields = [self.string(getattr(i, f)) for f in fields]
            writer.writerow(i_fields)


class TqdmBufferedReader(io.BufferedReader):

  def __init__(self, raw, progress_bar):
    io.BufferedReader.__init__(self, raw)
    self.progress_bar = progress_bar

  def read(self, *args, **kwargs):
    buf = io.BufferedReader.read(self, *args, **kwargs)
    self.increment(len(buf))
    return buf

  def increment(self, length):
    self.progress_bar.update(length)
