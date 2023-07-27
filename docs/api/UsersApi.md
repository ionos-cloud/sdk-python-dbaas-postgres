# UsersApi

All URIs are relative to *https://api.ionos.com/databases/postgresql*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**users_delete**](UsersApi.md#users_delete) | **DELETE** /clusters/{clusterId}/users/{username} | Delete user |
| [**users_get**](UsersApi.md#users_get) | **GET** /clusters/{clusterId}/users/{username} | Get user |
| [**users_list**](UsersApi.md#users_list) | **GET** /clusters/{clusterId}/users | List users |
| [**users_patch**](UsersApi.md#users_patch) | **PATCH** /clusters/{clusterId}/users/{username} | Patch user |
| [**users_post**](UsersApi.md#users_post) | **POST** /clusters/{clusterId}/users | Create a user |


# **users_delete**
> users_delete(cluster_id, username)

Delete user

Deletes a single user

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
    api_instance = ionoscloud_dbaas_postgres.UsersApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    username = 'benjamin' # str | The authentication username.
    try:
        # Delete user
        api_instance.users_delete(cluster_id, username)
    except ApiException as e:
        print('Exception when calling UsersApi.users_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **username** | **str**| The authentication username. |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **users_get**
> UserResource users_get(cluster_id, username)

Get user

Retrieves a single user

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
    api_instance = ionoscloud_dbaas_postgres.UsersApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    username = 'benjamin' # str | The authentication username.
    try:
        # Get user
        api_response = api_instance.users_get(cluster_id, username)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UsersApi.users_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **username** | **str**| The authentication username. |  |

### Return type

[**UserResource**](../models/UserResource.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **users_list**
> UserList users_list(cluster_id, limit=limit, offset=offset, system=system)

List users

Retrieves a list of users

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
    api_instance = ionoscloud_dbaas_postgres.UsersApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    try:
        # List users
        api_response = api_instance.users_list(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UsersApi.users_list: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100] |
| **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0] |
| **system** | **bool**| If set to &#39;true&#39; all users, including system users are returned. System users cannot be deleted or updated. | [optional]  |

### Return type

[**UserList**](../models/UserList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **users_patch**
> UserResource users_patch(cluster_id, username, users_patch_request)

Patch user

Patches a single user. Only changing the password is supported. System users cannot be patched.

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
    api_instance = ionoscloud_dbaas_postgres.UsersApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    username = 'benjamin' # str | The authentication username.
    users_patch_request = ionoscloud_dbaas_postgres.UsersPatchRequest() # UsersPatchRequest | Patch containing all properties that should be updated
    try:
        # Patch user
        api_response = api_instance.users_patch(cluster_id, username, users_patch_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UsersApi.users_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **username** | **str**| The authentication username. |  |
| **users_patch_request** | [**UsersPatchRequest**](../models/UsersPatchRequest.md)| Patch containing all properties that should be updated |  |

### Return type

[**UserResource**](../models/UserResource.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **users_post**
> UserResource users_post(cluster_id, user)

Create a user

Create a new Postgres User

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
    api_instance = ionoscloud_dbaas_postgres.UsersApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    user = ionoscloud_dbaas_postgres.User() # User | 
    try:
        # Create a user
        api_response = api_instance.users_post(cluster_id, user)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UsersApi.users_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **user** | [**User**](../models/User.md)|  |  |

### Return type

[**UserResource**](../models/UserResource.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

