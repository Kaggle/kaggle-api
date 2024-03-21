# DatasetNewVersionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_notes** | **str** | The version notes for the new dataset version | 
**subtitle** | **str** | The subtitle to set on the dataset | [optional] 
**description** | **str** | The description to set on the dataset | [optional] 
**files** | [**list[UploadFile]**](UploadFile.md) | A list of files that should be associated with the dataset | 
**convert_to_csv** | **bool** | Whether or not a tabular dataset should be converted to csv | [optional] [default to True]
**category_ids** | **list[str]** | A list of tag IDs to associated with the dataset | [optional] 
**delete_old_versions** | **bool** | Whether or not all previous versions of the dataset should be deleted upon creating the new version | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


