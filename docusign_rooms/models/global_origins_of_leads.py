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


class GlobalOriginsOfLeads(object):
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
        'origins_of_leads': 'list[OriginOfLead]'
    }

    attribute_map = {
        'origins_of_leads': 'originsOfLeads'
    }

    def __init__(self, origins_of_leads=None):  # noqa: E501
        """GlobalOriginsOfLeads - a model defined in Swagger"""  # noqa: E501

        self._origins_of_leads = None
        self.discriminator = None

        if origins_of_leads is not None:
            self.origins_of_leads = origins_of_leads

    @property
    def origins_of_leads(self):
        """Gets the origins_of_leads of this GlobalOriginsOfLeads.  # noqa: E501


        :return: The origins_of_leads of this GlobalOriginsOfLeads.  # noqa: E501
        :rtype: list[OriginOfLead]
        """
        return self._origins_of_leads

    @origins_of_leads.setter
    def origins_of_leads(self, origins_of_leads):
        """Sets the origins_of_leads of this GlobalOriginsOfLeads.


        :param origins_of_leads: The origins_of_leads of this GlobalOriginsOfLeads.  # noqa: E501
        :type: list[OriginOfLead]
        """

        self._origins_of_leads = origins_of_leads

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
        if issubclass(GlobalOriginsOfLeads, dict):
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
        if not isinstance(other, GlobalOriginsOfLeads):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other