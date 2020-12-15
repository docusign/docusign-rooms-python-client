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


class Document(object):
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
        'document_id': 'int',
        'name': 'str',
        'room_id': 'int',
        'owner_id': 'int',
        'size': 'int',
        'folder_id': 'int',
        'created_date': 'datetime',
        'is_signed': 'bool',
        'content_type': 'str',
        'base64_contents': 'str'
    }

    attribute_map = {
        'document_id': 'documentId',
        'name': 'name',
        'room_id': 'roomId',
        'owner_id': 'ownerId',
        'size': 'size',
        'folder_id': 'folderId',
        'created_date': 'createdDate',
        'is_signed': 'isSigned',
        'content_type': 'contentType',
        'base64_contents': 'base64Contents'
    }

    def __init__(self, document_id=None, name=None, room_id=None, owner_id=None, size=None, folder_id=None, created_date=None, is_signed=None, content_type=None, base64_contents=None):  # noqa: E501
        """Document - a model defined in Swagger"""  # noqa: E501

        self._document_id = None
        self._name = None
        self._room_id = None
        self._owner_id = None
        self._size = None
        self._folder_id = None
        self._created_date = None
        self._is_signed = None
        self._content_type = None
        self._base64_contents = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        self.name = name
        if room_id is not None:
            self.room_id = room_id
        if owner_id is not None:
            self.owner_id = owner_id
        if size is not None:
            self.size = size
        if folder_id is not None:
            self.folder_id = folder_id
        if created_date is not None:
            self.created_date = created_date
        if is_signed is not None:
            self.is_signed = is_signed
        if content_type is not None:
            self.content_type = content_type
        self.base64_contents = base64_contents

    @property
    def document_id(self):
        """Gets the document_id of this Document.  # noqa: E501


        :return: The document_id of this Document.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Document.


        :param document_id: The document_id of this Document.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def name(self):
        """Gets the name of this Document.  # noqa: E501


        :return: The name of this Document.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Document.


        :param name: The name of this Document.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def room_id(self):
        """Gets the room_id of this Document.  # noqa: E501


        :return: The room_id of this Document.  # noqa: E501
        :rtype: int
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this Document.


        :param room_id: The room_id of this Document.  # noqa: E501
        :type: int
        """

        self._room_id = room_id

    @property
    def owner_id(self):
        """Gets the owner_id of this Document.  # noqa: E501


        :return: The owner_id of this Document.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Document.


        :param owner_id: The owner_id of this Document.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def size(self):
        """Gets the size of this Document.  # noqa: E501


        :return: The size of this Document.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Document.


        :param size: The size of this Document.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def folder_id(self):
        """Gets the folder_id of this Document.  # noqa: E501


        :return: The folder_id of this Document.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this Document.


        :param folder_id: The folder_id of this Document.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def created_date(self):
        """Gets the created_date of this Document.  # noqa: E501


        :return: The created_date of this Document.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Document.


        :param created_date: The created_date of this Document.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def is_signed(self):
        """Gets the is_signed of this Document.  # noqa: E501


        :return: The is_signed of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._is_signed

    @is_signed.setter
    def is_signed(self, is_signed):
        """Sets the is_signed of this Document.


        :param is_signed: The is_signed of this Document.  # noqa: E501
        :type: bool
        """

        self._is_signed = is_signed

    @property
    def content_type(self):
        """Gets the content_type of this Document.  # noqa: E501


        :return: The content_type of this Document.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Document.


        :param content_type: The content_type of this Document.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def base64_contents(self):
        """Gets the base64_contents of this Document.  # noqa: E501


        :return: The base64_contents of this Document.  # noqa: E501
        :rtype: str
        """
        return self._base64_contents

    @base64_contents.setter
    def base64_contents(self, base64_contents):
        """Sets the base64_contents of this Document.


        :param base64_contents: The base64_contents of this Document.  # noqa: E501
        :type: str
        """
        if base64_contents is None:
            raise ValueError("Invalid value for `base64_contents`, must not be `None`")  # noqa: E501

        self._base64_contents = base64_contents

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
        if issubclass(Document, dict):
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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other