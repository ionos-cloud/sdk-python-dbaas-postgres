# BackupsApi

All URIs are relative to *https://api.ionos.com/databases/postgresql*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**cluster_backups_get**](BackupsApi.md#cluster_backups_get) | **GET** /clusters/{clusterId}/backups | List backups of cluster |
| [**clusters_backups_find_by_id**](BackupsApi.md#clusters_backups_find_by_id) | **GET** /clusters/backups/{backupId} | Fetch a cluster backup |
| [**clusters_backups_get**](BackupsApi.md#clusters_backups_get) | **GET** /clusters/backups | List cluster backups |


# **cluster_backups_get**
> ClusterBackupList cluster_backups_get(cluster_id)

List backups of cluster

Retrieves a list of all backups of the given PostgreSQL cluster.

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
    api_instance = ionoscloud_dbaas_postgres.BackupsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    try:
        # List backups of cluster
        api_response = api_instance.cluster_backups_get(cluster_id)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling BackupsApi.cluster_backups_get: %s\n' % e)
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
    api_instance = ionoscloud_dbaas_postgres.BackupsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    try:
        # List backups of cluster
        api_response = api_instance.cluster_backups_get(cluster_id)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling BackupsApi.cluster_backups_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |

### Return type

[**ClusterBackupList**](ClusterBackupList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_backups_find_by_id**
> BackupResponse clusters_backups_find_by_id(backup_id)

Fetch a cluster backup

Retrieve a PostgreSQL cluster backup by using its ID. This value can be found when you GET a list of PostgreSQL cluster backups. 

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
    api_instance = ionoscloud_dbaas_postgres.BackupsApi(api_client)
    backup_id = 'backup_id_example' # str | The unique ID of the backup.
    try:
        # Fetch a cluster backup
        api_response = api_instance.clusters_backups_find_by_id(backup_id)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling BackupsApi.clusters_backups_find_by_id: %s\n' % e)
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
    api_instance = ionoscloud_dbaas_postgres.BackupsApi(api_client)
    backup_id = 'backup_id_example' # str | The unique ID of the backup.
    try:
        # Fetch a cluster backup
        api_response = api_instance.clusters_backups_find_by_id(backup_id)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling BackupsApi.clusters_backups_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **backup_id** | **str**| The unique ID of the backup. |  |

### Return type

[**BackupResponse**](BackupResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_backups_get**
> ClusterBackupList clusters_backups_get()

List cluster backups

Retrieves a list of all PostgreSQL cluster backups.

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
    api_instance = ionoscloud_dbaas_postgres.BackupsApi(api_client)
    try:
        # List cluster backups
        api_response = api_instance.clusters_backups_get()
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling BackupsApi.clusters_backups_get: %s\n' % e)
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
    api_instance = ionoscloud_dbaas_postgres.BackupsApi(api_client)
    try:
        # List cluster backups
        api_response = api_instance.clusters_backups_get()
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling BackupsApi.clusters_backups_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterBackupList**](ClusterBackupList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

