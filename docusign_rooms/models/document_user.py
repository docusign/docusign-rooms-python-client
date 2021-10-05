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


class DocumentUser(object):
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
        'document_id': 'int',
        'name': 'str',
        'has_access': 'bool',
        'can_approve_task': 'bool',
        'can_assign_to_task_list': 'bool',
        'can_copy': 'bool',
        'can_delete': 'bool',
        'can_remove_from_task_list': 'bool',
        'can_remove_approval': 'bool',
        'can_rename': 'bool',
        'can_share': 'bool',
        'can_view_activity': 'bool'
    }

    attribute_map = {
        'user_id': 'userId',
        'document_id': 'documentId',
        'name': 'name',
        'has_access': 'hasAccess',
        'can_approve_task': 'canApproveTask',
        'can_assign_to_task_list': 'canAssignToTaskList',
        'can_copy': 'canCopy',
        'can_delete': 'canDelete',
        'can_remove_from_task_list': 'canRemoveFromTaskList',
        'can_remove_approval': 'canRemoveApproval',
        'can_rename': 'canRename',
        'can_share': 'canShare',
        'can_view_activity': 'canViewActivity'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DocumentUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_id = None
        self._document_id = None
        self._name = None
        self._has_access = None
        self._can_approve_task = None
        self._can_assign_to_task_list = None
        self._can_copy = None
        self._can_delete = None
        self._can_remove_from_task_list = None
        self._can_remove_approval = None
        self._can_rename = None
        self._can_share = None
        self._can_view_activity = None
        self.discriminator = None

        setattr(self, "_{}".format('user_id'), kwargs.get('user_id', None))
        setattr(self, "_{}".format('document_id'), kwargs.get('document_id', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('has_access'), kwargs.get('has_access', None))
        setattr(self, "_{}".format('can_approve_task'), kwargs.get('can_approve_task', None))
        setattr(self, "_{}".format('can_assign_to_task_list'), kwargs.get('can_assign_to_task_list', None))
        setattr(self, "_{}".format('can_copy'), kwargs.get('can_copy', None))
        setattr(self, "_{}".format('can_delete'), kwargs.get('can_delete', None))
        setattr(self, "_{}".format('can_remove_from_task_list'), kwargs.get('can_remove_from_task_list', None))
        setattr(self, "_{}".format('can_remove_approval'), kwargs.get('can_remove_approval', None))
        setattr(self, "_{}".format('can_rename'), kwargs.get('can_rename', None))
        setattr(self, "_{}".format('can_share'), kwargs.get('can_share', None))
        setattr(self, "_{}".format('can_view_activity'), kwargs.get('can_view_activity', None))

    @property
    def user_id(self):
        """Gets the user_id of this DocumentUser.  # noqa: E501


        :return: The user_id of this DocumentUser.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DocumentUser.


        :param user_id: The user_id of this DocumentUser.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def document_id(self):
        """Gets the document_id of this DocumentUser.  # noqa: E501


        :return: The document_id of this DocumentUser.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this DocumentUser.


        :param document_id: The document_id of this DocumentUser.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def name(self):
        """Gets the name of this DocumentUser.  # noqa: E501


        :return: The name of this DocumentUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentUser.


        :param name: The name of this DocumentUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def has_access(self):
        """Gets the has_access of this DocumentUser.  # noqa: E501


        :return: The has_access of this DocumentUser.  # noqa: E501
        :rtype: bool
        """
        return self._has_access

    @has_access.setter
    def has_access(self, has_access):
        """Sets the has_access of this DocumentUser.


        :param has_access: The has_access of this DocumentUser.  # noqa: E501
        :type: bool
        """

        self._has_access = has_access

    @property
    def can_approve_task(self):
        """Gets the can_approve_task of this DocumentUser.  # noqa: E501


        :return: The can_approve_task of this DocumentUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_approve_task

    @can_approve_task.setter
    def can_approve_task(self, can_approve_task):
        """Sets the can_approve_task of this DocumentUser.


        :param can_approve_task: The can_approve_task of this DocumentUser.  # noqa: E501
        :type: bool
        """

        self._can_approve_task = can_approve_task

    @property
    def can_assign_to_task_list(self):
        """Gets the can_assign_to_task_list of this DocumentUser.  # noqa: E501


        :return: The can_assign_to_task_list of this DocumentUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_assign_to_task_list

    @can_assign_to_task_list.setter
    def can_assign_to_task_list(self, can_assign_to_task_list):
        """Sets the can_assign_to_task_list of this DocumentUser.


        :param can_assign_to_task_list: The can_assign_to_task_list of this DocumentUser.  # noqa: E501
        :type: bool
        """

        self._can_assign_to_task_list = can_assign_to_task_list

    @property
    def can_copy(self):
        """Gets the can_copy of this DocumentUser.  # noqa: E501


        :return: The can_copy of this DocumentUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_copy

    @can_copy.setter
    def can_copy(self, can_copy):
        """Sets the can_copy of this DocumentUser.


        :param can_copy: The can_copy of this DocumentUser.  # noqa: E501
        :type: bool
        """

        self._can_copy = can_copy

    @property
    def can_delete(self):
        """Gets the can_delete of this DocumentUser.  # noqa: E501


        :return: The can_delete of this DocumentUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this DocumentUser.


        :param can_delete: The can_delete of this DocumentUser.  # noqa: E501
        :type: bool
        """

        self._can_delete = can_delete

    @property
    def can_remove_from_task_list(self):
        """Gets the can_remove_from_task_list of this DocumentUser.  # noqa: E501


        :return: The can_remove_from_task_list of this DocumentUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_remove_from_task_list

    @can_remove_from_task_list.setter
    def can_remove_from_task_list(self, can_remove_from_task_list):
        """Sets the can_remove_from_task_list of this DocumentUser.


        :param can_remove_from_task_list: The can_remove_from_task_list of this DocumentUser.  # noqa: E501
        :type: bool
        """

        self._can_remove_from_task_list = can_remove_from_task_list

    @property
    def can_remove_approval(self):
        """Gets the can_remove_approval of this DocumentUser.  # noqa: E501


        :return: The can_remove_approval of this DocumentUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_remove_approval

    @can_remove_approval.setter
    def can_remove_approval(self, can_remove_approval):
        """Sets the can_remove_approval of this DocumentUser.


        :param can_remove_approval: The can_remove_approval of this DocumentUser.  # noqa: E501
        :type: bool
        """

        self._can_remove_approval = can_remove_approval

    @property
    def can_rename(self):
        """Gets the can_rename of this DocumentUser.  # noqa: E501


        :return: The can_rename of this DocumentUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_rename

    @can_rename.setter
    def can_rename(self, can_rename):
        """Sets the can_rename of this DocumentUser.


        :param can_rename: The can_rename of this DocumentUser.  # noqa: E501
        :type: bool
        """

        self._can_rename = can_rename

    @property
    def can_share(self):
        """Gets the can_share of this DocumentUser.  # noqa: E501


        :return: The can_share of this DocumentUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_share

    @can_share.setter
    def can_share(self, can_share):
        """Sets the can_share of this DocumentUser.


        :param can_share: The can_share of this DocumentUser.  # noqa: E501
        :type: bool
        """

        self._can_share = can_share

    @property
    def can_view_activity(self):
        """Gets the can_view_activity of this DocumentUser.  # noqa: E501


        :return: The can_view_activity of this DocumentUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_view_activity

    @can_view_activity.setter
    def can_view_activity(self, can_view_activity):
        """Sets the can_view_activity of this DocumentUser.


        :param can_view_activity: The can_view_activity of this DocumentUser.  # noqa: E501
        :type: bool
        """

        self._can_view_activity = can_view_activity

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
        if issubclass(DocumentUser, dict):
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
        if not isinstance(other, DocumentUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentUser):
            return True

        return self.to_dict() != other.to_dict()
