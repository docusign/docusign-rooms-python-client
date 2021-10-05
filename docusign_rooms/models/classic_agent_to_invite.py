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


class ClassicAgentToInvite(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'office_id': 'int',
        'company_type_id': 'str',
        'e_sign_permission_profile_id': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'office_id': 'officeId',
        'company_type_id': 'companyTypeId',
        'e_sign_permission_profile_id': 'eSignPermissionProfileId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ClassicAgentToInvite - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_name = None
        self._last_name = None
        self._email = None
        self._office_id = None
        self._company_type_id = None
        self._e_sign_permission_profile_id = None
        self.discriminator = None

        setattr(self, "_{}".format('first_name'), kwargs.get('first_name', None))
        setattr(self, "_{}".format('last_name'), kwargs.get('last_name', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('office_id'), kwargs.get('office_id', None))
        setattr(self, "_{}".format('company_type_id'), kwargs.get('company_type_id', None))
        setattr(self, "_{}".format('e_sign_permission_profile_id'), kwargs.get('e_sign_permission_profile_id', None))

    @property
    def first_name(self):
        """Gets the first_name of this ClassicAgentToInvite.  # noqa: E501


        :return: The first_name of this ClassicAgentToInvite.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ClassicAgentToInvite.


        :param first_name: The first_name of this ClassicAgentToInvite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ClassicAgentToInvite.  # noqa: E501


        :return: The last_name of this ClassicAgentToInvite.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ClassicAgentToInvite.


        :param last_name: The last_name of this ClassicAgentToInvite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this ClassicAgentToInvite.  # noqa: E501


        :return: The email of this ClassicAgentToInvite.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ClassicAgentToInvite.


        :param email: The email of this ClassicAgentToInvite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def office_id(self):
        """Gets the office_id of this ClassicAgentToInvite.  # noqa: E501


        :return: The office_id of this ClassicAgentToInvite.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this ClassicAgentToInvite.


        :param office_id: The office_id of this ClassicAgentToInvite.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and office_id is None:
            raise ValueError("Invalid value for `office_id`, must not be `None`")  # noqa: E501

        self._office_id = office_id

    @property
    def company_type_id(self):
        """Gets the company_type_id of this ClassicAgentToInvite.  # noqa: E501


        :return: The company_type_id of this ClassicAgentToInvite.  # noqa: E501
        :rtype: str
        """
        return self._company_type_id

    @company_type_id.setter
    def company_type_id(self, company_type_id):
        """Sets the company_type_id of this ClassicAgentToInvite.


        :param company_type_id: The company_type_id of this ClassicAgentToInvite.  # noqa: E501
        :type: str
        """

        self._company_type_id = company_type_id

    @property
    def e_sign_permission_profile_id(self):
        """Gets the e_sign_permission_profile_id of this ClassicAgentToInvite.  # noqa: E501

        Required when the company is tightly bound to an eSign account; otherwise ignored.  # noqa: E501

        :return: The e_sign_permission_profile_id of this ClassicAgentToInvite.  # noqa: E501
        :rtype: str
        """
        return self._e_sign_permission_profile_id

    @e_sign_permission_profile_id.setter
    def e_sign_permission_profile_id(self, e_sign_permission_profile_id):
        """Sets the e_sign_permission_profile_id of this ClassicAgentToInvite.

        Required when the company is tightly bound to an eSign account; otherwise ignored.  # noqa: E501

        :param e_sign_permission_profile_id: The e_sign_permission_profile_id of this ClassicAgentToInvite.  # noqa: E501
        :type: str
        """

        self._e_sign_permission_profile_id = e_sign_permission_profile_id

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
        if issubclass(ClassicAgentToInvite, dict):
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
        if not isinstance(other, ClassicAgentToInvite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClassicAgentToInvite):
            return True

        return self.to_dict() != other.to_dict()
