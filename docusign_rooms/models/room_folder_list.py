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


class RoomFolderList(object):
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
        'folders': 'list[RoomFolder]',
        'result_set_size': 'int',
        'start_position': 'int',
        'end_position': 'int',
        'next_uri': 'str',
        'prior_uri': 'str'
    }

    attribute_map = {
        'folders': 'folders',
        'result_set_size': 'resultSetSize',
        'start_position': 'startPosition',
        'end_position': 'endPosition',
        'next_uri': 'nextUri',
        'prior_uri': 'priorUri'
    }

    def __init__(self, folders=None, result_set_size=None, start_position=None, end_position=None, next_uri=None, prior_uri=None):  # noqa: E501
        """RoomFolderList - a model defined in Swagger"""  # noqa: E501

        self._folders = None
        self._result_set_size = None
        self._start_position = None
        self._end_position = None
        self._next_uri = None
        self._prior_uri = None
        self.discriminator = None

        if folders is not None:
            self.folders = folders
        if result_set_size is not None:
            self.result_set_size = result_set_size
        if start_position is not None:
            self.start_position = start_position
        if end_position is not None:
            self.end_position = end_position
        if next_uri is not None:
            self.next_uri = next_uri
        if prior_uri is not None:
            self.prior_uri = prior_uri

    @property
    def folders(self):
        """Gets the folders of this RoomFolderList.  # noqa: E501


        :return: The folders of this RoomFolderList.  # noqa: E501
        :rtype: list[RoomFolder]
        """
        return self._folders

    @folders.setter
    def folders(self, folders):
        """Sets the folders of this RoomFolderList.


        :param folders: The folders of this RoomFolderList.  # noqa: E501
        :type: list[RoomFolder]
        """

        self._folders = folders

    @property
    def result_set_size(self):
        """Gets the result_set_size of this RoomFolderList.  # noqa: E501


        :return: The result_set_size of this RoomFolderList.  # noqa: E501
        :rtype: int
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """Sets the result_set_size of this RoomFolderList.


        :param result_set_size: The result_set_size of this RoomFolderList.  # noqa: E501
        :type: int
        """

        self._result_set_size = result_set_size

    @property
    def start_position(self):
        """Gets the start_position of this RoomFolderList.  # noqa: E501


        :return: The start_position of this RoomFolderList.  # noqa: E501
        :rtype: int
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """Sets the start_position of this RoomFolderList.


        :param start_position: The start_position of this RoomFolderList.  # noqa: E501
        :type: int
        """

        self._start_position = start_position

    @property
    def end_position(self):
        """Gets the end_position of this RoomFolderList.  # noqa: E501


        :return: The end_position of this RoomFolderList.  # noqa: E501
        :rtype: int
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """Sets the end_position of this RoomFolderList.


        :param end_position: The end_position of this RoomFolderList.  # noqa: E501
        :type: int
        """

        self._end_position = end_position

    @property
    def next_uri(self):
        """Gets the next_uri of this RoomFolderList.  # noqa: E501


        :return: The next_uri of this RoomFolderList.  # noqa: E501
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """Sets the next_uri of this RoomFolderList.


        :param next_uri: The next_uri of this RoomFolderList.  # noqa: E501
        :type: str
        """

        self._next_uri = next_uri

    @property
    def prior_uri(self):
        """Gets the prior_uri of this RoomFolderList.  # noqa: E501


        :return: The prior_uri of this RoomFolderList.  # noqa: E501
        :rtype: str
        """
        return self._prior_uri

    @prior_uri.setter
    def prior_uri(self, prior_uri):
        """Sets the prior_uri of this RoomFolderList.


        :param prior_uri: The prior_uri of this RoomFolderList.  # noqa: E501
        :type: str
        """

        self._prior_uri = prior_uri

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
        if issubclass(RoomFolderList, dict):
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
        if not isinstance(other, RoomFolderList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
