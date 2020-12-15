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


class FinancingType(object):
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
        'financing_type_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'financing_type_id': 'financingTypeId',
        'name': 'name'
    }

    def __init__(self, financing_type_id=None, name=None):  # noqa: E501
        """FinancingType - a model defined in Swagger"""  # noqa: E501

        self._financing_type_id = None
        self._name = None
        self.discriminator = None

        if financing_type_id is not None:
            self.financing_type_id = financing_type_id
        if name is not None:
            self.name = name

    @property
    def financing_type_id(self):
        """Gets the financing_type_id of this FinancingType.  # noqa: E501


        :return: The financing_type_id of this FinancingType.  # noqa: E501
        :rtype: str
        """
        return self._financing_type_id

    @financing_type_id.setter
    def financing_type_id(self, financing_type_id):
        """Sets the financing_type_id of this FinancingType.


        :param financing_type_id: The financing_type_id of this FinancingType.  # noqa: E501
        :type: str
        """

        self._financing_type_id = financing_type_id

    @property
    def name(self):
        """Gets the name of this FinancingType.  # noqa: E501


        :return: The name of this FinancingType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FinancingType.


        :param name: The name of this FinancingType.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(FinancingType, dict):
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
        if not isinstance(other, FinancingType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other