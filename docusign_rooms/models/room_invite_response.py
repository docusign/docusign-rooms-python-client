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


class RoomInviteResponse(object):
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
        'user_id': 'int',
        'room_id': 'int',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'transaction_side_id': 'str',
        'role_id': 'int'
    }

    attribute_map = {
        'user_id': 'userId',
        'room_id': 'roomId',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'transaction_side_id': 'transactionSideId',
        'role_id': 'roleId'
    }

    def __init__(self, user_id=None, room_id=None, email=None, first_name=None, last_name=None, transaction_side_id=None, role_id=None):  # noqa: E501
        """RoomInviteResponse - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._room_id = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._transaction_side_id = None
        self._role_id = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if room_id is not None:
            self.room_id = room_id
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if transaction_side_id is not None:
            self.transaction_side_id = transaction_side_id
        if role_id is not None:
            self.role_id = role_id

    @property
    def user_id(self):
        """Gets the user_id of this RoomInviteResponse.  # noqa: E501


        :return: The user_id of this RoomInviteResponse.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RoomInviteResponse.


        :param user_id: The user_id of this RoomInviteResponse.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def room_id(self):
        """Gets the room_id of this RoomInviteResponse.  # noqa: E501


        :return: The room_id of this RoomInviteResponse.  # noqa: E501
        :rtype: int
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this RoomInviteResponse.


        :param room_id: The room_id of this RoomInviteResponse.  # noqa: E501
        :type: int
        """

        self._room_id = room_id

    @property
    def email(self):
        """Gets the email of this RoomInviteResponse.  # noqa: E501


        :return: The email of this RoomInviteResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RoomInviteResponse.


        :param email: The email of this RoomInviteResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this RoomInviteResponse.  # noqa: E501


        :return: The first_name of this RoomInviteResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this RoomInviteResponse.


        :param first_name: The first_name of this RoomInviteResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this RoomInviteResponse.  # noqa: E501


        :return: The last_name of this RoomInviteResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this RoomInviteResponse.


        :param last_name: The last_name of this RoomInviteResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def transaction_side_id(self):
        """Gets the transaction_side_id of this RoomInviteResponse.  # noqa: E501


        :return: The transaction_side_id of this RoomInviteResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_side_id

    @transaction_side_id.setter
    def transaction_side_id(self, transaction_side_id):
        """Sets the transaction_side_id of this RoomInviteResponse.


        :param transaction_side_id: The transaction_side_id of this RoomInviteResponse.  # noqa: E501
        :type: str
        """

        self._transaction_side_id = transaction_side_id

    @property
    def role_id(self):
        """Gets the role_id of this RoomInviteResponse.  # noqa: E501


        :return: The role_id of this RoomInviteResponse.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this RoomInviteResponse.


        :param role_id: The role_id of this RoomInviteResponse.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

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
        if issubclass(RoomInviteResponse, dict):
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
        if not isinstance(other, RoomInviteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
