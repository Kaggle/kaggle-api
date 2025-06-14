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


class StartBlobUploadResponse(object):
    """
    Attributes:
      project_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    project_types = {"token": "str", "create_url": "str"}

    attribute_map = {"token": "token", "create_url": "createUrl"}

    def __init__(self, token=None, create_url=None):  # noqa: E501
        """StartBlobUploadResponse - a model defined in Swagger"""  # noqa: E501

        self._token = None
        self._create_url = None
        self.discriminator = None

        self.token = token
        self.create_url = create_url

    @property
    def token(self):
        """Gets the token of this StartBlobUploadResponse.  # noqa: E501.

        Opaque string token used to reference the new blob/file.  # noqa:
        E501

        :return: The token of this StartBlobUploadResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this StartBlobUploadResponse.

        Opaque string token used to reference the new blob/file.  # noqa:
        E501

        :param token: The token of this StartBlobUploadResponse. # noqa:
            E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def create_url(self):
        """Gets the create_url of this StartBlobUploadResponse.  # noqa: E501.

        URL to use to start the upload.  # noqa: E501

        :return: The create_url of this StartBlobUploadResponse. # noqa:
            E501
        :rtype: str
        """
        return self._create_url

    @create_url.setter
    def create_url(self, create_url):
        """Sets the create_url of this StartBlobUploadResponse.

        URL to use to start the upload.  # noqa: E501

        :param create_url: The create_url of this StartBlobUploadResponse. #
            noqa: E501
        :type: str
        """
        if create_url is None:
            raise ValueError("Invalid value for `create_url`, must not be `None`")  # noqa: E501

        self._create_url = create_url

    def to_dict(self):
        """Returns the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.project_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, StartBlobUploadResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal."""
        return not self == other
