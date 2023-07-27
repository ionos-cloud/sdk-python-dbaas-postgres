# PaginationLinks

URLs to navigate the different pages. 
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **prev** | **str** | URL (with offset and limit parameters) of the previous page; only present if offset is greater than 0.  | [optional] [readonly]  |
| **var_self** | **str** | URL (with offset and limit parameters) of the current page.  | [optional] [readonly]  |
| **next** | **str** | URL (with offset and limit parameters) of the next page; only present if offset + limit is less than the total number of elements.  | [optional] [readonly]  |


