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


class TaskListForCreate(object):
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
        'task_list_template_id': 'int'
    }

    attribute_map = {
        'task_list_template_id': 'taskListTemplateId'
    }

    def __init__(self, task_list_template_id=None):  # noqa: E501
        """TaskListForCreate - a model defined in Swagger"""  # noqa: E501

        self._task_list_template_id = None
        self.discriminator = None

        if task_list_template_id is not None:
            self.task_list_template_id = task_list_template_id

    @property
    def task_list_template_id(self):
        """Gets the task_list_template_id of this TaskListForCreate.  # noqa: E501


        :return: The task_list_template_id of this TaskListForCreate.  # noqa: E501
        :rtype: int
        """
        return self._task_list_template_id

    @task_list_template_id.setter
    def task_list_template_id(self, task_list_template_id):
        """Sets the task_list_template_id of this TaskListForCreate.


        :param task_list_template_id: The task_list_template_id of this TaskListForCreate.  # noqa: E501
        :type: int
        """

        self._task_list_template_id = task_list_template_id

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
        if issubclass(TaskListForCreate, dict):
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
        if not isinstance(other, TaskListForCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other