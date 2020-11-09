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


class Field(object):
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
        'field_id': 'str',
        'field_definition_id': 'str',
        'title': 'str',
        'api_name': 'str',
        'type': 'str',
        'fields': 'list[Field]',
        'configuration': 'FieldConfiguration',
        'custom_data': 'CustomData'
    }

    attribute_map = {
        'field_id': 'fieldId',
        'field_definition_id': 'fieldDefinitionId',
        'title': 'title',
        'api_name': 'apiName',
        'type': 'type',
        'fields': 'fields',
        'configuration': 'configuration',
        'custom_data': 'customData'
    }

    def __init__(self, field_id=None, field_definition_id=None, title=None, api_name=None, type=None, fields=None, configuration=None, custom_data=None):  # noqa: E501
        """Field - a model defined in Swagger"""  # noqa: E501

        self._field_id = None
        self._field_definition_id = None
        self._title = None
        self._api_name = None
        self._type = None
        self._fields = None
        self._configuration = None
        self._custom_data = None
        self.discriminator = None

        if field_id is not None:
            self.field_id = field_id
        if field_definition_id is not None:
            self.field_definition_id = field_definition_id
        if title is not None:
            self.title = title
        if api_name is not None:
            self.api_name = api_name
        if type is not None:
            self.type = type
        if fields is not None:
            self.fields = fields
        if configuration is not None:
            self.configuration = configuration
        if custom_data is not None:
            self.custom_data = custom_data

    @property
    def field_id(self):
        """Gets the field_id of this Field.  # noqa: E501


        :return: The field_id of this Field.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this Field.


        :param field_id: The field_id of this Field.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def field_definition_id(self):
        """Gets the field_definition_id of this Field.  # noqa: E501


        :return: The field_definition_id of this Field.  # noqa: E501
        :rtype: str
        """
        return self._field_definition_id

    @field_definition_id.setter
    def field_definition_id(self, field_definition_id):
        """Sets the field_definition_id of this Field.


        :param field_definition_id: The field_definition_id of this Field.  # noqa: E501
        :type: str
        """

        self._field_definition_id = field_definition_id

    @property
    def title(self):
        """Gets the title of this Field.  # noqa: E501


        :return: The title of this Field.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Field.


        :param title: The title of this Field.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def api_name(self):
        """Gets the api_name of this Field.  # noqa: E501


        :return: The api_name of this Field.  # noqa: E501
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this Field.


        :param api_name: The api_name of this Field.  # noqa: E501
        :type: str
        """

        self._api_name = api_name

    @property
    def type(self):
        """Gets the type of this Field.  # noqa: E501


        :return: The type of this Field.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Field.


        :param type: The type of this Field.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def fields(self):
        """Gets the fields of this Field.  # noqa: E501


        :return: The fields of this Field.  # noqa: E501
        :rtype: list[Field]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Field.


        :param fields: The fields of this Field.  # noqa: E501
        :type: list[Field]
        """

        self._fields = fields

    @property
    def configuration(self):
        """Gets the configuration of this Field.  # noqa: E501


        :return: The configuration of this Field.  # noqa: E501
        :rtype: FieldConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this Field.


        :param configuration: The configuration of this Field.  # noqa: E501
        :type: FieldConfiguration
        """

        self._configuration = configuration

    @property
    def custom_data(self):
        """Gets the custom_data of this Field.  # noqa: E501


        :return: The custom_data of this Field.  # noqa: E501
        :rtype: CustomData
        """
        return self._custom_data

    @custom_data.setter
    def custom_data(self, custom_data):
        """Sets the custom_data of this Field.


        :param custom_data: The custom_data of this Field.  # noqa: E501
        :type: CustomData
        """

        self._custom_data = custom_data

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
        if issubclass(Field, dict):
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
        if not isinstance(other, Field):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
