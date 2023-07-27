# LogsApi

All URIs are relative to *https://api.ionos.com/databases/postgresql*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**cluster_logs_get**](LogsApi.md#cluster_logs_get) | **GET** /clusters/{clusterId}/logs | Get logs of your cluster |


# **cluster_logs_get**
> ClusterLogs cluster_logs_get(cluster_id, start=start, end=end, direction=direction, limit=limit)

Get logs of your cluster

Retrieves PostgreSQL logs based on the given parameters.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dbaas_postgres
from ionoscloud_dbaas_postgres.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/databases/postgresql
configuration = ionoscloud_dbaas_postgres.Configuration(
    host = 'https://api.ionos.com/databases/postgresql',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dbaas_postgres.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_postgres.LogsApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    try:
        # Get logs of your cluster
        api_response = api_instance.cluster_logs_get(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LogsApi.cluster_logs_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **start** | **datetime**| The start time for the query in RFC3339 format. Must not be more than 30 days ago but before the end parameter. The default is 30 days ago. | [optional]  |
| **end** | **datetime**| The end time for the query in RFC3339 format. Must not be greater than now. The default is the current timestamp. | [optional]  |
| **direction** | **str**| The direction in which to scan through the logs. The logs are returned in order of the direction. | [optional] [default to &#39;BACKWARD&#39;] |
| **limit** | **int**| The maximal number of log lines to return.  If the limit is reached then log lines will be cut at the end (respecting the scan direction). | [optional] [default to 100] |

### Return type

[**ClusterLogs**](../models/ClusterLogs.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

