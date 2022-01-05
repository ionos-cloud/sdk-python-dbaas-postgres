from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dbaas_postgres.api_client import ApiClient
from ionoscloud_dbaas_postgres.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ClustersApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cluster_postgres_versions_get(self, cluster_id, **kwargs):  # noqa: E501
        """List PostgreSQL versions  # noqa: E501

        Retrieves a list of all PostgreSQL versions available for this cluster including the current version.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cluster_postgres_versions_get(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
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
        :rtype: PostgresVersionList
        """
        kwargs['_return_http_data_only'] = True
        return self.cluster_postgres_versions_get_with_http_info(cluster_id, **kwargs)  # noqa: E501

    def cluster_postgres_versions_get_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """List PostgreSQL versions  # noqa: E501

        Retrieves a list of all PostgreSQL versions available for this cluster including the current version.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cluster_postgres_versions_get_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
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
        :rtype: tuple(PostgresVersionList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id'
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
                    " to method cluster_postgres_versions_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `cluster_postgres_versions_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'PostgresVersionList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/postgresversions', 'GET',
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

    def clusters_delete(self, cluster_id, **kwargs):  # noqa: E501
        """Delete a cluster  # noqa: E501

        Delete a PostgreSQL cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_delete(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
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
        :rtype: ClusterResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_delete_with_http_info(cluster_id, **kwargs)  # noqa: E501

    def clusters_delete_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """Delete a cluster  # noqa: E501

        Delete a PostgreSQL cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_delete_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
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
        :rtype: tuple(ClusterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id'
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
                    " to method clusters_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `clusters_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterResponse'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}', 'DELETE',
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

    def clusters_find_by_id(self, cluster_id, **kwargs):  # noqa: E501
        """Fetch a cluster  # noqa: E501

        You can retrieve a PostgreSQL cluster by using its ID. This value can be found in the response body when a PostgreSQL cluster is created or when you GET a list of PostgreSQL clusters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_find_by_id(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
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
        :rtype: ClusterResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_find_by_id_with_http_info(cluster_id, **kwargs)  # noqa: E501

    def clusters_find_by_id_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """Fetch a cluster  # noqa: E501

        You can retrieve a PostgreSQL cluster by using its ID. This value can be found in the response body when a PostgreSQL cluster is created or when you GET a list of PostgreSQL clusters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_find_by_id_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
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
        :rtype: tuple(ClusterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id'
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
                    " to method clusters_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `clusters_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterResponse'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}', 'GET',
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

    def clusters_get(self, **kwargs):  # noqa: E501
        """List clusters  # noqa: E501

        Retrieves a list of PostgreSQL clusters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_get(async_req=True)
        >>> result = thread.get()

        :param filter_name: Response filter to list only the PostgreSQL clusters that contain the specified name. The value is case insensitive and matched on the 'displayName' field. 
        :type filter_name: str
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
        :rtype: ClusterList
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_get_with_http_info(**kwargs)  # noqa: E501

    def clusters_get_with_http_info(self, **kwargs):  # noqa: E501
        """List clusters  # noqa: E501

        Retrieves a list of PostgreSQL clusters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param filter_name: Response filter to list only the PostgreSQL clusters that contain the specified name. The value is case insensitive and matched on the 'displayName' field. 
        :type filter_name: str
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
        :rtype: tuple(ClusterList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'filter_name'
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
                    " to method clusters_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_name' in local_var_params and local_var_params['filter_name'] is not None:  # noqa: E501
            query_params.append(('filter.name', local_var_params['filter_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters', 'GET',
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

    def clusters_patch(self, cluster_id, patch_cluster_request, **kwargs):  # noqa: E501
        """Patch a cluster  # noqa: E501

        Patch attributes of a PostgreSQL cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_patch(cluster_id, patch_cluster_request, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param patch_cluster_request: The modified cluster. (required)
        :type patch_cluster_request: PatchClusterRequest
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
        :rtype: ClusterResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_patch_with_http_info(cluster_id, patch_cluster_request, **kwargs)  # noqa: E501

    def clusters_patch_with_http_info(self, cluster_id, patch_cluster_request, **kwargs):  # noqa: E501
        """Patch a cluster  # noqa: E501

        Patch attributes of a PostgreSQL cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_patch_with_http_info(cluster_id, patch_cluster_request, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param patch_cluster_request: The modified cluster. (required)
        :type patch_cluster_request: PatchClusterRequest
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
        :rtype: tuple(ClusterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'patch_cluster_request'
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
                    " to method clusters_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `clusters_patch`")  # noqa: E501
        # verify the required parameter 'patch_cluster_request' is set
        if self.api_client.client_side_validation and ('patch_cluster_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['patch_cluster_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `patch_cluster_request` when calling `clusters_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_cluster_request' in local_var_params:
            body_params = local_var_params['patch_cluster_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterResponse'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}', 'PATCH',
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

    def clusters_post(self, create_cluster_request, **kwargs):  # noqa: E501
        """Create a cluster  # noqa: E501

        Creates a new PostgreSQL cluster. If the `fromBackup` field is populated, the new cluster will be created based on the given backup.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_post(create_cluster_request, async_req=True)
        >>> result = thread.get()

        :param create_cluster_request: The cluster to be created. (required)
        :type create_cluster_request: CreateClusterRequest
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
        :rtype: ClusterResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_post_with_http_info(create_cluster_request, **kwargs)  # noqa: E501

    def clusters_post_with_http_info(self, create_cluster_request, **kwargs):  # noqa: E501
        """Create a cluster  # noqa: E501

        Creates a new PostgreSQL cluster. If the `fromBackup` field is populated, the new cluster will be created based on the given backup.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_post_with_http_info(create_cluster_request, async_req=True)
        >>> result = thread.get()

        :param create_cluster_request: The cluster to be created. (required)
        :type create_cluster_request: CreateClusterRequest
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
        :rtype: tuple(ClusterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'create_cluster_request'
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
                    " to method clusters_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'create_cluster_request' is set
        if self.api_client.client_side_validation and ('create_cluster_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_cluster_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_cluster_request` when calling `clusters_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_cluster_request' in local_var_params:
            body_params = local_var_params['create_cluster_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterResponse'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters', 'POST',
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

    def postgres_versions_get(self, **kwargs):  # noqa: E501
        """List PostgreSQL versions  # noqa: E501

        Retrieves a list of all available PostgreSQL versions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.postgres_versions_get(async_req=True)
        >>> result = thread.get()

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
        :rtype: PostgresVersionList
        """
        kwargs['_return_http_data_only'] = True
        return self.postgres_versions_get_with_http_info(**kwargs)  # noqa: E501

    def postgres_versions_get_with_http_info(self, **kwargs):  # noqa: E501
        """List PostgreSQL versions  # noqa: E501

        Retrieves a list of all available PostgreSQL versions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.postgres_versions_get_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(PostgresVersionList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
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
                    " to method postgres_versions_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'PostgresVersionList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/postgresversions', 'GET',
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
