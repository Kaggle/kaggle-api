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

from setuptools import setup, find_packages

setup(
    name = 'kaggle',
    version = '1.3.8',
    description = 'Kaggle API',
    long_description = 'Official API for https://www.kaggle.com, accessible using a command line tool implemented in Python. Beta release - Kaggle reserves the right to modify the API functionality currently offered.',
    author = 'Kaggle',
    author_email = 'support@kaggle.com',
    url = 'https://github.com/Kaggle/kaggle-api',
    keywords = ['Kaggle', 'API'],
    entry_points = {
        'console_scripts': [
          'kaggle = kaggle.cli:main'
        ]
    },
    install_requires = ['urllib3 >= 1.15', 'six >= 1.10', 'certifi', 'python-dateutil', 'requests'],
    packages = find_packages(),
    license = 'Apache 2.0'
)
