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


class Region(object):
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
        'region_id': 'int',
        'name': 'str',
        'created_date': 'datetime'
    }

    attribute_map = {
        'region_id': 'regionId',
        'name': 'name',
        'created_date': 'createdDate'
    }

    def __init__(self, region_id=None, name=None, created_date=None):  # noqa: E501
        """Region - a model defined in Swagger"""  # noqa: E501

        self._region_id = None
        self._name = None
        self._created_date = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        self.name = name
        if created_date is not None:
            self.created_date = created_date

    @property
    def region_id(self):
        """Gets the region_id of this Region.  # noqa: E501


        :return: The region_id of this Region.  # noqa: E501
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this Region.


        :param region_id: The region_id of this Region.  # noqa: E501
        :type: int
        """

        self._region_id = region_id

    @property
    def name(self):
        """Gets the name of this Region.  # noqa: E501


        :return: The name of this Region.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Region.


        :param name: The name of this Region.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_date(self):
        """Gets the created_date of this Region.  # noqa: E501


        :return: The created_date of this Region.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Region.


        :param created_date: The created_date of this Region.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

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
        if issubclass(Region, dict):
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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
