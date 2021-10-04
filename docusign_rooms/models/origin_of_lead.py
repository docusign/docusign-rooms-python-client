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


class OriginOfLead(object):
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
        'origin_of_lead_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'origin_of_lead_id': 'originOfLeadId',
        'name': 'name'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """OriginOfLead - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._origin_of_lead_id = None
        self._name = None
        self.discriminator = None

        setattr(self, "_{}".format('origin_of_lead_id'), kwargs.get('origin_of_lead_id', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))

    @property
    def origin_of_lead_id(self):
        """Gets the origin_of_lead_id of this OriginOfLead.  # noqa: E501


        :return: The origin_of_lead_id of this OriginOfLead.  # noqa: E501
        :rtype: str
        """
        return self._origin_of_lead_id

    @origin_of_lead_id.setter
    def origin_of_lead_id(self, origin_of_lead_id):
        """Sets the origin_of_lead_id of this OriginOfLead.


        :param origin_of_lead_id: The origin_of_lead_id of this OriginOfLead.  # noqa: E501
        :type: str
        """

        self._origin_of_lead_id = origin_of_lead_id

    @property
    def name(self):
        """Gets the name of this OriginOfLead.  # noqa: E501


        :return: The name of this OriginOfLead.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OriginOfLead.


        :param name: The name of this OriginOfLead.  # noqa: E501
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
        if issubclass(OriginOfLead, dict):
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
        if not isinstance(other, OriginOfLead):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OriginOfLead):
            return True

        return self.to_dict() != other.to_dict()
