# CHANGELOG

## v1.0.3 (July, 2022)
  
### Features
* add size and location to ClusterBackup
* added certificate pinning option

## v1.0.2 (May, 2022)

### Enhancements:
* `location` and `backup_location` parameters on `CreateClusterProperties` are now strings
  * `Location` and `BackupLocation` models are now removed
  
### Features
* **new values** for `storage_type` parameter: _**SSD_STANDARD**, **SSD_PREMIUM**_. Value **_SSD_** is deprecated. Use the equivalent **_SSD_PREMIUM_** instead.


## v1.0.1 (March, 2022)

### Features:

* added **new property** `backup_location` on `CreateClusterProperties`
* added **new query parameter** `direction` on `cluster_logs_get` method

### Enhancements:

* added support for query parameters
* added token authentication
* added proxy support

## v1.0.0 (January, 2022)

### Features:

* first release 🎉
