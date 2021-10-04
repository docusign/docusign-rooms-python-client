# coding: utf-8

"""
    DocuSign Rooms API - v2

    An API for an integrator to access the features of DocuSign Rooms  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_rooms.client.configuration import Configuration


class FormGroupFormToAssign(object):
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
        'form_id': 'str',
        'is_required': 'bool'
    }

    attribute_map = {
        'form_id': 'formId',
        'is_required': 'isRequired'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """FormGroupFormToAssign - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._form_id = None
        self._is_required = None
        self.discriminator = None

        setattr(self, "_{}".format('form_id'), kwargs.get('form_id', None))
        setattr(self, "_{}".format('is_required'), kwargs.get('is_required', None))

    @property
    def form_id(self):
        """Gets the form_id of this FormGroupFormToAssign.  # noqa: E501


        :return: The form_id of this FormGroupFormToAssign.  # noqa: E501
        :rtype: str
        """
        return self._form_id

    @form_id.setter
    def form_id(self, form_id):
        """Sets the form_id of this FormGroupFormToAssign.


        :param form_id: The form_id of this FormGroupFormToAssign.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and form_id is None:
            raise ValueError("Invalid value for `form_id`, must not be `None`")  # noqa: E501

        self._form_id = form_id

    @property
    def is_required(self):
        """Gets the is_required of this FormGroupFormToAssign.  # noqa: E501


        :return: The is_required of this FormGroupFormToAssign.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this FormGroupFormToAssign.


        :param is_required: The is_required of this FormGroupFormToAssign.  # noqa: E501
        :type: bool
        """

        self._is_required = is_required

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
        if issubclass(FormGroupFormToAssign, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FormGroupFormToAssign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormGroupFormToAssign):
            return True

        return self.to_dict() != other.to_dict()
