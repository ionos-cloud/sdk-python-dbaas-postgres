![CI Python DBaaS Postgres](https://github.com/ionos-cloud/sdk-resources/workflows/[%20CI%20]%20DBaaS%20Postgres%20/%20Python/badge.svg)
[![Gitter](https://img.shields.io/gitter/room/ionos-cloud/sdk-general)](https://gitter.im/ionos-cloud/sdk-general)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dbaas-postgres&metric=alert_status)](https://sonarcloud.io/summary?id=sdk-python-dbaas-postgres)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dbaas-postgres&metric=bugs)](https://sonarcloud.io/summary/new_code?id=sdk-python-dbaas-postgres)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dbaas-postgres&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-dbaas-postgres)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dbaas-postgres&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-dbaas-postgres)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dbaas-postgres&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-dbaas-postgres)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dbaas-postgres&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=sdk-python-dbaas-postgres)
[![Release](https://img.shields.io/github/v/release/ionos-cloud/sdk-python-dbaas-postgres.svg)](https://github.com/ionos-cloud/sdk-python-dbaas-postgres/releases/latest)
[![Release Date](https://img.shields.io/github/release-date/ionos-cloud/sdk-python-dbaas-postgres.svg)](https://github.com/ionos-cloud/sdk-python-dbaas-postgres/releases/latest)
[![PyPI version](https://img.shields.io/pypi/v/ionoscloud-dbaas-postgres)](https://pypi.org/project/ionoscloud-dbaas-postgres/)

![Alt text](.github/IONOS.CLOUD.BLU.svg?raw=true "Title")


# Python API client for ionoscloud_dbaas_postgres

An enterprise-grade Database is provided as a Service (DBaaS) solution that
can be managed through a browser-based \"Data Center Designer\" (DCD) tool or
via an easy to use API.

The API allows you to create additional PostgreSQL database clusters or modify existing
ones. It is designed to allow users to leverage the same power and
flexibility found within the DCD visual tool. Both tools are consistent with
their concepts and lend well to making the experience smooth and intuitive.


## Overview
The IONOS Cloud SDK for Python provides you with access to the IONOS Cloud Dbaas Postgres API. The client library supports both simple and complex requests. It is designed for developers who are building applications in Python. All API operations are performed over SSL and authenticated using your IONOS Cloud portal credentials. The API can be accessed within an instance running in IONOS Cloud or directly over the Internet from any application that can send an HTTPS request and receive an HTTPS response.


### Installation & Usage

**Requirements:**
- Python >= 3.5

### pip install

Since this package is hosted on [Pypi](https://pypi.org/) you can install it by using:

```bash
pip install ionoscloud-dbaas-postgres
```

If the python package is hosted on a repository, you can install directly using:

```bash
pip install git+https://github.com/ionos-cloud/sdk-python-dbaas-postgres.git
```

Note: you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ionos-cloud/sdk-python-dbaas-postgres.git`

Then import the package:

```python
import ionoscloud_dbaas_postgres
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```bash
python setup.py install --user
```

or `sudo python setup.py install` to install the package for all users

Then import the package:

```python
import ionoscloud_dbaas_postgres
```

> **_NOTE:_**  The Python SDK does not support Python 2. It only supports Python >= 3.5.

### Authentication

The username and password **or** the authentication token can be manually specified when initializing the SDK client:

```python
configuration = ionoscloud_dbaas_postgres.Configuration(
                username='YOUR_USERNAME',
                password='YOUR_PASSWORD',
                token='YOUR_TOKEN'
                )
client = ionoscloud_dbaas_postgres.ApiClient(configuration)
```

Environment variables can also be used. This is an example of how one would do that:

```python
import os

configuration = ionoscloud_dbaas_postgres.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                token=os.environ.get('IONOS_TOKEN')
                )
client = ionoscloud_dbaas_postgres.ApiClient(configuration)
```

**Warning**: Make sure to follow the Information Security Best Practices when using credentials within your code or storing them in a file.


### HTTP proxies

You can use http proxies by setting the following environment variables:
- `IONOS_HTTP_PROXY` - proxy URL
- `IONOS_HTTP_PROXY_HEADERS` - proxy headers

### Changing the base URL

Base URL for the HTTP operation can be changed in the following way:

```python
import os

configuration = ionoscloud_dbaas_postgres.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                host=os.environ.get('IONOS_API_URL'),
                server_index=None,
                )
client = ionoscloud_dbaas_postgres.ApiClient(configuration)
```

## Certificate pinning:

You can enable certificate pinning if you want to bypass the normal certificate checking procedure,
by doing the following:

Set env variable IONOS_PINNED_CERT=<insert_sha256_public_fingerprint_here>

You can get the sha256 fingerprint most easily from the browser by inspecting the certificate.


## Documentation for API Endpoints

All URIs are relative to *https://api.ionos.com/databases/postgresql*
<details >
    <summary title="Click to toggle">API Endpoints table</summary>


| Class | Method | HTTP request | Description |
| ------------- | ------------- | ------------- | ------------- |
| BackupsApi | [**cluster_backups_get**](docs/api/BackupsApi.md#cluster_backups_get) | **GET** /clusters/{clusterId}/backups | List backups of cluster |
| BackupsApi | [**clusters_backups_find_by_id**](docs/api/BackupsApi.md#clusters_backups_find_by_id) | **GET** /clusters/backups/{backupId} | Fetch a cluster backup |
| BackupsApi | [**clusters_backups_get**](docs/api/BackupsApi.md#clusters_backups_get) | **GET** /clusters/backups | List cluster backups |
| ClustersApi | [**cluster_postgres_versions_get**](docs/api/ClustersApi.md#cluster_postgres_versions_get) | **GET** /clusters/{clusterId}/postgresversions | List PostgreSQL versions |
| ClustersApi | [**clusters_delete**](docs/api/ClustersApi.md#clusters_delete) | **DELETE** /clusters/{clusterId} | Delete a cluster |
| ClustersApi | [**clusters_find_by_id**](docs/api/ClustersApi.md#clusters_find_by_id) | **GET** /clusters/{clusterId} | Fetch a cluster |
| ClustersApi | [**clusters_get**](docs/api/ClustersApi.md#clusters_get) | **GET** /clusters | List clusters |
| ClustersApi | [**clusters_patch**](docs/api/ClustersApi.md#clusters_patch) | **PATCH** /clusters/{clusterId} | Patch a cluster |
| ClustersApi | [**clusters_post**](docs/api/ClustersApi.md#clusters_post) | **POST** /clusters | Create a cluster |
| ClustersApi | [**postgres_versions_get**](docs/api/ClustersApi.md#postgres_versions_get) | **GET** /clusters/postgresversions | List PostgreSQL versions |
| DatabasesApi | [**databases_delete**](docs/api/DatabasesApi.md#databases_delete) | **DELETE** /clusters/{clusterId}/databases/{databasename} | Delete database |
| DatabasesApi | [**databases_get**](docs/api/DatabasesApi.md#databases_get) | **GET** /clusters/{clusterId}/databases/{databasename} | Get database |
| DatabasesApi | [**databases_list**](docs/api/DatabasesApi.md#databases_list) | **GET** /clusters/{clusterId}/databases | List databases |
| DatabasesApi | [**databases_post**](docs/api/DatabasesApi.md#databases_post) | **POST** /clusters/{clusterId}/databases | Create a database |
| LogsApi | [**cluster_logs_get**](docs/api/LogsApi.md#cluster_logs_get) | **GET** /clusters/{clusterId}/logs | Get logs of your cluster |
| MetadataApi | [**infos_version_get**](docs/api/MetadataApi.md#infos_version_get) | **GET** /infos/version | Get the current API version |
| MetadataApi | [**infos_versions_get**](docs/api/MetadataApi.md#infos_versions_get) | **GET** /infos/versions | Fetch all API versions |
| RestoresApi | [**cluster_restore_post**](docs/api/RestoresApi.md#cluster_restore_post) | **POST** /clusters/{clusterId}/restore | In-place restore of a cluster |
| UsersApi | [**users_delete**](docs/api/UsersApi.md#users_delete) | **DELETE** /clusters/{clusterId}/users/{username} | Delete user |
| UsersApi | [**users_get**](docs/api/UsersApi.md#users_get) | **GET** /clusters/{clusterId}/users/{username} | Get user |
| UsersApi | [**users_list**](docs/api/UsersApi.md#users_list) | **GET** /clusters/{clusterId}/users | List users |
| UsersApi | [**users_patch**](docs/api/UsersApi.md#users_patch) | **PATCH** /clusters/{clusterId}/users/{username} | Patch user |
| UsersApi | [**users_post**](docs/api/UsersApi.md#users_post) | **POST** /clusters/{clusterId}/users | Create a user |

</details>

## Documentation For Models

All URIs are relative to *https://api.ionos.com/databases/postgresql*
<details >
<summary title="Click to toggle">API models list</summary>

 - [APIVersion](docs/models/APIVersion)
 - [BackupMetadata](docs/models/BackupMetadata)
 - [BackupResponse](docs/models/BackupResponse)
 - [ClusterBackup](docs/models/ClusterBackup)
 - [ClusterBackupList](docs/models/ClusterBackupList)
 - [ClusterBackupListAllOf](docs/models/ClusterBackupListAllOf)
 - [ClusterList](docs/models/ClusterList)
 - [ClusterListAllOf](docs/models/ClusterListAllOf)
 - [ClusterLogs](docs/models/ClusterLogs)
 - [ClusterLogsInstances](docs/models/ClusterLogsInstances)
 - [ClusterLogsInstancesMessages](docs/models/ClusterLogsInstancesMessages)
 - [ClusterMetadata](docs/models/ClusterMetadata)
 - [ClusterProperties](docs/models/ClusterProperties)
 - [ClusterResponse](docs/models/ClusterResponse)
 - [Connection](docs/models/Connection)
 - [CreateClusterProperties](docs/models/CreateClusterProperties)
 - [CreateClusterRequest](docs/models/CreateClusterRequest)
 - [CreateRestoreRequest](docs/models/CreateRestoreRequest)
 - [DBUser](docs/models/DBUser)
 - [Database](docs/models/Database)
 - [DatabaseItems](docs/models/DatabaseItems)
 - [DatabaseList](docs/models/DatabaseList)
 - [DatabaseProperties](docs/models/DatabaseProperties)
 - [DatabaseResource](docs/models/DatabaseResource)
 - [DayOfTheWeek](docs/models/DayOfTheWeek)
 - [DeprecatedPagination](docs/models/DeprecatedPagination)
 - [ErrorMessage](docs/models/ErrorMessage)
 - [ErrorResponse](docs/models/ErrorResponse)
 - [MaintenanceWindow](docs/models/MaintenanceWindow)
 - [Metadata](docs/models/Metadata)
 - [Pagination](docs/models/Pagination)
 - [PaginationLinks](docs/models/PaginationLinks)
 - [PatchClusterProperties](docs/models/PatchClusterProperties)
 - [PatchClusterRequest](docs/models/PatchClusterRequest)
 - [PatchUserProperties](docs/models/PatchUserProperties)
 - [PostgresVersionList](docs/models/PostgresVersionList)
 - [PostgresVersionListData](docs/models/PostgresVersionListData)
 - [Resource](docs/models/Resource)
 - [ResourceMetadata](docs/models/ResourceMetadata)
 - [ResourceType](docs/models/ResourceType)
 - [State](docs/models/State)
 - [StorageType](docs/models/StorageType)
 - [SynchronizationMode](docs/models/SynchronizationMode)
 - [User](docs/models/User)
 - [UserItems](docs/models/UserItems)
 - [UserList](docs/models/UserList)
 - [UserProperties](docs/models/UserProperties)
 - [UserResource](docs/models/UserResource)
 - [UsersPatchRequest](docs/models/UsersPatchRequest)


[[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

</details>