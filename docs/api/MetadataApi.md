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
    api_instance = ionoscloud_dbaas_postgres.MetadataApi(api_client)
    try:
        # Get the current API version
        api_response = api_instance.infos_version_get()
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling MetadataApi.infos_version_get: %s\n' % e)
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
    api_instance = ionoscloud_dbaas_postgres.MetadataApi(api_client)
    try:
        # Get the current API version
        api_response = api_instance.infos_version_get()
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling MetadataApi.infos_version_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIVersion**](APIVersion.md)

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
    api_instance = ionoscloud_dbaas_postgres.MetadataApi(api_client)
    try:
        # Fetch all API versions
        api_response = api_instance.infos_versions_get()
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling MetadataApi.infos_versions_get: %s\n' % e)
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
    api_instance = ionoscloud_dbaas_postgres.MetadataApi(api_client)
    try:
        # Fetch all API versions
        api_response = api_instance.infos_versions_get()
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling MetadataApi.infos_versions_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[APIVersion]**](APIVersion.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

