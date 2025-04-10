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

import pprint
import re  # noqa: F401

import six


class StartBlobUploadRequest(object):
  """
    Attributes:
      project_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
  project_types = {
      'type': 'object',
      'name': 'str',
      'content_length': 'int',
      'content_type': 'str',
      'last_modified_epoch_seconds': 'int'
  }

  attribute_map = {
      'type': 'type',
      'name': 'name',
      'content_length': 'contentLength',
      'content_type': 'contentType',
      'last_modified_epoch_seconds': 'lastModifiedEpochSeconds'
  }

  def __init__(self,
               type=None,
               name=None,
               content_length=None,
               content_type=None,
               last_modified_epoch_seconds=None):  # noqa: E501
    """StartBlobUploadRequest - a model defined in Swagger"""  # noqa: E501

    self._type = None
    self._name = None
    self._content_length = None
    self._content_type = None
    self._last_modified_epoch_seconds = None
    self.discriminator = None

    if type is not None:
      self.type = type
    self.name = name
    self.content_length = content_length
    if content_type is not None:
      self.content_type = content_type
    if last_modified_epoch_seconds is not None:
      self.last_modified_epoch_seconds = last_modified_epoch_seconds

  @property
  def type(self):
    """Gets the type of this StartBlobUploadRequest.  # noqa: E501.

    The type of the blob (one of \"dataset\", \"model\", \"inbox\")  #
    noqa: E501

    :return: The type of this StartBlobUploadRequest.  # noqa: E501
    :rtype: object
    """
    return self._type

  @type.setter
  def type(self, type):
    """Sets the type of this StartBlobUploadRequest.

    The type of the blob (one of \"dataset\", \"model\", \"inbox\")  #
    noqa: E501

    :param type: The type of this StartBlobUploadRequest.  # noqa: E501
    :type: object
    """

    self._type = type

  @property
  def name(self):
    """Gets the name of this StartBlobUploadRequest.  # noqa: E501.

    Name of the file  # noqa: E501

    :return: The name of this StartBlobUploadRequest.  # noqa: E501
    :rtype: str
    """
    return self._name

  @name.setter
  def name(self, name):
    """Sets the name of this StartBlobUploadRequest.

    Name of the file  # noqa: E501

    :param name: The name of this StartBlobUploadRequest.  # noqa: E501
    :type: str
    """
    if name is None:
      raise ValueError(
          "Invalid value for `name`, must not be `None`")  # noqa: E501

    self._name = name

  @property
  def content_length(self):
    """Gets the content_length of this StartBlobUploadRequest.  # noqa: E501.

    Content length of the file in bytes  # noqa: E501

    :return: The content_length of this StartBlobUploadRequest. # noqa:
        E501
    :rtype: int
    """
    return self._content_length

  @content_length.setter
  def content_length(self, content_length):
    """Sets the content_length of this StartBlobUploadRequest.

    Content length of the file in bytes  # noqa: E501

    :param content_length: The content_length of this
        StartBlobUploadRequest. # noqa: E501
    :type: int
    """
    if content_length is None:
      raise ValueError("Invalid value for `content_length`, must not be `None`"
                      )  # noqa: E501

    self._content_length = content_length

  @property
  def content_type(self):
    """Gets the content_type of this StartBlobUploadRequest.  # noqa: E501.

    Content/MIME type (e.g. \"text/plain\") of the file  # noqa: E501

    :return: The content_type of this StartBlobUploadRequest. # noqa:
        E501
    :rtype: str
    """
    return self._content_type

  @content_type.setter
  def content_type(self, content_type):
    """Sets the content_type of this StartBlobUploadRequest.

    Content/MIME type (e.g. \"text/plain\") of the file  # noqa: E501

    :param content_type: The content_type of this
        StartBlobUploadRequest. # noqa: E501
    :type: str
    """

    self._content_type = content_type

  @property
  def last_modified_epoch_seconds(self):
    """Gets the last_modified_epoch_seconds of this StartBlobUploadRequest.  #
    noqa: E501.

    Last modified date of file in seconds since epoch in UTC  # noqa:
    E501

    :return: The last_modified_epoch_seconds of this
        StartBlobUploadRequest. # noqa: E501
    :rtype: int
    """
    return self._last_modified_epoch_seconds

  @last_modified_epoch_seconds.setter
  def last_modified_epoch_seconds(self, last_modified_epoch_seconds):
    """Sets the last_modified_epoch_seconds of this StartBlobUploadRequest.

    Last modified date of file in seconds since epoch in UTC  # noqa:
    E501

    :param last_modified_epoch_seconds: The last_modified_epoch_seconds
        of this StartBlobUploadRequest. # noqa: E501
    :type: int
    """

    self._last_modified_epoch_seconds = last_modified_epoch_seconds

  def to_dict(self):
    """Returns the model properties as a dict."""
    result = {}

    for attr, _ in six.iteritems(self.project_types):
      value = getattr(self, attr)
      if isinstance(value, list):
        result[attr] = list(
            map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
      elif hasattr(value, "to_dict"):
        result[attr] = value.to_dict()
      elif isinstance(value, dict):
        result[attr] = dict(
            map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item, value.items()))
      else:
        result[attr] = value

    return result

  def to_str(self):
    """Returns the string representation of the model."""
    return pprint.pformat(self.to_dict())

  def __repr__(self):
    """For `print` and `pprint`"""
    return self.to_str()

  def __eq__(self, other):
    """Returns true if both objects are equal."""
    if not isinstance(other, StartBlobUploadRequest):
      return False

    return self.__dict__ == other.__dict__

  def __ne__(self, other):
    """Returns true if both objects are not equal."""
    return not self == other
