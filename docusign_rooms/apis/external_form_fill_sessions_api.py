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


class ExternalFormFillSessionsApi(object):
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

    def create_external_form_fill_session(self, account_id, **kwargs):
        """
        Creates an external form fill session.
        Returns a URL for a new external form fill session, based on the `roomId` and `formId` or `formIds` that you specify in the `formFillSessionForCreate` request body.  User may supply up to 10 `formIds`. Eventually, `formId` will be deprecated.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_external_form_fill_session(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :param ExternalFormFillSessionForCreate body: Request body that accepts the `roomId` and `formId` or `formIds` that you specify in the `formFillSessionForCreate` request body. User may supply up to 10 `formIds`. Eventually, `formId` will be deprecated
        :return: ExternalFormFillSession
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_external_form_fill_session_with_http_info(account_id, **kwargs)
        else:
            (data) = self.create_external_form_fill_session_with_http_info(account_id, **kwargs)
            return data

    def create_external_form_fill_session_with_http_info(self, account_id, **kwargs):
        """
        Creates an external form fill session.
        Returns a URL for a new external form fill session, based on the `roomId` and `formId` or `formIds` that you specify in the `formFillSessionForCreate` request body.  User may supply up to 10 `formIds`. Eventually, `formId` will be deprecated.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_external_form_fill_session_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :param ExternalFormFillSessionForCreate body: Request body that accepts the `roomId` and `formId` or `formIds` that you specify in the `formFillSessionForCreate` request body. User may supply up to 10 `formIds`. Eventually, `formId` will be deprecated
        :return: ExternalFormFillSession
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_external_form_fill_session" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_external_form_fill_session`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/external_form_fill_sessions'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json-patch+json', 'application/json', 'text/json', 'application/*+json', 'application/xml', 'text/xml', 'application/*+xml'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ExternalFormFillSession',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
