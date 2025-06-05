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


class ModelNewRequest(object):
    """
    Attributes:
      project_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    project_types = {
        "owner_slug": "str",
        "slug": "str",
        "title": "str",
        "subtitle": "str",
        "is_private": "bool",
        "description": "str",
        "publish_time": "date",
        "provenance_sources": "str",
    }

    attribute_map = {
        "owner_slug": "ownerSlug",
        "slug": "slug",
        "title": "title",
        "subtitle": "subtitle",
        "is_private": "isPrivate",
        "description": "description",
        "publish_time": "publishTime",
        "provenance_sources": "provenanceSources",
    }

    def __init__(
        self,
        owner_slug=None,
        slug=None,
        title=None,
        subtitle=None,
        is_private=True,
        description="",
        publish_time=None,
        provenance_sources="",
    ):  # noqa: E501

        self._owner_slug = None
        self._slug = None
        self._title = None
        self._subtitle = None
        self._is_private = None
        self._description = None
        self._publish_time = None
        self._provenance_sources = None
        self.discriminator = None

        self.owner_slug = owner_slug
        self.slug = slug
        self.title = title
        if subtitle is not None:
            self.subtitle = subtitle
        self.is_private = is_private
        if description is not None:
            self.description = description
        if publish_time is not None:
            self.publish_time = publish_time
        if provenance_sources is not None:
            self.provenance_sources = provenance_sources

    @property
    def owner_slug(self):
        """Gets the owner_slug of this ModelNewRequest.  # noqa: E501.

        The owner's slug  # noqa: E501

        :return: The owner_slug of this ModelNewRequest.  # noqa: E501
        :rtype: str
        """
        return self._owner_slug

    @owner_slug.setter
    def owner_slug(self, owner_slug):
        """Sets the owner_slug of this ModelNewRequest.

        The owner's slug  # noqa: E501

        :param owner_slug: The owner_slug of this ModelNewRequest. #
            noqa: E501
        :type: str
        """
        if owner_slug is None:
            raise ValueError("Invalid value for `owner_slug`, must not be `None`")  # noqa: E501

        self._owner_slug = owner_slug

    @property
    def slug(self):
        """Gets the slug of this ModelNewRequest.  # noqa: E501.

        The slug that the model should be created with  # noqa: E501

        :return: The slug of this ModelNewRequest.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this ModelNewRequest.

        The slug that the model should be created with  # noqa: E501

        :param slug: The slug of this ModelNewRequest.  # noqa: E501
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501

        self._slug = slug

    @property
    def title(self):
        """Gets the title of this ModelNewRequest.  # noqa: E501.

        The title of the new model  # noqa: E501

        :return: The title of this ModelNewRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ModelNewRequest.

        The title of the new model  # noqa: E501

        :param title: The title of this ModelNewRequest.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def subtitle(self):
        """Gets the subtitle of this ModelNewRequest.  # noqa: E501.

        The subtitle of the new model  # noqa: E501

        :return: The subtitle of this ModelNewRequest.  # noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this ModelNewRequest.

        The subtitle of the new model  # noqa: E501

        :param subtitle: The subtitle of this ModelNewRequest. # noqa:
            E501
        :type: str
        """

        self._subtitle = subtitle

    @property
    def is_private(self):
        """Gets the is_private of this ModelNewRequest.  # noqa: E501.

        Whether or not the model should be private  # noqa: E501

        :return: The is_private of this ModelNewRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this ModelNewRequest.

        Whether or not the model should be private  # noqa: E501

        :param is_private: The is_private of this ModelNewRequest. #
            noqa: E501
        :type: bool
        """
        if is_private is None:
            raise ValueError("Invalid value for `is_private`, must not be `None`")  # noqa: E501

        self._is_private = is_private

    @property
    def description(self):
        """Gets the description of this ModelNewRequest.  # noqa: E501.

        The description to be set on the model  # noqa: E501

        :return: The description of this ModelNewRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelNewRequest.

        The description to be set on the model  # noqa: E501

        :param description: The description of this ModelNewRequest. #
            noqa: E501
        :type: str
        """

        self._description = description

    @property
    def publish_time(self):
        """Gets the publish_time of this ModelNewRequest.  # noqa: E501.

        When the model was initially published  # noqa: E501

        :return: The publish_time of this ModelNewRequest.  # noqa: E501
        :rtype: date
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this ModelNewRequest.

        When the model was initially published  # noqa: E501

        :param publish_time: The publish_time of this ModelNewRequest. #
            noqa: E501
        :type: date
        """

        self._publish_time = publish_time

    @property
    def provenance_sources(self):
        """Gets the provenance_sources of this ModelNewRequest.  # noqa: E501.

        The provenance sources to be set on the model  # noqa: E501

        :return: The provenance_sources of this ModelNewRequest. #
            noqa: E501
        :rtype: str
        """
        return self._provenance_sources

    @provenance_sources.setter
    def provenance_sources(self, provenance_sources):
        """Sets the provenance_sources of this ModelNewRequest.

        The provenance sources to be set on the model  # noqa: E501

        :param provenance_sources: The provenance_sources of this
            ModelNewRequest. # noqa: E501
        :type: str
        """

        self._provenance_sources = provenance_sources

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
        if not isinstance(other, ModelNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal."""
        return not self == other
