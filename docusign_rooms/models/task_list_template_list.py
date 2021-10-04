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


class TaskListTemplateList(object):
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
        'task_list_templates': 'list[TaskListTemplate]',
        'result_set_size': 'int',
        'start_position': 'int',
        'end_position': 'int',
        'next_uri': 'str',
        'prior_uri': 'str',
        'total_row_count': 'int'
    }

    attribute_map = {
        'task_list_templates': 'taskListTemplates',
        'result_set_size': 'resultSetSize',
        'start_position': 'startPosition',
        'end_position': 'endPosition',
        'next_uri': 'nextUri',
        'prior_uri': 'priorUri',
        'total_row_count': 'totalRowCount'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """TaskListTemplateList - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._task_list_templates = None
        self._result_set_size = None
        self._start_position = None
        self._end_position = None
        self._next_uri = None
        self._prior_uri = None
        self._total_row_count = None
        self.discriminator = None

        setattr(self, "_{}".format('task_list_templates'), kwargs.get('task_list_templates', None))
        setattr(self, "_{}".format('result_set_size'), kwargs.get('result_set_size', None))
        setattr(self, "_{}".format('start_position'), kwargs.get('start_position', None))
        setattr(self, "_{}".format('end_position'), kwargs.get('end_position', None))
        setattr(self, "_{}".format('next_uri'), kwargs.get('next_uri', None))
        setattr(self, "_{}".format('prior_uri'), kwargs.get('prior_uri', None))
        setattr(self, "_{}".format('total_row_count'), kwargs.get('total_row_count', None))

    @property
    def task_list_templates(self):
        """Gets the task_list_templates of this TaskListTemplateList.  # noqa: E501


        :return: The task_list_templates of this TaskListTemplateList.  # noqa: E501
        :rtype: list[TaskListTemplate]
        """
        return self._task_list_templates

    @task_list_templates.setter
    def task_list_templates(self, task_list_templates):
        """Sets the task_list_templates of this TaskListTemplateList.


        :param task_list_templates: The task_list_templates of this TaskListTemplateList.  # noqa: E501
        :type: list[TaskListTemplate]
        """

        self._task_list_templates = task_list_templates

    @property
    def result_set_size(self):
        """Gets the result_set_size of this TaskListTemplateList.  # noqa: E501


        :return: The result_set_size of this TaskListTemplateList.  # noqa: E501
        :rtype: int
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """Sets the result_set_size of this TaskListTemplateList.


        :param result_set_size: The result_set_size of this TaskListTemplateList.  # noqa: E501
        :type: int
        """

        self._result_set_size = result_set_size

    @property
    def start_position(self):
        """Gets the start_position of this TaskListTemplateList.  # noqa: E501


        :return: The start_position of this TaskListTemplateList.  # noqa: E501
        :rtype: int
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """Sets the start_position of this TaskListTemplateList.


        :param start_position: The start_position of this TaskListTemplateList.  # noqa: E501
        :type: int
        """

        self._start_position = start_position

    @property
    def end_position(self):
        """Gets the end_position of this TaskListTemplateList.  # noqa: E501


        :return: The end_position of this TaskListTemplateList.  # noqa: E501
        :rtype: int
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """Sets the end_position of this TaskListTemplateList.


        :param end_position: The end_position of this TaskListTemplateList.  # noqa: E501
        :type: int
        """

        self._end_position = end_position

    @property
    def next_uri(self):
        """Gets the next_uri of this TaskListTemplateList.  # noqa: E501


        :return: The next_uri of this TaskListTemplateList.  # noqa: E501
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """Sets the next_uri of this TaskListTemplateList.


        :param next_uri: The next_uri of this TaskListTemplateList.  # noqa: E501
        :type: str
        """

        self._next_uri = next_uri

    @property
    def prior_uri(self):
        """Gets the prior_uri of this TaskListTemplateList.  # noqa: E501


        :return: The prior_uri of this TaskListTemplateList.  # noqa: E501
        :rtype: str
        """
        return self._prior_uri

    @prior_uri.setter
    def prior_uri(self, prior_uri):
        """Sets the prior_uri of this TaskListTemplateList.


        :param prior_uri: The prior_uri of this TaskListTemplateList.  # noqa: E501
        :type: str
        """

        self._prior_uri = prior_uri

    @property
    def total_row_count(self):
        """Gets the total_row_count of this TaskListTemplateList.  # noqa: E501


        :return: The total_row_count of this TaskListTemplateList.  # noqa: E501
        :rtype: int
        """
        return self._total_row_count

    @total_row_count.setter
    def total_row_count(self, total_row_count):
        """Sets the total_row_count of this TaskListTemplateList.


        :param total_row_count: The total_row_count of this TaskListTemplateList.  # noqa: E501
        :type: int
        """

        self._total_row_count = total_row_count

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
        if issubclass(TaskListTemplateList, dict):
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
        if not isinstance(other, TaskListTemplateList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskListTemplateList):
            return True

        return self.to_dict() != other.to_dict()
