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


class FormGroupSummary(object):
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
        'form_group_id': 'str',
        'name': 'str',
        'form_count': 'int'
    }

    attribute_map = {
        'form_group_id': 'formGroupId',
        'name': 'name',
        'form_count': 'formCount'
    }

    def __init__(self, form_group_id=None, name=None, form_count=None):  # noqa: E501
        """FormGroupSummary - a model defined in Swagger"""  # noqa: E501

        self._form_group_id = None
        self._name = None
        self._form_count = None
        self.discriminator = None

        if form_group_id is not None:
            self.form_group_id = form_group_id
        if name is not None:
            self.name = name
        if form_count is not None:
            self.form_count = form_count

    @property
    def form_group_id(self):
        """Gets the form_group_id of this FormGroupSummary.  # noqa: E501


        :return: The form_group_id of this FormGroupSummary.  # noqa: E501
        :rtype: str
        """
        return self._form_group_id

    @form_group_id.setter
    def form_group_id(self, form_group_id):
        """Sets the form_group_id of this FormGroupSummary.


        :param form_group_id: The form_group_id of this FormGroupSummary.  # noqa: E501
        :type: str
        """

        self._form_group_id = form_group_id

    @property
    def name(self):
        """Gets the name of this FormGroupSummary.  # noqa: E501


        :return: The name of this FormGroupSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormGroupSummary.


        :param name: The name of this FormGroupSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def form_count(self):
        """Gets the form_count of this FormGroupSummary.  # noqa: E501


        :return: The form_count of this FormGroupSummary.  # noqa: E501
        :rtype: int
        """
        return self._form_count

    @form_count.setter
    def form_count(self, form_count):
        """Sets the form_count of this FormGroupSummary.


        :param form_count: The form_count of this FormGroupSummary.  # noqa: E501
        :type: int
        """

        self._form_count = form_count

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
        if issubclass(FormGroupSummary, dict):
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
        if not isinstance(other, FormGroupSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other