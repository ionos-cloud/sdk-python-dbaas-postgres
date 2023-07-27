# DatabasesApi

All URIs are relative to *https://api.ionos.com/databases/postgresql*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**databases_delete**](DatabasesApi.md#databases_delete) | **DELETE** /clusters/{clusterId}/databases/{databasename} | Delete database |
| [**databases_get**](DatabasesApi.md#databases_get) | **GET** /clusters/{clusterId}/databases/{databasename} | Get database |
| [**databases_list**](DatabasesApi.md#databases_list) | **GET** /clusters/{clusterId}/databases | List databases |
| [**databases_post**](DatabasesApi.md#databases_post) | **POST** /clusters/{clusterId}/databases | Create a database |


# **databases_delete**
> databases_delete(cluster_id, databasename)

Delete database

Deletes a single database

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
    api_instance = ionoscloud_dbaas_postgres.DatabasesApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    databasename = 'benjamindb' # str | The database name.
    try:
        # Delete database
        api_instance.databases_delete(cluster_id, databasename)
    except ApiException as e:
        print('Exception when calling DatabasesApi.databases_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **databasename** | **str**| The database name. |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **databases_get**
> DatabaseResource databases_get(cluster_id, databasename)

Get database

Retrieves a single database

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
    api_instance = ionoscloud_dbaas_postgres.DatabasesApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    databasename = 'benjamindb' # str | The database name.
    try:
        # Get database
        api_response = api_instance.databases_get(cluster_id, databasename)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DatabasesApi.databases_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **databasename** | **str**| The database name. |  |

### Return type

[**DatabaseResource**](../models/DatabaseResource.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **databases_list**
> DatabaseList databases_list(cluster_id, limit=limit, offset=offset)

List databases

Retrieves a list of databases

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
    api_instance = ionoscloud_dbaas_postgres.DatabasesApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    try:
        # List databases
        api_response = api_instance.databases_list(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DatabasesApi.databases_list: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100] |
| **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0] |

### Return type

[**DatabaseList**](../models/DatabaseList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **databases_post**
> DatabaseResource databases_post(cluster_id, database)

Create a database

Create a new database

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
    api_instance = ionoscloud_dbaas_postgres.DatabasesApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    database = ionoscloud_dbaas_postgres.Database() # Database | a database to create
    try:
        # Create a database
        api_response = api_instance.databases_post(cluster_id, database)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DatabasesApi.databases_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **database** | [**Database**](../models/Database.md)| a database to create |  |

### Return type

[**DatabaseResource**](../models/DatabaseResource.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

