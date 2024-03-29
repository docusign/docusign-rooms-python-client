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


class ExternalFormFillSessionForCreate(object):
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
        'form_id': 'str',
        'room_id': 'int',
        'form_ids': 'list[str]',
        'x_frame_allowed_url': 'str'
    }

    attribute_map = {
        'form_id': 'formId',
        'room_id': 'roomId',
        'form_ids': 'formIds',
        'x_frame_allowed_url': 'xFrameAllowedUrl'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ExternalFormFillSessionForCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._form_id = None
        self._room_id = None
        self._form_ids = None
        self._x_frame_allowed_url = None
        self.discriminator = None

        setattr(self, "_{}".format('form_id'), kwargs.get('form_id', None))
        setattr(self, "_{}".format('room_id'), kwargs.get('room_id', None))
        setattr(self, "_{}".format('form_ids'), kwargs.get('form_ids', None))
        setattr(self, "_{}".format('x_frame_allowed_url'), kwargs.get('x_frame_allowed_url', None))

    @property
    def form_id(self):
        """Gets the form_id of this ExternalFormFillSessionForCreate.  # noqa: E501


        :return: The form_id of this ExternalFormFillSessionForCreate.  # noqa: E501
        :rtype: str
        """
        return self._form_id

    @form_id.setter
    def form_id(self, form_id):
        """Sets the form_id of this ExternalFormFillSessionForCreate.


        :param form_id: The form_id of this ExternalFormFillSessionForCreate.  # noqa: E501
        :type: str
        """

        self._form_id = form_id

    @property
    def room_id(self):
        """Gets the room_id of this ExternalFormFillSessionForCreate.  # noqa: E501


        :return: The room_id of this ExternalFormFillSessionForCreate.  # noqa: E501
        :rtype: int
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ExternalFormFillSessionForCreate.


        :param room_id: The room_id of this ExternalFormFillSessionForCreate.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and room_id is None:
            raise ValueError("Invalid value for `room_id`, must not be `None`")  # noqa: E501

        self._room_id = room_id

    @property
    def form_ids(self):
        """Gets the form_ids of this ExternalFormFillSessionForCreate.  # noqa: E501


        :return: The form_ids of this ExternalFormFillSessionForCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._form_ids

    @form_ids.setter
    def form_ids(self, form_ids):
        """Sets the form_ids of this ExternalFormFillSessionForCreate.


        :param form_ids: The form_ids of this ExternalFormFillSessionForCreate.  # noqa: E501
        :type: list[str]
        """

        self._form_ids = form_ids

    @property
    def x_frame_allowed_url(self):
        """Gets the x_frame_allowed_url of this ExternalFormFillSessionForCreate.  # noqa: E501


        :return: The x_frame_allowed_url of this ExternalFormFillSessionForCreate.  # noqa: E501
        :rtype: str
        """
        return self._x_frame_allowed_url

    @x_frame_allowed_url.setter
    def x_frame_allowed_url(self, x_frame_allowed_url):
        """Sets the x_frame_allowed_url of this ExternalFormFillSessionForCreate.


        :param x_frame_allowed_url: The x_frame_allowed_url of this ExternalFormFillSessionForCreate.  # noqa: E501
        :type: str
        """

        self._x_frame_allowed_url = x_frame_allowed_url

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
        if issubclass(ExternalFormFillSessionForCreate, dict):
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
        if not isinstance(other, ExternalFormFillSessionForCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalFormFillSessionForCreate):
            return True

        return self.to_dict() != other.to_dict()
