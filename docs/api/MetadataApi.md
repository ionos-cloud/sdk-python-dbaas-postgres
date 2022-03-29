# MetadataApi

All URIs are relative to *https://api.ionos.com/databases/postgresql*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**infos_version_get**](MetadataApi.md#infos_version_get) | **GET** /infos/version | Get the current API version |
| [**infos_versions_get**](MetadataApi.md#infos_versions_get) | **GET** /infos/versions | Fetch all API versions |


# **infos_version_get**
> APIVersion infos_version_get()

Get the current API version

Retrieves the current version of the responding API.

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
    api_instance = ionoscloud_dbaas_postgres.MetadataApi(api_client)
    try:
        # Get the current API version
        api_response = api_instance.infos_version_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling MetadataApi.infos_version_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIVersion**](../models/APIVersion.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **infos_versions_get**
> list[APIVersion] infos_versions_get()

Fetch all API versions

Retrieves all available versions of the responding API.

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
    api_instance = ionoscloud_dbaas_postgres.MetadataApi(api_client)
    try:
        # Fetch all API versions
        api_response = api_instance.infos_versions_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling MetadataApi.infos_versions_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[APIVersion]**](../models/APIVersion.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

