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


class DocumentsApi(object):
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

    def create_document_user(self, document_id, account_id, **kwargs):
        """
        Grants access to a document for a user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_document_user(document_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int document_id:  (required)
        :param str account_id: (required)
        :param DocumentUserForCreate body:
        :return: DocumentUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_document_user_with_http_info(document_id, account_id, **kwargs)
        else:
            (data) = self.create_document_user_with_http_info(document_id, account_id, **kwargs)
            return data

    def create_document_user_with_http_info(self, document_id, account_id, **kwargs):
        """
        Grants access to a document for a user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_document_user_with_http_info(document_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int document_id:  (required)
        :param str account_id: (required)
        :param DocumentUserForCreate body:
        :return: DocumentUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id', 'account_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_document_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `create_document_user`")
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_document_user`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/documents/{documentId}/users'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
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
            select_header_accept(['text/plain', 'application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DocumentUser',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_document(self, document_id, account_id, **kwargs):
        """
        Deletes a document.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_document(document_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int document_id:  (required)
        :param str account_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_document_with_http_info(document_id, account_id, **kwargs)
        else:
            (data) = self.delete_document_with_http_info(document_id, account_id, **kwargs)
            return data

    def delete_document_with_http_info(self, document_id, account_id, **kwargs):
        """
        Deletes a document.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_document_with_http_info(document_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int document_id:  (required)
        :param str account_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id', 'account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `delete_document`")
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_document`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_document(self, document_id, account_id, **kwargs):
        """
        Get information about the Document with the given DocumentId.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_document(document_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int document_id:  (required)
        :param str account_id: (required)
        :param bool include_contents: 
        :return: Document
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_document_with_http_info(document_id, account_id, **kwargs)
        else:
            (data) = self.get_document_with_http_info(document_id, account_id, **kwargs)
            return data

    def get_document_with_http_info(self, document_id, account_id, **kwargs):
        """
        Get information about the Document with the given DocumentId.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_document_with_http_info(document_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int document_id:  (required)
        :param str account_id: (required)
        :param bool include_contents: 
        :return: Document
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id', 'account_id', 'include_contents']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_document`")
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_document`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}
        if 'include_contents' in params:
            query_params['includeContents'] = params['include_contents']

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
                                        response_type='Document',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
