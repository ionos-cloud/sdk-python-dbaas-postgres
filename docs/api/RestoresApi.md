# RestoresApi

All URIs are relative to *https://api.ionos.com/databases/postgresql*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**cluster_restore_post**](RestoresApi.md#cluster_restore_post) | **POST** /clusters/{clusterId}/restore | In-place restore of a cluster |


# **cluster_restore_post**
> cluster_restore_post(cluster_id, create_restore_request)

In-place restore of a cluster

Triggers an in-place restore of the given PostgreSQL.

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
    api_instance = ionoscloud_dbaas_postgres.RestoresApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    create_restore_request = ionoscloud_dbaas_postgres.CreateRestoreRequest() # CreateRestoreRequest | The restore request to create.
    try:
        # In-place restore of a cluster
        api_instance.cluster_restore_post(cluster_id, create_restore_request)
    except ApiException as e:
        print('Exception when calling RestoresApi.cluster_restore_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **create_restore_request** | [**CreateRestoreRequest**](../models/CreateRestoreRequest.md)| The restore request to create. |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

