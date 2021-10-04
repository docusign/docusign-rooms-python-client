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


class ClassicManagerToInvite(object):
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
        'default_office_id': 'int',
        'title_id': 'int',
        'access_level': 'AccessLevel',
        'permissions': 'ClassicManagerPermissions',
        'offices': 'list[int]',
        'regions': 'list[int]',
        'e_sign_permission_profile_id': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'default_office_id': 'defaultOfficeId',
        'title_id': 'titleId',
        'access_level': 'accessLevel',
        'permissions': 'permissions',
        'offices': 'offices',
        'regions': 'regions',
        'e_sign_permission_profile_id': 'eSignPermissionProfileId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ClassicManagerToInvite - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_name = None
        self._last_name = None
        self._email = None
        self._default_office_id = None
        self._title_id = None
        self._access_level = None
        self._permissions = None
        self._offices = None
        self._regions = None
        self._e_sign_permission_profile_id = None
        self.discriminator = None

        setattr(self, "_{}".format('first_name'), kwargs.get('first_name', None))
        setattr(self, "_{}".format('last_name'), kwargs.get('last_name', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('default_office_id'), kwargs.get('default_office_id', None))
        setattr(self, "_{}".format('title_id'), kwargs.get('title_id', None))
        setattr(self, "_{}".format('access_level'), kwargs.get('access_level', None))
        setattr(self, "_{}".format('permissions'), kwargs.get('permissions', None))
        setattr(self, "_{}".format('offices'), kwargs.get('offices', None))
        setattr(self, "_{}".format('regions'), kwargs.get('regions', None))
        setattr(self, "_{}".format('e_sign_permission_profile_id'), kwargs.get('e_sign_permission_profile_id', None))

    @property
    def first_name(self):
        """Gets the first_name of this ClassicManagerToInvite.  # noqa: E501


        :return: The first_name of this ClassicManagerToInvite.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ClassicManagerToInvite.


        :param first_name: The first_name of this ClassicManagerToInvite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ClassicManagerToInvite.  # noqa: E501


        :return: The last_name of this ClassicManagerToInvite.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ClassicManagerToInvite.


        :param last_name: The last_name of this ClassicManagerToInvite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this ClassicManagerToInvite.  # noqa: E501


        :return: The email of this ClassicManagerToInvite.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ClassicManagerToInvite.


        :param email: The email of this ClassicManagerToInvite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def default_office_id(self):
        """Gets the default_office_id of this ClassicManagerToInvite.  # noqa: E501


        :return: The default_office_id of this ClassicManagerToInvite.  # noqa: E501
        :rtype: int
        """
        return self._default_office_id

    @default_office_id.setter
    def default_office_id(self, default_office_id):
        """Sets the default_office_id of this ClassicManagerToInvite.


        :param default_office_id: The default_office_id of this ClassicManagerToInvite.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and default_office_id is None:
            raise ValueError("Invalid value for `default_office_id`, must not be `None`")  # noqa: E501

        self._default_office_id = default_office_id

    @property
    def title_id(self):
        """Gets the title_id of this ClassicManagerToInvite.  # noqa: E501


        :return: The title_id of this ClassicManagerToInvite.  # noqa: E501
        :rtype: int
        """
        return self._title_id

    @title_id.setter
    def title_id(self, title_id):
        """Sets the title_id of this ClassicManagerToInvite.


        :param title_id: The title_id of this ClassicManagerToInvite.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and title_id is None:
            raise ValueError("Invalid value for `title_id`, must not be `None`")  # noqa: E501

        self._title_id = title_id

    @property
    def access_level(self):
        """Gets the access_level of this ClassicManagerToInvite.  # noqa: E501


        :return: The access_level of this ClassicManagerToInvite.  # noqa: E501
        :rtype: AccessLevel
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this ClassicManagerToInvite.


        :param access_level: The access_level of this ClassicManagerToInvite.  # noqa: E501
        :type: AccessLevel
        """
        if self._configuration.client_side_validation and access_level is None:
            raise ValueError("Invalid value for `access_level`, must not be `None`")  # noqa: E501

        self._access_level = access_level

    @property
    def permissions(self):
        """Gets the permissions of this ClassicManagerToInvite.  # noqa: E501


        :return: The permissions of this ClassicManagerToInvite.  # noqa: E501
        :rtype: ClassicManagerPermissions
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ClassicManagerToInvite.


        :param permissions: The permissions of this ClassicManagerToInvite.  # noqa: E501
        :type: ClassicManagerPermissions
        """
        if self._configuration.client_side_validation and permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def offices(self):
        """Gets the offices of this ClassicManagerToInvite.  # noqa: E501


        :return: The offices of this ClassicManagerToInvite.  # noqa: E501
        :rtype: list[int]
        """
        return self._offices

    @offices.setter
    def offices(self, offices):
        """Sets the offices of this ClassicManagerToInvite.


        :param offices: The offices of this ClassicManagerToInvite.  # noqa: E501
        :type: list[int]
        """

        self._offices = offices

    @property
    def regions(self):
        """Gets the regions of this ClassicManagerToInvite.  # noqa: E501


        :return: The regions of this ClassicManagerToInvite.  # noqa: E501
        :rtype: list[int]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ClassicManagerToInvite.


        :param regions: The regions of this ClassicManagerToInvite.  # noqa: E501
        :type: list[int]
        """

        self._regions = regions

    @property
    def e_sign_permission_profile_id(self):
        """Gets the e_sign_permission_profile_id of this ClassicManagerToInvite.  # noqa: E501

        Required when the company is tightly bound to an eSign account; otherwise ignored.  # noqa: E501

        :return: The e_sign_permission_profile_id of this ClassicManagerToInvite.  # noqa: E501
        :rtype: str
        """
        return self._e_sign_permission_profile_id

    @e_sign_permission_profile_id.setter
    def e_sign_permission_profile_id(self, e_sign_permission_profile_id):
        """Sets the e_sign_permission_profile_id of this ClassicManagerToInvite.

        Required when the company is tightly bound to an eSign account; otherwise ignored.  # noqa: E501

        :param e_sign_permission_profile_id: The e_sign_permission_profile_id of this ClassicManagerToInvite.  # noqa: E501
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
        if issubclass(ClassicManagerToInvite, dict):
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
        if not isinstance(other, ClassicManagerToInvite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClassicManagerToInvite):
            return True

        return self.to_dict() != other.to_dict()
