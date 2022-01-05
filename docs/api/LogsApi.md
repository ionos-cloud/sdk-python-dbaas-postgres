# LogsApi

All URIs are relative to *https://api.ionos.com/databases/postgresql*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**cluster_logs_get**](LogsApi.md#cluster_logs_get) | **GET** /clusters/{clusterId}/logs | Get logs of your cluster |


# **cluster_logs_get**
> ClusterLogs cluster_logs_get(cluster_id, limit=limit, start=start, end=end)

Get logs of your cluster

Retrieves PostgreSQL logs based on the given parameters.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import ionoscloud_dbaas_postgres
from ionoscloud_dbaas_postgres.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/databases/postgresql
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dbaas_postgres.Configuration(
    host = 'https://api.ionos.com/databases/postgresql',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud_dbaas_postgres.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_postgres.LogsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    limit = 56 # int | The maximal number of log lines to return. (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | The start time for the query in RFC3339 format. (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | The end time for the query in RFC3339 format. (optional)
    try:
        # Get logs of your cluster
        api_response = api_instance.cluster_logs_get(cluster_id, limit=limit, start=start, end=end)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LogsApi.cluster_logs_get: %s\n' % e)
```

* Api Key Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import ionoscloud_dbaas_postgres
from ionoscloud_dbaas_postgres.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/databases/postgresql
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dbaas_postgres.Configuration(
    host = 'https://api.ionos.com/databases/postgresql',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: tokenAuth
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud_dbaas_postgres.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_postgres.LogsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    limit = 56 # int | The maximal number of log lines to return. (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | The start time for the query in RFC3339 format. (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | The end time for the query in RFC3339 format. (optional)
    try:
        # Get logs of your cluster
        api_response = api_instance.cluster_logs_get(cluster_id, limit=limit, start=start, end=end)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LogsApi.cluster_logs_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **limit** | **int**| The maximal number of log lines to return. | [optional]  |
| **start** | **datetime**| The start time for the query in RFC3339 format. | [optional]  |
| **end** | **datetime**| The end time for the query in RFC3339 format. | [optional]  |

### Return type

[**ClusterLogs**](ClusterLogs.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

