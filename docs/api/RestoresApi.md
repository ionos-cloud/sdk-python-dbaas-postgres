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
    api_instance = ionoscloud_dbaas_postgres.RestoresApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    create_restore_request = ionoscloud_dbaas_postgres.CreateRestoreRequest() # CreateRestoreRequest | The restore request to create.
    try:
        # In-place restore of a cluster
        api_instance.cluster_restore_post(cluster_id, create_restore_request)
    except ApiException as e:
        print('Exception when calling RestoresApi.cluster_restore_post: %s\n' % e)
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
    api_instance = ionoscloud_dbaas_postgres.RestoresApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
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
| **create_restore_request** | [**CreateRestoreRequest**](CreateRestoreRequest.md)| The restore request to create. |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

