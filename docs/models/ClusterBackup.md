# ClusterBackup

A backup object.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **str** | The unique ID of the resource. | [optional]  |
| **cluster_id** | **str** | The unique ID of the cluster. | [optional]  |
| **version** | **str** | The PostgreSQL version this backup was created from. | [optional]  |
| **is_active** | **bool** | Whether a cluster currently backs up data to this backup. | [optional]  |
| **earliest_recovery_target_time** | **datetime** | The oldest available timestamp to which you can restore. | [optional]  |
| **size** | **int** | Size of all base backups including the wal size in MB. | [optional]  |
| **location** | **str** | The S3 location where the backups will be stored. | [optional]  |


