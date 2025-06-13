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


class ModelInstanceUpdateRequest(object):
    """
    Attributes:
      project_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    project_types = {
        "overview": "str",
        "usage": "str",
        "license_name": "str",
        "fine_tunable": "bool",
        "training_data": "list[str]",
        "model_instance_type": "str",
        "base_model_instance": "str",
        "external_base_model_url": "int",
        "update_mask": "str",
    }

    attribute_map = {
        "overview": "overview",
        "usage": "usage",
        "license_name": "licenseName",
        "fine_tunable": "fineTunable",
        "training_data": "trainingData",
        "model_instance_type": "modelInstanceType",
        "base_model_instance": "baseModelInstance",
        "external_base_model_url": "externalBaseModelUrl",
        "update_mask": "updateMask",
    }

    def __init__(
        self,
        overview=None,
        usage=None,
        license_name="Apache 2.0",
        fine_tunable=True,
        training_data=None,
        model_instance_type=None,
        base_model_instance=None,
        external_base_model_url=None,
        update_mask=None,
    ):  # noqa: E501

        self._overview = None
        self._usage = None
        self._license_name = None
        self._fine_tunable = None
        self._training_data = None
        self._model_instance_type = None
        self._base_model_instance = None
        self._external_base_model_url = None
        self._update_mask = None
        self.discriminator = None

        if overview is not None:
            self.overview = overview
        if usage is not None:
            self.usage = usage
        if license_name is not None:
            self.license_name = license_name
        if fine_tunable is not None:
            self.fine_tunable = fine_tunable
        if training_data is not None:
            self.training_data = training_data
        if model_instance_type is not None:
            self.model_instance_type = model_instance_type
        if base_model_instance is not None:
            self.base_model_instance = base_model_instance
        if external_base_model_url is not None:
            self.external_base_model_url = external_base_model_url
        self.update_mask = update_mask

    @property
    def overview(self):
        """Gets the overview of this ModelInstanceUpdateRequest.  # noqa: E501.

        The overview of the model instance (markdown)  # noqa: E501

        :return: The overview of this ModelInstanceUpdateRequest. #
            noqa: E501
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """Sets the overview of this ModelInstanceUpdateRequest.

        The overview of the model instance (markdown)  # noqa: E501

        :param overview: The overview of this
            ModelInstanceUpdateRequest. # noqa: E501
        :type: str
        """

        self._overview = overview

    @property
    def usage(self):
        """Gets the usage of this ModelInstanceUpdateRequest.  # noqa: E501.

        The description of how to use the model instance (markdown)  #
        noqa: E501

        :return: The usage of this ModelInstanceUpdateRequest. # noqa:
            E501
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ModelInstanceUpdateRequest.

        The description of how to use the model instance (markdown)  #
        noqa: E501

        :param usage: The usage of this ModelInstanceUpdateRequest. #
            noqa: E501
        :type: str
        """

        self._usage = usage

    @property
    def license_name(self):
        """Gets the license_name of this ModelInstanceUpdateRequest.  # noqa:
        E501.

        The license that should be associated with the model instance  #
        noqa: E501

        :return: The license_name of this ModelInstanceUpdateRequest. #
            noqa: E501
        :rtype: str
        """
        return self._license_name

    @license_name.setter
    def license_name(self, license_name):
        """Sets the license_name of this ModelInstanceUpdateRequest.

        The license that should be associated with the model instance  #
        noqa: E501

        :param license_name: The license_name of this
            ModelInstanceUpdateRequest. # noqa: E501
        :type: str
        """
        allowed_values = [
            "CC0 1.0",
            "CC BY-NC-SA 4.0",
            "Unknown",
            "CC BY-SA 4.0",
            "GPL 2",
            "CC BY-SA 3.0",
            "Other",
            "Other (specified in description)",
            "CC BY 4.0",
            "Attribution 4.0 International (CC BY 4.0)",
            "CC BY-NC 4.0",
            "Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)",
            "PDDL",
            "ODC Public Domain Dedication and Licence (PDDL)",
            "CC BY 3.0",
            "Attribution 3.0 Unported (CC BY 3.0)",
            "CC BY 3.0 IGO",
            "Attribution 3.0 IGO (CC BY 3.0 IGO)",
            "CC BY-NC-SA 3.0 IGO",
            "Attribution-NonCommercial-ShareAlike 3.0 IGO (CC BY-NC-SA 3.0 IGO)",
            "CDLA Permissive 1.0",
            "Community Data License Agreement - Permissive - Version 1.0",
            "CDLA Sharing 1.0",
            "Community Data License Agreement - Sharing - Version 1.0",
            "CC BY-ND 4.0",
            "Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)",
            "CC BY-NC-ND 4.0",
            "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)",
            "ODC-BY 1.0",
            "ODC Attribution License (ODC-By)",
            "LGPL 3.0",
            "GNU Lesser General Public License 3.0",
            "AGPL 3.0",
            "GNU Affero General Public License 3.0",
            "FDL 1.3",
            "GNU Free Documentation License 1.3",
            "apache-2.0",
            "Apache 2.0",
            "mit",
            "MIT",
            "bsd-3-clause",
            "BSD-3-Clause",
            "Llama 2",
            "Llama 2 Community License",
            "Gemma",
            "gpl-3",
            "GPL 3",
            "RAIL-M",
            "AI Pubs Open RAIL-M License",
            "AIPubs Research-Use RAIL-M",
            "AI Pubs Research-Use RAIL-M License",
            "BigScience OpenRAIL-M",
            "BigScience Open RAIL-M License",
            "RAIL",
            "RAIL (specified in description)",
            "Llama 3",
            "Llama 3 Community License",
        ]  # noqa: E501
        if license_name not in allowed_values:
            raise ValueError(
                "Invalid value for `license_name` ({0}), must be one of {1}".format(  # noqa: E501
                    license_name, allowed_values
                )
            )

        self._license_name = license_name

    @property
    def fine_tunable(self):
        """Gets the fine_tunable of this ModelInstanceUpdateRequest.  # noqa:
        E501.

        Whether the model instance is fine tunable  # noqa: E501

        :return: The fine_tunable of this ModelInstanceUpdateRequest. #
            noqa: E501
        :rtype: bool
        """
        return self._fine_tunable

    @fine_tunable.setter
    def fine_tunable(self, fine_tunable):
        """Sets the fine_tunable of this ModelInstanceUpdateRequest.

        Whether the model instance is fine tunable  # noqa: E501

        :param fine_tunable: The fine_tunable of this
            ModelInstanceUpdateRequest. # noqa: E501
        :type: bool
        """

        self._fine_tunable = fine_tunable

    @property
    def training_data(self):
        """Gets the training_data of this ModelInstanceUpdateRequest.  # noqa:
        E501.

        A list of training data (urls or names)  # noqa: E501

        :return: The training_data of this ModelInstanceUpdateRequest. #
            noqa: E501
        :rtype: list[str]
        """
        return self._training_data

    @training_data.setter
    def training_data(self, training_data):
        """Sets the training_data of this ModelInstanceUpdateRequest.

        A list of training data (urls or names)  # noqa: E501

        :param training_data: The training_data of this
            ModelInstanceUpdateRequest. # noqa: E501
        :type: list[str]
        """

        self._training_data = training_data

    @property
    def model_instance_type(self):
        """Gets the model_instance_type of this ModelInstanceUpdateRequest.  #
        noqa: E501.

        Whether the model instance is a base model, external variant,
        internal variant, or unspecified  # noqa: E501

        :return: The model_instance_type of this
            ModelInstanceUpdateRequest. # noqa: E501
        :rtype: str
        """
        return self._model_instance_type

    @model_instance_type.setter
    def model_instance_type(self, model_instance_type):
        """Sets the model_instance_type of this ModelInstanceUpdateRequest.

        Whether the model instance is a base model, external variant,
        internal variant, or unspecified  # noqa: E501

        :param model_instance_type: The model_instance_type of this
            ModelInstanceUpdateRequest. # noqa: E501
        :type: str
        """
        allowed_values = ["Unspecified", "BaseModel", "KaggleVariant", "ExternalVariant"]  # noqa: E501
        if model_instance_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_instance_type` ({0}), must be one of {1}".format(  # noqa: E501
                    model_instance_type, allowed_values
                )
            )

        self._model_instance_type = model_instance_type

    @property
    def base_model_instance(self):
        """Gets the base_model_instance of this ModelInstanceUpdateRequest.  #
        noqa: E501.

        If this is an internal variant, the `{owner-slug}/{model-slug}/{framework}/{instance-slug}` of the base model instance  # noqa: E501

        :return: The base_model_instance of this ModelInstanceUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_model_instance

    @base_model_instance.setter
    def base_model_instance(self, base_model_instance):
        """Sets the base_model_instance of this ModelInstanceUpdateRequest.

        If this is an internal variant, the `{owner-slug}/{model-slug}/{framework}/{instance-slug}` of the base model instance  # noqa: E501

        :param base_model_instance: The base_model_instance of this ModelInstanceUpdateRequest.  # noqa: E501
        :type: str
        """

        self._base_model_instance = base_model_instance

    @property
    def external_base_model_url(self):
        """Gets the external_base_model_url of this ModelInstanceUpdateRequest.
        # noqa: E501.

        If this is an external variant, a URL to the base model  # noqa:
        E501

        :return: The external_base_model_url of this
            ModelInstanceUpdateRequest. # noqa: E501
        :rtype: int
        """
        return self._external_base_model_url

    @external_base_model_url.setter
    def external_base_model_url(self, external_base_model_url):
        """Sets the external_base_model_url of this ModelInstanceUpdateRequest.

        If this is an external variant, a URL to the base model  # noqa:
        E501

        :param external_base_model_url: The external_base_model_url of
            this ModelInstanceUpdateRequest. # noqa: E501
        :type: int
        """

        self._external_base_model_url = external_base_model_url

    @property
    def update_mask(self):
        """Gets the update_mask of this ModelInstanceUpdateRequest.  # noqa:
        E501.

        Describes which fields to update  # noqa: E501

        :return: The update_mask of this ModelInstanceUpdateRequest. #
            noqa: E501
        :rtype: str
        """
        return self._update_mask

    @update_mask.setter
    def update_mask(self, update_mask):
        """Sets the update_mask of this ModelInstanceUpdateRequest.

        Describes which fields to update  # noqa: E501

        :param update_mask: The update_mask of this
            ModelInstanceUpdateRequest. # noqa: E501
        :type: str
        """
        if update_mask is None:
            raise ValueError("Invalid value for `update_mask`, must not be `None`")  # noqa: E501

        self._update_mask = update_mask

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
        if not isinstance(other, ModelInstanceUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal."""
        return not self == other
