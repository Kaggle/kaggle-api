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

# coding=utf-8
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
from ..models.kaggle_models_extended import Kernel
from ..models.kaggle_models_extended import KernelPushResponse
from ..models.kaggle_models_extended import LeaderboardEntry
from ..models.kaggle_models_extended import ListFilesResult
from ..models.kaggle_models_extended import Submission
from ..models.kaggle_models_extended import SubmitResult
from ..models.kernel_push_request import KernelPushRequest
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
    __version__ = '1.4.6'

    CONFIG_NAME_PROXY = 'proxy'
    CONFIG_NAME_COMPETITION = 'competition'
    CONFIG_NAME_PATH = 'path'
    CONFIG_NAME_USER = 'username'
    CONFIG_NAME_KEY = 'key'

    HEADER_API_VERSION = 'X-Kaggle-ApiVersion'
    DATASET_METADATA_FILE = 'dataset-metadata.json'
    OLD_DATASET_METADATA_FILE = 'datapackage.json'
    KERNEL_METADATA_FILE = 'kernel-metadata.json'

    config_dir = os.environ.get('KAGGLE_CONFIG_DIR') or os.path.join(
        expanduser('~'), '.kaggle')
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    config_file = 'kaggle.json'
    config = os.path.join(config_dir, config_file)
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
            config_data = self.read_config_file(config_data)

        # Step 2:, get username/password from environment
        config_data = self.read_config_environment(config_data)

        # Step 3: load into configuration!
        self._load_config(config_data)

    def read_config_environment(self, config_data={}, quiet=False):
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

        # Add all variables that start with KAGGLE_ to config data

        for key, val in os.environ.items():
            if key.startswith('KAGGLE_'):
                config_key = key.replace('KAGGLE_', '', 1).lower()
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
                raise ValueError('Error: Missing %s in configuration.' % item)

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
                raise ValueError(
                    'The specified proxy ' +
                    config_data[self.CONFIG_NAME_PROXY] +
                    ' is not valid, please check your proxy settings')
            else:
                raise ValueError(
                    'Unauthorized: you must download an API key or export '
                    'credentials to the environment. Please see\n ' +
                    'https://github.com/Kaggle/kaggle-api#api-credentials ' +
                    'for instructions.')

    def read_config_file(self, config_data, quiet=False):
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
                        print(
                            'Warning: Your Kaggle API key is readable by other'
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

    def _read_config_file(self):
        '''read in the configuration file, a json file defined at self.confi'''

        try:
            with open(self.config, 'r') as f:
                config_data = json.load(f)
        except FileNotFoundError:
            config_data = {}

        return config_data

    def _write_config_file(self, config_data, indent=2):
        '''write config data to file.
        '''
        with open(self.config, 'w') as f:
            json.dump(config_data, f, indent=indent)

    def set_config_value(self, name, value, quiet=False):
        '''a client helper function to set a configuration value, meaning
           reading in the configuration file (if it exists), saving a new
           config value, and then writing back
        '''

        config_data = self._read_config_file()

        if value is not None:

            # Update the config file with the value
            config_data[name] = value

            # Update the instance with the value
            self.config_values[name] = value

            # If defined by client, set and save!
            self._write_config_file(config_data)

            if not quiet:
                self.print_config_value(name, separator=' is now set to: ')

    def unset_config_value(self, name, quiet=False):
        '''unset a configuration value'''

        config_data = self._read_config_file()

        if name in config_data:

            del config_data[name]

            self._write_config_file(config_data)

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

    def get_default_download_dir(self, *subdirs):
        '''get the path configuration value, otherwise return default.
        '''
        # Look up value for key "path" in the config
        path = self.get_config_value(self.CONFIG_NAME_PATH)

        # If not set in config, default to present working directory
        if path is None:
            return os.getcwd()

        return os.path.join(path, *subdirs)

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
        print('Configuration values from ' + self.config_dir)
        self.print_config_value(self.CONFIG_NAME_USER, prefix='- ')
        self.print_config_value(self.CONFIG_NAME_PATH, prefix='- ')
        self.print_config_value(self.CONFIG_NAME_PROXY, prefix='- ')
        self.print_config_value(self.CONFIG_NAME_COMPETITION, prefix='- ')


## Competitions

    def competitions_list(self,
                          group=None,
                          category=None,
                          sort_by=None,
                          page=1,
                          search=None):
        valid_groups = ['general', 'entered', 'inClass']
        if group and group not in valid_groups:
            raise ValueError('Invalid group specified. Valid options are ' +
                             str(valid_groups))

        valid_categories = [
            'all', 'featured', 'research', 'recruitment', 'gettingStarted',
            'masters', 'playground'
        ]
        if category and category not in valid_categories:
            raise ValueError('Invalid category specified. Valid options are ' +
                             str(valid_categories))

        valid_sort_by = [
            'grouped', 'prize', 'earliestDeadline', 'latestDeadline',
            'numberOfTeams', 'recentlyCreated'
        ]
        if sort_by and sort_by not in valid_sort_by:
            raise ValueError('Invalid sort_by specified. Valid options are ' +
                             str(valid_sort_by))

        competitions_list_result = self.process_response(
            self.competitions_list_with_http_info(
                group=group or '',
                category=category or '',
                sort_by=sort_by or '',
                page=page,
                search=search or ''))
        return [Competition(c) for c in competitions_list_result]

    def competitions_list_cli(self,
                              group=None,
                              category=None,
                              sort_by=None,
                              page=1,
                              search=None,
                              csv_display=False):
        competitions = self.competitions_list(
            group=group,
            category=category,
            sort_by=sort_by,
            page=page,
            search=search)
        fields = [
            'ref', 'deadline', 'category', 'reward', 'teamCount',
            'userHasEntered'
        ]
        if competitions:
            if csv_display:
                self.print_csv(competitions, fields)
            else:
                self.print_table(competitions, fields)
        else:
            print('No competitions found')

    def competition_submit(self, file_name, message, competition, quiet=False):
        if competition is None:
            competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
            if competition is not None and not quiet:
                print('Using competition: ' + competition)

        if competition is None:
            raise ValueError('No competition specified')
        else:
            url_result = self.process_response(
                self.competitions_submissions_url_with_http_info(
                    file_name=os.path.basename(file_name),
                    content_length=os.path.getsize(file_name),
                    last_modified_date_utc=int(
                        os.path.getmtime(file_name) * 1000)))
            url_result_list = url_result['createUrl'].split('/')
            upload_result = self.process_response(
                self.competitions_submissions_upload_with_http_info(
                    file=file_name,
                    guid=url_result_list[-3],
                    content_length=url_result_list[-2],
                    last_modified_date_utc=url_result_list[-1]))
            upload_result_token = upload_result['token']
            submit_result = self.process_response(
                self.competitions_submissions_submit_with_http_info(
                    id=competition,
                    blob_file_tokens=upload_result_token,
                    submission_description=message))
            return SubmitResult(submit_result)

    def competition_submit_cli(self,
                               file_name,
                               message,
                               competition,
                               competition_opt=None,
                               quiet=False):
        competition = competition or competition_opt
        try:
            submit_result = self.competition_submit(file_name, message,
                                                    competition, quiet)
        except ApiException as e:
            if e.status == 404:
                print('Could not find competition - please verify that you '
                      'entered the correct competition ID and that the '
                      'competition is still accepting submissions.')
                return None
            else:
                raise e
        return submit_result

    def competition_submissions(self, competition):
        submissions_result = self.process_response(
            self.competitions_submissions_list_with_http_info(id=competition))
        return [Submission(s) for s in submissions_result]

    def competition_submissions_cli(self,
                                    competition=None,
                                    competition_opt=None,
                                    csv_display=False,
                                    quiet=False):
        competition = competition or competition_opt
        if competition is None:
            competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
            if competition is not None and not quiet:
                print('Using competition: ' + competition)

        if competition is None:
            raise ValueError('No competition specified')
        else:
            submissions = self.competition_submissions(competition)
            fields = [
                'fileName', 'date', 'description', 'status', 'publicScore',
                'privateScore'
            ]
            if submissions:
                if csv_display:
                    self.print_csv(submissions, fields)
                else:
                    self.print_table(submissions, fields)
            else:
                print('No submissions found')

    def competition_list_files(self, competition):
        competition_list_files_result = self.process_response(
            self.competitions_data_list_files_with_http_info(id=competition))
        return [File(f) for f in competition_list_files_result]

    def competition_list_files_cli(self,
                                   competition,
                                   competition_opt=None,
                                   csv_display=False,
                                   quiet=False):
        competition = competition or competition_opt
        if competition is None:
            competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
            if competition is not None and not quiet:
                print('Using competition: ' + competition)

        if competition is None:
            raise ValueError('No competition specified')
        else:
            files = self.competition_list_files(competition)
            fields = ['name', 'size', 'creationDate']
            if files:
                if csv_display:
                    self.print_csv(files, fields)
                else:
                    self.print_table(files, fields)
            else:
                print('No files found')

    def competition_download_file(self,
                                  competition,
                                  file_name,
                                  path=None,
                                  force=False,
                                  quiet=False):
        if path is None:
            effective_path = self.get_default_download_dir(
                'competitions', competition)
        else:
            effective_path = path

        response = self.process_response(
            self.competitions_data_download_file_with_http_info(
                id=competition, file_name=file_name, _preload_content=False))
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
        if not files:
            print('This competition does not have any available data files')
        for file_name in files:
            self.competition_download_file(competition, file_name.ref, path,
                                           force, quiet)

    def competition_download_cli(self,
                                 competition,
                                 competition_opt=None,
                                 file_name=None,
                                 path=None,
                                 force=False,
                                 quiet=False):
        competition = competition or competition_opt
        if competition is None:
            competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
            if competition is not None and not quiet:
                print('Using competition: ' + competition)

        if competition is None:
            raise ValueError('No competition specified')
        else:
            if file_name is None:
                self.competition_download_files(competition, path, force,
                                                quiet)
            else:
                self.competition_download_file(competition, file_name, path,
                                               force, quiet)

    def competition_leaderboard_download(self, competition, path, quiet=True):
        response = self.process_response(
            self.competition_download_leaderboard_with_http_info(
                competition, _preload_content=False))

        if path is None:
            effective_path = self.get_default_download_dir(
                'competitions', competition)
        else:
            effective_path = path

        file_name = competition + '.zip'
        outfile = os.path.join(effective_path, file_name)
        self.download_file(response, outfile, quiet)

    def competition_leaderboard_view(self, competition):
        result = self.process_response(
            self.competition_view_leaderboard_with_http_info(competition))
        return [LeaderboardEntry(e) for e in result['submissions']]

    def competition_leaderboard_cli(self,
                                    competition,
                                    competition_opt=None,
                                    path=None,
                                    view=False,
                                    download=False,
                                    csv_display=False,
                                    quiet=False):
        competition = competition or competition_opt
        if not view and not download:
            raise ValueError('Either --show or --download must be specified')

        if competition is None:
            competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
            if competition is not None and not quiet:
                print('Using competition: ' + competition)

        if competition is None:
            raise ValueError('No competition specified')

        if download:
            self.competition_leaderboard_download(competition, path, quiet)

        if view:
            results = self.competition_leaderboard_view(competition)
            fields = ['teamId', 'teamName', 'submissionDate', 'score']
            if results:
                if csv_display:
                    self.print_csv(results, fields)
                else:
                    self.print_table(results, fields)
            else:
                print('No results found')

    def dataset_list(self,
                     sort_by=None,
                     size=None,
                     file_type=None,
                     license_name=None,
                     tag_ids=None,
                     search=None,
                     user=None,
                     mine=False,
                     page=1):
        valid_sort_bys = ['hottest', 'votes', 'updated', 'active', 'published']
        if sort_by and sort_by not in valid_sort_bys:
            raise ValueError('Invalid sort by specified. Valid options are ' +
                             str(valid_sort_bys))

        valid_sizes = ['all', 'small', 'medium', 'large']
        if size and size not in valid_sizes:
            raise ValueError('Invalid size specified. Valid options are ' +
                             str(valid_sizes))

        valid_file_types = ['all', 'csv', 'sqlite', 'json', 'bigQuery']
        if file_type and file_type not in valid_file_types:
            raise ValueError('Invalid file type specified. Valid options are '
                             + str(valid_file_types))

        valid_license_names = ['all', 'cc', 'gpl', 'odb', 'other']
        if license_name and license_name not in valid_license_names:
            raise ValueError('Invalid license specified. Valid options are ' +
                             str(valid_license_names))

        if int(page) <= 0:
            raise ValueError('Page number must be >= 1')

        group = 'public'
        if mine:
            group = 'my'
            if user:
                raise ValueError('Cannot specify both mine and a user')
        if user:
            group = 'user'

        datasets_list_result = self.process_response(
            self.datasets_list_with_http_info(
                group=group,
                sort_by=sort_by or 'hottest',
                size=size or 'all',
                filetype=file_type or 'all',
                license=license_name or 'all',
                tagids=tag_ids or '',
                search=search or '',
                user=user or '',
                page=page))
        return [Dataset(d) for d in datasets_list_result]

    def dataset_list_cli(self,
                         sort_by=None,
                         size=None,
                         file_type=None,
                         license_name=None,
                         tag_ids=None,
                         search=None,
                         user=None,
                         mine=False,
                         page=1,
                         csv_display=False):
        datasets = self.dataset_list(sort_by, size, file_type, license_name,
                                     tag_ids, search, user, mine, page)
        fields = ['ref', 'title', 'size', 'lastUpdated', 'downloadCount']
        if datasets:
            if csv_display:
                self.print_csv(datasets, fields)
            else:
                self.print_table(datasets, fields)
        else:
            print('No datasets found')

    def dataset_view(self, dataset):
        if '/' in dataset:
            self.validate_dataset_string(dataset)
            dataset_urls = dataset.split('/')
            owner_slug = dataset_urls[0]
            dataset_slug = dataset_urls[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            dataset_slug = dataset

        result = self.process_response(
            self.datasets_view_with_http_info(owner_slug, dataset_slug))
        return Dataset(result)

    def dataset_metadata(self, dataset, path):
        if dataset is None:
            raise ValueError('A dataset must be specified')
        if '/' in dataset:
            self.validate_dataset_string(dataset)
            dataset_urls = dataset.split('/')
            owner_slug = dataset_urls[0]
            dataset_slug = dataset_urls[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            dataset_slug = dataset

        if path is None:
            effective_path = self.get_default_download_dir(
                'datasets', owner_slug, dataset_slug)
        else:
            effective_path = path

        if not os.path.exists(effective_path):
            os.makedirs(effective_path)

        result = self.process_response(
            self.datasets_view_with_http_info(owner_slug, dataset_slug))

        data = {}
        data['id'] = result['ref']
        data['id_no'] = result['id']
        data['title'] = result['title']
        data['subtitle'] = result['subtitle']
        data['description'] = result['description']
        data['keywords'] = list(map(lambda t: t['name'], result['tags']))
        data['resources'] = list(
            map(lambda r: self.convert_to_dataset_file_metadata(r, effective_path),
                result['files']))

        meta_file = os.path.join(effective_path, self.DATASET_METADATA_FILE)
        with open(meta_file, 'w') as f:
            json.dump(data, f, indent=2)

        return meta_file

    def dataset_metadata_cli(self, dataset, path, dataset_opt=None):
        dataset = dataset or dataset_opt
        meta_file = self.dataset_metadata(dataset, path)
        print('Downloaded metadata to ' + meta_file)

    def dataset_list_files(self, dataset):
        if dataset is None:
            raise ValueError('A dataset must be specified')
        if '/' in dataset:
            self.validate_dataset_string(dataset)
            dataset_urls = dataset.split('/')
            owner_slug = dataset_urls[0]
            dataset_slug = dataset_urls[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            dataset_slug = dataset
        dataset_list_files_result = self.process_response(
            self.datasets_list_files_with_http_info(
                owner_slug=owner_slug, dataset_slug=dataset_slug))
        return ListFilesResult(dataset_list_files_result)

    def dataset_list_files_cli(self,
                               dataset,
                               dataset_opt=None,
                               csv_display=False):
        dataset = dataset or dataset_opt
        result = self.dataset_list_files(dataset)
        if result:
            if result.error_message:
                print(result.error_message)
            else:
                fields = ['name', 'size', 'creationDate']
                if csv_display:
                    self.print_csv(result.files, fields)
                else:
                    self.print_table(result.files, fields)
        else:
            print('No files found')

    def dataset_status(self, dataset):
        if dataset is None:
            raise ValueError('A dataset must be specified')
        if '/' in dataset:
            self.validate_dataset_string(dataset)
            dataset_urls = dataset.split('/')
            owner_slug = dataset_urls[0]
            dataset_slug = dataset_urls[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            dataset_slug = dataset
        dataset_status_result = self.process_response(
            self.datasets_status_with_http_info(
                owner_slug=owner_slug, dataset_slug=dataset_slug))
        return dataset_status_result

    def dataset_status_cli(self, dataset, dataset_opt=None):
        dataset = dataset or dataset_opt
        return self.dataset_status(dataset)

    def dataset_download_file(self,
                              dataset,
                              file_name,
                              path=None,
                              force=False,
                              quiet=True):
        if '/' in dataset:
            self.validate_dataset_string(dataset)
            dataset_urls = dataset.split('/')
            owner_slug = dataset_urls[0]
            dataset_slug = dataset_urls[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            dataset_slug = dataset

        if path is None:
            effective_path = self.get_default_download_dir(
                'datasets', owner_slug, dataset_slug)
        else:
            effective_path = path

        response = self.process_response(
            self.datasets_download_file_with_http_info(
                owner_slug=owner_slug,
                dataset_slug=dataset_slug,
                file_name=file_name,
                _preload_content=False))
        url = response.retries.history[0].redirect_location.split('?')[0]
        outfile = os.path.join(effective_path, url.split('/')[-1])
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
        if dataset is None:
            raise ValueError('A dataset must be specified')
        if '/' in dataset:
            self.validate_dataset_string(dataset)
            dataset_urls = dataset.split('/')
            owner_slug = dataset_urls[0]
            dataset_slug = dataset_urls[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            dataset_slug = dataset

        if path is None:
            effective_path = self.get_default_download_dir(
                'datasets', owner_slug, dataset_slug)
        else:
            effective_path = path

        response = self.process_response(
            self.datasets_download_with_http_info(
                owner_slug=owner_slug,
                dataset_slug=dataset_slug,
                _preload_content=False))

        outfile = os.path.join(effective_path, dataset_slug + '.zip')
        if force or self.download_needed(response, outfile, quiet):
            self.download_file(response, outfile, quiet)
            downloaded = True
        else:
            downloaded = False

        if downloaded:
            outfile = os.path.join(effective_path, dataset_slug + '.zip')
            try:
                with zipfile.ZipFile(outfile) as z:
                    z.extractall(effective_path)
            except zipfile.BadZipFile as e:
                raise ValueError(
                    'Bad zip file, please report on '
                    'www.github.com/kaggle/kaggle-api', e)

    def dataset_download_cli(self,
                             dataset,
                             dataset_opt=None,
                             file_name=None,
                             path=None,
                             force=False,
                             quiet=False):
        dataset = dataset or dataset_opt
        if file_name is None:
            self.dataset_download_files(dataset, path, force, quiet)
        else:
            self.dataset_download_file(dataset, file_name, path, force, quiet)

    def dataset_upload_file(self, path, quiet):
        file_name = os.path.basename(path)
        content_length = os.path.getsize(path)
        last_modified_date_utc = int(os.path.getmtime(path))
        result = FileUploadInfo(
            self.process_response(
                self.datasets_upload_file_with_http_info(
                    file_name, content_length, last_modified_date_utc)))

        success = self.upload_complete(path, result.createUrl, quiet)

        if success:
            return result.token
        return None

    def dataset_create_version(self,
                               folder,
                               version_notes,
                               quiet=False,
                               convert_to_csv=True,
                               delete_old_versions=False):
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_file = self.get_dataset_metadata_file(folder)

        # read json
        with open(meta_file, 'r') as f:
            meta_data = json.load(f)
        ref = self.get_or_default(meta_data, 'id', None)
        id_no = self.get_or_default(meta_data, 'id_no', None)
        if not ref and not id_no:
            raise ValueError('ID or slug must be specified in the metadata')

        subtitle = meta_data.get('subtitle')
        if subtitle and (len(subtitle) < 20 or len(subtitle) > 80):
            raise ValueError(
                'Subtitle length must be between 20 and 80 characters')
        resources = meta_data.get('resources')
        self.validate_resources(folder, resources)

        description = meta_data.get('description')
        keywords = self.get_or_default(meta_data, 'keywords', [])

        request = DatasetNewVersionRequest(
            version_notes=version_notes,
            subtitle=subtitle,
            description=description,
            files=[],
            convert_to_csv=convert_to_csv,
            category_ids=keywords,
            delete_old_versions=delete_old_versions)
        self.upload_files(request, resources, folder, quiet)

        if id_no:
            result = DatasetNewVersionResponse(
                self.process_response(
                    self.datasets_create_version_by_id_with_http_info(
                        id_no, request)))
        else:
            if ref == self.config_values[self.
                                         CONFIG_NAME_USER] + '/INSERT_SLUG_HERE':
                raise ValueError(
                    'Default slug detected, please change values before '
                    'uploading')
            self.validate_dataset_string(ref)
            ref_list = ref.split('/')
            owner_slug = ref_list[0]
            dataset_slug = ref_list[1]
            result = DatasetNewVersionResponse(
                self.process_response(
                    self.datasets_create_version_with_http_info(
                        owner_slug, dataset_slug, request)))

        return result

    def dataset_create_version_cli(self,
                                   folder,
                                   version_notes,
                                   quiet=False,
                                   convert_to_csv=True,
                                   delete_old_versions=False):
        result = self.dataset_create_version(
            folder,
            version_notes,
            quiet=quiet,
            convert_to_csv=convert_to_csv,
            delete_old_versions=delete_old_versions)
        if result.invalidTags:
            print(
                ('The following are not valid tags and could not be added to '
                 'the dataset: ') + str(result.invalidTags))
        if result is None:
            print('Dataset version creation error: See previous output')
        elif result.status.lower() == 'ok':
            print('Dataset version is being created. Please check progress at '
                  + result.url)
        else:
            print('Dataset version creation error: ' + result.error)

    def dataset_initialize(self, folder):
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        ref = self.config_values[self.CONFIG_NAME_USER] + '/INSERT_SLUG_HERE'
        licenses = []
        default_license = {'name': 'CC0-1.0'}
        licenses.append(default_license)

        meta_data = {
            'title': 'INSERT_TITLE_HERE',
            'id': ref,
            'licenses': licenses
        }
        meta_file = os.path.join(folder, self.DATASET_METADATA_FILE)
        with open(meta_file, 'w') as f:
            json.dump(meta_data, f, indent=2)

        print('Data package template written to: ' + meta_file)
        return meta_file

    def dataset_initialize_cli(self, folder=None):
        if folder is None:
            folder = os.getcwd()
        self.dataset_initialize(folder)

    def dataset_create_new(self,
                           folder,
                           public=False,
                           quiet=False,
                           convert_to_csv=True):
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_file = self.get_dataset_metadata_file(folder)

        # read json
        with open(meta_file, 'r') as f:
            meta_data = json.load(f)
        ref = self.get_or_fail(meta_data, 'id')
        title = self.get_or_fail(meta_data, 'title')
        licenses = self.get_or_fail(meta_data, 'licenses')
        ref_list = ref.split('/')
        owner_slug = ref_list[0]
        dataset_slug = ref_list[1]

        # validations
        if ref == self.config_values[self.
                                     CONFIG_NAME_USER] + '/INSERT_SLUG_HERE':
            raise ValueError(
                'Default slug detected, please change values before uploading')
        if title == 'INSERT_TITLE_HERE':
            raise ValueError(
                'Default title detected, please change values before uploading'
            )
        if len(licenses) != 1:
            raise ValueError('Please specify exactly one license')
        if len(dataset_slug) < 6 or len(dataset_slug) > 50:
            raise ValueError(
                'The dataset slug must be between 6 and 50 characters')
        if len(title) < 6 or len(title) > 50:
            raise ValueError(
                'The dataset title must be between 6 and 50 characters')
        resources = meta_data.get('resources')
        if resources:
            self.validate_resources(folder, resources)

        license_name = self.get_or_fail(licenses[0], 'name')
        description = meta_data.get('description')
        keywords = self.get_or_default(meta_data, 'keywords', [])

        subtitle = meta_data.get('subtitle')
        if subtitle and (len(subtitle) < 20 or len(subtitle) > 80):
            raise ValueError(
                'Subtitle length must be between 20 and 80 characters')

        request = DatasetNewRequest(
            title=title,
            slug=dataset_slug,
            owner_slug=owner_slug,
            license_name=license_name,
            subtitle=subtitle,
            description=description,
            files=[],
            is_private=not public,
            convert_to_csv=convert_to_csv,
            category_ids=keywords)
        resources = meta_data.get('resources')
        self.upload_files(request, resources, folder, quiet)
        result = DatasetNewResponse(
            self.process_response(
                self.datasets_create_new_with_http_info(request)))

        return result

    def dataset_create_new_cli(self,
                               folder=None,
                               public=False,
                               quiet=False,
                               convert_to_csv=True):
        if folder is None:
            folder = os.getcwd()
        result = self.dataset_create_new(folder, public, quiet, convert_to_csv)
        if result.invalidTags:
            print('The following are not valid tags and could not be added to '
                  'the dataset: ' + str(result.invalidTags))
        if result.status.lower() == 'ok':
            if public:
                print('Your public Dataset is being created. Please check '
                      'progress at ' + result.url)
            else:
                print('Your private Dataset is being created. Please check '
                      'progress at ' + result.url)
        else:
            print('Dataset creation error: ' + result.error)

    def download_file(self, response, outfile, quiet=True, chunk_size=1048576):
        outpath = os.path.dirname(outfile)
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        size = int(response.headers['Content-Length'])
        size_read = 0
        if not quiet:
            print('Downloading ' + os.path.basename(outfile) + ' to ' +
                  outpath)
        with tqdm(
                total=size,
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

    def kernels_list(self,
                     page=1,
                     page_size=20,
                     dataset=None,
                     competition=None,
                     parent_kernel=None,
                     search=None,
                     mine=False,
                     user=None,
                     language=None,
                     kernel_type=None,
                     output_type=None,
                     sort_by=None):
        if int(page) <= 0:
            raise ValueError('Page number must be >= 1')

        page_size = int(page_size)
        if page_size <= 0:
            raise ValueError('Page size must be >= 1')
        if page_size > 100:
            page_size = 100

        valid_languages = ['all', 'python', 'r', 'sqlite', 'julia']
        if language and language not in valid_languages:
            raise ValueError('Invalid language specified. Valid options are ' +
                             str(valid_languages))

        valid_kernel_types = ['all', 'script', 'notebook']
        if kernel_type and kernel_type not in valid_kernel_types:
            raise ValueError(
                'Invalid kernel type specified. Valid options are ' +
                str(valid_kernel_types))

        valid_output_types = ['all', 'visualization', 'data']
        if output_type and output_type not in valid_output_types:
            raise ValueError(
                'Invalid output type specified. Valid options are ' +
                str(valid_output_types))

        valid_sort_by = [
            'hotness', 'commentCount', 'dateCreated', 'dateRun', 'relevance',
            'scoreAscending', 'scoreDescending', 'viewCount', 'voteCount'
        ]
        if sort_by and sort_by not in valid_sort_by:
            raise ValueError(
                'Invalid sort by type specified. Valid options are ' +
                str(valid_sort_by))
        if sort_by == 'relevance' and search == '':
            raise ValueError('Cannot sort by relevance without a search term.')

        self.validate_dataset_string(dataset)
        self.validate_kernel_string(parent_kernel)

        group = 'everyone'
        if mine:
            group = 'profile'

        kernels_list_result = self.process_response(
            self.kernels_list_with_http_info(
                page=page,
                page_size=page_size,
                group=group,
                user=user or '',
                language=language or 'all',
                kernel_type=kernel_type or 'all',
                output_type=output_type or 'all',
                sort_by=sort_by or 'hotness',
                dataset=dataset or '',
                competition=competition or '',
                parent_kernel=parent_kernel or '',
                search=search or ''))
        return [Kernel(k) for k in kernels_list_result]

    def kernels_list_cli(self,
                         mine=False,
                         page=1,
                         page_size=20,
                         search=None,
                         csv_display=False,
                         parent=None,
                         competition=None,
                         dataset=None,
                         user=None,
                         language=None,
                         kernel_type=None,
                         output_type=None,
                         sort_by=None):
        kernels = self.kernels_list(
            page=page,
            page_size=page_size,
            search=search,
            mine=mine,
            dataset=dataset,
            competition=competition,
            parent_kernel=parent,
            user=user,
            language=language,
            kernel_type=kernel_type,
            output_type=output_type,
            sort_by=sort_by)
        fields = ['ref', 'title', 'author', 'lastRunTime', 'totalVotes']
        if kernels:
            if csv_display:
                self.print_csv(kernels, fields)
            else:
                self.print_table(kernels, fields)
        else:
            print('No kernels found')

    def kernels_initialize(self, folder, kernel=None):
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        resources = []
        resource = {'path': 'INSERT_SCRIPT_PATH_HERE'}
        resources.append(resource)

        username = self.get_config_value(self.CONFIG_NAME_USER)
        meta_data = {
            'id': username + '/INSERT_KERNEL_SLUG_HERE',
            'title': 'INSERT_TITLE_HERE',
            'code_file': 'INSERT_CODE_FILE_PATH_HERE',
            'language': 'INSERT_LANGUAGE_HERE',
            'kernel_type': 'INSERT_KERNEL_TYPE_HERE',
            'is_private': 'true',
            'enable_gpu': 'false',
            'enable_internet': 'false',
            'dataset_sources': [],
            'competition_sources': [],
            'kernel_sources': [],
        }
        meta_file = os.path.join(folder, self.KERNEL_METADATA_FILE)
        with open(meta_file, 'w') as f:
            json.dump(meta_data, f, indent=2)

        return meta_file

    def kernels_initialize_cli(self, folder=None, kernel=None):
        if folder is None:
            folder = os.getcwd()
        meta_file = self.kernels_initialize(folder, kernel)
        print('Kernel metadata template written to: ' + meta_file)

    def kernels_push(self, folder):
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_file = os.path.join(folder, self.KERNEL_METADATA_FILE)
        if not os.path.isfile(meta_file):
            raise ValueError('Metadata file not found: ' +
                             self.KERNEL_METADATA_FILE)

        with open(meta_file, 'r') as f:
            meta_data = json.load(f)

        code_path = self.get_or_default(meta_data, 'code_file', '')
        if not code_path:
            raise ValueError('A source file must be specified in the metadata')

        code_file = os.path.join(folder, code_path)
        if not os.path.isfile(code_file):
            raise ValueError('Source file not found: ' + code_file)

        slug = meta_data.get('id')
        id_no = meta_data.get('id_no')
        if not slug and not id_no:
            raise ValueError('ID or slug must be specified in the metadata')
        if slug:
            self.validate_kernel_string(slug)

        valid_languages = ['python', 'r', 'rmarkdown']
        language = self.get_or_default(meta_data, 'language', '')
        if language not in valid_languages:
            raise ValueError(
                'A valid language must be specified in the metadata. Valid '
                'options are ' + str(valid_languages))

        valid_kernel_types = ['script', 'notebook']
        kernel_type = self.get_or_default(meta_data, 'kernel_type', '')
        if kernel_type not in valid_kernel_types:
            raise ValueError(
                'A valid kernel type must be specified in the metadata. Valid '
                'options are ' + str(valid_kernel_types))

        if kernel_type == 'notebook' and language == 'rmarkdown':
            language = 'r'

        dataset_sources = self.get_or_default(meta_data, 'dataset_sources', [])
        for source in dataset_sources:
            self.validate_dataset_string(source)

        kernel_sources = self.get_or_default(meta_data, 'kernel_sources', [])
        for source in kernel_sources:
            self.validate_kernel_string(source)

        with open(code_file, 'r') as f:
            script_body = f.read()

        if kernel_type == 'notebook':
            json_body = json.loads(script_body)
            if 'cells' in json_body:
                for cell in json_body['cells']:
                    if 'outputs' in cell and cell['cell_type'] == 'code':
                        cell['outputs'] = []
            script_body = json.dumps(json_body)

        kernel_push_request = KernelPushRequest(
            id=id_no,
            slug=slug,
            new_title=self.get_or_default(meta_data, 'title', None),
            text=script_body,
            language=language,
            kernel_type=kernel_type,
            is_private=self.get_or_default(meta_data, 'is_private', None),
            enable_gpu=self.get_or_default(meta_data, 'enable_gpu', None),
            enable_internet=self.get_or_default(meta_data, 'enable_internet',
                                                None),
            dataset_data_sources=dataset_sources,
            competition_data_sources=self.get_or_default(
                meta_data, 'competition_sources', []),
            kernel_data_sources=kernel_sources,
            category_ids=self.get_or_default(meta_data, 'keywords', []))

        result = KernelPushResponse(
            self.process_response(
                self.kernel_push_with_http_info(
                    kernel_push_request=kernel_push_request)))
        return result

    def kernels_push_cli(self, folder):
        folder = folder or os.getcwd()
        result = self.kernels_push(folder)

        if result is None:
            print('Kernel push error: see previous output')
        elif not result.error:
            if result.invalidTags:
                print(
                    'The following are not valid tags and could not be added '
                    'to the kernel: ' + str(result.invalidTags))
            if result.invalidDatasetSources:
                print(
                    'The following are not valid dataset sources and could not '
                    'be added to the kernel: ' +
                    str(result.invalidDatasetSources))
            if result.invalidCompetitionSources:
                print(
                    'The following are not valid competition sources and could '
                    'not be added to the kernel: ' +
                    str(result.invalidCompetitionSources))
            if result.invalidKernelSources:
                print(
                    'The following are not valid kernel sources and could not '
                    'be added to the kernel: ' +
                    str(result.invalidKernelSources))
            print('Kernel successfully pushed.  Please check progress at ' +
                  result.url)
        else:
            print('Kernel push error: ' + result.error)

    def kernels_pull(self, kernel, path, metadata=False, quiet=True):
        if kernel is None:
            if path is None:
                existing_metadata_path = os.path.join(
                    os.getcwd(), self.KERNEL_METADATA_FILE)
            else:
                existing_metadata_path = os.path.join(
                    path, self.KERNEL_METADATA_FILE)
            if os.path.exists(existing_metadata_path):
                with open(existing_metadata_path) as f:
                    existing_metadata = json.load(f)
                    kernel = existing_metadata['id']
                    if 'INSERT_KERNEL_SLUG_HERE' in kernel:
                        raise ValueError('A kernel must be specified')
                    else:
                        print('Using kernel ' + kernel)

        if '/' in kernel:
            self.validate_kernel_string(kernel)
            kernel_url_list = kernel.split('/')
            owner_slug = kernel_url_list[0]
            kernel_slug = kernel_url_list[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            kernel_slug = kernel

        if path is None:
            effective_path = self.get_default_download_dir(
                'kernels', owner_slug, kernel_slug)
        else:
            effective_path = path

        if not os.path.exists(effective_path):
            os.makedirs(effective_path)

        response = self.process_response(
            self.kernel_pull_with_http_info(owner_slug, kernel_slug))
        blob = response['blob']

        if not os.path.isfile(effective_path):
            language = blob['language'].lower()
            kernel_type = blob['kernelType'].lower()
            extension = None
            if kernel_type == 'script':
                if language == 'python':
                    extension = '.py'
                elif language == 'r':
                    extension = '.R'
                elif language == 'rmarkdown':
                    extension = '.Rmd'
                elif language == 'sqlite':
                    extension = '.sql'
                elif language == 'julia':
                    extension = '.jl'
            elif kernel_type == 'notebook':
                if language == 'python':
                    extension = '.ipynb'
                elif language == 'r':
                    extension = '.irnb'
                elif language == 'julia':
                    extension = '.ijlnb'
            file_name = blob['slug'] + extension

            if file_name is None:
                print(
                    'Unknown language %s + kernel type %s - please report this '
                    'on the kaggle-api github issues' % (language,
                                                         kernel_type))
                print(
                    'Saving as a python file, even though this may not be the '
                    'correct language')
                file_name = 'script.py'
            script_path = os.path.join(effective_path, file_name)
        else:
            script_path = effective_path
            file_name = os.path.basename(effective_path)

        with open(script_path, 'w') as f:
            f.write(blob['source'])

        if metadata:
            if os.path.isfile(effective_path):
                effective_dir = os.path.dirname(effective_path)
            else:
                effective_dir = effective_path

            data = {}

            server_metadata = response['metadata']
            data['id'] = server_metadata['ref']
            data['id_no'] = server_metadata['id']
            data['title'] = server_metadata['title']
            data['code_file'] = file_name
            data['language'] = server_metadata['language']
            data['kernel_type'] = server_metadata['kernelType']
            self.set_if_present(server_metadata, 'isPrivate', data,
                                'is_private')
            self.set_if_present(server_metadata, 'enableGpu', data,
                                'enable_gpu')
            self.set_if_present(server_metadata, 'enableInternet', data,
                                'enable_internet')
            self.set_if_present(server_metadata, 'categoryIds', data,
                                'keywords')
            self.set_if_present(server_metadata, 'datasetDataSources', data,
                                'dataset_sources')
            self.set_if_present(server_metadata, 'kernelDataSources', data,
                                'kernel_sources')
            self.set_if_present(server_metadata, 'competitionDataSources',
                                data, 'competition_sources')

            metadata_path = os.path.join(effective_dir,
                                         self.KERNEL_METADATA_FILE)
            with open(metadata_path, 'w') as f:
                json.dump(data, f, indent=2)

            return effective_dir
        else:
            return script_path

    def kernels_pull_cli(self,
                         kernel,
                         kernel_opt=None,
                         path=None,
                         metadata=False):
        kernel = kernel or kernel_opt
        effective_path = self.kernels_pull(
            kernel, path=path, metadata=metadata, quiet=False)
        if metadata:
            print('Source code and metadata downloaded to ' + effective_path)
        else:
            print('Source code downloaded to ' + effective_path)

    def kernels_output(self, kernel, path, force=False, quiet=True):
        if kernel is None:
            raise ValueError('A kernel must be specified')
        if '/' in kernel:
            self.validate_kernel_string(kernel)
            kernel_url_list = kernel.split('/')
            owner_slug = kernel_url_list[0]
            kernel_slug = kernel_url_list[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            kernel_slug = kernel

        if path is None:
            target_dir = self.get_default_download_dir('kernels', owner_slug,
                                                       kernel_slug, 'output')
        else:
            target_dir = path

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        if not os.path.isdir(target_dir):
            raise ValueError(
                'You must specify a directory for the kernels output')

        response = self.process_response(
            self.kernel_output_with_http_info(owner_slug, kernel_slug))
        outfiles = []
        for item in response['files']:
            outfile = os.path.join(target_dir, item['fileName'])
            outfiles.append(outfile)
            download_response = requests.get(item['url'])
            if force or self.download_needed(item, outfile, quiet):
                with open(outfile, 'wb') as out:
                    out.write(download_response.content)
                if not quiet:
                    print('Output file downloaded to %s' % outfile)

        log = response['log']
        if log:
            outfile = os.path.join(target_dir, kernel_slug + '.log')
            outfiles.append(outfile)
            with open(outfile, 'w') as out:
                out.write(log)
            if not quiet:
                print('Kernel log downloaded to %s ' % outfile)

        return outfiles

    def kernels_output_cli(self,
                           kernel,
                           kernel_opt=None,
                           path=None,
                           force=False,
                           quiet=False):
        kernel = kernel or kernel_opt
        self.kernels_output(kernel, path, force, quiet)

    def kernels_status(self, kernel):
        if kernel is None:
            raise ValueError('A kernel must be specified')
        if '/' in kernel:
            self.validate_kernel_string(kernel)
            kernel_url_list = kernel.split('/')
            owner_slug = kernel_url_list[0]
            kernel_slug = kernel_url_list[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            kernel_slug = kernel
        response = self.process_response(
            self.kernel_status_with_http_info(owner_slug, kernel_slug))
        return response

    def kernels_status_cli(self, kernel, kernel_opt=None):
        kernel = kernel or kernel_opt
        response = self.kernels_status(kernel)
        status = response['status']
        message = response['failureMessage']
        if message:
            print('%s has status "%s"' % (kernel, status))
            print('Failure message: "%s"' % message)
        else:
            print('%s has status "%s"' % (kernel, status))

    def download_needed(self, response, outfile, quiet=True):
        try:
            remote_date = datetime.strptime(response.headers['Last-Modified'],
                                            '%a, %d %b %Y %X %Z')
            if isfile(outfile):
                local_date = datetime.fromtimestamp(os.path.getmtime(outfile))
                if remote_date <= local_date:
                    if not quiet:
                        print(
                            os.path.basename(outfile) +
                            ': Skipping, found more recently modified local '
                            'copy (use --force to force download)')
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
            justify = '>' if isinstance(getattr(
                items[0], f), int) or f == 'size' or f == 'reward' else '<'
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

    def get_or_fail(self, data, key):
        if key in data:
            return data[key]
        raise ValueError('Key ' + key + ' not found in data')

    def get_or_default(self, data, key, default):
        if key in data:
            return data[key]
        return default

    def set_if_present(self, data, key, output, output_key):
        if key in data:
            output[output_key] = data[key]

    def get_dataset_metadata_file(self, folder):
        meta_file = os.path.join(folder, self.DATASET_METADATA_FILE)
        if not os.path.isfile(meta_file):
            meta_file = os.path.join(folder, self.OLD_DATASET_METADATA_FILE)
            if not os.path.isfile(meta_file):
                raise ValueError('Metadata file not found: ' +
                                 self.DATASET_METADATA_FILE)
        return meta_file

    def process_response(self, result):
        if len(result) == 3:
            data = result[0]
            headers = result[2]
            if self.HEADER_API_VERSION in headers:
                api_version = headers[self.HEADER_API_VERSION]
                if (not self.already_printed_version_warning
                        and not self.is_up_to_date(api_version)):
                    print('Warning: Looks like you\'re using an outdated API '
                          'Version, please consider updating (server ' +
                          api_version + ' / client ' + self.__version__ + ')')
                    self.already_printed_version_warning = True
            return data
        return result

    def is_up_to_date(self, server_version):
        client_split = self.__version__.split('.')
        client_len = len(client_split)
        server_split = server_version.split('.')
        server_len = len(server_split)

        # Make both lists the same length
        for i in range(client_len, server_len):
            client_split.append('0')
        for i in range(server_len, client_len):
            server_split.append('0')

        for i in range(0, client_len):
            if 'b' in client_split[i]:
                # Using a beta version, don't check
                return True
            client = int(client_split[i])
            server = int(server_split[i])
            if client < server:
                return False
            elif server < client:
                return True

        return True

    def upload_files(self, request, resources, folder, quiet):
        for file_name in os.listdir(folder):
            if (file_name == self.DATASET_METADATA_FILE
                    or file_name == self.OLD_DATASET_METADATA_FILE
                    or file_name == self.KERNEL_METADATA_FILE):
                continue
            full_path = os.path.join(folder, file_name)

            if not quiet:
                print('Starting upload for file ' + file_name)
            if os.path.isfile(full_path):
                content_length = os.path.getsize(full_path)
                token = self.dataset_upload_file(full_path, quiet)
                if token is None:
                    if not quiet:
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
                                fields = self.get_or_default(
                                    item['schema'], 'fields', [])
                                processed = []
                                count = 0
                                for field in fields:
                                    processed.append(
                                        self.process_column(field))
                                    processed[count].order = count
                                    count += 1
                                upload_file.columns = processed

                request.files.append(upload_file)
            else:
                if not quiet:
                    print('Skipping: ' + file_name)

    def process_column(self, column):
        processed_column = DatasetColumn(
            name=self.get_or_fail(column, 'name'),
            description=self.get_or_default(column, 'description', ''))
        if 'type' in column:
            original_type = column['type'].lower()
            processed_column.original_type = original_type
            if (original_type == 'string' or original_type == 'date'
                    or original_type == 'time' or original_type == 'yearmonth'
                    or original_type == 'duration'
                    or original_type == 'geopoint'
                    or original_type == 'geojson'):
                processed_column.type = 'string'
            elif (original_type == 'numeric' or original_type == 'number'
                  or original_type == 'year'):
                processed_column.type = 'numeric'
            elif original_type == 'boolean':
                processed_column.type = 'boolean'
            elif original_type == 'datetime':
                processed_column.type = 'datetime'
            else:
                # Possibly extended data type - not going to try to track those
                # here. Will set the type and let the server handle it.
                processed_column.type = original_type
        return processed_column

    def upload_complete(self, path, url, quiet):
        file_size = os.path.getsize(path)
        try:
            with tqdm(
                    total=file_size,
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

    def validate_dataset_string(self, dataset):
        if dataset:
            if '/' not in dataset:
                raise ValueError('Dataset must be specified in the form of '
                                 '\'{username}/{dataset-slug}\'')

            split = dataset.split('/')
            if not split[0] or not split[1]:
                raise ValueError('Invalid dataset specification ' + dataset)

    def validate_kernel_string(self, kernel):
        if kernel:
            if '/' not in kernel:
                raise ValueError('Kernel must be specified in the form of '
                                 '\'{username}/{kernel-slug}\'')

            split = kernel.split('/')
            if not split[0] or not split[1]:
                raise ValueError('Invalid kernel specification ' + kernel)

    def validate_resources(self, folder, resources):
        self.validate_files_exist(folder, resources)
        self.validate_no_duplicate_paths(resources)

    def validate_files_exist(self, folder, resources):
        for item in resources:
            file_name = item.get('path')
            full_path = os.path.join(folder, file_name)
            if not os.path.isfile(full_path):
                raise ValueError('%s does not exist' % full_path)

    def validate_no_duplicate_paths(self, resources):
        paths = set()
        for item in resources:
            file_name = item.get('path')
            if file_name in paths:
                raise ValueError(
                    '%s path was specified more than once in the metadata' %
                    file_name)
            paths.add(file_name)

    def convert_to_dataset_file_metadata(self, file_data, path):
        as_metadata = {
            'path': os.path.join(path, file_data['name']),
            'description': file_data['description']
        }

        schema = {}
        fields = []
        for column in file_data['columns']:
            field = {
                'name': column['name'],
                'title': column['description'],
                'type': column['type']
            }
            fields.append(field)
        schema['fields'] = fields
        as_metadata['schema'] = schema

        return as_metadata


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
