# DatasetNewRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the new dataset | 
**slug** | **str** | The slug that the dataset should be created with | [optional] 
**owner_slug** | **str** | The owner&#39;s username | [optional] 
**license_name** | **str** | The license that should be associated with the dataset | [optional] [default to 'unknown']
**subtitle** | **str** | The subtitle to be set on the dataset | [optional] 
**description** | **str** | The description to be set on the dataset | [optional] [default to '']
**files** | [**list[UploadFile]**](UploadFile.md) | A list of files that should be associated with the dataset | 
**is_private** | **bool** | Whether or not the dataset should be private | [optional] [default to True]
**convert_to_csv** | **bool** | Whether or not a tabular dataset should be converted to csv | [optional] [default to True]
**category_ids** | **list[str]** | A list of tag IDs to associated with the dataset | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


