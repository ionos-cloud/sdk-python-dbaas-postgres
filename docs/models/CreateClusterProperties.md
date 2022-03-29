# CreateClusterProperties

Properties with all data needed to create a new PostgreSQL cluster. 
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **postgres_version** | **str** | The PostgreSQL version of your cluster. |  |
| **instances** | **int** | The total number of instances in the cluster (one master and n-1 standbys).  |  |
| **cores** | **int** | The number of CPU cores per instance. |  |
| **ram** | **int** | The amount of memory per instance in megabytes. Has to be a multiple of 1024. |  |
| **storage_size** | **int** | The amount of storage per instance in megabytes. |  |
| **storage_type** | [**StorageType**](StorageType.md) |  |  |
| **connections** | [**list[Connection]**](Connection.md) |  |  |
| **location** | [**Location**](Location.md) |  |  |
| **backup_location** | [**BackupLocation**](BackupLocation.md) |  | [optional]  |
| **display_name** | **str** | The friendly name of your cluster. |  |
| **maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional]  |
| **credentials** | [**DBUser**](DBUser.md) |  |  |
| **synchronization_mode** | [**SynchronizationMode**](SynchronizationMode.md) |  |  |
| **from_backup** | [**CreateRestoreRequest**](CreateRestoreRequest.md) |  | [optional]  |


