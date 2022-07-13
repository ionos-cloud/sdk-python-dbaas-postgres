# ClusterBackupList

List of backups.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **type** | [**ResourceType**](ResourceType.md) |  | [optional]  |
| **id** | **str** | The unique ID of the resource. | [optional]  |
| **items** | [**list[BackupResponse]**](BackupResponse.md) |  | [optional]  |
| **offset** | **int** | The offset specified in the request (if none was specified, the default offset is 0) (not implemented yet).  | [optional] [readonly]  |
| **limit** | **int** | The limit specified in the request (if none was specified, use the endpoint&#39;s default pagination limit) (not implemented yet, always return number of items).  | [optional] [readonly]  |
| **links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional]  |


