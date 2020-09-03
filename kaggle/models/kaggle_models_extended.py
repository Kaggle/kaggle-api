#!/usr/bin/python
#
# Copyright 2020 Kaggle Inc
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
import os
from datetime import datetime


class Competition(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)
        self.tags = [Tag(t) for t in self.tags]

    def __repr__(self):
        return self.ref


class SubmitResult(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)

    def __repr__(self):
        return self.message


class Submission(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)
        if self.totalBytes is None:
            self.size = None
        else:
            self.size = File.get_size(self.totalBytes)

    def __repr__(self):
        return str(self.ref)


class LeaderboardEntry(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)

    def __repr__(self):
        return self.teamId


class Dataset(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)
        self.tags = [Tag(t) for t in self.tags]
        self.files = [File(f) for f in self.files]
        self.versions = [DatasetVersion(v) for v in self.versions]
        self.size = File.get_size(self.totalBytes)

    def __repr__(self):
        return self.ref


class Metadata(object):
    def __init__(self, init_info):
        parsed_info = {k: parse(v) for k, v in init_info.items()}
        # backwards compatibility
        self.id = parsed_info["ownerUser"] + "/" + parsed_info['datasetSlug']
        self.id_no = parsed_info['datasetId']
        self.__dict__.update(parsed_info)

    def __repr__(self):
        return str(self.datasetId)


class DatasetVersion(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)

    def __repr__(self):
        return str(self.versionNumber)


class File(object):
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


class Tag(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)

    def __repr__(self):
        return self.ref


class FileUploadInfo(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)

    def __repr__(self):
        return self.token


class DatasetNewVersionResponse(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)

    def __repr__(self):
        return self.url


class DatasetNewResponse(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)

    def __repr__(self):
        return self.url


class ListFilesResult(object):
    def __init__(self, init_dict):
        self.error_message = init_dict['errorMessage']
        files = init_dict['datasetFiles']
        if files:
            self.files = [File(f) for f in files]
        else:
            self.files = {}

    def __repr__(self):
        return self.error_message


class Kernel:
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)

    def __repr__(self):
        return self.title


class KernelPushResponse(object):
    def __init__(self, init_dict):
        parsed_dict = {k: parse(v) for k, v in init_dict.items()}
        self.__dict__.update(parsed_dict)

    def __repr__(self):
        return self.newUrl


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
