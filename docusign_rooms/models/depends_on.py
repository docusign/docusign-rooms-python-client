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


class DependsOn(object):
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
        'action_type': 'str',
        'parent_api_name': 'str'
    }

    attribute_map = {
        'action_type': 'actionType',
        'parent_api_name': 'parentApiName'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DependsOn - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action_type = None
        self._parent_api_name = None
        self.discriminator = None

        setattr(self, "_{}".format('action_type'), kwargs.get('action_type', None))
        setattr(self, "_{}".format('parent_api_name'), kwargs.get('parent_api_name', None))

    @property
    def action_type(self):
        """Gets the action_type of this DependsOn.  # noqa: E501


        :return: The action_type of this DependsOn.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this DependsOn.


        :param action_type: The action_type of this DependsOn.  # noqa: E501
        :type: str
        """

        self._action_type = action_type

    @property
    def parent_api_name(self):
        """Gets the parent_api_name of this DependsOn.  # noqa: E501


        :return: The parent_api_name of this DependsOn.  # noqa: E501
        :rtype: str
        """
        return self._parent_api_name

    @parent_api_name.setter
    def parent_api_name(self, parent_api_name):
        """Sets the parent_api_name of this DependsOn.


        :param parent_api_name: The parent_api_name of this DependsOn.  # noqa: E501
        :type: str
        """

        self._parent_api_name = parent_api_name

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
        if issubclass(DependsOn, dict):
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
        if not isinstance(other, DependsOn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DependsOn):
            return True

        return self.to_dict() != other.to_dict()
