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


class OfficesApi(object):
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

    def create_office(self, account_id, **kwargs):
        """
        Create an office.
        Create an office.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_office(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :param OfficeForCreate body: Creates an office with given name and other details like Region,Address
        :return: Office
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_office_with_http_info(account_id, **kwargs)
        else:
            (data) = self.create_office_with_http_info(account_id, **kwargs)
            return data

    def create_office_with_http_info(self, account_id, **kwargs):
        """
        Create an office.
        Create an office.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_office_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :param OfficeForCreate body: Creates an office with given name and other details like Region,Address
        :return: Office
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
                    " to method create_office" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_office`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/offices'.replace('{format}', 'json')
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
                                        response_type='Office',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_office(self, office_id, account_id, **kwargs):
        """
        Delete an office.
        This method deletes an office from a Rooms account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_office(office_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int office_id: Office ID to be deleted (required)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_office_with_http_info(office_id, account_id, **kwargs)
        else:
            (data) = self.delete_office_with_http_info(office_id, account_id, **kwargs)
            return data

    def delete_office_with_http_info(self, office_id, account_id, **kwargs):
        """
        Delete an office.
        This method deletes an office from a Rooms account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_office_with_http_info(office_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int office_id: Office ID to be deleted (required)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office_id', 'account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_office" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office_id' is set
        if ('office_id' not in params) or (params['office_id'] is None):
            raise ValueError("Missing the required parameter `office_id` when calling `delete_office`")
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_office`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/offices/{officeId}'.replace('{format}', 'json')
        path_params = {}
        if 'office_id' in params:
            path_params['officeId'] = params['office_id']
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])

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

    def get_office(self, office_id, account_id, **kwargs):
        """
        Get information about the office with the given officeId.
        Get information about the office with the given officeId.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_office(office_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int office_id: The id of the office. (required)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :return: Office
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_office_with_http_info(office_id, account_id, **kwargs)
        else:
            (data) = self.get_office_with_http_info(office_id, account_id, **kwargs)
            return data

    def get_office_with_http_info(self, office_id, account_id, **kwargs):
        """
        Get information about the office with the given officeId.
        Get information about the office with the given officeId.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_office_with_http_info(office_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int office_id: The id of the office. (required)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :return: Office
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office_id', 'account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_office" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office_id' is set
        if ('office_id' not in params) or (params['office_id'] is None):
            raise ValueError("Missing the required parameter `office_id` when calling `get_office`")
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_office`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/offices/{officeId}'.replace('{format}', 'json')
        path_params = {}
        if 'office_id' in params:
            path_params['officeId'] = params['office_id']
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Office',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_offices(self, account_id, **kwargs):
        """
        Get all offices.
        This method returns a list of offices associated with an account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_offices(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :param int count: Number of offices to include in the response, (Default 100)
        :param int start_position: Position in the overall list of offices to begin results.
        :param bool only_accessible: When true, the response only includes offices accessible to the calling user.
        :param str search: When specified, the response only includes offices whose names includes the specified search string.
        :return: OfficeSummaryList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_offices_with_http_info(account_id, **kwargs)
        else:
            (data) = self.get_offices_with_http_info(account_id, **kwargs)
            return data

    def get_offices_with_http_info(self, account_id, **kwargs):
        """
        Get all offices.
        This method returns a list of offices associated with an account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_offices_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :param int count: Number of offices to include in the response, (Default 100)
        :param int start_position: Position in the overall list of offices to begin results.
        :param bool only_accessible: When true, the response only includes offices accessible to the calling user.
        :param str search: When specified, the response only includes offices whose names includes the specified search string.
        :return: OfficeSummaryList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'count', 'start_position', 'only_accessible', 'search']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_offices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_offices`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/offices'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}
        if 'count' in params:
            query_params['count'] = params['count']
        if 'start_position' in params:
            query_params['startPosition'] = params['start_position']
        if 'only_accessible' in params:
            query_params['onlyAccessible'] = params['only_accessible']
        if 'search' in params:
            query_params['search'] = params['search']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OfficeSummaryList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_reference_counts(self, office_id, account_id, **kwargs):
        """
        Lists the number of objects of each type that reference the office.
        This method returns a list of each type of object and the number of objects of that type referencing the specified office. Note that an office cannot be deleted while existing objects reference it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_reference_counts(office_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int office_id: ID of the office (required)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :return: OfficeReferenceCountList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_reference_counts_with_http_info(office_id, account_id, **kwargs)
        else:
            (data) = self.get_reference_counts_with_http_info(office_id, account_id, **kwargs)
            return data

    def get_reference_counts_with_http_info(self, office_id, account_id, **kwargs):
        """
        Lists the number of objects of each type that reference the office.
        This method returns a list of each type of object and the number of objects of that type referencing the specified office. Note that an office cannot be deleted while existing objects reference it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_reference_counts_with_http_info(office_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int office_id: ID of the office (required)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :return: OfficeReferenceCountList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office_id', 'account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_reference_counts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office_id' is set
        if ('office_id' not in params) or (params['office_id'] is None):
            raise ValueError("Missing the required parameter `office_id` when calling `get_reference_counts`")
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_reference_counts`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/offices/{officeId}/reference_counts'.replace('{format}', 'json')
        path_params = {}
        if 'office_id' in params:
            path_params['officeId'] = params['office_id']
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OfficeReferenceCountList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
