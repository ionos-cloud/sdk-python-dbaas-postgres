# PatchClusterProperties

Properties of the payload to change a cluster
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **cores** | **int** | The number of CPU cores per instance. | [optional]  |
| **ram** | **int** | The amount of memory per instance in megabytes. Has to be a multiple of 1024. | [optional]  |
| **storage_size** | **int** | The amount of storage per instance in megabytes. | [optional]  |
| **connections** | [**list[Connection]**](Connection.md) |  | [optional]  |
| **display_name** | **str** | The friendly name of your cluster. | [optional]  |
| **maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional]  |
| **postgres_version** | **str** | The PostgreSQL version of your cluster. | [optional]  |
| **instances** | **int** | The total number of instances in the cluster (one master and n-1 standbys).  | [optional]  |


