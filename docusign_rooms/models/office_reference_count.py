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


class OfficeReferenceCount(object):
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
        'reference_type': 'str',
        'referenced_count': 'int'
    }

    attribute_map = {
        'reference_type': 'referenceType',
        'referenced_count': 'referencedCount'
    }

    def __init__(self, reference_type=None, referenced_count=None):  # noqa: E501
        """OfficeReferenceCount - a model defined in Swagger"""  # noqa: E501

        self._reference_type = None
        self._referenced_count = None
        self.discriminator = None

        if reference_type is not None:
            self.reference_type = reference_type
        if referenced_count is not None:
            self.referenced_count = referenced_count

    @property
    def reference_type(self):
        """Gets the reference_type of this OfficeReferenceCount.  # noqa: E501


        :return: The reference_type of this OfficeReferenceCount.  # noqa: E501
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this OfficeReferenceCount.


        :param reference_type: The reference_type of this OfficeReferenceCount.  # noqa: E501
        :type: str
        """

        self._reference_type = reference_type

    @property
    def referenced_count(self):
        """Gets the referenced_count of this OfficeReferenceCount.  # noqa: E501


        :return: The referenced_count of this OfficeReferenceCount.  # noqa: E501
        :rtype: int
        """
        return self._referenced_count

    @referenced_count.setter
    def referenced_count(self, referenced_count):
        """Sets the referenced_count of this OfficeReferenceCount.


        :param referenced_count: The referenced_count of this OfficeReferenceCount.  # noqa: E501
        :type: int
        """

        self._referenced_count = referenced_count

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
        if issubclass(OfficeReferenceCount, dict):
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
        if not isinstance(other, OfficeReferenceCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
