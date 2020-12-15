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


class RoomUserSummary(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'transaction_side_id': 'str',
        'role_id': 'int',
        'title_id': 'int',
        'company_name': 'str',
        'role_name': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'transaction_side_id': 'transactionSideId',
        'role_id': 'roleId',
        'title_id': 'titleId',
        'company_name': 'companyName',
        'role_name': 'roleName'
    }

    def __init__(self, user_id=None, email=None, first_name=None, last_name=None, transaction_side_id=None, role_id=None, title_id=None, company_name=None, role_name=None):  # noqa: E501
        """RoomUserSummary - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._transaction_side_id = None
        self._role_id = None
        self._title_id = None
        self._company_name = None
        self._role_name = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
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
        if title_id is not None:
            self.title_id = title_id
        if company_name is not None:
            self.company_name = company_name
        if role_name is not None:
            self.role_name = role_name

    @property
    def user_id(self):
        """Gets the user_id of this RoomUserSummary.  # noqa: E501


        :return: The user_id of this RoomUserSummary.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RoomUserSummary.


        :param user_id: The user_id of this RoomUserSummary.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def email(self):
        """Gets the email of this RoomUserSummary.  # noqa: E501


        :return: The email of this RoomUserSummary.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RoomUserSummary.


        :param email: The email of this RoomUserSummary.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this RoomUserSummary.  # noqa: E501


        :return: The first_name of this RoomUserSummary.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this RoomUserSummary.


        :param first_name: The first_name of this RoomUserSummary.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this RoomUserSummary.  # noqa: E501


        :return: The last_name of this RoomUserSummary.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this RoomUserSummary.


        :param last_name: The last_name of this RoomUserSummary.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def transaction_side_id(self):
        """Gets the transaction_side_id of this RoomUserSummary.  # noqa: E501


        :return: The transaction_side_id of this RoomUserSummary.  # noqa: E501
        :rtype: str
        """
        return self._transaction_side_id

    @transaction_side_id.setter
    def transaction_side_id(self, transaction_side_id):
        """Sets the transaction_side_id of this RoomUserSummary.


        :param transaction_side_id: The transaction_side_id of this RoomUserSummary.  # noqa: E501
        :type: str
        """

        self._transaction_side_id = transaction_side_id

    @property
    def role_id(self):
        """Gets the role_id of this RoomUserSummary.  # noqa: E501


        :return: The role_id of this RoomUserSummary.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this RoomUserSummary.


        :param role_id: The role_id of this RoomUserSummary.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

    @property
    def title_id(self):
        """Gets the title_id of this RoomUserSummary.  # noqa: E501


        :return: The title_id of this RoomUserSummary.  # noqa: E501
        :rtype: int
        """
        return self._title_id

    @title_id.setter
    def title_id(self, title_id):
        """Sets the title_id of this RoomUserSummary.


        :param title_id: The title_id of this RoomUserSummary.  # noqa: E501
        :type: int
        """

        self._title_id = title_id

    @property
    def company_name(self):
        """Gets the company_name of this RoomUserSummary.  # noqa: E501


        :return: The company_name of this RoomUserSummary.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this RoomUserSummary.


        :param company_name: The company_name of this RoomUserSummary.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def role_name(self):
        """Gets the role_name of this RoomUserSummary.  # noqa: E501


        :return: The role_name of this RoomUserSummary.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this RoomUserSummary.


        :param role_name: The role_name of this RoomUserSummary.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

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
        if issubclass(RoomUserSummary, dict):
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
        if not isinstance(other, RoomUserSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
