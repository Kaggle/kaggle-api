#!/usr/bin/python
#
# Copyright 2019 Kaggle Inc
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
from random import random
import sys
import shutil
import tarfile
import time
import zipfile
import tempfile
from ..api_client import ApiClient
from kaggle.configuration import Configuration
from .kaggle_api import KaggleApi
from ..models.api_blob_type import ApiBlobType
from ..models.collaborator import Collaborator
from ..models.create_inbox_file_request import CreateInboxFileRequest
from ..models.dataset_column import DatasetColumn
from ..models.dataset_new_request import DatasetNewRequest
from ..models.dataset_new_version_request import DatasetNewVersionRequest
from ..models.dataset_update_settings_request import DatasetUpdateSettingsRequest
from ..models.kaggle_models_extended import Competition
from ..models.kaggle_models_extended import Dataset
from ..models.kaggle_models_extended import DatasetNewResponse
from ..models.kaggle_models_extended import DatasetNewVersionResponse
from ..models.kaggle_models_extended import File
from ..models.kaggle_models_extended import Kernel
from ..models.kaggle_models_extended import KernelPushResponse
from ..models.kaggle_models_extended import LeaderboardEntry
from ..models.kaggle_models_extended import ListFilesResult
from ..models.kaggle_models_extended import Metadata
from ..models.kaggle_models_extended import Model
from ..models.kaggle_models_extended import ModelNewResponse
from ..models.kaggle_models_extended import ModelDeleteResponse
from ..models.kaggle_models_extended import ResumableUploadResult
from ..models.kaggle_models_extended import Submission
from ..models.kaggle_models_extended import SubmitResult
from ..models.kernel_push_request import KernelPushRequest
from ..models.license import License
from ..models.model_new_request import ModelNewRequest
from ..models.model_new_instance_request import ModelNewInstanceRequest
from ..models.model_instance_new_version_request import ModelInstanceNewVersionRequest
from ..models.model_update_request import ModelUpdateRequest
from ..models.model_instance_update_request import ModelInstanceUpdateRequest
from ..models.start_blob_upload_request import StartBlobUploadRequest
from ..models.start_blob_upload_response import StartBlobUploadResponse
from ..models.upload_file import UploadFile
import requests
from requests.adapters import HTTPAdapter
import requests.packages.urllib3.exceptions as urllib3_exceptions
from requests.packages.urllib3.util.retry import Retry
from ..rest import ApiException
import six
from slugify import slugify
from tqdm import tqdm
import bleach
import time

try:
    unicode  # Python 2
except NameError:
    unicode = str  # Python 3


class DirectoryArchive(object):

    def __init__(self, fullpath, format):
        self._fullpath = fullpath
        self._format = format
        self.name = None
        self.path = None

    def __enter__(self):
        self._temp_dir = tempfile.mkdtemp()
        _, dir_name = os.path.split(self._fullpath)
        self.path = shutil.make_archive(os.path.join(self._temp_dir, dir_name),
                                        self._format, self._fullpath)
        _, self.name = os.path.split(self.path)
        return self

    def __exit__(self, *args):
        shutil.rmtree(self._temp_dir)


class ResumableUploadContext(object):

    def __init__(self, no_resume=False):
        self.no_resume = no_resume
        self._temp_dir = os.path.join(tempfile.gettempdir(), '.kaggle/uploads')
        self._file_uploads = []

    def __enter__(self):
        if self.no_resume:
            return
        self._create_temp_dir()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.no_resume:
            return
        if exc_type is not None:
            # Don't delete the upload file info when there is an error
            # to give it a chance to retry/resume on the next invocation.
            return
        for file_upload in self._file_uploads:
            file_upload.cleanup()

    def get_upload_info_file_path(self, path):
        return os.path.join(
            self._temp_dir,
            '%s.json' % path.replace(os.path.sep, '_').replace(':', '_'))

    def new_resumable_file_upload(self, path, start_blob_upload_request):
        file_upload = ResumableFileUpload(path, start_blob_upload_request,
                                          self)
        self._file_uploads.append(file_upload)
        file_upload.load()
        return file_upload

    def _create_temp_dir(self):
        try:
            os.makedirs(self._temp_dir)
        except FileExistsError:
            pass


class ResumableFileUpload(object):
    # Reference: https://cloud.google.com/storage/docs/resumable-uploads
    # A resumable upload must be completed within a week of being initiated
    RESUMABLE_UPLOAD_EXPIRY_SECONDS = 6 * 24 * 3600

    def __init__(self, path, start_blob_upload_request, context):
        self.path = path
        self.start_blob_upload_request = start_blob_upload_request
        self.context = context
        self.timestamp = int(time.time())
        self.start_blob_upload_response = None
        self.can_resume = False
        self.upload_complete = False
        if self.context.no_resume:
            return
        self._upload_info_file_path = self.context.get_upload_info_file_path(
            path)

    def get_token(self):
        if self.upload_complete:
            return self.start_blob_upload_response.token
        return None

    def load(self):
        if self.context.no_resume:
            return
        self._load_previous_if_any()

    def _load_previous_if_any(self):
        if not os.path.exists(self._upload_info_file_path):
            return False

        try:
            with io.open(self._upload_info_file_path, 'r') as f:
                previous = ResumableFileUpload.from_dict(
                    json.load(f), self.context)
                if self._is_previous_valid(previous):
                    self.start_blob_upload_response = previous.start_blob_upload_response
                    self.timestamp = previous.timestamp
                    self.can_resume = True
        except Exception as e:
            print('Error while trying to load upload info:', e)

    def _is_previous_valid(self, previous):
        return previous.path == self.path and \
               previous.start_blob_upload_request == self.start_blob_upload_request and \
               previous.timestamp > time.time() - ResumableFileUpload.RESUMABLE_UPLOAD_EXPIRY_SECONDS

    def upload_initiated(self, start_blob_upload_response):
        if self.context.no_resume:
            return

        self.start_blob_upload_response = start_blob_upload_response
        with io.open(self._upload_info_file_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=True)

    def upload_completed(self):
        if self.context.no_resume:
            return

        self.upload_complete = True
        self._save()

    def _save(self):
        with io.open(self._upload_info_file_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=True)

    def cleanup(self):
        if self.context.no_resume:
            return

        try:
            os.remove(self._upload_info_file_path)
        except OSError:
            pass

    def to_dict(self):
        return {
            'path':
            self.path,
            'start_blob_upload_request':
            self.start_blob_upload_request.to_dict(),
            'timestamp':
            self.timestamp,
            'start_blob_upload_response':
            self.start_blob_upload_response.to_dict()
            if self.start_blob_upload_response is not None else None,
            'upload_complete':
            self.upload_complete,
        }

    def from_dict(other, context):
        new = ResumableFileUpload(
            other['path'],
            StartBlobUploadRequest(**other['start_blob_upload_request']),
            context)
        new.timestamp = other.get('timestamp')
        start_blob_upload_response = other.get('start_blob_upload_response')
        if start_blob_upload_response is not None:
            new.start_blob_upload_response = StartBlobUploadResponse(
                **start_blob_upload_response)
            new.upload_complete = other.get('upload_complete') or False
        return new

    def to_str(self):
        return str(self.to_dict())

    def __repr__(self):
        return self.to_str()


class KaggleApi(KaggleApi):
    __version__ = '1.6.17'

    CONFIG_NAME_PROXY = 'proxy'
    CONFIG_NAME_COMPETITION = 'competition'
    CONFIG_NAME_PATH = 'path'
    CONFIG_NAME_USER = 'username'
    CONFIG_NAME_KEY = 'key'
    CONFIG_NAME_SSL_CA_CERT = 'ssl_ca_cert'

    HEADER_API_VERSION = 'X-Kaggle-ApiVersion'
    DATASET_METADATA_FILE = 'dataset-metadata.json'
    OLD_DATASET_METADATA_FILE = 'datapackage.json'
    KERNEL_METADATA_FILE = 'kernel-metadata.json'
    MODEL_METADATA_FILE = 'model-metadata.json'
    MODEL_INSTANCE_METADATA_FILE = 'model-instance-metadata.json'
    MAX_NUM_INBOX_FILES_TO_UPLOAD = 1000
    MAX_UPLOAD_RESUME_ATTEMPTS = 10

    config_dir = os.environ.get('KAGGLE_CONFIG_DIR')

    if not config_dir:
        config_dir = os.path.join(expanduser('~'), '.kaggle')
        # Use ~/.kaggle if it already exists for backwards compatibility,
        # otherwise follow XDG base directory specification
        if sys.platform.startswith('linux') and not os.path.exists(config_dir):
            config_dir = os.path.join(
                (os.environ.get('XDG_CONFIG_HOME')
                 or os.path.join(expanduser('~'), '.config')), 'kaggle')

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    config_file = 'kaggle.json'
    config = os.path.join(config_dir, config_file)
    config_values = {}
    already_printed_version_warning = False

    # Kernels valid types
    valid_push_kernel_types = ['script', 'notebook']
    valid_push_language_types = ['python', 'r', 'rmarkdown']
    valid_push_pinning_types = ['original', 'latest']
    valid_list_languages = ['all', 'python', 'r', 'sqlite', 'julia']
    valid_list_kernel_types = ['all', 'script', 'notebook']
    valid_list_output_types = ['all', 'visualization', 'data']
    valid_list_sort_by = [
        'hotness', 'commentCount', 'dateCreated', 'dateRun', 'relevance',
        'scoreAscending', 'scoreDescending', 'viewCount', 'voteCount'
    ]

    # Competitions valid types
    valid_competition_groups = ['general', 'entered', 'inClass']
    valid_competition_categories = [
        'all', 'featured', 'research', 'recruitment', 'gettingStarted',
        'masters', 'playground'
    ]
    valid_competition_sort_by = [
        'grouped', 'prize', 'earliestDeadline', 'latestDeadline',
        'numberOfTeams', 'recentlyCreated'
    ]

    # Datasets valid types
    valid_dataset_file_types = ['all', 'csv', 'sqlite', 'json', 'bigQuery']
    valid_dataset_license_names = ['all', 'cc', 'gpl', 'odb', 'other']
    valid_dataset_sort_bys = [
        'hottest', 'votes', 'updated', 'active', 'published'
    ]

    # Models valid types
    valid_model_sort_bys = [
        'hotness', 'downloadCount', 'voteCount', 'notebookCount', 'createTime'
    ]

    # Command prefixes that are valid without authentication.
    command_prefixes_allowing_anonymous_access = ('datasets download',
                                                  'datasets files')

    # Hack for https://github.com/Kaggle/kaggle-api/issues/22 / b/78194015
    if six.PY2:
        reload(sys)
        sys.setdefaultencoding('latin1')

    def _is_retriable(self, e):
        return issubclass(type(e), ConnectionError) or \
            issubclass(type(e), urllib3_exceptions.ConnectionError) or \
            issubclass(type(e), urllib3_exceptions.ConnectTimeoutError) or \
            issubclass(type(e), urllib3_exceptions.ProtocolError) or \
            issubclass(type(e), requests.exceptions.ConnectionError) or \
            issubclass(type(e), requests.exceptions.ConnectTimeout)

    def _calculate_backoff_delay(self, attempt, initial_delay_millis,
                                 retry_multiplier, randomness_factor):
        delay_ms = initial_delay_millis * (retry_multiplier**attempt)
        random_wait_ms = int(random() - 0.5) * 2 * delay_ms * randomness_factor
        total_delay = (delay_ms + random_wait_ms) / 1000.0
        return total_delay

    def with_retry(self,
                   func,
                   max_retries=10,
                   initial_delay_millis=500,
                   retry_multiplier=1.7,
                   randomness_factor=0.5):

        def retriable_func(*args):
            for i in range(1, max_retries + 1):
                try:
                    return func(*args)
                except Exception as e:
                    if self._is_retriable(e) and i < max_retries:
                        total_delay = self._calculate_backoff_delay(
                            i, initial_delay_millis, retry_multiplier,
                            randomness_factor)
                        print(
                            'Request failed: %s. Will retry in %2.1f seconds' %
                            (e, total_delay))
                        time.sleep(total_delay)
                        continue
                    raise

        return retriable_func

    ## Authentication

    def authenticate(self):
        """authenticate the user with the Kaggle API. This method will generate
           a configuration, first checking the environment for credential
           variables, and falling back to looking for the .kaggle/kaggle.json
           configuration file.
        """

        config_data = {}
        # Ex: 'datasets list', 'competitions files', 'models instances get', etc.
        api_command = ' '.join(sys.argv[1:])

        # Step 1: try getting username/password from environment
        config_data = self.read_config_environment(config_data)

        # Step 2: if credentials were not in env read in configuration file
        if self.CONFIG_NAME_USER not in config_data \
                or self.CONFIG_NAME_KEY not in config_data:
            if os.path.exists(self.config):
                config_data = self.read_config_file(config_data)
            elif self._is_help_or_version_command(api_command) or (
                    len(sys.argv) > 2 and api_command.startswith(
                        self.command_prefixes_allowing_anonymous_access)):
                # Some API commands should be allowed without authentication.
                return
            else:
                raise IOError('Could not find {}. Make sure it\'s located in'
                              ' {}. Or use the environment method. See setup'
                              ' instructions at'
                              ' https://github.com/Kaggle/kaggle-api/'.format(
                                  self.config_file, self.config_dir))

        # Step 3: load into configuration!
        self._load_config(config_data)

    def _is_help_or_version_command(self, api_command):
        """determines if the string command passed in is for a help or version
           command.
           Parameters
           ==========
           api_command: a string, 'datasets list', 'competitions files',
                        'models instances get', etc.
        """
        return api_command.endswith(('-h', '--help', '-v', '--version'))

    def read_config_environment(self, config_data=None, quiet=False):
        """read_config_environment is the second effort to get a username
           and key to authenticate to the Kaggle API. The environment keys
           are equivalent to the kaggle.json file, but with "KAGGLE_" prefix
           to define a unique namespace.

           Parameters
           ==========
           config_data: a partially loaded configuration dictionary (optional)
           quiet: suppress verbose print of output (default is False)
        """

        # Add all variables that start with KAGGLE_ to config data

        if config_data is None:
            config_data = {}
        for key, val in os.environ.items():
            if key.startswith('KAGGLE_'):
                config_key = key.replace('KAGGLE_', '', 1).lower()
                config_data[config_key] = val

        return config_data

    ## Configuration

    def _load_config(self, config_data):
        """the final step of the authenticate steps, where we load the values
           from config_data into the Configuration object.

           Parameters
           ==========
           config_data: a dictionary with configuration values (keys) to read
                        into self.config_values

        """
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

        # Cert File

        if self.CONFIG_NAME_SSL_CA_CERT in config_data:
            configuration.ssl_ca_cert = config_data[
                self.CONFIG_NAME_SSL_CA_CERT]

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

    def read_config_file(self, config_data=None, quiet=False):
        """read_config_file is the first effort to get a username
           and key to authenticate to the Kaggle API. Since we can get the
           username and password from the environment, it's not required.

           Parameters
           ==========
           config_data: the Configuration object to save a username and
                        password, if defined
           quiet: suppress verbose print of output (default is False)
        """
        if config_data is None:
            config_data = {}

        if os.path.exists(self.config):

            try:
                if os.name != 'nt':
                    permissions = os.stat(self.config).st_mode
                    if (permissions & 4) or (permissions & 32):
                        print(
                            'Warning: Your Kaggle API key is readable by other '
                            'users on this system! To fix this, you can run ' +
                            '\'chmod 600 {}\''.format(self.config))

                with open(self.config) as f:
                    config_data = json.load(f)
            except:
                pass

        else:

            # Warn the user that configuration will be reliant on environment
            if not quiet:
                print('No Kaggle API config file found, will use environment.')

        return config_data

    def _read_config_file(self):
        """read in the configuration file, a json file defined at self.config"""

        try:
            with open(self.config, 'r') as f:
                config_data = json.load(f)
        except FileNotFoundError:
            config_data = {}

        return config_data

    def _write_config_file(self, config_data, indent=2):
        """write config data to file.

           Parameters
           ==========
           config_data: the Configuration object to save a username and
                        password, if defined
           indent: number of tab indentations to use when writing json
        """
        with open(self.config, 'w') as f:
            json.dump(config_data, f, indent=indent)

    def set_config_value(self, name, value, quiet=False):
        """a client helper function to set a configuration value, meaning
           reading in the configuration file (if it exists), saving a new
           config value, and then writing back

           Parameters
           ==========
           name: the name of the value to set (key in dictionary)
           value: the value to set at the key
           quiet: disable verbose output if True (default is False)
        """

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
        """unset a configuration value
            Parameters
           ==========
           name: the name of the value to unset (remove key in dictionary)
           quiet: disable verbose output if True (default is False)
        """

        config_data = self._read_config_file()

        if name in config_data:

            del config_data[name]

            self._write_config_file(config_data)

            if not quiet:
                self.print_config_value(name, separator=' is now set to: ')

    def get_config_value(self, name):
        """ return a config value (with key name) if it's in the config_values,
            otherwise return None

            Parameters
            ==========
            name: the config value key to get

        """
        if name in self.config_values:
            return self.config_values[name]

    def get_default_download_dir(self, *subdirs):
        """ Get the download path for a file. If not defined, return default
            from config.

            Parameters
            ==========
            subdirs: a single (or list of) subfolders under the basepath
        """
        # Look up value for key "path" in the config
        path = self.get_config_value(self.CONFIG_NAME_PATH)

        # If not set in config, default to present working directory
        if path is None:
            return os.getcwd()

        return os.path.join(path, *subdirs)

    def print_config_value(self, name, prefix='- ', separator=': '):
        """print a single configuration value, based on a prefix and separator

           Parameters
           ==========
           name: the key of the config valur in self.config_values to print
           prefix: the prefix to print
           separator: the separator to use (default is : )
        """

        value_out = 'None'
        if name in self.config_values and self.config_values[name] is not None:
            value_out = self.config_values[name]
        print(prefix + name + separator + value_out)

    def print_config_values(self, prefix='- '):
        """a wrapper to print_config_value to print all configuration values
            Parameters
           ==========
           prefix: the character prefix to put before the printed config value
                   defaults to "- "
        """
        print('Configuration values from ' + self.config_dir)
        self.print_config_value(self.CONFIG_NAME_USER, prefix=prefix)
        self.print_config_value(self.CONFIG_NAME_PATH, prefix=prefix)
        self.print_config_value(self.CONFIG_NAME_PROXY, prefix=prefix)
        self.print_config_value(self.CONFIG_NAME_COMPETITION, prefix=prefix)

    ## Competitions

    def competitions_list(self,
                          group=None,
                          category=None,
                          sort_by=None,
                          page=1,
                          search=None):
        """ make call to list competitions, format the response, and return
            a list of Competition instances

            Parameters
            ==========

            page: the page to return (default is 1)
            search: a search term to use (default is empty string)
            sort_by: how to sort the result, see valid_competition_sort_by for options
            category: category to filter result to
            group: group to filter result to
        """
        if group and group not in self.valid_competition_groups:
            raise ValueError('Invalid group specified. Valid options are ' +
                             str(self.valid_competition_groups))

        if category and category not in self.valid_competition_categories:
            raise ValueError('Invalid category specified. Valid options are ' +
                             str(self.valid_competition_categories))

        if sort_by and sort_by not in self.valid_competition_sort_by:
            raise ValueError('Invalid sort_by specified. Valid options are ' +
                             str(self.valid_competition_sort_by))

        competitions_list_result = self.process_response(
            self.competitions_list_with_http_info(group=group or '',
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
        """ a wrapper for competitions_list for the client.

            Parameters
            ==========
            group: group to filter result to
            category: category to filter result to
            sort_by: how to sort the result, see valid_sort_by for options
            page: the page to return (default is 1)
            search: a search term to use (default is empty string)
            csv_display: if True, print comma separated values
        """
        competitions = self.competitions_list(group=group,
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
        """ submit a competition!

            Parameters
            ==========
            file_name: the competition metadata file
            message: the submission description
            competition: the competition name
            quiet: suppress verbose output (default is False)
        """
        if competition is None:
            competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
            if competition is not None and not quiet:
                print('Using competition: ' + competition)

        if competition is None:
            raise ValueError('No competition specified')
        else:
            url_result = self.process_response(
                self.competitions_submissions_url_with_http_info(
                    id=competition,
                    file_name=os.path.basename(file_name),
                    content_length=os.path.getsize(file_name),
                    last_modified_date_utc=int(os.path.getmtime(file_name))))

            # Temporary while new worker is gradually turned on.  'isComplete'
            # exists on the old DTO but not the new, so this is an hacky but
            # easy solution to figure out which submission logic to use
            if 'isComplete' in url_result:
                # Old submissions path
                url_result_list = url_result['createUrl'].split('/')
                upload_result = self.process_response(
                    self.competitions_submissions_upload_with_http_info(
                        file=file_name,
                        guid=url_result_list[-3],
                        content_length=url_result_list[-2],
                        last_modified_date_utc=url_result_list[-1]))
                upload_result_token = upload_result['token']
            else:
                # New submissions path!
                upload_status = self.upload_complete(file_name,
                                                     url_result['createUrl'],
                                                     quiet)
                if upload_status != ResumableUploadResult.COMPLETE:
                    # Actual error is printed during upload_complete. Not
                    # ideal but changing would not be backwards compatible
                    return "Could not submit to competition"

                upload_result_token = url_result['token']

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
        """ submit a competition using the client. Arguments are same as for
            competition_submit, except for extra arguments provided here.
             Parameters
            ==========
            competition_opt: an alternative competition option provided by cli
        """
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

    def competition_submissions(self,
                                competition,
                                page_token=None,
                                page_size=20):
        """ get the list of Submission for a particular competition

            Parameters
            ==========
            competition: the name of the competition
            page_token: token for pagination
            page_size: the number of items per page
        """
        submissions_result = self.process_response(
            self.competitions_submissions_list_with_http_info(id=competition))
        return [Submission(s) for s in submissions_result]

    def competition_submissions_cli(self,
                                    competition=None,
                                    competition_opt=None,
                                    csv_display=False,
                                    page_token=None,
                                    page_size=20,
                                    quiet=False):
        """ wrapper to competition_submission, will return either json or csv
            to the user. Additional parameters are listed below, see
            competition_submissions for rest.

            Parameters
            ==========
            competition: the name of the competition. If None, look to config
            competition_opt: an alternative competition option provided by cli
            csv_display: if True, print comma separated values
            page_token: token for pagination
            page_size: the number of items per page
            quiet: suppress verbose output (default is False)
        """
        competition = competition or competition_opt
        if competition is None:
            competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
            if competition is not None and not quiet:
                print('Using competition: ' + competition)

        if competition is None:
            raise ValueError('No competition specified')
        else:
            submissions = self.competition_submissions(competition, page_token,
                                                       page_size)
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

    def competition_list_files(self,
                               competition,
                               page_token=None,
                               page_size=20):
        """ list files for competition
             Parameters
            ==========
            competition: the name of the competition
            page_token: the page token for pagination
            page_size: the number of items per page
        """
        competition_list_files_result = self.process_response(
            self.competitions_data_list_files_with_http_info(
                id=competition, page_token=page_token, page_size=page_size))
        return FileList(competition_list_files_result)

    def competition_list_files_cli(self,
                                   competition,
                                   competition_opt=None,
                                   csv_display=False,
                                   page_token=None,
                                   page_size=20,
                                   quiet=False):
        """ List files for a competition, if it exists

            Parameters
            ==========
            competition: the name of the competition. If None, look to config
            competition_opt: an alternative competition option provided by cli
            csv_display: if True, print comma separated values
            page_token: the page token for pagination
            page_size: the number of items per page
            quiet: suppress verbose output (default is False)
        """
        competition = competition or competition_opt
        if competition is None:
            competition = self.get_config_value(self.CONFIG_NAME_COMPETITION)
            if competition is not None and not quiet:
                print('Using competition: ' + competition)

        if competition is None:
            raise ValueError('No competition specified')
        else:
            result = self.competition_list_files(competition, page_token,
                                                 page_size)
            next_page_token = result.nextPageToken
            if next_page_token:
                print('Next Page Token = {}'.format(next_page_token))
            fields = ['name', 'size', 'creationDate']
            if result:
                if csv_display:
                    self.print_csv(result.files, fields)
                else:
                    self.print_table(result.files, fields)
            else:
                print('No files found')

    def competition_download_file(self,
                                  competition,
                                  file_name,
                                  path=None,
                                  force=False,
                                  quiet=False):
        """ download a competition file to a designated location, or use
            a default location

            Parameters
            =========
            competition: the name of the competition
            file_name: the configuration file name
            path: a path to download the file to
            force: force the download if the file already exists (default False)
            quiet: suppress verbose output (default is False)
        """
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
            self.download_file(response, outfile, quiet, not force)

    def competition_download_files(self,
                                   competition,
                                   path=None,
                                   force=False,
                                   quiet=True):
        """ downloads all competition files.

            Parameters
            =========
            competition: the name of the competition
            path: a path to download the file to
            force: force the download if the file already exists (default False)
            quiet: suppress verbose output (default is True)
        """
        if path is None:
            effective_path = self.get_default_download_dir(
                'competitions', competition)
        else:
            effective_path = path

        response = self.process_response(
            self.competitions_data_download_files_with_http_info(
                id=competition, _preload_content=False))
        url = response.retries.history[0].redirect_location.split('?')[0]
        outfile = os.path.join(effective_path,
                               competition + '.' + url.split('.')[-1])

        if force or self.download_needed(response, outfile, quiet):
            self.download_file(response, outfile, quiet, not force)

    def competition_download_cli(self,
                                 competition,
                                 competition_opt=None,
                                 file_name=None,
                                 path=None,
                                 force=False,
                                 quiet=False):
        """ a wrapper to competition_download_files, but first will parse input
            from API client. Additional parameters are listed here, see
            competition_download for remaining.

            Parameters
            =========
            competition: the name of the competition
            competition_opt: an alternative competition option provided by cli
            file_name: the configuration file name
            path: a path to download the file to
            force: force the download if the file already exists (default False)
            quiet: suppress verbose output (default is False)
        """
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
        """ Download competition leaderboards

            Parameters
            =========
            competition: the name of the competition
            path: a path to download the file to
            quiet: suppress verbose output (default is True)
        """
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
        """ view a leaderboard based on a competition name

            Parameters
            ==========
            competition: the competition name to view leadboard for
        """
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
        """ a wrapper for competition_leaderbord_view that will print the
            results as a table or comma separated values

            Parameters
            ==========
            competition: the competition name to view leadboard for
            competition_opt: an alternative competition option provided by cli
            path: a path to download to, if download is True
            view: if True, show the results in the terminal as csv or table
            download: if True, download the entire leaderboard
            csv_display: if True, print comma separated values instead of table
            quiet: suppress verbose output (default is False)
        """
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
                     page=1,
                     max_size=None,
                     min_size=None):
        """ return a list of datasets!

            Parameters
            ==========
            sort_by: how to sort the result, see valid_dataset_sort_bys for options
            size: Deprecated
            file_type: the format, see valid_dataset_file_types for string options
            license_name: string descriptor for license, see valid_dataset_license_names
            tag_ids: tag identifiers to filter the search
            search: a search term to use (default is empty string)
            user: username to filter the search to
            mine: boolean if True, group is changed to "my" to return personal
            page: the page to return (default is 1)
            max_size: the maximum size of the dataset to return (bytes)
            min_size: the minimum size of the dataset to return (bytes)
        """
        if sort_by and sort_by not in self.valid_dataset_sort_bys:
            raise ValueError('Invalid sort by specified. Valid options are ' +
                             str(self.valid_dataset_sort_bys))

        if size:
            raise ValueError(
                'The --size parameter has been deprecated. ' +
                'Please use --max-size and --min-size to filter dataset sizes.'
            )

        if file_type and file_type not in self.valid_dataset_file_types:
            raise ValueError(
                'Invalid file type specified. Valid options are ' +
                str(self.valid_dataset_file_types))

        if license_name and license_name not in self.valid_dataset_license_names:
            raise ValueError('Invalid license specified. Valid options are ' +
                             str(self.valid_dataset_license_names))

        if int(page) <= 0:
            raise ValueError('Page number must be >= 1')

        if max_size and min_size:
            if (int(max_size) < int(min_size)):
                raise ValueError('Max Size must be max_size >= min_size')
        if (max_size and int(max_size) <= 0):
            raise ValueError('Max Size must be > 0')
        elif (min_size and int(min_size) < 0):
            raise ValueError('Min Size must be >= 0')

        group = 'public'
        if mine:
            group = 'my'
            if user:
                raise ValueError('Cannot specify both mine and a user')
        if user:
            group = 'user'

        datasets_list_result = self.process_response(
            self.datasets_list_with_http_info(group=group,
                                              sort_by=sort_by or 'hottest',
                                              size=size,
                                              filetype=file_type or 'all',
                                              license=license_name or 'all',
                                              tagids=tag_ids or '',
                                              search=search or '',
                                              user=user or '',
                                              page=page,
                                              max_size=max_size,
                                              min_size=min_size))
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
                         csv_display=False,
                         max_size=None,
                         min_size=None):
        """ a wrapper to dataset_list for the client. Additional parameters
            are described here, see dataset_list for others.

            Parameters
            ==========
            sort_by: how to sort the result, see valid_dataset_sort_bys for options
            size: DEPRECATED
            file_type: the format, see valid_dataset_file_types for string options
            license_name: string descriptor for license, see valid_dataset_license_names
            tag_ids: tag identifiers to filter the search
            search: a search term to use (default is empty string)
            user: username to filter the search to
            mine: boolean if True, group is changed to "my" to return personal
            page: the page to return (default is 1)
            csv_display: if True, print comma separated values instead of table
            max_size: the maximum size of the dataset to return (bytes)
            min_size: the minimum size of the dataset to return (bytes)
        """
        datasets = self.dataset_list(sort_by, size, file_type, license_name,
                                     tag_ids, search, user, mine, page,
                                     max_size, min_size)
        fields = [
            'ref', 'title', 'size', 'lastUpdated', 'downloadCount',
            'voteCount', 'usabilityRating'
        ]
        if datasets:
            if csv_display:
                self.print_csv(datasets, fields)
            else:
                self.print_table(datasets, fields)
        else:
            print('No datasets found')

    def dataset_metadata_prep(self, dataset, path):
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

        return (owner_slug, dataset_slug, effective_path)

    def dataset_metadata_update(self, dataset, path):
        (owner_slug, dataset_slug,
         effective_path) = self.dataset_metadata_prep(dataset, path)
        meta_file = self.get_dataset_metadata_file(effective_path)
        with open(meta_file, 'r') as f:
            metadata = json.load(f)
            updateSettingsRequest = DatasetUpdateSettingsRequest(
                title=metadata['title'],
                subtitle=metadata['subtitle'],
                description=metadata['description'],
                is_private=metadata['isPrivate'],
                licenses=[
                    License(name=l['name']) for l in metadata['licenses']
                ],
                keywords=metadata['keywords'],
                collaborators=[
                    Collaborator(username=c['username'], role=c['role'])
                    for c in metadata['collaborators']
                ],
                data=metadata['data'])
            result = self.process_response(
                self.metadata_post_with_http_info(owner_slug, dataset_slug,
                                                  updateSettingsRequest))
            if (len(result['errors']) > 0):
                [print(e['message']) for e in result['errors']]
                exit(1)

    def dataset_metadata(self, dataset, path):
        (owner_slug, dataset_slug,
         effective_path) = self.dataset_metadata_prep(dataset, path)

        if not os.path.exists(effective_path):
            os.makedirs(effective_path)

        result = self.process_response(
            self.metadata_get_with_http_info(owner_slug, dataset_slug))
        if (result['errorMessage']):
            raise Exception(result['errorMessage'])

        metadata = Metadata(result['info'])

        meta_file = os.path.join(effective_path, self.DATASET_METADATA_FILE)
        with open(meta_file, 'w') as f:
            json.dump(metadata, f, indent=2, default=lambda o: o.__dict__)

        return meta_file

    def dataset_metadata_cli(self, dataset, path, update, dataset_opt=None):
        dataset = dataset or dataset_opt
        if (update):
            print('updating dataset metadata')
            self.dataset_metadata_update(dataset, path)
            print('successfully updated dataset metadata')
        else:
            meta_file = self.dataset_metadata(dataset, path)
            print('Downloaded metadata to ' + meta_file)

    def dataset_list_files(self, dataset, page_token=None, page_size=20):
        """ list files for a dataset
             Parameters
            ==========
            dataset: the string identified of the dataset
                     should be in format [owner]/[dataset-name]
            page_token: the page token for pagination
            page_size: the number of items per page
        """
        if dataset is None:
            raise ValueError('A dataset must be specified')
        owner_slug, dataset_slug, dataset_version_number = self.split_dataset_string(
            dataset)

        dataset_list_files_result = self.process_response(
            self.datasets_list_files_with_http_info(
                owner_slug=owner_slug,
                dataset_slug=dataset_slug,
                dataset_version_number=dataset_version_number,
                page_token=page_token,
                page_size=page_size))
        return ListFilesResult(dataset_list_files_result)

    def dataset_list_files_cli(self,
                               dataset,
                               dataset_opt=None,
                               csv_display=False,
                               page_token=None,
                               page_size=20):
        """ a wrapper to dataset_list_files for the client
            (list files for a dataset)
             Parameters
            ==========
            dataset: the string identified of the dataset
                     should be in format [owner]/[dataset-name]
            dataset_opt: an alternative option to providing a dataset
            csv_display: if True, print comma separated values instead of table
            page_token: the page token for pagination
            page_size: the number of items per page
        """
        dataset = dataset or dataset_opt
        result = self.dataset_list_files(dataset, page_token, page_size)

        if result:
            if result.error_message:
                print(result.error_message)
            else:
                next_page_token = result.nextPageToken
                if next_page_token:
                    print('Next Page Token = {}'.format(next_page_token))
                fields = ['name', 'size', 'creationDate']
                if csv_display:
                    self.print_csv(result.files, fields)
                else:
                    self.print_table(result.files, fields)
        else:
            print('No files found')

    def dataset_status(self, dataset):
        """ call to get the status of a dataset from the API
             Parameters
            ==========
            dataset: the string identified of the dataset
                     should be in format [owner]/[dataset-name]
        """
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
            self.datasets_status_with_http_info(owner_slug=owner_slug,
                                                dataset_slug=dataset_slug))
        return dataset_status_result

    def dataset_status_cli(self, dataset, dataset_opt=None):
        """ wrapper for client for dataset_status, with additional
            dataset_opt to get the status of a dataset from the API
             Parameters
            ==========
            dataset_opt: an alternative to dataset
        """
        dataset = dataset or dataset_opt
        return self.dataset_status(dataset)

    def dataset_download_file(self,
                              dataset,
                              file_name,
                              path=None,
                              force=False,
                              quiet=True,
                              licenses=[]):
        """ download a single file for a dataset

            Parameters
            ==========
            dataset: the string identified of the dataset
                     should be in format [owner]/[dataset-name]
            file_name: the dataset configuration file
            path: if defined, download to this location
            force: force the download if the file already exists (default False)
            quiet: suppress verbose output (default is True)
            licenses: a list of license names, e.g. ['CC0-1.0']
        """
        if '/' in dataset:
            self.validate_dataset_string(dataset)
            owner_slug, dataset_slug, dataset_version_number = self.split_dataset_string(
                dataset)
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            dataset_slug = dataset
            dataset_version_number = None

        if path is None:
            effective_path = self.get_default_download_dir(
                'datasets', owner_slug, dataset_slug)
        else:
            effective_path = path

        self._print_dataset_url_and_license(owner_slug, dataset_slug,
                                            dataset_version_number, licenses)

        response = self.process_response(
            self.datasets_download_file_with_http_info(
                owner_slug=owner_slug,
                dataset_slug=dataset_slug,
                dataset_version_number=dataset_version_number,
                file_name=file_name,
                _preload_content=False))
        url = response.retries.history[0].redirect_location.split('?')[0]
        outfile = os.path.join(effective_path, url.split('/')[-1])
        if force or self.download_needed(response, outfile, quiet):
            self.download_file(response, outfile, quiet, not force)
            return True
        else:
            return False

    def dataset_download_files(self,
                               dataset,
                               path=None,
                               force=False,
                               quiet=True,
                               unzip=False,
                               licenses=[]):
        """ download all files for a dataset

            Parameters
            ==========
            dataset: the string identified of the dataset
                     should be in format [owner]/[dataset-name]
            path: the path to download the dataset to
            force: force the download if the file already exists (default False)
            quiet: suppress verbose output (default is True)
            unzip: if True, unzip files upon download (default is False)
            licenses: a list of license names, e.g. ['CC0-1.0']
        """
        if dataset is None:
            raise ValueError('A dataset must be specified')
        owner_slug, dataset_slug, dataset_version_number = self.split_dataset_string(
            dataset)
        if path is None:
            effective_path = self.get_default_download_dir(
                'datasets', owner_slug, dataset_slug)
        else:
            effective_path = path

        self._print_dataset_url_and_license(owner_slug, dataset_slug,
                                            dataset_version_number, licenses)

        response = self.process_response(
            self.datasets_download_with_http_info(
                owner_slug=owner_slug,
                dataset_slug=dataset_slug,
                dataset_version_number=dataset_version_number,
                _preload_content=False))

        outfile = os.path.join(effective_path, dataset_slug + '.zip')
        if force or self.download_needed(response, outfile, quiet):
            self.download_file(response, outfile, quiet, not force)
            downloaded = True
        else:
            downloaded = False

        if downloaded:
            outfile = os.path.join(effective_path, dataset_slug + '.zip')
            if unzip:
                try:
                    with zipfile.ZipFile(outfile) as z:
                        z.extractall(effective_path)
                except zipfile.BadZipFile as e:
                    raise ValueError(
                        'Bad zip file, please report on '
                        'www.github.com/kaggle/kaggle-api', e)

                try:
                    os.remove(outfile)
                except OSError as e:
                    print('Could not delete zip file, got %s' % e)

    def _print_dataset_url_and_license(self, owner_slug, dataset_slug,
                                       dataset_version_number, licenses):
        if dataset_version_number is None:
            print('Dataset URL: https://www.kaggle.com/datasets/%s/%s' %
                  (owner_slug, dataset_slug))
        else:
            print(
                'Dataset URL: https://www.kaggle.com/datasets/%s/%s/versions/%s'
                % (owner_slug, dataset_slug, dataset_version_number))

        if len(licenses) > 0:
            print('License(s): %s' % (','.join(licenses)))

    def dataset_download_cli(self,
                             dataset,
                             dataset_opt=None,
                             file_name=None,
                             path=None,
                             unzip=False,
                             force=False,
                             quiet=False):
        """ client wrapper for dataset_download_files and download dataset file,
            either for a specific file (when file_name is provided),
            or all files for a dataset (plural)

            Parameters
            ==========
            dataset: the string identified of the dataset
                     should be in format [owner]/[dataset-name]
            dataset_opt: an alternative option to providing a dataset
            file_name: the dataset configuration file
            path: the path to download the dataset to
            force: force the download if the file already exists (default False)
            quiet: suppress verbose output (default is False)
            unzip: if True, unzip files upon download (default is False)
        """
        dataset = dataset or dataset_opt

        owner_slug, dataset_slug, _ = self.split_dataset_string(dataset)
        metadata = self.process_response(
            self.metadata_get_with_http_info(owner_slug, dataset_slug))

        if 'info' in metadata and 'licenses' in metadata['info']:
            # license_objs format is like: [{ 'name': 'CC0-1.0' }]
            license_objs = metadata['info']['licenses']
            licenses = [
                license_obj['name'] for license_obj in license_objs
                if 'name' in license_obj
            ]
        else:
            licenses = [
                'Error retrieving license. Please visit the Dataset URL to view license information.'
            ]

        if file_name is None:
            self.dataset_download_files(dataset,
                                        path=path,
                                        unzip=unzip,
                                        force=force,
                                        quiet=quiet,
                                        licenses=licenses)
        else:
            self.dataset_download_file(dataset,
                                       file_name,
                                       path=path,
                                       force=force,
                                       quiet=quiet,
                                       licenses=licenses)

    def _upload_blob(self, path, quiet, blob_type, upload_context):
        """ upload a file

            Parameters
            ==========
            path: the complete path to upload
            quiet: suppress verbose output (default is False)
            blob_type (ApiBlobType): To which entity the file/blob refers
            upload_context (ResumableUploadContext): Context for resumable uploads
        """
        file_name = os.path.basename(path)
        content_length = os.path.getsize(path)
        last_modified_epoch_seconds = int(os.path.getmtime(path))

        start_blob_upload_request = StartBlobUploadRequest(
            blob_type,
            file_name,
            content_length,
            last_modified_epoch_seconds=last_modified_epoch_seconds)

        file_upload = upload_context.new_resumable_file_upload(
            path, start_blob_upload_request)

        for i in range(0, self.MAX_UPLOAD_RESUME_ATTEMPTS):
            if file_upload.upload_complete:
                return file_upload

            if not file_upload.can_resume:
                # Initiate upload on Kaggle backend to get the url and token.
                start_blob_upload_response = self.process_response(
                    self.with_retry(self.upload_file_with_http_info)(
                        file_upload.start_blob_upload_request))
                file_upload.upload_initiated(start_blob_upload_response)

            upload_result = self.upload_complete(
                path,
                file_upload.start_blob_upload_response.create_url,
                quiet,
                resume=file_upload.can_resume)
            if upload_result == ResumableUploadResult.INCOMPLETE:
                continue  # Continue (i.e., retry/resume) only if the upload is incomplete.

            if upload_result == ResumableUploadResult.COMPLETE:
                file_upload.upload_completed()
            break

        return file_upload.get_token()

    def dataset_create_version(self,
                               folder,
                               version_notes,
                               quiet=False,
                               convert_to_csv=True,
                               delete_old_versions=False,
                               dir_mode='skip'):
        """ create a version of a dataset

            Parameters
            ==========
            folder: the folder with the dataset configuration / data files
            version_notes: notes to add for the version
            quiet: suppress verbose output (default is False)
            convert_to_csv: on upload, if data should be converted to csv
            delete_old_versions: if True, do that (default False)
            dir_mode: What to do with directories: "skip" - ignore; "zip" - compress and upload
        """
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_file = self.get_dataset_metadata_file(folder)

        # read json
        with open(meta_file) as f:
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
        if resources:
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

        with ResumableUploadContext() as upload_context:
            self.upload_files(request, resources, folder, ApiBlobType.DATASET,
                              upload_context, quiet, dir_mode)

            if id_no:
                result = DatasetNewVersionResponse(
                    self.process_response(
                        self.with_retry(
                            self.datasets_create_version_by_id_with_http_info)(
                                id_no, request)))
            else:
                if ref == self.config_values[
                        self.CONFIG_NAME_USER] + '/INSERT_SLUG_HERE':
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
                                   delete_old_versions=False,
                                   dir_mode='skip'):
        """ client wrapper for creating a version of a dataset
             Parameters
            ==========
            folder: the folder with the dataset configuration / data files
            version_notes: notes to add for the version
            quiet: suppress verbose output (default is False)
            convert_to_csv: on upload, if data should be converted to csv
            delete_old_versions: if True, do that (default False)
            dir_mode: What to do with directories: "skip" - ignore; "zip" - compress and upload
        """
        folder = folder or os.getcwd()
        result = self.dataset_create_version(
            folder,
            version_notes,
            quiet=quiet,
            convert_to_csv=convert_to_csv,
            delete_old_versions=delete_old_versions,
            dir_mode=dir_mode)

        if result is None:
            print('Dataset version creation error: See previous output')
        elif result.invalidTags:
            print(
                ('The following are not valid tags and could not be added to '
                 'the dataset: ') + str(result.invalidTags))
        elif result.status.lower() == 'ok':
            print(
                'Dataset version is being created. Please check progress at ' +
                result.url)
        else:
            print('Dataset version creation error: ' + result.error)

    def dataset_initialize(self, folder):
        """ initialize a folder with a a dataset configuration (metadata) file

            Parameters
            ==========
            folder: the folder to initialize the metadata file in
        """
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
        folder = folder or os.getcwd()
        self.dataset_initialize(folder)

    def dataset_create_new(self,
                           folder,
                           public=False,
                           quiet=False,
                           convert_to_csv=True,
                           dir_mode='skip'):
        """ create a new dataset, meaning the same as creating a version but
            with extra metadata like license and user/owner.
             Parameters
            ==========
            folder: the folder to get the metadata file from
            public: should the dataset be public?
            quiet: suppress verbose output (default is False)
            convert_to_csv: if True, convert data to comma separated value
            dir_mode: What to do with directories: "skip" - ignore; "zip" - compress and upload
        """
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_file = self.get_dataset_metadata_file(folder)

        # read json
        with open(meta_file) as f:
            meta_data = json.load(f)
        ref = self.get_or_fail(meta_data, 'id')
        title = self.get_or_fail(meta_data, 'title')
        licenses = self.get_or_fail(meta_data, 'licenses')
        ref_list = ref.split('/')
        owner_slug = ref_list[0]
        dataset_slug = ref_list[1]

        # validations
        if ref == self.config_values[
                self.CONFIG_NAME_USER] + '/INSERT_SLUG_HERE':
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

        request = DatasetNewRequest(title=title,
                                    slug=dataset_slug,
                                    owner_slug=owner_slug,
                                    license_name=license_name,
                                    subtitle=subtitle,
                                    description=description,
                                    files=[],
                                    is_private=not public,
                                    convert_to_csv=convert_to_csv,
                                    category_ids=keywords)

        with ResumableUploadContext() as upload_context:
            self.upload_files(request, resources, folder, ApiBlobType.DATASET,
                              upload_context, quiet, dir_mode)
            result = DatasetNewResponse(
                self.process_response(
                    self.with_retry(
                        self.datasets_create_new_with_http_info)(request)))

        return result

    def dataset_create_new_cli(self,
                               folder=None,
                               public=False,
                               quiet=False,
                               convert_to_csv=True,
                               dir_mode='skip'):
        """ client wrapper for creating a new dataset
             Parameters
            ==========
            folder: the folder to get the metadata file from
            public: should the dataset be public?
            quiet: suppress verbose output (default is False)
            convert_to_csv: if True, convert data to comma separated value
            dir_mode: What to do with directories: "skip" - ignore; "zip" - compress and upload
        """
        folder = folder or os.getcwd()
        result = self.dataset_create_new(folder, public, quiet, convert_to_csv,
                                         dir_mode)
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

    def download_file(self,
                      response,
                      outfile,
                      quiet=True,
                      resume=False,
                      chunk_size=1048576):
        """ download a file to an output file based on a chunk size

            Parameters
            ==========
            response: the response to download
            outfile: the output file to download to
            quiet: suppress verbose output (default is True)
            chunk_size: the size of the chunk to stream
            resume: whether to resume an existing download
        """

        outpath = os.path.dirname(outfile)
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        size = int(response.headers['Content-Length'])
        size_read = 0
        open_mode = 'wb'
        remote_date = datetime.strptime(response.headers['Last-Modified'],
                                        '%a, %d %b %Y %H:%M:%S %Z')
        remote_date_timestamp = time.mktime(remote_date.timetuple())

        if not quiet:
            print('Downloading ' + os.path.basename(outfile) + ' to ' +
                  outpath)

        file_exists = os.path.isfile(outfile)
        resumable = 'Accept-Ranges' in response.headers and response.headers[
            'Accept-Ranges'] == 'bytes'

        if resume and resumable and file_exists:
            size_read = os.path.getsize(outfile)
            open_mode = 'ab'

            if not quiet:
                print("... resuming from %d bytes (%d bytes left) ..." % (
                    size_read,
                    size - size_read,
                ))

            request_history = response.retries.history[0]
            response = self.api_client.request(
                request_history.method,
                request_history.redirect_location,
                headers={'Range': 'bytes=%d-' % (size_read, )},
                _preload_content=False)

        with tqdm(total=size,
                  initial=size_read,
                  unit='B',
                  unit_scale=True,
                  unit_divisor=1024,
                  disable=quiet) as pbar:
            with open(outfile, open_mode) as out:
                while True:
                    data = response.read(chunk_size)
                    if not data:
                        break
                    out.write(data)
                    os.utime(outfile,
                             times=(remote_date_timestamp - 1,
                                    remote_date_timestamp - 1))
                    size_read = min(size, size_read + chunk_size)
                    pbar.update(len(data))
            if not quiet:
                print('\n', end='')

            os.utime(outfile,
                     times=(remote_date_timestamp, remote_date_timestamp))

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
        """ list kernels based on a set of search criteria

            Parameters
            ==========
            page: the page of results to return (default is 1)
            page_size: results per page (default is 20)
            dataset: if defined, filter to this dataset (default None)
            competition: if defined, filter to this competition (default None)
            parent_kernel: if defined, filter to those with specified parent
            search: a custom search string to pass to the list query
            mine: if true, group is specified as "my" to return personal kernels
            user: filter results to a specific user
            language: the programming language of the kernel
            kernel_type: the type of kernel, one of valid_list_kernel_types (str)
            output_type: the output type, one of valid_list_output_types (str)
            sort_by: if defined, sort results by this string (valid_list_sort_by)
        """
        if int(page) <= 0:
            raise ValueError('Page number must be >= 1')

        page_size = int(page_size)
        if page_size <= 0:
            raise ValueError('Page size must be >= 1')
        if page_size > 100:
            page_size = 100

        if language and language not in self.valid_list_languages:
            raise ValueError('Invalid language specified. Valid options are ' +
                             str(self.valid_list_languages))

        if kernel_type and kernel_type not in self.valid_list_kernel_types:
            raise ValueError(
                'Invalid kernel type specified. Valid options are ' +
                str(self.valid_list_kernel_types))

        if output_type and output_type not in self.valid_list_output_types:
            raise ValueError(
                'Invalid output type specified. Valid options are ' +
                str(self.valid_list_output_types))

        if sort_by and sort_by not in self.valid_list_sort_by:
            raise ValueError(
                'Invalid sort by type specified. Valid options are ' +
                str(self.valid_list_sort_by))

        if sort_by == 'relevance' and search == '':
            raise ValueError('Cannot sort by relevance without a search term.')

        self.validate_dataset_string(dataset)
        self.validate_kernel_string(parent_kernel)

        group = 'everyone'
        if mine:
            group = 'profile'

        kernels_list_result = self.process_response(
            self.kernels_list_with_http_info(page=page,
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
        """ client wrapper for kernels_list, see this function for arguments.
            Additional arguments are provided here.
             Parameters
            ==========
            csv_display: if True, print comma separated values instead of table
        """
        kernels = self.kernels_list(page=page,
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
            print('Not found')

    def kernels_list_files(self, kernel, page_token=None, page_size=20):
        """ list files for a kernel
            Parameters
            ==========
            kernel: the string identifier of the kernel
                     should be in format [owner]/[kernel-name]
            page_token: the page token for pagination
            page_size: the number of items per page
        """
        if kernel is None:
            raise ValueError('A kernel must be specified')
        user_name, kernel_slug, kernel_version_number = self.split_dataset_string(
            kernel)

        kernels_list_files_result = self.process_response(
            self.kernels_list_files_with_http_info(kernel_slug=kernel_slug,
                                                   user_name=user_name,
                                                   page_token=page_token,
                                                   page_size=page_size))
        return FileList(kernels_list_files_result)

    def kernels_list_files_cli(self,
                               kernel,
                               kernel_opt=None,
                               csv_display=False,
                               page_token=None,
                               page_size=20):
        """ a wrapper to kernel_list_files for the client
            (list files for a kernel)
             Parameters
            ==========
            kernel: the string identifier of the kernel
                     should be in format [owner]/[kernel-name]
            kernel_opt: an alternative option to providing a kernel
            csv_display: if True, print comma separated values instead of table
            page_token: the page token for pagination
            page_size: the number of items per page
        """
        kernel = kernel or kernel_opt
        result = self.kernels_list_files(kernel, page_token, page_size)

        if result is None:
            print('No files found')
            return

        if result.error_message:
            print(result.error_message)
            return

        next_page_token = result.nextPageToken
        if next_page_token:
            print('Next Page Token = {}'.format(next_page_token))
        fields = ['name', 'size', 'creationDate']
        if csv_display:
            self.print_csv(result.files, fields)
        else:
            self.print_table(result.files, fields)

    def kernels_initialize(self, folder):
        """ create a new kernel in a specified folder from template, including
            json metadata that grabs values from the configuration.
             Parameters
            ==========
            folder: the path of the folder
        """
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        resources = []
        resource = {'path': 'INSERT_SCRIPT_PATH_HERE'}
        resources.append(resource)

        username = self.get_config_value(self.CONFIG_NAME_USER)
        meta_data = {
            'id':
            username + '/INSERT_KERNEL_SLUG_HERE',
            'title':
            'INSERT_TITLE_HERE',
            'code_file':
            'INSERT_CODE_FILE_PATH_HERE',
            'language':
            'Pick one of: {' +
            ','.join(x for x in self.valid_push_language_types) + '}',
            'kernel_type':
            'Pick one of: {' +
            ','.join(x for x in self.valid_push_kernel_types) + '}',
            'is_private':
            'true',
            'enable_gpu':
            'false',
            'enable_tpu':
            'false',
            'enable_internet':
            'true',
            'dataset_sources': [],
            'competition_sources': [],
            'kernel_sources': [],
            'model_sources': [],
        }
        meta_file = os.path.join(folder, self.KERNEL_METADATA_FILE)
        with open(meta_file, 'w') as f:
            json.dump(meta_data, f, indent=2)

        return meta_file

    def kernels_initialize_cli(self, folder=None):
        """ client wrapper for kernels_initialize, takes same arguments but
            sets default folder to be None. If None, defaults to present
            working directory.
             Parameters
            ==========
            folder: the path of the folder (None defaults to ${PWD})
        """
        folder = folder or os.getcwd()
        meta_file = self.kernels_initialize(folder)
        print('Kernel metadata template written to: ' + meta_file)

    def kernels_push(self, folder):
        """ read the metadata file and kernel files from a notebook, validate
            both, and use Kernel API to push to Kaggle if all is valid.
             Parameters
            ==========
            folder: the path of the folder
        """
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_file = os.path.join(folder, self.KERNEL_METADATA_FILE)
        if not os.path.isfile(meta_file):
            raise ValueError('Metadata file not found: ' +
                             self.KERNEL_METADATA_FILE)

        with open(meta_file) as f:
            meta_data = json.load(f)

        title = self.get_or_default(meta_data, 'title', None)
        if title and len(title) < 5:
            raise ValueError('Title must be at least five characters')

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
            if '/' in slug:
                kernel_slug = slug.split('/')[1]
            else:
                kernel_slug = slug
            if title:
                as_slug = slugify(title)
                if kernel_slug.lower() != as_slug:
                    print(
                        'Your kernel title does not resolve to the specified '
                        'id. This may result in surprising behavior. We '
                        'suggest making your title something that resolves to '
                        'the specified id. See %s for more information on '
                        'how slugs are determined.' %
                        'https://en.wikipedia.org/wiki/Clean_URL#Slug')

        language = self.get_or_default(meta_data, 'language', '')
        if language not in self.valid_push_language_types:
            raise ValueError(
                'A valid language must be specified in the metadata. Valid '
                'options are ' + str(self.valid_push_language_types))

        kernel_type = self.get_or_default(meta_data, 'kernel_type', '')
        if kernel_type not in self.valid_push_kernel_types:
            raise ValueError(
                'A valid kernel type must be specified in the metadata. Valid '
                'options are ' + str(self.valid_push_kernel_types))

        if kernel_type == 'notebook' and language == 'rmarkdown':
            language = 'r'

        dataset_sources = self.get_or_default(meta_data, 'dataset_sources', [])
        for source in dataset_sources:
            self.validate_dataset_string(source)

        kernel_sources = self.get_or_default(meta_data, 'kernel_sources', [])
        for source in kernel_sources:
            self.validate_kernel_string(source)

        model_sources = self.get_or_default(meta_data, 'model_sources', [])
        for source in model_sources:
            self.validate_model_string(source)

        docker_pinning_type = self.get_or_default(meta_data,
                                                  'docker_image_pinning_type',
                                                  None)
        if (docker_pinning_type is not None
                and docker_pinning_type not in self.valid_push_pinning_types):
            raise ValueError(
                'If specified, the docker_image_pinning_type must be '
                'one of ' + str(self.valid_push_pinning_types))

        with open(code_file) as f:
            script_body = f.read()

        if kernel_type == 'notebook':
            json_body = json.loads(script_body)
            if 'cells' in json_body:
                for cell in json_body['cells']:
                    if 'outputs' in cell and cell['cell_type'] == 'code':
                        cell['outputs'] = []
                    # The spec allows a list of strings,
                    # but the server expects just one
                    if 'source' in cell and isinstance(cell['source'], list):
                        cell['source'] = ''.join(cell['source'])
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
            enable_tpu=self.get_or_default(meta_data, 'enable_tpu', None),
            enable_internet=self.get_or_default(meta_data, 'enable_internet',
                                                None),
            dataset_data_sources=dataset_sources,
            competition_data_sources=self.get_or_default(
                meta_data, 'competition_sources', []),
            kernel_data_sources=kernel_sources,
            model_data_sources=model_sources,
            category_ids=self.get_or_default(meta_data, 'keywords', []),
            docker_image_pinning_type=docker_pinning_type)

        result = KernelPushResponse(
            self.process_response(
                self.kernel_push_with_http_info(
                    kernel_push_request=kernel_push_request)))
        return result

    def kernels_push_cli(self, folder):
        """ client wrapper for kernels_push, with same arguments.
        """
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

            if result.versionNumber:
                print('Kernel version %s successfully pushed.  Please check '
                      'progress at %s' % (result.versionNumber, result.url))
            else:
                # Shouldn't happen but didn't test exhaustively
                print('Kernel version successfully pushed.  Please check '
                      'progress at %s' % result.url)
        else:
            print('Kernel push error: ' + result.error)

    def kernels_pull(self, kernel, path, metadata=False, quiet=True):
        """ pull a kernel, including a metadata file (if metadata is True)
            and associated files to a specified path.
             Parameters
            ==========
            kernel: the kernel to pull
            path: the path to pull files to on the filesystem
            metadata: if True, also pull metadata
            quiet: suppress verbosity (default is True)
        """
        existing_metadata = None
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

        if os.path.isfile(effective_path):
            effective_dir = os.path.dirname(effective_path)
        else:
            effective_dir = effective_path
        metadata_path = os.path.join(effective_dir, self.KERNEL_METADATA_FILE)

        if not os.path.isfile(effective_path):
            language = blob['language'].lower()
            kernel_type = blob['kernelType'].lower()

            file_name = None
            if existing_metadata:
                file_name = existing_metadata['code_file']
            elif os.path.isfile(metadata_path):
                with open(metadata_path) as f:
                    file_name = json.load(f)['code_file']

            if not file_name or file_name == "INSERT_CODE_FILE_PATH_HERE":
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
                    'on the kaggle-api github issues' %
                    (language, kernel_type))
                print(
                    'Saving as a python file, even though this may not be the '
                    'correct language')
                file_name = 'script.py'
            script_path = os.path.join(effective_path, file_name)
        else:
            script_path = effective_path
            file_name = os.path.basename(effective_path)

        with open(script_path, 'w', encoding="utf-8") as f:
            f.write(blob['source'])

        if metadata:
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
            self.set_if_present(server_metadata, 'enableTpu', data,
                                'enable_tpu')
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
            self.set_if_present(server_metadata, 'modelDataSources', data,
                                'model_sources')
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
        """ client wrapper for kernels_pull
        """
        kernel = kernel or kernel_opt
        effective_path = self.kernels_pull(kernel,
                                           path=path,
                                           metadata=metadata,
                                           quiet=False)
        if metadata:
            print('Source code and metadata downloaded to ' + effective_path)
        else:
            print('Source code downloaded to ' + effective_path)

    def kernels_output(self, kernel, path, force=False, quiet=True):
        """ retrieve output for a specified kernel
             Parameters
            ==========
            kernel: the kernel to output
            path: the path to pull files to on the filesystem
            force: if output already exists, force overwrite (default False)
            quiet: suppress verbosity (default is True)
        """
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
                os.makedirs(os.path.split(outfile)[0], exist_ok=True)
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
        """ client wrapper for kernels_output, with same arguments. Extra
            arguments are described below, and see kernels_output for others.
             Parameters
            ==========
            kernel_opt: option from client instead of kernel, if not defined
        """
        kernel = kernel or kernel_opt
        self.kernels_output(kernel, path, force, quiet)

    def kernels_status(self, kernel):
        """ call to the api to get the status of a kernel.
             Parameters
            ==========
            kernel: the kernel to get the status for
        """
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
        """ client wrapper for kernel_status
             Parameters
            ==========
            kernel_opt: additional option from the client, if kernel not defined
        """
        kernel = kernel or kernel_opt
        response = self.kernels_status(kernel)
        status = response['status']
        message = response['failureMessage']
        if message:
            print('%s has status "%s"' % (kernel, status))
            print('Failure message: "%s"' % message)
        else:
            print('%s has status "%s"' % (kernel, status))

    def model_get(self, model):
        """ call to get a model from the API
             Parameters
            ==========
            model: the string identified of the model
                     should be in format [owner]/[model-name]
        """
        owner_slug, model_slug = self.split_model_string(model)

        model_get_result = self.process_response(
            self.get_model_with_http_info(owner_slug, model_slug))
        return model_get_result

    def model_get_cli(self, model, folder=None):
        """ wrapper for client for model_get, with additional
            model_opt to get a model from the API
             Parameters
            ==========
            model: the string identified of the model
                     should be in format [owner]/[model-name]
            folder: the folder to download the model metadata file
        """
        model = self.model_get(model)
        if folder is None:
            self.print_obj(model)
        else:
            meta_file = os.path.join(folder, self.MODEL_METADATA_FILE)

            data = {}
            data['id'] = model['id']
            model_ref_split = model['ref'].split('/')
            data['ownerSlug'] = model_ref_split[0]
            data['slug'] = model_ref_split[1]
            data['title'] = model['title']
            data['subtitle'] = model['subtitle']
            data['isPrivate'] = model['isPrivate']
            data['description'] = model['description']
            data['publishTime'] = model['publishTime']

            with open(meta_file, 'w') as f:
                json.dump(data, f, indent=2)
            print('Metadata file written to {}'.format(meta_file))

    def model_list(self,
                   sort_by=None,
                   search=None,
                   owner=None,
                   page_size=20,
                   page_token=None):
        """ return a list of models!

            Parameters
            ==========
            sort_by: how to sort the result, see valid_model_sort_bys for options
            search: a search term to use (default is empty string)
            owner: username or organization slug to filter the search to
            page_size: the page size to return (default is 20)
            page_token: the page token for pagination
        """
        if sort_by and sort_by not in self.valid_model_sort_bys:
            raise ValueError('Invalid sort by specified. Valid options are ' +
                             str(self.valid_model_sort_bys))

        if int(page_size) <= 0:
            raise ValueError('Page size must be >= 1')

        models_list_result = self.process_response(
            self.models_list_with_http_info(sort_by=sort_by or 'hotness',
                                            search=search or '',
                                            owner=owner or '',
                                            page_size=page_size,
                                            page_token=page_token))

        next_page_token = models_list_result['nextPageToken']
        if next_page_token:
            print('Next Page Token = {}'.format(next_page_token))

        return [Model(m) for m in models_list_result['models']]

    def model_list_cli(self,
                       sort_by=None,
                       search=None,
                       owner=None,
                       page_size=20,
                       page_token=None,
                       csv_display=False):
        """ a wrapper to model_list for the client. Additional parameters
            are described here, see model_list for others.

            Parameters
            ==========
            sort_by: how to sort the result, see valid_model_sort_bys for options
            search: a search term to use (default is empty string)
            owner: username or organization slug to filter the search to
            page_size: the page size to return (default is 20)
            page_token: the page token for pagination
            csv_display: if True, print comma separated values instead of table
        """
        models = self.model_list(sort_by, search, owner, page_size, page_token)
        fields = ['id', 'ref', 'title', 'subtitle', 'author']
        if models:
            if csv_display:
                self.print_csv(models, fields)
            else:
                self.print_table(models, fields)
        else:
            print('No models found')

    def model_initialize(self, folder):
        """ initialize a folder with a model configuration (metadata) file
            Parameters
            ==========
            folder: the folder to initialize the metadata file in
        """
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_data = {
            'ownerSlug': 'INSERT_OWNER_SLUG_HERE',
            'title': 'INSERT_TITLE_HERE',
            'slug': 'INSERT_SLUG_HERE',
            'subtitle': '',
            'isPrivate': True,
            'description': '''# Model Summary

# Model Characteristics

# Data Overview

# Evaluation Results
''',
            'publishTime': '',
            'provenanceSources': ''
        }
        meta_file = os.path.join(folder, self.MODEL_METADATA_FILE)
        with open(meta_file, 'w') as f:
            json.dump(meta_data, f, indent=2)

        print('Model template written to: ' + meta_file)
        return meta_file

    def model_initialize_cli(self, folder=None):
        folder = folder or os.getcwd()
        self.model_initialize(folder)

    def model_create_new(self, folder):
        """ create a new model.
             Parameters
            ==========
            folder: the folder to get the metadata file from
        """
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_file = self.get_model_metadata_file(folder)

        # read json
        with open(meta_file) as f:
            meta_data = json.load(f)
        owner_slug = self.get_or_fail(meta_data, 'ownerSlug')
        slug = self.get_or_fail(meta_data, 'slug')
        title = self.get_or_fail(meta_data, 'title')
        subtitle = meta_data.get('subtitle')
        is_private = self.get_or_fail(meta_data, 'isPrivate')
        description = self.sanitize_markdown(
            self.get_or_fail(meta_data, 'description'))
        publish_time = meta_data.get('publishTime')
        provenance_sources = meta_data.get('provenanceSources')

        # validations
        if owner_slug == 'INSERT_OWNER_SLUG_HERE':
            raise ValueError(
                'Default ownerSlug detected, please change values before uploading'
            )
        if title == 'INSERT_TITLE_HERE':
            raise ValueError(
                'Default title detected, please change values before uploading'
            )
        if slug == 'INSERT_SLUG_HERE':
            raise ValueError(
                'Default slug detected, please change values before uploading')
        if not isinstance(is_private, bool):
            raise ValueError('model.isPrivate must be a boolean')
        if publish_time:
            self.validate_date(publish_time)

        request = ModelNewRequest(owner_slug=owner_slug,
                                  slug=slug,
                                  title=title,
                                  subtitle=subtitle,
                                  is_private=is_private,
                                  description=description,
                                  publish_time=publish_time,
                                  provenance_sources=provenance_sources)
        result = ModelNewResponse(
            self.process_response(
                self.models_create_new_with_http_info(request)))

        return result

    def model_create_new_cli(self, folder=None):
        """ client wrapper for creating a new model
             Parameters
            ==========
            folder: the folder to get the metadata file from
        """
        folder = folder or os.getcwd()
        result = self.model_create_new(folder)

        if result.hasId:
            print('Your model was created. Id={}. Url={}'.format(
                result.id, result.url))
        else:
            print('Model creation error: ' + result.error)

    def model_delete(self, model, yes):
        """ call to delete a model from the API
             Parameters
            ==========
            model: the string identified of the model
                     should be in format [owner]/[model-name]
            yes: automatic confirmation
        """
        owner_slug, model_slug = self.split_model_string(model)

        if not yes:
            if not self.confirmation():
                print('Deletion cancelled')
                exit(0)

        res = ModelDeleteResponse(
            self.process_response(
                self.delete_model_with_http_info(owner_slug, model_slug)))
        return res

    def model_delete_cli(self, model, yes):
        """ wrapper for client for model_delete
             Parameters
            ==========
            model: the string identified of the model
                     should be in format [owner]/[model-name]
            yes: automatic confirmation
        """
        result = self.model_delete(model, yes)

        if result.hasError:
            print('Model deletion error: ' + result.error)
        else:
            print('The model was deleted.')

    def model_update(self, folder):
        """ update a model.
             Parameters
            ==========
            folder: the folder to get the metadata file from
        """
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_file = self.get_model_metadata_file(folder)

        # read json
        with open(meta_file) as f:
            meta_data = json.load(f)
        owner_slug = self.get_or_fail(meta_data, 'ownerSlug')
        slug = self.get_or_fail(meta_data, 'slug')
        title = self.get_or_default(meta_data, 'title', None)
        subtitle = self.get_or_default(meta_data, 'subtitle', None)
        is_private = self.get_or_default(meta_data, 'isPrivate', None)
        description = self.get_or_default(meta_data, 'description', None)
        publish_time = self.get_or_default(meta_data, 'publishTime', None)
        provenance_sources = self.get_or_default(meta_data,
                                                 'provenanceSources', None)

        # validations
        if owner_slug == 'INSERT_OWNER_SLUG_HERE':
            raise ValueError(
                'Default ownerSlug detected, please change values before uploading'
            )
        if slug == 'INSERT_SLUG_HERE':
            raise ValueError(
                'Default slug detected, please change values before uploading')
        if is_private != None and not isinstance(is_private, bool):
            raise ValueError('model.isPrivate must be a boolean')
        if publish_time:
            self.validate_date(publish_time)

        # mask
        update_mask = {'paths': []}
        if title != None:
            update_mask['paths'].append('title')
        if subtitle != None:
            update_mask['paths'].append('subtitle')
        if is_private != None:
            update_mask['paths'].append('is_private')
        else:
            is_private = True  # default value, not updated
        if description != None:
            description = self.sanitize_markdown(description)
            update_mask['paths'].append('description')
        if publish_time != None:
            update_mask['paths'].append('publish_time')
        if provenance_sources != None:
            update_mask['paths'].append('provenance_sources')

        request = ModelUpdateRequest(title=title,
                                     subtitle=subtitle,
                                     is_private=is_private,
                                     description=description,
                                     publish_time=publish_time,
                                     provenance_sources=provenance_sources,
                                     update_mask=update_mask)
        result = ModelNewResponse(
            self.process_response(
                self.update_model_with_http_info(owner_slug, slug, request)))

        return result

    def model_update_cli(self, folder=None):
        """ client wrapper for updating a model
             Parameters
            ==========
            folder: the folder to get the metadata file from
        """
        folder = folder or os.getcwd()
        result = self.model_update(folder)

        if result.hasId:
            print('Your model was updated. Id={}. Url={}'.format(
                result.id, result.url))
        else:
            print('Model update error: ' + result.error)

    def model_instance_get(self, model_instance):
        """ call to get a model instance from the API
             Parameters
            ==========
            model_instance: the string identified of the model instance
                     should be in format [owner]/[model-name]/[framework]/[instance-slug]
        """
        if model_instance is None:
            raise ValueError('A model instance must be specified')
        owner_slug, model_slug, framework, instance_slug = self.split_model_instance_string(
            model_instance)

        mi = self.process_response(
            self.get_model_instance_with_http_info(owner_slug, model_slug,
                                                   framework, instance_slug))
        return mi

    def model_instance_get_cli(self, model_instance, folder=None):
        """ wrapper for client for model_instance_get
             Parameters
            ==========
            model_instance: the string identified of the model instance
                     should be in format [owner]/[model-name]/[framework]/[instance-slug]
            folder: the folder to download the model metadata file
        """
        mi = self.model_instance_get(model_instance)
        if folder is None:
            self.print_obj(mi)
        else:
            meta_file = os.path.join(folder, self.MODEL_INSTANCE_METADATA_FILE)

            owner_slug, model_slug, framework, instance_slug = self.split_model_instance_string(
                model_instance)

            data = {}
            data['id'] = mi['id']
            data['ownerSlug'] = owner_slug
            data['modelSlug'] = model_slug
            data['instanceSlug'] = mi['slug']
            data['framework'] = mi['framework']
            data['overview'] = mi['overview']
            data['usage'] = mi['usage']
            data['licenseName'] = mi['licenseName']
            data['fineTunable'] = mi['fineTunable']
            data['trainingData'] = mi['trainingData']
            data['versionId'] = mi['versionId']
            data['versionNumber'] = mi['versionNumber']
            data['modelInstanceType'] = mi['modelInstanceType']
            if mi['baseModelInstanceInformation'] is not None:
                data['baseModelInstance'] = '{}/{}/{}/{}'.format(
                    mi['baseModelInstanceInformation']['owner']['slug'],
                    mi['baseModelInstanceInformation']['modelSlug'],
                    mi['baseModelInstanceInformation']['framework'],
                    mi['baseModelInstanceInformation']['instanceSlug'])
            data['externalBaseModelUrl'] = mi['externalBaseModelUrl']

            with open(meta_file, 'w') as f:
                json.dump(data, f, indent=2)
            print('Metadata file written to {}'.format(meta_file))

    def model_instance_initialize(self, folder):
        """ initialize a folder with a model instance configuration (metadata) file
             Parameters
            ==========
            folder: the folder to initialize the metadata file in
        """
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_data = {
            'ownerSlug': 'INSERT_OWNER_SLUG_HERE',
            'modelSlug': 'INSERT_EXISTING_MODEL_SLUG_HERE',
            'instanceSlug': 'INSERT_INSTANCE_SLUG_HERE',
            'framework': 'INSERT_FRAMEWORK_HERE',
            'overview': '',
            'usage': '''# Model Format

# Training Data

# Model Inputs

# Model Outputs

# Model Usage

# Fine-tuning

# Changelog
''',
            'licenseName': 'Apache 2.0',
            'fineTunable': False,
            'trainingData': [],
            'modelInstanceType': 'Unspecified',
            'baseModelInstanceId': 0,
            'externalBaseModelUrl': ''
        }
        meta_file = os.path.join(folder, self.MODEL_INSTANCE_METADATA_FILE)
        with open(meta_file, 'w') as f:
            json.dump(meta_data, f, indent=2)

        print('Model Instance template written to: ' + meta_file)
        return meta_file

    def model_instance_initialize_cli(self, folder):
        folder = folder or os.getcwd()
        self.model_instance_initialize(folder)

    def model_instance_create(self, folder, quiet=False, dir_mode='skip'):
        """ create a new model instance.
             Parameters
            ==========
            folder: the folder to get the metadata file from
            quiet: suppress verbose output (default is False)
            dir_mode: what to do with directories: "skip" - ignore; "zip" - compress and upload
        """
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_file = self.get_model_instance_metadata_file(folder)

        # read json
        with open(meta_file) as f:
            meta_data = json.load(f)
        owner_slug = self.get_or_fail(meta_data, 'ownerSlug')
        model_slug = self.get_or_fail(meta_data, 'modelSlug')
        instance_slug = self.get_or_fail(meta_data, 'instanceSlug')
        framework = self.get_or_fail(meta_data, 'framework')
        overview = self.sanitize_markdown(
            self.get_or_default(meta_data, 'overview', ''))
        usage = self.sanitize_markdown(
            self.get_or_default(meta_data, 'usage', ''))
        license_name = self.get_or_fail(meta_data, 'licenseName')
        fine_tunable = self.get_or_default(meta_data, 'fineTunable', False)
        training_data = self.get_or_default(meta_data, 'trainingData', [])
        model_instance_type = self.get_or_default(meta_data,
                                                  'modelInstanceType',
                                                  'Unspecified')
        base_model_instance = self.get_or_default(meta_data,
                                                  'baseModelInstance', '')
        external_base_model_url = self.get_or_default(meta_data,
                                                      'externalBaseModelUrl',
                                                      '')

        # validations
        if owner_slug == 'INSERT_OWNER_SLUG_HERE':
            raise ValueError(
                'Default ownerSlug detected, please change values before uploading'
            )
        if model_slug == 'INSERT_EXISTING_MODEL_SLUG_HERE':
            raise ValueError(
                'Default modelSlug detected, please change values before uploading'
            )
        if instance_slug == 'INSERT_INSTANCE_SLUG_HERE':
            raise ValueError(
                'Default instanceSlug detected, please change values before uploading'
            )
        if framework == 'INSERT_FRAMEWORK_HERE':
            raise ValueError(
                'Default framework detected, please change values before uploading'
            )
        if license_name == '':
            raise ValueError('Please specify a license')
        if not isinstance(fine_tunable, bool):
            raise ValueError('modelInstance.fineTunable must be a boolean')
        if not isinstance(training_data, list):
            raise ValueError('modelInstance.trainingData must be a list')

        request = ModelNewInstanceRequest(
            instance_slug=instance_slug,
            framework=framework,
            overview=overview,
            usage=usage,
            license_name=license_name,
            fine_tunable=fine_tunable,
            training_data=training_data,
            model_instance_type=model_instance_type,
            base_model_instance=base_model_instance,
            external_base_model_url=external_base_model_url,
            files=[])

        with ResumableUploadContext() as upload_context:
            self.upload_files(request, None, folder, ApiBlobType.MODEL,
                              upload_context, quiet, dir_mode)
            result = ModelNewResponse(
                self.process_response(
                    self.with_retry(
                        self.models_create_instance_with_http_info)(owner_slug,
                                                                    model_slug,
                                                                    request)))

            return result

    def model_instance_create_cli(self, folder, quiet=False, dir_mode='skip'):
        """ client wrapper for creating a new model instance
             Parameters
            ==========
            folder: the folder to get the metadata file from
            quiet: suppress verbose output (default is False)
            dir_mode: what to do with directories: "skip" - ignore; "zip" - compress and upload
        """
        folder = folder or os.getcwd()
        result = self.model_instance_create(folder, quiet, dir_mode)

        if result.hasId:
            print('Your model instance was created. Id={}. Url={}'.format(
                result.id, result.url))
        else:
            print('Model instance creation error: ' + result.error)

    def model_instance_delete(self, model_instance, yes):
        """ call to delete a model instance from the API
             Parameters
            ==========
            model_instance: the string identified of the model instance
                     should be in format [owner]/[model-name]/[framework]/[instance-slug]
            yes: automatic confirmation
        """
        if model_instance is None:
            raise ValueError('A model instance must be specified')
        owner_slug, model_slug, framework, instance_slug = self.split_model_instance_string(
            model_instance)

        if not yes:
            if not self.confirmation():
                print('Deletion cancelled')
                exit(0)

        res = ModelDeleteResponse(
            self.process_response(
                self.delete_model_instance_with_http_info(
                    owner_slug, model_slug, framework, instance_slug)))
        return res

    def model_instance_delete_cli(self, model_instance, yes):
        """ wrapper for client for model_instance_delete
             Parameters
            ==========
            model_instance: the string identified of the model instance
                     should be in format [owner]/[model-name]/[framework]/[instance-slug]
            yes: automatic confirmation
        """
        result = self.model_instance_delete(model_instance, yes)

        if result.hasError:
            print('Model instance deletion error: ' + result.error)
        else:
            print('The model instance was deleted.')

    def model_instance_files(self,
                             model_instance,
                             page_token=None,
                             page_size=20,
                             csv_display=False):
        """ list all files for the current version of a model instance

            Parameters
            ==========
            model_instance: the string identifier of the model instance
                    should be in format [owner]/[model-name]/[framework]/[instance-slug]
            page_token: token for pagination
            page_size: the number of items per page
            csv_display: if True, print comma separated values instead of table
        """
        if model_instance is None:
            raise ValueError('A model_instance must be specified')

        self.validate_model_instance_string(model_instance)
        urls = model_instance.split('/')
        [owner_slug, model_slug, framework, instance_slug] = urls

        response = self.process_response(
            self.model_instance_files_with_http_info(
                owner_slug=owner_slug,
                model_slug=model_slug,
                framework=framework,
                instance_slug=instance_slug,
                page_size=page_size,
                page_token=page_token,
                _preload_content=True))

        if response:
            next_page_token = response['nextPageToken']
            if next_page_token:
                print('Next Page Token = {}'.format(next_page_token))
            return FileList(response)
        else:
            print('No files found')

    def model_instance_files_cli(self,
                                 model_instance,
                                 page_token=None,
                                 page_size=20,
                                 csv_display=False):
        """ client wrapper for model_instance_files.

            Parameters
            ==========
            model_instance: the string identified of the model instance version
                    should be in format [owner]/[model-name]/[framework]/[instance-slug]
            page_token: token for pagination
            page_size: the number of items per page
            csv_display: if True, print comma separated values instead of table
        """
        result = self.model_instance_files(model_instance,
                                           page_token=page_token,
                                           page_size=page_size,
                                           csv_display=csv_display)
        if result and result.files is not None:
            fields = ['name', 'size', 'creationDate']
            if csv_display:
                self.print_csv(result.files, fields)
            else:
                self.print_table(result.files, fields)

    def model_instance_update(self, folder):
        """ update a model instance.
             Parameters
            ==========
            folder: the folder to get the metadata file from
        """
        if not os.path.isdir(folder):
            raise ValueError('Invalid folder: ' + folder)

        meta_file = self.get_model_instance_metadata_file(folder)

        # read json
        with open(meta_file) as f:
            meta_data = json.load(f)
        owner_slug = self.get_or_fail(meta_data, 'ownerSlug')
        model_slug = self.get_or_fail(meta_data, 'modelSlug')
        framework = self.get_or_fail(meta_data, 'framework')
        instance_slug = self.get_or_fail(meta_data, 'instanceSlug')
        overview = self.get_or_default(meta_data, 'overview', None)
        usage = self.get_or_default(meta_data, 'usage', None)
        license_name = self.get_or_default(meta_data, 'licenseName', None)
        fine_tunable = self.get_or_default(meta_data, 'fineTunable', None)
        training_data = self.get_or_default(meta_data, 'trainingData', None)
        model_instance_type = self.get_or_default(meta_data,
                                                  'modelInstanceType', None)
        base_model_instance = self.get_or_default(meta_data,
                                                  'baseModelInstance', None)
        external_base_model_url = self.get_or_default(meta_data,
                                                      'externalBaseModelUrl',
                                                      None)

        # validations
        if owner_slug == 'INSERT_OWNER_SLUG_HERE':
            raise ValueError(
                'Default ownerSlug detected, please change values before uploading'
            )
        if model_slug == 'INSERT_SLUG_HERE':
            raise ValueError(
                'Default model slug detected, please change values before uploading'
            )
        if instance_slug == 'INSERT_INSTANCE_SLUG_HERE':
            raise ValueError(
                'Default instance slug detected, please change values before uploading'
            )
        if framework == 'INSERT_FRAMEWORK_HERE':
            raise ValueError(
                'Default framework detected, please change values before uploading'
            )
        if fine_tunable != None and not isinstance(fine_tunable, bool):
            raise ValueError('modelInstance.fineTunable must be a boolean')
        if training_data != None and not isinstance(training_data, list):
            raise ValueError('modelInstance.trainingData must be a list')

        # mask
        update_mask = {'paths': []}
        if overview != None:
            overview = self.sanitize_markdown(overview)
            update_mask['paths'].append('overview')
        if usage != None:
            usage = self.sanitize_markdown(usage)
            update_mask['paths'].append('usage')
        if license_name != None:
            update_mask['paths'].append('license_name')
        else:
            license_name = "Apache 2.0"  # default value even if not updated
        if fine_tunable != None:
            update_mask['paths'].append('fine_tunable')
        if training_data != None:
            update_mask['paths'].append('training_data')
        if model_instance_type != None:
            update_mask['paths'].append('model_instance_type')
        if base_model_instance != None:
            update_mask['paths'].append('base_model_instance')
        if external_base_model_url != None:
            update_mask['paths'].append('external_base_model_url')

        request = ModelInstanceUpdateRequest(
            overview=overview,
            usage=usage,
            license_name=license_name,
            fine_tunable=fine_tunable,
            training_data=training_data,
            model_instance_type=model_instance_type,
            base_model_instance=base_model_instance,
            external_base_model_url=external_base_model_url,
            update_mask=update_mask)
        result = ModelNewResponse(
            self.process_response(
                self.update_model_instance_with_http_info(
                    owner_slug, model_slug, framework, instance_slug,
                    request)))

        return result

    def model_instance_update_cli(self, folder=None):
        """ client wrapper for updating a model instance
             Parameters
            ==========
            folder: the folder to get the metadata file from
        """
        folder = folder or os.getcwd()
        result = self.model_instance_update(folder)

        if result.hasId:
            print('Your model instance was updated. Id={}. Url={}'.format(
                result.id, result.url))
        else:
            print('Model update error: ' + result.error)

    def model_instance_version_create(self,
                                      model_instance,
                                      folder,
                                      version_notes='',
                                      quiet=False,
                                      dir_mode='skip'):
        """ create a new model instance version.
             Parameters
            ==========
            model_instance: the string identified of the model instance
                     should be in format [owner]/[model-name]/[framework]/[instance-slug]
            folder: the folder to get the metadata file from
            version_notes: the version notes to record for this new version
            quiet: suppress verbose output (default is False)
            dir_mode: what to do with directories: "skip" - ignore; "zip" - compress and upload
        """
        owner_slug, model_slug, framework, instance_slug = self.split_model_instance_string(
            model_instance)

        request = ModelInstanceNewVersionRequest(version_notes=version_notes,
                                                 files=[])

        with ResumableUploadContext() as upload_context:
            self.upload_files(request, None, folder, ApiBlobType.MODEL,
                              upload_context, quiet, dir_mode)
            result = ModelNewResponse(
                self.process_response(
                    self.with_retry(
                        self.models_create_instance_version_with_http_info)(
                            owner_slug, model_slug, framework, instance_slug,
                            request)))

            return result

    def model_instance_version_create_cli(self,
                                          model_instance,
                                          folder,
                                          version_notes='',
                                          quiet=False,
                                          dir_mode='skip'):
        """ client wrapper for creating a new model instance version
             Parameters
            ==========
            model_instance: the string identified of the model instance
                     should be in format [owner]/[model-name]/[framework]/[instance-slug]
            folder: the folder to get the metadata file from
            version_notes: the version notes to record for this new version
            quiet: suppress verbose output (default is False)
            dir_mode: what to do with directories: "skip" - ignore; "zip" - compress and upload
        """
        result = self.model_instance_version_create(model_instance, folder,
                                                    version_notes, quiet,
                                                    dir_mode)

        if result.hasId:
            print('Your model instance version was created. Url={}'.format(
                result.url))
        else:
            print('Model instance version creation error: ' + result.error)

    def model_instance_version_download(self,
                                        model_instance_version,
                                        path=None,
                                        force=False,
                                        quiet=True,
                                        untar=False):
        """ download all files for a model instance version

            Parameters
            ==========
            model_instance_version: the string identified of the model instance version
                    should be in format [owner]/[model-name]/[framework]/[instance-slug]/[version-number]
            path: the path to download the model instance version to
            force: force the download if the file already exists (default False)
            quiet: suppress verbose output (default is True)
            untar: if True, untar files upon download (default is False)
        """
        if model_instance_version is None:
            raise ValueError('A model_instance_version must be specified')

        self.validate_model_instance_version_string(model_instance_version)
        urls = model_instance_version.split('/')
        owner_slug = urls[0]
        model_slug = urls[1]
        framework = urls[2]
        instance_slug = urls[3]
        version_number = urls[4]

        if path is None:
            effective_path = self.get_default_download_dir(
                'models', owner_slug, model_slug, framework, instance_slug,
                version_number)
        else:
            effective_path = path

        response = self.process_response(
            self.model_instance_versions_download_with_http_info(
                owner_slug=owner_slug,
                model_slug=model_slug,
                framework=framework,
                instance_slug=instance_slug,
                version_number=version_number,
                _preload_content=False))

        outfile = os.path.join(effective_path, model_slug + '.tar.gz')
        if force or self.download_needed(response, outfile, quiet):
            self.download_file(response, outfile, quiet, not force)
            downloaded = True
        else:
            downloaded = False

        if downloaded:
            if untar:
                try:
                    with tarfile.open(outfile, mode='r:gz') as t:
                        t.extractall(effective_path)
                except Exception as e:
                    raise ValueError(
                        'Error extracting the tar.gz file, please report on '
                        'www.github.com/kaggle/kaggle-api', e)

                try:
                    os.remove(outfile)
                except OSError as e:
                    print('Could not delete tar file, got %s' % e)
        return outfile

    def model_instance_version_download_cli(self,
                                            model_instance_version,
                                            path=None,
                                            untar=False,
                                            force=False,
                                            quiet=False):
        """ client wrapper for model_instance_version_download.

            Parameters
            ==========
            model_instance_version: the string identified of the model instance version
                    should be in format [owner]/[model-name]/[framework]/[instance-slug]/[version-number]
            path: the path to download the model instance version to
            force: force the download if the file already exists (default False)
            quiet: suppress verbose output (default is False)
            untar: if True, untar files upon download (default is False)
        """
        return self.model_instance_version_download(model_instance_version,
                                                    path=path,
                                                    untar=untar,
                                                    force=force,
                                                    quiet=quiet)

    def model_instance_version_files(self,
                                     model_instance_version,
                                     page_token=None,
                                     page_size=20,
                                     csv_display=False):
        """ list all files for a model instance version

            Parameters
            ==========
            model_instance_version: the string identifier of the model instance version
                    should be in format [owner]/[model-name]/[framework]/[instance-slug]/[version-number]
            page_token: token for pagination
            page_size: the number of items per page
            csv_display: if True, print comma separated values instead of table
        """
        if model_instance_version is None:
            raise ValueError('A model_instance_version must be specified')

        self.validate_model_instance_version_string(model_instance_version)
        urls = model_instance_version.split('/')
        [owner_slug, model_slug, framework, instance_slug,
         version_number] = urls

        response = self.process_response(
            self.model_instance_version_files_with_http_info(
                owner_slug=owner_slug,
                model_slug=model_slug,
                framework=framework,
                instance_slug=instance_slug,
                version_number=version_number,
                page_size=page_size,
                page_token=page_token,
                _preload_content=True))

        if response:
            next_page_token = response['nextPageToken']
            if next_page_token:
                print('Next Page Token = {}'.format(next_page_token))
            return FileList(response)
        else:
            print('No files found')

    def model_instance_version_files_cli(self,
                                         model_instance_version,
                                         page_token=None,
                                         page_size=20,
                                         csv_display=False):
        """ client wrapper for model_instance_version_files.

            Parameters
            ==========
            model_instance_version: the string identified of the model instance version
                    should be in format [owner]/[model-name]/[framework]/[instance-slug]/[version-number]
            page_token: token for pagination
            page_size: the number of items per page
            csv_display: if True, print comma separated values instead of table
        """
        result = self.model_instance_version_files(model_instance_version,
                                                   page_token=page_token,
                                                   page_size=page_size,
                                                   csv_display=csv_display)
        if result and result.files is not None:
            fields = ['name', 'size', 'creationDate']
            if csv_display:
                self.print_csv(result.files, fields)
            else:
                self.print_table(result.files, fields)

    def model_instance_version_delete(self, model_instance_version, yes):
        """ call to delete a model instance version from the API
             Parameters
            ==========
            model_instance_version: the string identified of the model instance version
                should be in format [owner]/[model-name]/[framework]/[instance-slug]/[version-number]
            yes: automatic confirmation
        """
        if model_instance_version is None:
            raise ValueError('A model instance version must be specified')

        self.validate_model_instance_version_string(model_instance_version)
        urls = model_instance_version.split('/')
        owner_slug = urls[0]
        model_slug = urls[1]
        framework = urls[2]
        instance_slug = urls[3]
        version_number = urls[4]

        if not yes:
            if not self.confirmation():
                print('Deletion cancelled')
                exit(0)

        res = ModelDeleteResponse(
            self.process_response(
                self.delete_model_instance_version_with_http_info(
                    owner_slug, model_slug, framework, instance_slug,
                    version_number)))
        return res

    def model_instance_version_delete_cli(self, model_instance_version, yes):
        """ wrapper for client for model_instance_version_delete
             Parameters
            ==========
            model_instance_version: the string identified of the model instance version
                should be in format [owner]/[model-name]/[framework]/[instance-slug]/[version-number]
            yes: automatic confirmation
        """
        result = self.model_instance_version_delete(model_instance_version,
                                                    yes)

        if result.hasError:
            print('Model instance version deletion error: ' + result.error)
        else:
            print('The model instance version was deleted.')

    def files_upload_cli(self, local_paths, inbox_path, no_resume,
                         no_compress):
        if len(local_paths) > self.MAX_NUM_INBOX_FILES_TO_UPLOAD:
            print('Cannot upload more than %d files!' %
                  self.MAX_NUM_INBOX_FILES_TO_UPLOAD)
            return

        files_to_create = []
        with ResumableUploadContext(no_resume) as upload_context:
            for local_path in local_paths:
                (upload_file,
                 file_name) = self.file_upload_cli(local_path, inbox_path,
                                                   no_compress, upload_context)
                if upload_file is None:
                    continue

                create_inbox_file_request = CreateInboxFileRequest(
                    virtual_directory=inbox_path,
                    blob_file_token=upload_file.token)
                files_to_create.append((create_inbox_file_request, file_name))

            for (create_inbox_file_request, file_name) in files_to_create:
                self.process_response(
                    self.with_retry(
                        self.create_inbox_file)(create_inbox_file_request))
                print('Inbox file created:', file_name)

    def file_upload_cli(self, local_path, inbox_path, no_compress,
                        upload_context):
        full_path = os.path.abspath(local_path)
        parent_path = os.path.dirname(full_path)
        file_or_folder_name = os.path.basename(full_path)
        dir_mode = 'tar' if no_compress else 'zip'

        upload_file = self._upload_file_or_folder(parent_path,
                                                  file_or_folder_name,
                                                  ApiBlobType.INBOX,
                                                  upload_context, dir_mode)
        return (upload_file, file_or_folder_name)

    def print_obj(self, obj, indent=2):
        pretty = json.dumps(obj, indent=indent)
        print(pretty)

    def download_needed(self, response, outfile, quiet=True):
        """ determine if a download is needed based on timestamp. Return True
            if needed (remote is newer) or False if local is newest.
             Parameters
            ==========
            response: the response from the API
            outfile: the output file to write to
            quiet: suppress verbose output (default is True)
        """
        try:
            remote_date = datetime.strptime(response.headers['Last-Modified'],
                                            '%a, %d %b %Y %H:%M:%S %Z')
            file_exists = os.path.isfile(outfile)
            if file_exists:
                local_date = datetime.fromtimestamp(os.path.getmtime(outfile))
                remote_size = int(response.headers['Content-Length'])
                local_size = os.path.getsize(outfile)
                if local_size < remote_size:
                    return True
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
        """ print a table of items, for a set of fields defined

            Parameters
            ==========
            items: a list of items to print
            fields: a list of fields to select from items
        """
        formats = []
        borders = []
        if len(items) == 0:
            return
        for f in fields:
            length = max(len(f),
                         max([len(self.string(getattr(i, f))) for i in items]))
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
            try:
                print(row_format.format(*i_fields))
            except UnicodeEncodeError:
                print(row_format.format(*i_fields).encode('utf-8'))

    def print_csv(self, items, fields):
        """ print a set of fields in a set of items using a csv.writer

            Parameters
            ==========
            items: a list of items to print
            fields: a list of fields to select from items
        """
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

    def get_model_metadata_file(self, folder):
        meta_file = os.path.join(folder, self.MODEL_METADATA_FILE)
        if not os.path.isfile(meta_file):
            raise ValueError('Metadata file not found: ' +
                             self.MODEL_METADATA_FILE)
        return meta_file

    def get_model_instance_metadata_file(self, folder):
        meta_file = os.path.join(folder, self.MODEL_INSTANCE_METADATA_FILE)
        if not os.path.isfile(meta_file):
            raise ValueError('Metadata file not found: ' +
                             self.MODEL_INSTANCE_METADATA_FILE)
        return meta_file

    def process_response(self, result):
        """ process a response from the API. We check the API version against
            the client's to see if it's old, and give them a warning (once)

            Parameters
            ==========
            result: the result from the API
        """
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
            if isinstance(data,
                          dict) and 'code' in data and data['code'] != 200:
                raise Exception(data['message'])
            return data
        return result

    def is_up_to_date(self, server_version):
        """ determine if a client (on the local user's machine) is up to date
            with the version provided on the server. Return a boolean with True
            or False
             Parameters
            ==========
            server_version: the server version string to compare to the host
        """
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
            if 'a' in client_split[i] or 'b' in client_split[i]:
                # Using a alpha/beta version, don't check
                return True
            client = int(client_split[i])
            server = int(server_split[i])
            if client < server:
                return False
            elif server < client:
                return True

        return True

    def upload_files(self,
                     request,
                     resources,
                     folder,
                     blob_type,
                     upload_context,
                     quiet=False,
                     dir_mode='skip'):
        """ upload files in a folder
             Parameters
            ==========
            request: the prepared request
            resources: the files to upload
            folder: the folder to upload from
            blob_type (ApiBlobType): To which entity the file/blob refers
            upload_context (ResumableUploadContext): Context for resumable uploads
            quiet: suppress verbose output (default is False)
        """
        for file_name in os.listdir(folder):
            if (file_name in [
                    self.DATASET_METADATA_FILE, self.OLD_DATASET_METADATA_FILE,
                    self.KERNEL_METADATA_FILE, self.MODEL_METADATA_FILE,
                    self.MODEL_INSTANCE_METADATA_FILE
            ]):
                continue
            upload_file = self._upload_file_or_folder(folder, file_name,
                                                      blob_type,
                                                      upload_context, dir_mode,
                                                      quiet, resources)
            if upload_file is not None:
                request.files.append(upload_file)

    def _upload_file_or_folder(self,
                               parent_path,
                               file_or_folder_name,
                               blob_type,
                               upload_context,
                               dir_mode,
                               quiet=False,
                               resources=None):
        full_path = os.path.join(parent_path, file_or_folder_name)
        if os.path.isfile(full_path):
            return self._upload_file(file_or_folder_name, full_path, blob_type,
                                     upload_context, quiet, resources)

        elif os.path.isdir(full_path):
            if dir_mode in ['zip', 'tar']:
                with DirectoryArchive(full_path, dir_mode) as archive:
                    return self._upload_file(archive.name, archive.path,
                                             blob_type, upload_context, quiet,
                                             resources)
            elif not quiet:
                print("Skipping folder: " + file_or_folder_name +
                      "; use '--dir-mode' to upload folders")
        else:
            if not quiet:
                print('Skipping: ' + file_or_folder_name)
        return None

    def _upload_file(self, file_name, full_path, blob_type, upload_context,
                     quiet, resources):
        """ Helper function to upload a single file
            Parameters
            ==========
            file_name: name of the file to upload
            full_path: path to the file to upload
            blob_type (ApiBlobType): To which entity the file/blob refers
            upload_context (ResumableUploadContext): Context for resumable uploads
            quiet: suppress verbose output
            resources: optional file metadata
            :return: None - upload unsuccessful; instance of UploadFile - upload successful
        """

        if not quiet:
            print('Starting upload for file ' + file_name)

        content_length = os.path.getsize(full_path)
        token = self._upload_blob(full_path, quiet, blob_type, upload_context)
        if token is None:
            if not quiet:
                print('Upload unsuccessful: ' + file_name)
            return None
        if not quiet:
            print('Upload successful: ' + file_name + ' (' +
                  File.get_size(content_length) + ')')
        upload_file = UploadFile()
        upload_file.token = token
        if resources:
            for item in resources:
                if file_name == item.get('path'):
                    upload_file.description = item.get('description')
                    if 'schema' in item:
                        fields = self.get_or_default(item['schema'], 'fields',
                                                     [])
                        processed = []
                        count = 0
                        for field in fields:
                            processed.append(self.process_column(field))
                            processed[count].order = count
                            count += 1
                        upload_file.columns = processed
        return upload_file

    def process_column(self, column):
        """ process a column, check for the type, and return the processed
            column
             Parameters
            ==========
            column: a list of values in a column to be processed
        """
        processed_column = DatasetColumn(name=self.get_or_fail(column, 'name'),
                                         description=self.get_or_default(
                                             column, 'description', ''))
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

    def upload_complete(self, path, url, quiet, resume=False):
        """ function to complete an upload to retrieve a path from a url
             Parameters
            ==========
            path: the path for the upload that is read in
            url: the url to send the POST to
            quiet: suppress verbose output (default is False)
        """
        file_size = os.path.getsize(path)
        resumable_upload_result = ResumableUploadResult.Incomplete()

        try:
            if resume:
                resumable_upload_result = self._resume_upload(
                    url, file_size, quiet)
                if resumable_upload_result.result != ResumableUploadResult.INCOMPLETE:
                    return resumable_upload_result.result

            start_at = resumable_upload_result.start_at
            upload_size = file_size - start_at

            with tqdm(total=upload_size,
                      unit='B',
                      unit_scale=True,
                      unit_divisor=1024,
                      disable=quiet) as progress_bar:
                with io.open(path, 'rb', buffering=0) as fp:
                    session = requests.Session()
                    if start_at > 0:
                        fp.seek(start_at)
                        session.headers.update({
                            'Content-Length':
                            '%d' % upload_size,
                            'Content-Range':
                            'bytes %d-%d/%d' %
                            (start_at, file_size - 1, file_size)
                        })
                    reader = TqdmBufferedReader(fp, progress_bar)
                    retries = Retry(total=10, backoff_factor=0.5)
                    adapter = HTTPAdapter(max_retries=retries)
                    session.mount('http://', adapter)
                    session.mount('https://', adapter)
                    response = session.put(url, data=reader)
                    if self._is_upload_successful(response):
                        return ResumableUploadResult.COMPLETE
                    if response.status_code == 503:
                        return ResumableUploadResult.INCOMPLETE
                    # Server returned a non-resumable error so give up.
                    return ResumableUploadResult.FAILED
        except Exception as error:
            print(error)
            # There is probably some weird bug in our code so try to resume the upload
            # in case it works on the next try.
            return ResumableUploadResult.INCOMPLETE

    def _resume_upload(self, url, content_length, quiet):
        # Documentation: https://developers.google.com/drive/api/guides/manage-uploads#resume-upload
        session = requests.Session()
        session.headers.update({
            'Content-Length': '0',
            'Content-Range': 'bytes */%d' % content_length,
        })

        response = session.put(url)

        if self._is_upload_successful(response):
            return ResumableUploadResult.Complete()
        if response.status_code == 404:
            # Upload expired so need to start from scratch.
            if not query:
                print('Upload of %s expired. Please try again.' % path)
            return ResumableUploadResult.Failed()
        if response.status_code == 308:  # Resume Incomplete
            bytes_uploaded = self._get_bytes_already_uploaded(response, quiet)
            if bytes_uploaded is None:
                # There is an error with the Range header so need to start from scratch.
                return ResumableUploadResult.Failed()
            result = ResumableUploadResult.Incomplete(bytes_uploaded)
            if not quiet:
                print('Already uploaded %d bytes. Will resume upload at %d.' %
                      (result.bytes_uploaded, result.start_at))
            return result
        else:
            if not quiet:
                print('Server returned %d. Please try again.' %
                      response.status_code)
            return ResumableUploadResult.Failed()

    def _is_upload_successful(self, response):
        return response.status_code == 200 or response.status_code == 201

    def _get_bytes_already_uploaded(self, response, quiet):
        range_val = response.headers.get('Range')
        if range_val is None:
            return 0  # This means server hasn't received anything before.
        items = range_val.split('-')  # Example: bytes=0-1000 => ['0', '1000']
        if len(items) != 2:
            if not quiet:
                print('Invalid Range header format: %s. Will try again.' %
                      range_val)
            return None  # Shouldn't happen, something's wrong with Range header format.
        bytes_uploaded_str = items[-1]  # Example: ['0', '1000'] => '1000'
        try:
            return int(bytes_uploaded_str)  # Example: '1000' => 1000
        except ValueError:
            if not quiet:
                print('Invalid Range header format: %s. Will try again.' %
                      range_val)
            return None  # Shouldn't happen, something's wrong with Range header format.

    def validate_dataset_string(self, dataset):
        """ determine if a dataset string is valid, meaning it is in the format
            of {username}/{dataset-slug} or {username}/{dataset-slug}/{version-number}.
             Parameters
            ==========
            dataset: the dataset name to validate
        """
        if dataset:
            if '/' not in dataset:
                raise ValueError('Dataset must be specified in the form of '
                                 '\'{username}/{dataset-slug}\'')

            split = dataset.split('/')
            if not split[0] or not split[1] or len(split) > 3:
                raise ValueError('Invalid dataset specification ' + dataset)

    def split_dataset_string(self, dataset):
        """ split a dataset string into owner_slug, dataset_slug,
            and optional version_number
             Parameters
            ==========
            dataset: the dataset name to split
        """
        if '/' in dataset:
            self.validate_dataset_string(dataset)
            urls = dataset.split('/')
            if len(urls) == 3:
                return urls[0], urls[1], urls[2]
            else:
                return urls[0], urls[1], None
        else:
            return self.get_config_value(self.CONFIG_NAME_USER), dataset, None

    def validate_model_string(self, model):
        """ determine if a model string is valid, meaning it is in the format
            of {owner}/{model-slug}.
             Parameters
            ==========
            model: the model name to validate
        """
        if model:
            if model.count('/') != 1:
                raise ValueError('Model must be specified in the form of '
                                 '\'{owner}/{model-slug}\'')

            split = model.split('/')
            if not split[0] or not split[1]:
                raise ValueError('Invalid model specification ' + model)

    def split_model_string(self, model):
        """ split a model string into owner_slug, model_slug
             Parameters
            ==========
            model: the model name to split
        """
        if '/' in model:
            self.validate_model_string(model)
            model_urls = model.split('/')
            return model_urls[0], model_urls[1]
        else:
            return self.get_config_value(self.CONFIG_NAME_USER), model

    def validate_model_instance_string(self, model_instance):
        """ determine if a model instance string is valid, meaning it is in the format
            of {owner}/{model-slug}/{framework}/{instance-slug}.
             Parameters
            ==========
            model_instance: the model instance name to validate
        """
        if model_instance:
            if model_instance.count('/') != 3:
                raise ValueError(
                    'Model instance must be specified in the form of '
                    '\'{owner}/{model-slug}/{framework}/{instance-slug}\'')

            split = model_instance.split('/')
            if not split[0] or not split[1] or not split[2] or not split[3]:
                raise ValueError('Invalid model instance specification ' +
                                 model_instance)

    def split_model_instance_string(self, model_instance):
        """ split a model instance string into owner_slug, model_slug, 
            framework, instance_slug
             Parameters
            ==========
            model_instance: the model instance name to validate
        """
        self.validate_model_instance_string(model_instance)
        urls = model_instance.split('/')
        return urls[0], urls[1], urls[2], urls[3]

    def validate_model_instance_version_string(self, model_instance_version):
        """ determine if a model instance version string is valid, meaning it is in the format
            of {owner}/{model-slug}/{framework}/{instance-slug}/{version-number}.
             Parameters
            ==========
            model_instance_version: the model instance version name to validate
        """
        if model_instance_version:
            if model_instance_version.count('/') != 4:
                raise ValueError(
                    'Model instance version must be specified in the form of '
                    '\'{owner}/{model-slug}/{framework}/{instance-slug}/{version-number}\''
                )

            split = model_instance_version.split('/')
            if not split[0] or not split[1] or not split[2] or not split[
                    3] or not split[4]:
                raise ValueError(
                    'Invalid model instance version specification ' +
                    model_instance_version)

            try:
                version_number = int(split[4])
            except:
                raise ValueError(
                    'Model instance version\'s version-number must be an integer'
                )

    def validate_kernel_string(self, kernel):
        """ determine if a kernel string is valid, meaning it is in the format
            of {username}/{kernel-slug}.
             Parameters
            ==========
            kernel: the kernel name to validate
        """
        if kernel:
            if '/' not in kernel:
                raise ValueError('Kernel must be specified in the form of '
                                 '\'{username}/{kernel-slug}\'')

            split = kernel.split('/')
            if not split[0] or not split[1]:
                raise ValueError('Kernel must be specified in the form of '
                                 '\'{username}/{kernel-slug}\'')

            if len(split[1]) < 5:
                raise ValueError(
                    'Kernel slug must be at least five characters')

    def validate_model_string(self, model):
        """ determine if a model string is valid, meaning it is in the format
            of {username}/{model-slug}/{framework}/{variation-slug}/{version-number}.
             Parameters
            ==========
            model: the model name to validate
        """
        if model:
            if '/' not in model:
                raise ValueError(
                    'Model must be specified in the form of '
                    '\'{username}/{model-slug}/{framework}/{variation-slug}/{version-number}\''
                )

            split = model.split('/')
            if not split[0] or not split[1]:
                raise ValueError('Invalid model specification ' + model)

    def validate_resources(self, folder, resources):
        """ validate resources is a wrapper to validate the existence of files
            and that there are no duplicates for a folder and set of resources.

            Parameters
            ==========
            folder: the folder to validate
            resources: one or more resources to validate within the folder
        """
        self.validate_files_exist(folder, resources)
        self.validate_no_duplicate_paths(resources)

    def validate_files_exist(self, folder, resources):
        """ ensure that one or more resource files exist in a folder

            Parameters
            ==========
            folder: the folder to validate
            resources: one or more resources to validate within the folder
        """
        for item in resources:
            file_name = item.get('path')
            full_path = os.path.join(folder, file_name)
            if not os.path.isfile(full_path):
                raise ValueError('%s does not exist' % full_path)

    def validate_no_duplicate_paths(self, resources):
        """ ensure that the user has not provided duplicate paths in
            a list of resources.

            Parameters
            ==========
            resources: one or more resources to validate not duplicated
        """
        paths = set()
        for item in resources:
            file_name = item.get('path')
            if file_name in paths:
                raise ValueError(
                    '%s path was specified more than once in the metadata' %
                    file_name)
            paths.add(file_name)

    def convert_to_dataset_file_metadata(self, file_data, path):
        """ convert a set of file_data to a metadata file at path

            Parameters
            ==========
            file_data: a dictionary of file data to write to file
            path: the path to write the metadata to
        """
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

    def validate_date(self, date):
        datetime.strptime(date, "%Y-%m-%d")

    def sanitize_markdown(self, markdown):
        return bleach.clean(markdown)

    def confirmation(self):
        question = "Are you sure?"
        prompt = "[yes/no]"
        options = {"yes": True, "no": False}
        while True:
            sys.stdout.write('{} {} '.format(question, prompt))
            choice = input().lower()
            if choice in options:
                return options[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no'.\n")
                return False


class TqdmBufferedReader(io.BufferedReader):

    def __init__(self, raw, progress_bar):
        """ helper class to implement an io.BufferedReader
             Parameters
            ==========
            raw: bytes data to pass to the buffered reader
            progress_bar: a progress bar to initialize the reader
        """
        io.BufferedReader.__init__(self, raw)
        self.progress_bar = progress_bar

    def read(self, *args, **kwargs):
        """ read the buffer, passing named and non named arguments to the
            io.BufferedReader function.
        """
        buf = io.BufferedReader.read(self, *args, **kwargs)
        self.increment(len(buf))
        return buf

    def increment(self, length):
        """ increment the reader by some length

            Parameters
            ==========
            length: bytes to increment the reader by
        """
        self.progress_bar.update(length)


class FileList(object):

    def __init__(self, init_dict):
        self.error_message = ''
        files = init_dict['files']
        if files:
            for f in files:
                if 'size' in f:
                    f['totalBytes'] = f['size']
            self.files = [File(f) for f in files]
        else:
            self.files = []
        token = init_dict['nextPageToken']
        if token:
            self.nextPageToken = token
        else:
            self.nextPageToken = ""

    def __repr__(self):
        return ''
