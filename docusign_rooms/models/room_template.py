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


class RoomTemplate(object):
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
        'room_template_id': 'int',
        'name': 'str',
        'task_template_count': 'int'
    }

    attribute_map = {
        'room_template_id': 'roomTemplateId',
        'name': 'name',
        'task_template_count': 'taskTemplateCount'
    }

    def __init__(self, room_template_id=None, name=None, task_template_count=None):  # noqa: E501
        """RoomTemplate - a model defined in Swagger"""  # noqa: E501

        self._room_template_id = None
        self._name = None
        self._task_template_count = None
        self.discriminator = None

        if room_template_id is not None:
            self.room_template_id = room_template_id
        if name is not None:
            self.name = name
        if task_template_count is not None:
            self.task_template_count = task_template_count

    @property
    def room_template_id(self):
        """Gets the room_template_id of this RoomTemplate.  # noqa: E501


        :return: The room_template_id of this RoomTemplate.  # noqa: E501
        :rtype: int
        """
        return self._room_template_id

    @room_template_id.setter
    def room_template_id(self, room_template_id):
        """Sets the room_template_id of this RoomTemplate.


        :param room_template_id: The room_template_id of this RoomTemplate.  # noqa: E501
        :type: int
        """

        self._room_template_id = room_template_id

    @property
    def name(self):
        """Gets the name of this RoomTemplate.  # noqa: E501


        :return: The name of this RoomTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoomTemplate.


        :param name: The name of this RoomTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def task_template_count(self):
        """Gets the task_template_count of this RoomTemplate.  # noqa: E501


        :return: The task_template_count of this RoomTemplate.  # noqa: E501
        :rtype: int
        """
        return self._task_template_count

    @task_template_count.setter
    def task_template_count(self, task_template_count):
        """Sets the task_template_count of this RoomTemplate.


        :param task_template_count: The task_template_count of this RoomTemplate.  # noqa: E501
        :type: int
        """

        self._task_template_count = task_template_count

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
        if issubclass(RoomTemplate, dict):
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
        if not isinstance(other, RoomTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
