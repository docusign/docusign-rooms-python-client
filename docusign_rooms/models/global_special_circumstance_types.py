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


class GlobalSpecialCircumstanceTypes(object):
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
        'special_circumstance_types': 'list[SpecialCircumstanceType]'
    }

    attribute_map = {
        'special_circumstance_types': 'specialCircumstanceTypes'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """GlobalSpecialCircumstanceTypes - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._special_circumstance_types = None
        self.discriminator = None

        setattr(self, "_{}".format('special_circumstance_types'), kwargs.get('special_circumstance_types', None))

    @property
    def special_circumstance_types(self):
        """Gets the special_circumstance_types of this GlobalSpecialCircumstanceTypes.  # noqa: E501


        :return: The special_circumstance_types of this GlobalSpecialCircumstanceTypes.  # noqa: E501
        :rtype: list[SpecialCircumstanceType]
        """
        return self._special_circumstance_types

    @special_circumstance_types.setter
    def special_circumstance_types(self, special_circumstance_types):
        """Sets the special_circumstance_types of this GlobalSpecialCircumstanceTypes.


        :param special_circumstance_types: The special_circumstance_types of this GlobalSpecialCircumstanceTypes.  # noqa: E501
        :type: list[SpecialCircumstanceType]
        """

        self._special_circumstance_types = special_circumstance_types

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
        if issubclass(GlobalSpecialCircumstanceTypes, dict):
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
        if not isinstance(other, GlobalSpecialCircumstanceTypes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlobalSpecialCircumstanceTypes):
            return True

        return self.to_dict() != other.to_dict()
