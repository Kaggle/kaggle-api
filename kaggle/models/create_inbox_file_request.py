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

"""
    Kaggle API

    API for kaggle.com  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateInboxFileRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'virtual_directory': 'str',
        'blob_file_token': 'str'
    }

    attribute_map = {
        'virtual_directory': 'virtualDirectory',
        'blob_file_token': 'blobFileToken'
    }

    def __init__(self, virtual_directory=None, blob_file_token=None):  # noqa: E501
        """CreateInboxFileRequest - a model defined in Swagger"""  # noqa: E501

        self._virtual_directory = None
        self._blob_file_token = None
        self.discriminator = None

        self.virtual_directory = virtual_directory
        self.blob_file_token = blob_file_token

    @property
    def virtual_directory(self):
        """Gets the virtual_directory of this CreateInboxFileRequest.  # noqa: E501

        Directory name used for tagging the uploaded file  # noqa: E501

        :return: The virtual_directory of this CreateInboxFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._virtual_directory

    @virtual_directory.setter
    def virtual_directory(self, virtual_directory):
        """Sets the virtual_directory of this CreateInboxFileRequest.

        Directory name used for tagging the uploaded file  # noqa: E501

        :param virtual_directory: The virtual_directory of this CreateInboxFileRequest.  # noqa: E501
        :type: str
        """
        if virtual_directory is None:
            raise ValueError("Invalid value for `virtual_directory`, must not be `None`")  # noqa: E501

        self._virtual_directory = virtual_directory

    @property
    def blob_file_token(self):
        """Gets the blob_file_token of this CreateInboxFileRequest.  # noqa: E501

        Token representing the uploaded file  # noqa: E501

        :return: The blob_file_token of this CreateInboxFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._blob_file_token

    @blob_file_token.setter
    def blob_file_token(self, blob_file_token):
        """Sets the blob_file_token of this CreateInboxFileRequest.

        Token representing the uploaded file  # noqa: E501

        :param blob_file_token: The blob_file_token of this CreateInboxFileRequest.  # noqa: E501
        :type: str
        """
        if blob_file_token is None:
            raise ValueError("Invalid value for `blob_file_token`, must not be `None`")  # noqa: E501

        self._blob_file_token = blob_file_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateInboxFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
