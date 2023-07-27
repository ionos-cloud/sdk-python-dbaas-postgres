from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dbaas_postgres.api_client import ApiClient
from ionoscloud_dbaas_postgres.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DatabasesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def databases_delete(self, cluster_id, databasename, **kwargs):  # noqa: E501
        """Delete database  # noqa: E501

        Deletes a single database  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.databases_delete(cluster_id, databasename, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param databasename: The database name. (required)
        :type databasename: str
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
        return self.databases_delete_with_http_info(cluster_id, databasename, **kwargs)  # noqa: E501

    def databases_delete_with_http_info(self, cluster_id, databasename, **kwargs):  # noqa: E501
        """Delete database  # noqa: E501

        Deletes a single database  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.databases_delete_with_http_info(cluster_id, databasename, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param databasename: The database name. (required)
        :type databasename: str
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
            'databasename'
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
                    " to method databases_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `databases_delete`")  # noqa: E501
        # verify the required parameter 'databasename' is set
        if self.api_client.client_side_validation and ('databasename' not in local_var_params or  # noqa: E501
                                                        local_var_params['databasename'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `databasename` when calling `databases_delete`")  # noqa: E501

        if self.api_client.client_side_validation and ('databasename' in local_var_params and  # noqa: E501
                                                        len(local_var_params['databasename']) > 63):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `databasename` when calling `databases_delete`, length must be less than or equal to `63`")  # noqa: E501
        if self.api_client.client_side_validation and ('databasename' in local_var_params and  # noqa: E501
                                                        len(local_var_params['databasename']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `databasename` when calling `databases_delete`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501
        if 'databasename' in local_var_params:
            path_params['databasename'] = local_var_params['databasename']  # noqa: E501

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
            '/clusters/{clusterId}/databases/{databasename}', 'DELETE',
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

    def databases_get(self, cluster_id, databasename, **kwargs):  # noqa: E501
        """Get database  # noqa: E501

        Retrieves a single database  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.databases_get(cluster_id, databasename, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param databasename: The database name. (required)
        :type databasename: str
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
        :rtype: DatabaseResource
        """
        kwargs['_return_http_data_only'] = True
        return self.databases_get_with_http_info(cluster_id, databasename, **kwargs)  # noqa: E501

    def databases_get_with_http_info(self, cluster_id, databasename, **kwargs):  # noqa: E501
        """Get database  # noqa: E501

        Retrieves a single database  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.databases_get_with_http_info(cluster_id, databasename, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param databasename: The database name. (required)
        :type databasename: str
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
        :rtype: tuple(DatabaseResource, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'databasename'
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
                    " to method databases_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `databases_get`")  # noqa: E501
        # verify the required parameter 'databasename' is set
        if self.api_client.client_side_validation and ('databasename' not in local_var_params or  # noqa: E501
                                                        local_var_params['databasename'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `databasename` when calling `databases_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('databasename' in local_var_params and  # noqa: E501
                                                        len(local_var_params['databasename']) > 63):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `databasename` when calling `databases_get`, length must be less than or equal to `63`")  # noqa: E501
        if self.api_client.client_side_validation and ('databasename' in local_var_params and  # noqa: E501
                                                        len(local_var_params['databasename']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `databasename` when calling `databases_get`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501
        if 'databasename' in local_var_params:
            path_params['databasename'] = local_var_params['databasename']  # noqa: E501

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

        response_type = 'DatabaseResource'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/databases/{databasename}', 'GET',
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

    def databases_list(self, cluster_id, **kwargs):  # noqa: E501
        """List databases  # noqa: E501

        Retrieves a list of databases  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.databases_list(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param limit: The maximum number of elements to return. Use together with 'offset' for pagination.
        :type limit: int
        :param offset: The first element to return. Use together with 'limit' for pagination.
        :type offset: int
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
        :rtype: DatabaseList
        """
        kwargs['_return_http_data_only'] = True
        return self.databases_list_with_http_info(cluster_id, **kwargs)  # noqa: E501

    def databases_list_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """List databases  # noqa: E501

        Retrieves a list of databases  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.databases_list_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param limit: The maximum number of elements to return. Use together with 'offset' for pagination.
        :type limit: int
        :param offset: The first element to return. Use together with 'limit' for pagination.
        :type offset: int
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
        :rtype: tuple(DatabaseList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'limit',
            'offset'
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
                    " to method databases_list" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `databases_list`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `databases_list`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `databases_list`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'DatabaseList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/databases', 'GET',
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

    def databases_post(self, cluster_id, database, **kwargs):  # noqa: E501
        """Create a database  # noqa: E501

        Create a new database  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.databases_post(cluster_id, database, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param database: a database to create (required)
        :type database: Database
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
        :rtype: DatabaseResource
        """
        kwargs['_return_http_data_only'] = True
        return self.databases_post_with_http_info(cluster_id, database, **kwargs)  # noqa: E501

    def databases_post_with_http_info(self, cluster_id, database, **kwargs):  # noqa: E501
        """Create a database  # noqa: E501

        Create a new database  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.databases_post_with_http_info(cluster_id, database, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param database: a database to create (required)
        :type database: Database
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
        :rtype: tuple(DatabaseResource, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'database'
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
                    " to method databases_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `databases_post`")  # noqa: E501
        # verify the required parameter 'database' is set
        if self.api_client.client_side_validation and ('database' not in local_var_params or  # noqa: E501
                                                        local_var_params['database'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `database` when calling `databases_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'database' in local_var_params:
            body_params = local_var_params['database']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'DatabaseResource'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/databases', 'POST',
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
