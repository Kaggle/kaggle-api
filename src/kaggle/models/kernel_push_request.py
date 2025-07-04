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


class KernelPushRequest(object):
    """
    Attributes:
      project_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    project_types = {
        "id": "int",
        "slug": "str",
        "new_title": "str",
        "text": "str",
        "language": "str",
        "kernel_type": "str",
        "is_private": "bool",
        "enable_gpu": "bool",
        "enable_tpu": "bool",
        "enable_internet": "bool",
        "dataset_data_sources": "list[str]",
        "competition_data_sources": "list[str]",
        "kernel_data_sources": "list[str]",
        "model_data_sources": "list[str]",
        "category_ids": "list[str]",
        "docker_image_pinning_type": "str",
    }

    attribute_map = {
        "id": "id",
        "slug": "slug",
        "new_title": "newTitle",
        "text": "text",
        "language": "language",
        "kernel_type": "kernelType",
        "is_private": "isPrivate",
        "enable_gpu": "enableGpu",
        "enable_tpu": "enableTpu",
        "enable_internet": "enableInternet",
        "dataset_data_sources": "datasetDataSources",
        "competition_data_sources": "competitionDataSources",
        "kernel_data_sources": "kernelDataSources",
        "model_data_sources": "modelDataSources",
        "category_ids": "categoryIds",
        "docker_image_pinning_type": "dockerImagePinningType",
    }

    def __init__(
        self,
        id=None,
        slug=None,
        new_title=None,
        text=None,
        language=None,
        kernel_type=None,
        is_private=None,
        enable_gpu=None,
        enable_tpu=None,
        enable_internet=None,
        dataset_data_sources=None,
        competition_data_sources=None,
        kernel_data_sources=None,
        model_data_sources=None,
        category_ids=None,
        docker_image_pinning_type=None,
    ):  # noqa: E501

        self._id = None
        self._slug = None
        self._new_title = None
        self._text = None
        self._language = None
        self._kernel_type = None
        self._is_private = None
        self._enable_gpu = None
        self._enable_tpu = None
        self._enable_internet = None
        self._dataset_data_sources = None
        self._competition_data_sources = None
        self._kernel_data_sources = None
        self._model_data_sources = None
        self._category_ids = None
        self._docker_image_pinning_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if slug is not None:
            self.slug = slug
        if new_title is not None:
            self.new_title = new_title
        self.text = text
        self.language = language
        self.kernel_type = kernel_type
        if is_private is not None:
            self.is_private = is_private
        if enable_gpu is not None:
            self.enable_gpu = enable_gpu
        if enable_tpu is not None:
            self.enable_tpu = enable_tpu
        if enable_internet is not None:
            self.enable_internet = enable_internet
        if dataset_data_sources is not None:
            self.dataset_data_sources = dataset_data_sources
        if competition_data_sources is not None:
            self.competition_data_sources = competition_data_sources
        if kernel_data_sources is not None:
            self.kernel_data_sources = kernel_data_sources
        if model_data_sources is not None:
            self.model_data_sources = model_data_sources
        if category_ids is not None:
            self.category_ids = category_ids
        if docker_image_pinning_type is not None:
            self.docker_image_pinning_type = docker_image_pinning_type

    @property
    def id(self):
        """Gets the id of this KernelPushRequest.  # noqa: E501.

        The kernel's ID number. One of `id` and `slug` are required. If both are specified, `id` will be preferred  # noqa: E501

        :return: The id of this KernelPushRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KernelPushRequest.

        The kernel's ID number. One of `id` and `slug` are required. If both are specified, `id` will be preferred  # noqa: E501

        :param id: The id of this KernelPushRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def slug(self):
        """Gets the slug of this KernelPushRequest.  # noqa: E501.

        The full slug of the kernel to push to, in the format `USERNAME/KERNEL-SLUG`. The kernel slug must be the title lowercased with dashes (`-`) replacing spaces. One of `id` and `slug` are required. If both are specified, `id` will be preferred  # noqa: E501

        :return: The slug of this KernelPushRequest.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this KernelPushRequest.

        The full slug of the kernel to push to, in the format `USERNAME/KERNEL-SLUG`. The kernel slug must be the title lowercased with dashes (`-`) replacing spaces. One of `id` and `slug` are required. If both are specified, `id` will be preferred  # noqa: E501

        :param slug: The slug of this KernelPushRequest.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def new_title(self):
        """Gets the new_title of this KernelPushRequest.  # noqa: E501.

        The title to be set on the kernel  # noqa: E501

        :return: The new_title of this KernelPushRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_title

    @new_title.setter
    def new_title(self, new_title):
        """Sets the new_title of this KernelPushRequest.

        The title to be set on the kernel  # noqa: E501

        :param new_title: The new_title of this KernelPushRequest. #
            noqa: E501
        :type: str
        """

        self._new_title = new_title

    @property
    def text(self):
        """Gets the text of this KernelPushRequest.  # noqa: E501.

        The kernel's source code  # noqa: E501

        :return: The text of this KernelPushRequest.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this KernelPushRequest.

        The kernel's source code  # noqa: E501

        :param text: The text of this KernelPushRequest.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def language(self):
        """Gets the language of this KernelPushRequest.  # noqa: E501.

        The language that the kernel is written in  # noqa: E501

        :return: The language of this KernelPushRequest.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this KernelPushRequest.

        The language that the kernel is written in  # noqa: E501

        :param language: The language of this KernelPushRequest. #
            noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501
        allowed_values = ["python", "r", "rmarkdown"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}".format(language, allowed_values)  # noqa: E501
            )

        self._language = language

    @property
    def kernel_type(self):
        """Gets the kernel_type of this KernelPushRequest.  # noqa: E501.

        The type of kernel. Cannot be changed once the kernel has been
        created  # noqa: E501

        :return: The kernel_type of this KernelPushRequest. # noqa: E501
        :rtype: str
        """
        return self._kernel_type

    @kernel_type.setter
    def kernel_type(self, kernel_type):
        """Sets the kernel_type of this KernelPushRequest.

        The type of kernel. Cannot be changed once the kernel has been
        created  # noqa: E501

        :param kernel_type: The kernel_type of this KernelPushRequest. #
            noqa: E501
        :type: str
        """
        if kernel_type is None:
            raise ValueError("Invalid value for `kernel_type`, must not be `None`")  # noqa: E501
        allowed_values = ["script", "notebook"]  # noqa: E501
        if kernel_type not in allowed_values:
            raise ValueError(
                "Invalid value for `kernel_type` ({0}), must be one of {1}".format(  # noqa: E501
                    kernel_type, allowed_values
                )
            )

        self._kernel_type = kernel_type

    @property
    def is_private(self):
        """Gets the is_private of this KernelPushRequest.  # noqa: E501.

        Whether or not the kernel should be private  # noqa: E501

        :return: The is_private of this KernelPushRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this KernelPushRequest.

        Whether or not the kernel should be private  # noqa: E501

        :param is_private: The is_private of this KernelPushRequest. #
            noqa: E501
        :type: bool
        """

        self._is_private = is_private

    @property
    def enable_gpu(self):
        """Gets the enable_gpu of this KernelPushRequest.  # noqa: E501.

        Whether or not the kernel should run on a GPU  # noqa: E501

        :return: The enable_gpu of this KernelPushRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_gpu

    @enable_gpu.setter
    def enable_gpu(self, enable_gpu):
        """Sets the enable_gpu of this KernelPushRequest.

        Whether or not the kernel should run on a GPU  # noqa: E501

        :param enable_gpu: The enable_gpu of this KernelPushRequest. #
            noqa: E501
        :type: bool
        """

        self._enable_gpu = enable_gpu

    @property
    def enable_tpu(self):
        """Gets the enable_tpu of this KernelPushRequest.  # noqa: E501.

        Whether or not the kernel should run on a TPU  # noqa: E501

        :return: The enable_tpu of this KernelPushRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tpu

    @enable_tpu.setter
    def enable_tpu(self, enable_tpu):
        """Sets the enable_tpu of this KernelPushRequest.

        Whether or not the kernel should run on a TPU  # noqa: E501

        :param enable_tpu: The enable_tpu of this KernelPushRequest. #
            noqa: E501
        :type: bool
        """

        self._enable_tpu = enable_tpu

    @property
    def enable_internet(self):
        """Gets the enable_internet of this KernelPushRequest.  # noqa: E501.

        Whether or not the kernel should be able to access the internet
        # noqa: E501

        :return: The enable_internet of this KernelPushRequest. # noqa:
            E501
        :rtype: bool
        """
        return self._enable_internet

    @enable_internet.setter
    def enable_internet(self, enable_internet):
        """Sets the enable_internet of this KernelPushRequest.

        Whether or not the kernel should be able to access the internet
        # noqa: E501

        :param enable_internet: The enable_internet of this
            KernelPushRequest. # noqa: E501
        :type: bool
        """

        self._enable_internet = enable_internet

    @property
    def dataset_data_sources(self):
        """Gets the dataset_data_sources of this KernelPushRequest.  # noqa:
        E501.

        A list of dataset data sources that the kernel should use. Each
        dataset is specified as `USERNAME/DATASET-SLUG`  # noqa: E501

        :return: The dataset_data_sources of this KernelPushRequest. #
            noqa: E501
        :rtype: list[str]
        """
        return self._dataset_data_sources

    @dataset_data_sources.setter
    def dataset_data_sources(self, dataset_data_sources):
        """Sets the dataset_data_sources of this KernelPushRequest.

        A list of dataset data sources that the kernel should use. Each
        dataset is specified as `USERNAME/DATASET-SLUG`  # noqa: E501

        :param dataset_data_sources: The dataset_data_sources of this
            KernelPushRequest. # noqa: E501
        :type: list[str]
        """

        self._dataset_data_sources = dataset_data_sources

    @property
    def competition_data_sources(self):
        """Gets the competition_data_sources of this KernelPushRequest.  #
        noqa: E501.

        A list of competition data sources that the kernel should use  #
        noqa: E501

        :return: The competition_data_sources of this KernelPushRequest.
            # noqa: E501
        :rtype: list[str]
        """
        return self._competition_data_sources

    @competition_data_sources.setter
    def competition_data_sources(self, competition_data_sources):
        """Sets the competition_data_sources of this KernelPushRequest.

        A list of competition data sources that the kernel should use  #
        noqa: E501

        :param competition_data_sources: The competition_data_sources of
            this KernelPushRequest. # noqa: E501
        :type: list[str]
        """

        self._competition_data_sources = competition_data_sources

    @property
    def kernel_data_sources(self):
        """Gets the kernel_data_sources of this KernelPushRequest.  # noqa:
        E501.

        A list of kernel data sources that the kernel should use. Each
        dataset is specified as `USERNAME/KERNEL-SLUG`  # noqa: E501

        :return: The kernel_data_sources of this KernelPushRequest. #
            noqa: E501
        :rtype: list[str]
        """
        return self._kernel_data_sources

    @kernel_data_sources.setter
    def kernel_data_sources(self, kernel_data_sources):
        """Sets the kernel_data_sources of this KernelPushRequest.

        A list of kernel data sources that the kernel should use. Each
        dataset is specified as `USERNAME/KERNEL-SLUG`  # noqa: E501

        :param kernel_data_sources: The kernel_data_sources of this
            KernelPushRequest. # noqa: E501
        :type: list[str]
        """

        self._kernel_data_sources = kernel_data_sources

    @property
    def model_data_sources(self):
        """Gets the model_data_sources of this KernelPushRequest.  # noqa:
        E501.

        A list of model data sources that the kernel should use. Each model is specified as `USERNAME/MODEL-SLUG/FRAMEWORK/VARIATION-SLUG/VERSION-NUMBER`  # noqa: E501

        :return: The model_data_sources of this KernelPushRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_data_sources

    @model_data_sources.setter
    def model_data_sources(self, model_data_sources):
        """Sets the model_data_sources of this KernelPushRequest.

        A list of model data sources that the kernel should use. Each model is specified as `USERNAME/MODEL-SLUG/FRAMEWORK/VARIATION-SLUG/VERSION-NUMBER`  # noqa: E501

        :param model_data_sources: The model_data_sources of this KernelPushRequest.  # noqa: E501
        :type: list[str]
        """

        self._model_data_sources = model_data_sources

    @property
    def category_ids(self):
        """Gets the category_ids of this KernelPushRequest.  # noqa: E501.

        A list of tag IDs to associated with the kernel  # noqa: E501

        :return: The category_ids of this KernelPushRequest. # noqa:
            E501
        :rtype: list[str]
        """
        return self._category_ids

    @category_ids.setter
    def category_ids(self, category_ids):
        """Sets the category_ids of this KernelPushRequest.

        A list of tag IDs to associated with the kernel  # noqa: E501

        :param category_ids: The category_ids of this KernelPushRequest.
            # noqa: E501
        :type: list[str]
        """

        self._category_ids = category_ids

    @property
    def docker_image_pinning_type(self):
        """Gets the docker_image_pinning_type of this KernelPushRequest.  #
        noqa: E501.

        Which docker image to use for executing new versions going
        forward.  # noqa: E501

        :return: The docker_image_pinning_type of this
            KernelPushRequest. # noqa: E501
        :rtype: str
        """
        return self._docker_image_pinning_type

    @docker_image_pinning_type.setter
    def docker_image_pinning_type(self, docker_image_pinning_type):
        """Sets the docker_image_pinning_type of this KernelPushRequest.

        Which docker image to use for executing new versions going
        forward.  # noqa: E501

        :param docker_image_pinning_type: The docker_image_pinning_type
            of this KernelPushRequest. # noqa: E501
        :type: str
        """
        allowed_values = ["original", "latest"]  # noqa: E501
        if docker_image_pinning_type not in allowed_values:
            raise ValueError(
                "Invalid value for `docker_image_pinning_type` ({0}), must be one of {1}".format(  # noqa: E501
                    docker_image_pinning_type, allowed_values
                )
            )

        self._docker_image_pinning_type = docker_image_pinning_type

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
        if not isinstance(other, KernelPushRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal."""
        return not self == other
