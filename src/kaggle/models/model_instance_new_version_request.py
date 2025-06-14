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

from kaggle.models.upload_file import UploadFile  # noqa: F401,E501


class ModelInstanceNewVersionRequest(object):
    """
    Attributes:
      project_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    project_types = {"version_notes": "str", "files": "list[UploadFile]"}

    attribute_map = {"version_notes": "versionNotes", "files": "files"}

    def __init__(self, version_notes=None, files=None):  # noqa: E501

        self._version_notes = None
        self._files = None
        self.discriminator = None

        if version_notes is not None:
            self.version_notes = version_notes
        self.files = files

    @property
    def version_notes(self):
        """Gets the version_notes of this ModelInstanceNewVersionRequest.  #
        noqa: E501.

        The version notes for the model instance version  # noqa: E501

        :return: The version_notes of this
            ModelInstanceNewVersionRequest. # noqa: E501
        :rtype: str
        """
        return self._version_notes

    @version_notes.setter
    def version_notes(self, version_notes):
        """Sets the version_notes of this ModelInstanceNewVersionRequest.

        The version notes for the model instance version  # noqa: E501

        :param version_notes: The version_notes of this
            ModelInstanceNewVersionRequest. # noqa: E501
        :type: str
        """

        self._version_notes = version_notes

    @property
    def files(self):
        """Gets the files of this ModelInstanceNewVersionRequest.  # noqa:
        E501.

        A list of files that should be associated with the model
        instance version  # noqa: E501

        :return: The files of this ModelInstanceNewVersionRequest. #
            noqa: E501
        :rtype: list[UploadFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ModelInstanceNewVersionRequest.

        A list of files that should be associated with the model
        instance version  # noqa: E501

        :param files: The files of this ModelInstanceNewVersionRequest.
            # noqa: E501
        :type: list[UploadFile]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

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
        if not isinstance(other, ModelInstanceNewVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal."""
        return not self == other
