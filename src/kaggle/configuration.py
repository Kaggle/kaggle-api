#!/usr/bin/python
#
# Copyright 2024 Kaggle Inc
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

# coding: utf-8
from __future__ import absolute_import

import logging
import six
import sys
import urllib3


class Configuration:

  def __init__(self):
    """Constructor."""
    # Default Base url
    self.host = _get_endpoint_from_env() or "https://www.kaggle.com/api/v1"

    # Authentication Settings
    # dict to store API key(s)
    self.api_key = {}
    # dict to store API prefix (e.g. Bearer)
    self.api_key_prefix = {}
    # Username for HTTP basic authentication
    self.username = ""
    # Password for HTTP basic authentication
    self.password = ""

    # Logging Settings
    self.logger = {
        "package_logger": logging.getLogger("kaggle"),
        "urllib3_logger": logging.getLogger("urllib3")
    }
    # Log format
    self.logger_format = '%(asctime)s %(levelname)s %(message)s'
    # Log stream handler
    self.logger_stream_handler = None
    # Log file handler
    self.logger_file_handler = None
    # Debug file location
    self.logger_file = None
    # Debug switch
    self.debug = False

  @property
  def logger_file(self):
    """The logger file.

    If the logger_file is None, then add stream handler and remove file
    handler. Otherwise, add file handler and remove stream handler.

    :param value: The logger_file path.
    :type: str
    """
    return self.__logger_file

  @logger_file.setter
  def logger_file(self, value):
    """The logger file.

    If the logger_file is None, then add stream handler and remove file
    handler. Otherwise, add file handler and remove stream handler.

    :param value: The logger_file path.
    :type: str
    """
    self.__logger_file = value
    if self.__logger_file:
      # If set logging file,
      # then add file handler and remove stream handler.
      self.logger_file_handler = logging.FileHandler(self.__logger_file)
      self.logger_file_handler.setFormatter(self.logger_formatter)
      for _, logger in six.iteritems(self.logger):
        logger.addHandler(self.logger_file_handler)
        if self.logger_stream_handler:
          logger.removeHandler(self.logger_stream_handler)
    else:
      # If not set logging file,
      # then add stream handler and remove file handler.
      self.logger_stream_handler = logging.StreamHandler()
      self.logger_stream_handler.setFormatter(self.logger_formatter)
      for _, logger in six.iteritems(self.logger):
        logger.addHandler(self.logger_stream_handler)
        if self.logger_file_handler:
          logger.removeHandler(self.logger_file_handler)

  @property
  def debug(self):
    """Debug status.

    :param value: The debug status, True or False.
    :type: bool
    """
    return self.__debug

  @debug.setter
  def debug(self, value):
    """Debug status.

    :param value: The debug status, True or False.
    :type: bool
    """
    self.__debug = value
    if self.__debug:
      # if debug status is True, turn on debug logging
      for _, logger in six.iteritems(self.logger):
        logger.setLevel(logging.DEBUG)
    else:
      # if debug status is False, turn off debug logging,
      # setting log level to default `logging.WARNING`
      for _, logger in six.iteritems(self.logger):
        logger.setLevel(logging.WARNING)

  @property
  def logger_format(self):
    """The logger format.

    The logger_formatter will be updated when sets logger_format.

    :param value: The format string.
    :type: str
    """
    return self.__logger_format

  @logger_format.setter
  def logger_format(self, value):
    """The logger format.

    The logger_formatter will be updated when sets logger_format.

    :param value: The format string.
    :type: str
    """
    self.__logger_format = value
    self.logger_formatter = logging.Formatter(self.__logger_format)

  def get_api_key_with_prefix(self, identifier):
    """Gets API key (with prefix if set).

    :param identifier: The identifier of apiKey.
    :return: The token for api key authentication.
    """
    if (self.api_key.get(identifier) and self.api_key_prefix.get(identifier)):
      return self.api_key_prefix[identifier] + ' ' + self.api_key[
          identifier]  # noqa: E501
    elif self.api_key.get(identifier):
      return self.api_key[identifier]

  def get_basic_auth_token(self):
    """Gets HTTP basic authentication header (string).

    :return: The token for basic HTTP authentication.
    """
    return urllib3.util.make_headers(basic_auth=self.username + ':' +
                                     self.password).get('authorization')

  def auth_settings(self):
    """Gets Auth Settings dict for api client.

    :return: The Auth Settings information dict.
    """
    return {
        'basicAuth': {
            'type': 'basic',
            'in': 'header',
            'key': 'Authorization',
            'value': self.get_basic_auth_token()
        },
    }

  def to_debug_report(self):
    """Gets the essential information for debugging.

    :return: The report for debugging.
    """
    return "Python SDK Debug Report:\n" \
           "OS: {env}\n" \
           "Python Version: {pyversion}\n" \
           "Version of the API: 1\n" \
           "SDK Package Version: 1". \
      format(env=sys.platform, pyversion=sys.version)


def _get_endpoint_from_env():
  import os
  endpoint = os.environ.get("KAGGLE_API_ENDPOINT")
  if endpoint is None:
    return None
  endpoint = endpoint.rstrip("/")
  if endpoint.endswith("/api/v1"):
    return endpoint
  return endpoint + "/api/v1"
