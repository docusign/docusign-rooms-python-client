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


class OfficeForCreate(object):
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
        'name': 'str',
        'region_id': 'int',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'state_id': 'str',
        'postal_code': 'str',
        'country_id': 'str',
        'time_zone_id': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'name': 'name',
        'region_id': 'regionId',
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'state_id': 'stateId',
        'postal_code': 'postalCode',
        'country_id': 'countryId',
        'time_zone_id': 'timeZoneId',
        'phone': 'phone'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """OfficeForCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._region_id = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._state_id = None
        self._postal_code = None
        self._country_id = None
        self._time_zone_id = None
        self._phone = None
        self.discriminator = None

        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('region_id'), kwargs.get('region_id', None))
        setattr(self, "_{}".format('address1'), kwargs.get('address1', None))
        setattr(self, "_{}".format('address2'), kwargs.get('address2', None))
        setattr(self, "_{}".format('city'), kwargs.get('city', None))
        setattr(self, "_{}".format('state_id'), kwargs.get('state_id', None))
        setattr(self, "_{}".format('postal_code'), kwargs.get('postal_code', None))
        setattr(self, "_{}".format('country_id'), kwargs.get('country_id', None))
        setattr(self, "_{}".format('time_zone_id'), kwargs.get('time_zone_id', None))
        setattr(self, "_{}".format('phone'), kwargs.get('phone', None))

    @property
    def name(self):
        """Gets the name of this OfficeForCreate.  # noqa: E501


        :return: The name of this OfficeForCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OfficeForCreate.


        :param name: The name of this OfficeForCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def region_id(self):
        """Gets the region_id of this OfficeForCreate.  # noqa: E501


        :return: The region_id of this OfficeForCreate.  # noqa: E501
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this OfficeForCreate.


        :param region_id: The region_id of this OfficeForCreate.  # noqa: E501
        :type: int
        """

        self._region_id = region_id

    @property
    def address1(self):
        """Gets the address1 of this OfficeForCreate.  # noqa: E501


        :return: The address1 of this OfficeForCreate.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this OfficeForCreate.


        :param address1: The address1 of this OfficeForCreate.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this OfficeForCreate.  # noqa: E501


        :return: The address2 of this OfficeForCreate.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this OfficeForCreate.


        :param address2: The address2 of this OfficeForCreate.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this OfficeForCreate.  # noqa: E501


        :return: The city of this OfficeForCreate.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this OfficeForCreate.


        :param city: The city of this OfficeForCreate.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_id(self):
        """Gets the state_id of this OfficeForCreate.  # noqa: E501


        :return: The state_id of this OfficeForCreate.  # noqa: E501
        :rtype: str
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """Sets the state_id of this OfficeForCreate.


        :param state_id: The state_id of this OfficeForCreate.  # noqa: E501
        :type: str
        """

        self._state_id = state_id

    @property
    def postal_code(self):
        """Gets the postal_code of this OfficeForCreate.  # noqa: E501


        :return: The postal_code of this OfficeForCreate.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this OfficeForCreate.


        :param postal_code: The postal_code of this OfficeForCreate.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country_id(self):
        """Gets the country_id of this OfficeForCreate.  # noqa: E501


        :return: The country_id of this OfficeForCreate.  # noqa: E501
        :rtype: str
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this OfficeForCreate.


        :param country_id: The country_id of this OfficeForCreate.  # noqa: E501
        :type: str
        """

        self._country_id = country_id

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this OfficeForCreate.  # noqa: E501


        :return: The time_zone_id of this OfficeForCreate.  # noqa: E501
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this OfficeForCreate.


        :param time_zone_id: The time_zone_id of this OfficeForCreate.  # noqa: E501
        :type: str
        """

        self._time_zone_id = time_zone_id

    @property
    def phone(self):
        """Gets the phone of this OfficeForCreate.  # noqa: E501


        :return: The phone of this OfficeForCreate.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this OfficeForCreate.


        :param phone: The phone of this OfficeForCreate.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if issubclass(OfficeForCreate, dict):
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
        if not isinstance(other, OfficeForCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OfficeForCreate):
            return True

        return self.to_dict() != other.to_dict()
