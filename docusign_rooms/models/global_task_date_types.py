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


class GlobalTaskDateTypes(object):
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
        'task_date_types': 'list[TaskDateType]'
    }

    attribute_map = {
        'task_date_types': 'taskDateTypes'
    }

    def __init__(self, task_date_types=None):  # noqa: E501
        """GlobalTaskDateTypes - a model defined in Swagger"""  # noqa: E501

        self._task_date_types = None
        self.discriminator = None

        if task_date_types is not None:
            self.task_date_types = task_date_types

    @property
    def task_date_types(self):
        """Gets the task_date_types of this GlobalTaskDateTypes.  # noqa: E501


        :return: The task_date_types of this GlobalTaskDateTypes.  # noqa: E501
        :rtype: list[TaskDateType]
        """
        return self._task_date_types

    @task_date_types.setter
    def task_date_types(self, task_date_types):
        """Sets the task_date_types of this GlobalTaskDateTypes.


        :param task_date_types: The task_date_types of this GlobalTaskDateTypes.  # noqa: E501
        :type: list[TaskDateType]
        """

        self._task_date_types = task_date_types

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
        if issubclass(GlobalTaskDateTypes, dict):
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
        if not isinstance(other, GlobalTaskDateTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other