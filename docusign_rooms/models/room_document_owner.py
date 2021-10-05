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


class RoomDocumentOwner(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'company_name': 'str',
        'image_src': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'company_name': 'companyName',
        'image_src': 'imageSrc'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RoomDocumentOwner - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_id = None
        self._first_name = None
        self._last_name = None
        self._company_name = None
        self._image_src = None
        self.discriminator = None

        setattr(self, "_{}".format('user_id'), kwargs.get('user_id', None))
        setattr(self, "_{}".format('first_name'), kwargs.get('first_name', None))
        setattr(self, "_{}".format('last_name'), kwargs.get('last_name', None))
        setattr(self, "_{}".format('company_name'), kwargs.get('company_name', None))
        setattr(self, "_{}".format('image_src'), kwargs.get('image_src', None))

    @property
    def user_id(self):
        """Gets the user_id of this RoomDocumentOwner.  # noqa: E501


        :return: The user_id of this RoomDocumentOwner.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RoomDocumentOwner.


        :param user_id: The user_id of this RoomDocumentOwner.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def first_name(self):
        """Gets the first_name of this RoomDocumentOwner.  # noqa: E501


        :return: The first_name of this RoomDocumentOwner.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this RoomDocumentOwner.


        :param first_name: The first_name of this RoomDocumentOwner.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this RoomDocumentOwner.  # noqa: E501


        :return: The last_name of this RoomDocumentOwner.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this RoomDocumentOwner.


        :param last_name: The last_name of this RoomDocumentOwner.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def company_name(self):
        """Gets the company_name of this RoomDocumentOwner.  # noqa: E501


        :return: The company_name of this RoomDocumentOwner.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this RoomDocumentOwner.


        :param company_name: The company_name of this RoomDocumentOwner.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def image_src(self):
        """Gets the image_src of this RoomDocumentOwner.  # noqa: E501


        :return: The image_src of this RoomDocumentOwner.  # noqa: E501
        :rtype: str
        """
        return self._image_src

    @image_src.setter
    def image_src(self, image_src):
        """Sets the image_src of this RoomDocumentOwner.


        :param image_src: The image_src of this RoomDocumentOwner.  # noqa: E501
        :type: str
        """

        self._image_src = image_src

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
        if issubclass(RoomDocumentOwner, dict):
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
        if not isinstance(other, RoomDocumentOwner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoomDocumentOwner):
            return True

        return self.to_dict() != other.to_dict()
