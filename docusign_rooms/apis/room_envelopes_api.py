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


class RoomEnvelopesApi(object):
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

    def create_room_envelope(self, room_id, account_id, **kwargs):
        """
        Creates an envelope with given documents. Returns the eSign envelope ID created
        Creates an envelope with given documents. Returns the eSign envelope ID created
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_room_envelope(room_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int room_id: Room ID (required)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :param EnvelopeForCreate body: Envelope Name and list of document IDs
        :return: Envelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_room_envelope_with_http_info(room_id, account_id, **kwargs)
        else:
            (data) = self.create_room_envelope_with_http_info(room_id, account_id, **kwargs)
            return data

    def create_room_envelope_with_http_info(self, room_id, account_id, **kwargs):
        """
        Creates an envelope with given documents. Returns the eSign envelope ID created
        Creates an envelope with given documents. Returns the eSign envelope ID created
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_room_envelope_with_http_info(room_id, account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int room_id: Room ID (required)
        :param str account_id: (Required) The globally unique identifier (GUID) for the account. (required)
        :param EnvelopeForCreate body: Envelope Name and list of document IDs
        :return: Envelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id', 'account_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_room_envelope" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if ('room_id' not in params) or (params['room_id'] is None):
            raise ValueError("Missing the required parameter `room_id` when calling `create_room_envelope`")
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_room_envelope`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/rooms/{roomId}/envelopes'.replace('{format}', 'json')
        path_params = {}
        if 'room_id' in params:
            path_params['roomId'] = params['room_id']
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
                                        response_type='Envelope',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
