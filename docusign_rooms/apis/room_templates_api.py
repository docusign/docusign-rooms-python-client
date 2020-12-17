# coding: utf-8

"""
    DocuSign Rooms API - v2

    An API for an integrator to access the features of DocuSign Rooms  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..client.configuration import Configuration
from ..client.api_client import ApiClient


class RoomTemplatesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_room_templates(self, account_id, **kwargs):
        """
        Returns all room templates that the active user has access to
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_room_templates(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: (required)
        :param int office_id: Get all room templates you have access to for this office. Response includes Company and Region level  If onlyAssignable is true, and no officeId is provided, user's default office is assumed.
        :param bool only_assignable: Get list of templates you have access to. Default value false.
        :param bool only_enabled: When set to true, only returns room templates that are not disabled.
        :param int count: Number of room templates to return. Defaults to the maximum which is 100.
        :param int start_position: Position of the first item in the total results. Defaults to 0.
        :return: RoomTemplatesSummaryList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_room_templates_with_http_info(account_id, **kwargs)
        else:
            (data) = self.get_room_templates_with_http_info(account_id, **kwargs)
            return data

    def get_room_templates_with_http_info(self, account_id, **kwargs):
        """
        Returns all room templates that the active user has access to
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_room_templates_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: (required)
        :param int office_id: Get all room templates you have access to for this office. Response includes Company and Region level  If onlyAssignable is true, and no officeId is provided, user's default office is assumed.
        :param bool only_assignable: Get list of templates you have access to. Default value false.
        :param bool only_enabled: When set to true, only returns room templates that are not disabled.
        :param int count: Number of room templates to return. Defaults to the maximum which is 100.
        :param int start_position: Position of the first item in the total results. Defaults to 0.
        :return: RoomTemplatesSummaryList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'office_id', 'only_assignable', 'only_enabled', 'count', 'start_position']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_room_templates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_room_templates`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/room_templates'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}
        if 'office_id' in params:
            query_params['officeId'] = params['office_id']
        if 'only_assignable' in params:
            query_params['onlyAssignable'] = params['only_assignable']
        if 'only_enabled' in params:
            query_params['onlyEnabled'] = params['only_enabled']
        if 'count' in params:
            query_params['count'] = params['count']
        if 'start_position' in params:
            query_params['startPosition'] = params['start_position']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RoomTemplatesSummaryList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
