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


class DatasetUpdateSettingsRequest(object):
    """
    Attributes:
      project_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    project_types = {
        "title": "str",
        "subtitle": "str",
        "description": "str",
        "is_private": "bool",
        "licenses": "list[object]",
        "keywords": "list[str]",
        "collaborators": "list[object]",
        "data": "list[object]",
    }

    attribute_map = {
        "title": "title",
        "subtitle": "subtitle",
        "description": "description",
        "is_private": "isPrivate",
        "licenses": "licenses",
        "keywords": "keywords",
        "collaborators": "collaborators",
        "data": "data",
    }

    def __init__(
        self,
        title=None,
        subtitle=None,
        description=None,
        is_private=None,
        licenses=None,
        keywords=None,
        collaborators=None,
        data=None,
    ):  # noqa: E501

        self._title = None
        self._subtitle = None
        self._description = None
        self._is_private = None
        self._licenses = None
        self._keywords = None
        self._collaborators = None
        self._data = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if subtitle is not None:
            self.subtitle = subtitle
        if description is not None:
            self.description = description
        if is_private is not None:
            self.is_private = is_private
        if licenses is not None:
            self.licenses = licenses
        if keywords is not None:
            self.keywords = keywords
        if collaborators is not None:
            self.collaborators = collaborators
        if data is not None:
            self.data = data

    @property
    def title(self):
        """Gets the title of this DatasetUpdateSettingsRequest.  # noqa: E501.

        Title of the dataset  # noqa: E501

        :return: The title of this DatasetUpdateSettingsRequest. #
            noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DatasetUpdateSettingsRequest.

        Title of the dataset  # noqa: E501

        :param title: The title of this DatasetUpdateSettingsRequest. #
            noqa: E501
        :type: str
        """

        self._title = title

    @property
    def subtitle(self):
        """Gets the subtitle of this DatasetUpdateSettingsRequest.  # noqa:
        E501.

        Subtitle of the dataset  # noqa: E501

        :return: The subtitle of this DatasetUpdateSettingsRequest. #
            noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this DatasetUpdateSettingsRequest.

        Subtitle of the dataset  # noqa: E501

        :param subtitle: The subtitle of this
            DatasetUpdateSettingsRequest. # noqa: E501
        :type: str
        """

        self._subtitle = subtitle

    @property
    def description(self):
        """Gets the description of this DatasetUpdateSettingsRequest.  # noqa:
        E501.

        Decription of the dataset  # noqa: E501

        :return: The description of this DatasetUpdateSettingsRequest. #
            noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatasetUpdateSettingsRequest.

        Decription of the dataset  # noqa: E501

        :param description: The description of this
            DatasetUpdateSettingsRequest. # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_private(self):
        """Gets the is_private of this DatasetUpdateSettingsRequest.  # noqa:
        E501.

        Whether or not the dataset should be private  # noqa: E501

        :return: The is_private of this DatasetUpdateSettingsRequest. #
            noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this DatasetUpdateSettingsRequest.

        Whether or not the dataset should be private  # noqa: E501

        :param is_private: The is_private of this
            DatasetUpdateSettingsRequest. # noqa: E501
        :type: bool
        """

        self._is_private = is_private

    @property
    def licenses(self):
        """Gets the licenses of this DatasetUpdateSettingsRequest.  # noqa:
        E501.

        A list of licenses that apply to this dataset  # noqa: E501

        :return: The licenses of this DatasetUpdateSettingsRequest. #
            noqa: E501
        :rtype: list[object]
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        """Sets the licenses of this DatasetUpdateSettingsRequest.

        A list of licenses that apply to this dataset  # noqa: E501

        :param licenses: The licenses of this
            DatasetUpdateSettingsRequest. # noqa: E501
        :type: list[object]
        """

        self._licenses = licenses

    @property
    def keywords(self):
        """Gets the keywords of this DatasetUpdateSettingsRequest.  # noqa:
        E501.

        A list of keywords that apply to this dataset  # noqa: E501

        :return: The keywords of this DatasetUpdateSettingsRequest. #
            noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this DatasetUpdateSettingsRequest.

        A list of keywords that apply to this dataset  # noqa: E501

        :param keywords: The keywords of this
            DatasetUpdateSettingsRequest. # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def collaborators(self):
        """Gets the collaborators of this DatasetUpdateSettingsRequest.  #
        noqa: E501.

        A list of collaborators that may read or edit this dataset  #
        noqa: E501

        :return: The collaborators of this DatasetUpdateSettingsRequest.
            # noqa: E501
        :rtype: list[object]
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """Sets the collaborators of this DatasetUpdateSettingsRequest.

        A list of collaborators that may read or edit this dataset  #
        noqa: E501

        :param collaborators: The collaborators of this
            DatasetUpdateSettingsRequest. # noqa: E501
        :type: list[object]
        """

        self._collaborators = collaborators

    @property
    def data(self):
        """Gets the data of this DatasetUpdateSettingsRequest.  # noqa: E501.

        A list containing metadata for each file in the dataset  # noqa:
        E501

        :return: The data of this DatasetUpdateSettingsRequest. # noqa:
            E501
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DatasetUpdateSettingsRequest.

        A list containing metadata for each file in the dataset  # noqa:
        E501

        :param data: The data of this DatasetUpdateSettingsRequest. #
            noqa: E501
        :type: list[object]
        """

        self._data = data

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
        if not isinstance(other, DatasetUpdateSettingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal."""
        return not self == other
