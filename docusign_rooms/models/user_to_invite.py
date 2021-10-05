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


class UserToInvite(object):
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
        'role_id': 'int',
        'access_level': 'AccessLevel',
        'default_office_id': 'int',
        'regions': 'list[int]',
        'offices': 'list[int]',
        'e_sign_permission_profile_id': 'str',
        'redirect_url': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'role_id': 'roleId',
        'access_level': 'accessLevel',
        'default_office_id': 'defaultOfficeId',
        'regions': 'regions',
        'offices': 'offices',
        'e_sign_permission_profile_id': 'eSignPermissionProfileId',
        'redirect_url': 'redirectUrl'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """UserToInvite - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_name = None
        self._last_name = None
        self._email = None
        self._role_id = None
        self._access_level = None
        self._default_office_id = None
        self._regions = None
        self._offices = None
        self._e_sign_permission_profile_id = None
        self._redirect_url = None
        self.discriminator = None

        setattr(self, "_{}".format('first_name'), kwargs.get('first_name', None))
        setattr(self, "_{}".format('last_name'), kwargs.get('last_name', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('role_id'), kwargs.get('role_id', None))
        setattr(self, "_{}".format('access_level'), kwargs.get('access_level', None))
        setattr(self, "_{}".format('default_office_id'), kwargs.get('default_office_id', None))
        setattr(self, "_{}".format('regions'), kwargs.get('regions', None))
        setattr(self, "_{}".format('offices'), kwargs.get('offices', None))
        setattr(self, "_{}".format('e_sign_permission_profile_id'), kwargs.get('e_sign_permission_profile_id', None))
        setattr(self, "_{}".format('redirect_url'), kwargs.get('redirect_url', None))

    @property
    def first_name(self):
        """Gets the first_name of this UserToInvite.  # noqa: E501


        :return: The first_name of this UserToInvite.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserToInvite.


        :param first_name: The first_name of this UserToInvite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserToInvite.  # noqa: E501


        :return: The last_name of this UserToInvite.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserToInvite.


        :param last_name: The last_name of this UserToInvite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this UserToInvite.  # noqa: E501


        :return: The email of this UserToInvite.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserToInvite.


        :param email: The email of this UserToInvite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def role_id(self):
        """Gets the role_id of this UserToInvite.  # noqa: E501


        :return: The role_id of this UserToInvite.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this UserToInvite.


        :param role_id: The role_id of this UserToInvite.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def access_level(self):
        """Gets the access_level of this UserToInvite.  # noqa: E501


        :return: The access_level of this UserToInvite.  # noqa: E501
        :rtype: AccessLevel
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this UserToInvite.


        :param access_level: The access_level of this UserToInvite.  # noqa: E501
        :type: AccessLevel
        """
        if self._configuration.client_side_validation and access_level is None:
            raise ValueError("Invalid value for `access_level`, must not be `None`")  # noqa: E501

        self._access_level = access_level

    @property
    def default_office_id(self):
        """Gets the default_office_id of this UserToInvite.  # noqa: E501


        :return: The default_office_id of this UserToInvite.  # noqa: E501
        :rtype: int
        """
        return self._default_office_id

    @default_office_id.setter
    def default_office_id(self, default_office_id):
        """Sets the default_office_id of this UserToInvite.


        :param default_office_id: The default_office_id of this UserToInvite.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and default_office_id is None:
            raise ValueError("Invalid value for `default_office_id`, must not be `None`")  # noqa: E501

        self._default_office_id = default_office_id

    @property
    def regions(self):
        """Gets the regions of this UserToInvite.  # noqa: E501


        :return: The regions of this UserToInvite.  # noqa: E501
        :rtype: list[int]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this UserToInvite.


        :param regions: The regions of this UserToInvite.  # noqa: E501
        :type: list[int]
        """

        self._regions = regions

    @property
    def offices(self):
        """Gets the offices of this UserToInvite.  # noqa: E501


        :return: The offices of this UserToInvite.  # noqa: E501
        :rtype: list[int]
        """
        return self._offices

    @offices.setter
    def offices(self, offices):
        """Sets the offices of this UserToInvite.


        :param offices: The offices of this UserToInvite.  # noqa: E501
        :type: list[int]
        """

        self._offices = offices

    @property
    def e_sign_permission_profile_id(self):
        """Gets the e_sign_permission_profile_id of this UserToInvite.  # noqa: E501


        :return: The e_sign_permission_profile_id of this UserToInvite.  # noqa: E501
        :rtype: str
        """
        return self._e_sign_permission_profile_id

    @e_sign_permission_profile_id.setter
    def e_sign_permission_profile_id(self, e_sign_permission_profile_id):
        """Sets the e_sign_permission_profile_id of this UserToInvite.


        :param e_sign_permission_profile_id: The e_sign_permission_profile_id of this UserToInvite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and e_sign_permission_profile_id is None:
            raise ValueError("Invalid value for `e_sign_permission_profile_id`, must not be `None`")  # noqa: E501

        self._e_sign_permission_profile_id = e_sign_permission_profile_id

    @property
    def redirect_url(self):
        """Gets the redirect_url of this UserToInvite.  # noqa: E501


        :return: The redirect_url of this UserToInvite.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this UserToInvite.


        :param redirect_url: The redirect_url of this UserToInvite.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

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
        if issubclass(UserToInvite, dict):
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
        if not isinstance(other, UserToInvite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserToInvite):
            return True

        return self.to_dict() != other.to_dict()
