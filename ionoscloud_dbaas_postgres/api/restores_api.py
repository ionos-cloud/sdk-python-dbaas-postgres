from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dbaas_postgres.api_client import ApiClient
from ionoscloud_dbaas_postgres.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RestoresApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cluster_restore_post(self, cluster_id, create_restore_request, **kwargs):  # noqa: E501
        """In-place restore of a cluster  # noqa: E501

        Triggers an in-place restore of the given PostgreSQL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cluster_restore_post(cluster_id, create_restore_request, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param create_restore_request: The restore request to create. (required)
        :type create_restore_request: CreateRestoreRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.cluster_restore_post_with_http_info(cluster_id, create_restore_request, **kwargs)  # noqa: E501

    def cluster_restore_post_with_http_info(self, cluster_id, create_restore_request, **kwargs):  # noqa: E501
        """In-place restore of a cluster  # noqa: E501

        Triggers an in-place restore of the given PostgreSQL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cluster_restore_post_with_http_info(cluster_id, create_restore_request, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param create_restore_request: The restore request to create. (required)
        :type create_restore_request: CreateRestoreRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'create_restore_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cluster_restore_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `cluster_restore_post`")  # noqa: E501
        # verify the required parameter 'create_restore_request' is set
        if self.api_client.client_side_validation and ('create_restore_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_restore_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_restore_request` when calling `cluster_restore_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_restore_request' in local_var_params:
            body_params = local_var_params['create_restore_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/restore', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
