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


class RoomInvite(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'role_id': 'int',
        'transaction_side_id': 'str'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'role_id': 'roleId',
        'transaction_side_id': 'transactionSideId'
    }

    def __init__(self, email=None, first_name=None, last_name=None, role_id=None, transaction_side_id=None):  # noqa: E501
        """RoomInvite - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._first_name = None
        self._last_name = None
        self._role_id = None
        self._transaction_side_id = None
        self.discriminator = None

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role_id = role_id
        if transaction_side_id is not None:
            self.transaction_side_id = transaction_side_id

    @property
    def email(self):
        """Gets the email of this RoomInvite.  # noqa: E501


        :return: The email of this RoomInvite.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RoomInvite.


        :param email: The email of this RoomInvite.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this RoomInvite.  # noqa: E501


        :return: The first_name of this RoomInvite.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this RoomInvite.


        :param first_name: The first_name of this RoomInvite.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this RoomInvite.  # noqa: E501


        :return: The last_name of this RoomInvite.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this RoomInvite.


        :param last_name: The last_name of this RoomInvite.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def role_id(self):
        """Gets the role_id of this RoomInvite.  # noqa: E501


        :return: The role_id of this RoomInvite.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this RoomInvite.


        :param role_id: The role_id of this RoomInvite.  # noqa: E501
        :type: int
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def transaction_side_id(self):
        """Gets the transaction_side_id of this RoomInvite.  # noqa: E501

        Required for a real estate company; otherwise ignored.  # noqa: E501

        :return: The transaction_side_id of this RoomInvite.  # noqa: E501
        :rtype: str
        """
        return self._transaction_side_id

    @transaction_side_id.setter
    def transaction_side_id(self, transaction_side_id):
        """Sets the transaction_side_id of this RoomInvite.

        Required for a real estate company; otherwise ignored.  # noqa: E501

        :param transaction_side_id: The transaction_side_id of this RoomInvite.  # noqa: E501
        :type: str
        """

        self._transaction_side_id = transaction_side_id

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
        if issubclass(RoomInvite, dict):
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
        if not isinstance(other, RoomInvite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other