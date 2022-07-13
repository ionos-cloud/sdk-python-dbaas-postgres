# ClusterProperties

Properties of a database cluster.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **display_name** | **str** | The friendly name of your cluster. | [optional]  |
| **postgres_version** | **str** | The PostgreSQL version of your cluster. | [optional]  |
| **location** | **str** | The physical location where the cluster will be created. This will be where all of your instances live. Property cannot be modified after datacenter creation.  | [optional]  |
| **backup_location** | **str** | The S3 location where the backups will be stored. | [optional]  |
| **instances** | **int** | The total number of instances in the cluster (one master and n-1 standbys).  | [optional]  |
| **ram** | **int** | The amount of memory per instance in megabytes. Has to be a multiple of 1024. | [optional]  |
| **cores** | **int** | The number of CPU cores per instance. | [optional]  |
| **storage_size** | **int** | The amount of storage per instance in megabytes. | [optional]  |
| **storage_type** | [**StorageType**](StorageType.md) |  | [optional]  |
| **connections** | [**list[Connection]**](Connection.md) |  | [optional]  |
| **maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional]  |
| **synchronization_mode** | [**SynchronizationMode**](SynchronizationMode.md) |  | [optional]  |


