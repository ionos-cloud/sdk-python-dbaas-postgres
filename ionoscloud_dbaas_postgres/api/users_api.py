from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dbaas_postgres.api_client import ApiClient
from ionoscloud_dbaas_postgres.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UsersApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def users_delete(self, cluster_id, username, **kwargs):  # noqa: E501
        """Delete user  # noqa: E501

        Deletes a single user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.users_delete(cluster_id, username, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param username: The authentication username. (required)
        :type username: str
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
        return self.users_delete_with_http_info(cluster_id, username, **kwargs)  # noqa: E501

    def users_delete_with_http_info(self, cluster_id, username, **kwargs):  # noqa: E501
        """Delete user  # noqa: E501

        Deletes a single user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.users_delete_with_http_info(cluster_id, username, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param username: The authentication username. (required)
        :type username: str
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
            'username'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `users_delete`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in local_var_params or  # noqa: E501
                                                        local_var_params['username'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `username` when calling `users_delete`")  # noqa: E501

        if self.api_client.client_side_validation and ('username' in local_var_params and  # noqa: E501
                                                        len(local_var_params['username']) > 63):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `username` when calling `users_delete`, length must be less than or equal to `63`")  # noqa: E501
        if self.api_client.client_side_validation and ('username' in local_var_params and  # noqa: E501
                                                        len(local_var_params['username']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `username` when calling `users_delete`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/users/{username}', 'DELETE',
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

    def users_get(self, cluster_id, username, **kwargs):  # noqa: E501
        """Get user  # noqa: E501

        Retrieves a single user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.users_get(cluster_id, username, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param username: The authentication username. (required)
        :type username: str
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
        :rtype: UserResource
        """
        kwargs['_return_http_data_only'] = True
        return self.users_get_with_http_info(cluster_id, username, **kwargs)  # noqa: E501

    def users_get_with_http_info(self, cluster_id, username, **kwargs):  # noqa: E501
        """Get user  # noqa: E501

        Retrieves a single user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.users_get_with_http_info(cluster_id, username, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param username: The authentication username. (required)
        :type username: str
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
        :rtype: tuple(UserResource, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'username'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `users_get`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in local_var_params or  # noqa: E501
                                                        local_var_params['username'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `username` when calling `users_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('username' in local_var_params and  # noqa: E501
                                                        len(local_var_params['username']) > 63):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `username` when calling `users_get`, length must be less than or equal to `63`")  # noqa: E501
        if self.api_client.client_side_validation and ('username' in local_var_params and  # noqa: E501
                                                        len(local_var_params['username']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `username` when calling `users_get`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'UserResource'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/users/{username}', 'GET',
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

    def users_list(self, cluster_id, **kwargs):  # noqa: E501
        """List users  # noqa: E501

        Retrieves a list of users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.users_list(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param limit: The maximum number of elements to return. Use together with 'offset' for pagination.
        :type limit: int
        :param offset: The first element to return. Use together with 'limit' for pagination.
        :type offset: int
        :param system: If set to 'true' all users, including system users are returned. System users cannot be deleted or updated.
        :type system: bool
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
        :rtype: UserList
        """
        kwargs['_return_http_data_only'] = True
        return self.users_list_with_http_info(cluster_id, **kwargs)  # noqa: E501

    def users_list_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """List users  # noqa: E501

        Retrieves a list of users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.users_list_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param limit: The maximum number of elements to return. Use together with 'offset' for pagination.
        :type limit: int
        :param offset: The first element to return. Use together with 'limit' for pagination.
        :type offset: int
        :param system: If set to 'true' all users, including system users are returned. System users cannot be deleted or updated.
        :type system: bool
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
        :rtype: tuple(UserList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'limit',
            'offset',
            'system'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_list" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `users_list`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `users_list`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `users_list`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'system' in local_var_params and local_var_params['system'] is not None:  # noqa: E501
            query_params.append(('system', local_var_params['system']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'UserList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/users', 'GET',
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

    def users_patch(self, cluster_id, username, users_patch_request, **kwargs):  # noqa: E501
        """Patch user  # noqa: E501

        Patches a single user. Only changing the password is supported. System users cannot be patched.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.users_patch(cluster_id, username, users_patch_request, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param username: The authentication username. (required)
        :type username: str
        :param users_patch_request: Patch containing all properties that should be updated (required)
        :type users_patch_request: UsersPatchRequest
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
        :rtype: UserResource
        """
        kwargs['_return_http_data_only'] = True
        return self.users_patch_with_http_info(cluster_id, username, users_patch_request, **kwargs)  # noqa: E501

    def users_patch_with_http_info(self, cluster_id, username, users_patch_request, **kwargs):  # noqa: E501
        """Patch user  # noqa: E501

        Patches a single user. Only changing the password is supported. System users cannot be patched.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.users_patch_with_http_info(cluster_id, username, users_patch_request, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param username: The authentication username. (required)
        :type username: str
        :param users_patch_request: Patch containing all properties that should be updated (required)
        :type users_patch_request: UsersPatchRequest
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
        :rtype: tuple(UserResource, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'username',
            'users_patch_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `users_patch`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in local_var_params or  # noqa: E501
                                                        local_var_params['username'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `username` when calling `users_patch`")  # noqa: E501
        # verify the required parameter 'users_patch_request' is set
        if self.api_client.client_side_validation and ('users_patch_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['users_patch_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `users_patch_request` when calling `users_patch`")  # noqa: E501

        if self.api_client.client_side_validation and ('username' in local_var_params and  # noqa: E501
                                                        len(local_var_params['username']) > 63):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `username` when calling `users_patch`, length must be less than or equal to `63`")  # noqa: E501
        if self.api_client.client_side_validation and ('username' in local_var_params and  # noqa: E501
                                                        len(local_var_params['username']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `username` when calling `users_patch`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'users_patch_request' in local_var_params:
            body_params = local_var_params['users_patch_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'UserResource'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/users/{username}', 'PATCH',
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

    def users_post(self, cluster_id, user, **kwargs):  # noqa: E501
        """Create a user  # noqa: E501

        Create a new Postgres User  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.users_post(cluster_id, user, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param user: (required)
        :type user: User
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
        :rtype: UserResource
        """
        kwargs['_return_http_data_only'] = True
        return self.users_post_with_http_info(cluster_id, user, **kwargs)  # noqa: E501

    def users_post_with_http_info(self, cluster_id, user, **kwargs):  # noqa: E501
        """Create a user  # noqa: E501

        Create a new Postgres User  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.users_post_with_http_info(cluster_id, user, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param user: (required)
        :type user: User
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
        :rtype: tuple(UserResource, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'user'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `users_post`")  # noqa: E501
        # verify the required parameter 'user' is set
        if self.api_client.client_side_validation and ('user' not in local_var_params or  # noqa: E501
                                                        local_var_params['user'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user` when calling `users_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user' in local_var_params:
            body_params = local_var_params['user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'UserResource'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/users', 'POST',
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
