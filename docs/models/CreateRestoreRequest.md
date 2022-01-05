# CreateRestoreRequest

The restore request.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **backup_id** | **str** | The unique ID of the backup you want to restore. |  |
| **recovery_target_time** | **datetime** | If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely.  | [optional]  |


