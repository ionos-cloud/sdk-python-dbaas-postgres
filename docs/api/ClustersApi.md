# ClustersApi

All URIs are relative to *https://api.ionos.com/databases/postgresql*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**cluster_postgres_versions_get**](ClustersApi.md#cluster_postgres_versions_get) | **GET** /clusters/{clusterId}/postgresversions | List PostgreSQL versions |
| [**clusters_delete**](ClustersApi.md#clusters_delete) | **DELETE** /clusters/{clusterId} | Delete a cluster |
| [**clusters_find_by_id**](ClustersApi.md#clusters_find_by_id) | **GET** /clusters/{clusterId} | Fetch a cluster |
| [**clusters_get**](ClustersApi.md#clusters_get) | **GET** /clusters | List clusters |
| [**clusters_patch**](ClustersApi.md#clusters_patch) | **PATCH** /clusters/{clusterId} | Patch a cluster |
| [**clusters_post**](ClustersApi.md#clusters_post) | **POST** /clusters | Create a cluster |
| [**postgres_versions_get**](ClustersApi.md#postgres_versions_get) | **GET** /clusters/postgresversions | List PostgreSQL versions |


# **cluster_postgres_versions_get**
> PostgresVersionList cluster_postgres_versions_get(cluster_id)

List PostgreSQL versions

Retrieves a list of all PostgreSQL versions available for this cluster including the current version. 

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
    api_instance = ionoscloud_dbaas_postgres.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    try:
        # List PostgreSQL versions
        api_response = api_instance.cluster_postgres_versions_get(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.cluster_postgres_versions_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |

### Return type

[**PostgresVersionList**](../models/PostgresVersionList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_delete**
> ClusterResponse clusters_delete(cluster_id)

Delete a cluster

Delete a PostgreSQL cluster.

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
    api_instance = ionoscloud_dbaas_postgres.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    try:
        # Delete a cluster
        api_response = api_instance.clusters_delete(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.clusters_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_find_by_id**
> ClusterResponse clusters_find_by_id(cluster_id)

Fetch a cluster

You can retrieve a PostgreSQL cluster by using its ID. This value can be found in the response body when a PostgreSQL cluster is created or when you GET a list of PostgreSQL clusters. 

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
    api_instance = ionoscloud_dbaas_postgres.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    try:
        # Fetch a cluster
        api_response = api_instance.clusters_find_by_id(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.clusters_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_get**
> ClusterList clusters_get(limit=limit, offset=offset, filter_name=filter_name)

List clusters

Retrieves a list of PostgreSQL clusters.

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
    api_instance = ionoscloud_dbaas_postgres.ClustersApi(api_client)
    try:
        # List clusters
        api_response = api_instance.clusters_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.clusters_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100] |
| **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0] |
| **filter_name** | **str**| Response filter to list only the PostgreSQL clusters that contain the specified name. The value is case insensitive and matched on the &#39;displayName&#39; field.  | [optional]  |

### Return type

[**ClusterList**](../models/ClusterList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_patch**
> ClusterResponse clusters_patch(cluster_id, patch_cluster_request)

Patch a cluster

Patch attributes of a PostgreSQL cluster.

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
    api_instance = ionoscloud_dbaas_postgres.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    patch_cluster_request = ionoscloud_dbaas_postgres.PatchClusterRequest() # PatchClusterRequest | Part of the cluster which should be modified.
    try:
        # Patch a cluster
        api_response = api_instance.clusters_patch(cluster_id, patch_cluster_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.clusters_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **patch_cluster_request** | [**PatchClusterRequest**](../models/PatchClusterRequest.md)| Part of the cluster which should be modified. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **clusters_post**
> ClusterResponse clusters_post(create_cluster_request)

Create a cluster

Creates a new PostgreSQL cluster. If the `fromBackup` field is populated, the new cluster will be created based on the given backup. 

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
    api_instance = ionoscloud_dbaas_postgres.ClustersApi(api_client)
    create_cluster_request = ionoscloud_dbaas_postgres.CreateClusterRequest() # CreateClusterRequest | The cluster to be created.
    try:
        # Create a cluster
        api_response = api_instance.clusters_post(create_cluster_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.clusters_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_cluster_request** | [**CreateClusterRequest**](../models/CreateClusterRequest.md)| The cluster to be created. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **postgres_versions_get**
> PostgresVersionList postgres_versions_get()

List PostgreSQL versions

Retrieves a list of all available PostgreSQL versions.

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
    api_instance = ionoscloud_dbaas_postgres.ClustersApi(api_client)
    try:
        # List PostgreSQL versions
        api_response = api_instance.postgres_versions_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.postgres_versions_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PostgresVersionList**](../models/PostgresVersionList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

