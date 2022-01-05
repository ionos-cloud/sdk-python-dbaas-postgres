from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dbaas_postgres.api_client import ApiClient
from ionoscloud_dbaas_postgres.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class LogsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cluster_logs_get(self, cluster_id, **kwargs):  # noqa: E501
        """Get logs of your cluster  # noqa: E501

        Retrieves PostgreSQL logs based on the given parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cluster_logs_get(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param limit: The maximal number of log lines to return.
        :type limit: int
        :param start: The start time for the query in RFC3339 format.
        :type start: datetime
        :param end: The end time for the query in RFC3339 format.
        :type end: datetime
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
        :rtype: ClusterLogs
        """
        kwargs['_return_http_data_only'] = True
        return self.cluster_logs_get_with_http_info(cluster_id, **kwargs)  # noqa: E501

    def cluster_logs_get_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """Get logs of your cluster  # noqa: E501

        Retrieves PostgreSQL logs based on the given parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cluster_logs_get_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. (required)
        :type cluster_id: str
        :param limit: The maximal number of log lines to return.
        :type limit: int
        :param start: The start time for the query in RFC3339 format.
        :type start: datetime
        :param end: The end time for the query in RFC3339 format.
        :type end: datetime
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
        :rtype: tuple(ClusterLogs, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'limit',
            'start',
            'end'
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
                    " to method cluster_logs_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `cluster_logs_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 5000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `cluster_logs_get`, must be a value less than or equal to `5000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `cluster_logs_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'start' in local_var_params and local_var_params['start'] is not None:  # noqa: E501
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params and local_var_params['end'] is not None:  # noqa: E501
            query_params.append(('end', local_var_params['end']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterLogs'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/logs', 'GET',
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
