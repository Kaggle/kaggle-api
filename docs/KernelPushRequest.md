# KernelPushRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The kernel&#39;s ID number. One of &#x60;id&#x60; and &#x60;slug&#x60; are required. If both are specified, &#x60;id&#x60; will be preferred | [optional] 
**slug** | **str** | The full slug of the kernel to push to, in the format &#x60;USERNAME/KERNEL-SLUG&#x60;. The kernel slug must be the title lowercased with dashes (&#x60;-&#x60;) replacing spaces. One of &#x60;id&#x60; and &#x60;slug&#x60; are required. If both are specified, &#x60;id&#x60; will be preferred | [optional] 
**new_title** | **str** | The title to be set on the kernel | [optional] 
**text** | **str** | The kernel&#39;s source code | 
**language** | **str** | The language that the kernel is written in | 
**kernel_type** | **str** | The type of kernel. Cannot be changed once the kernel has been created | 
**is_private** | **bool** | Whether or not the kernel should be private | [optional] 
**enable_gpu** | **bool** | Whether or not the kernel should run on a GPU | [optional] 
**enable_tpu** | **bool** | Whether or not the kernel should run on a TPU | [optional] 
**enable_internet** | **bool** | Whether or not the kernel should be able to access the internet | [optional] 
**dataset_data_sources** | **list[str]** | A list of dataset data sources that the kernel should use. Each dataset is specified as &#x60;USERNAME/DATASET-SLUG&#x60; | [optional] 
**competition_data_sources** | **list[str]** | A list of competition data sources that the kernel should use | [optional] 
**kernel_data_sources** | **list[str]** | A list of kernel data sources that the kernel should use. Each dataset is specified as &#x60;USERNAME/KERNEL-SLUG&#x60; | [optional] 
**model_data_sources** | **list[str]** | A list of model data sources that the kernel should use. Each model is specified as &#x60;USERNAME/MODEL-SLUG/FRAMEWORK/VARIATION-SLUG/VERSION-NUMBER&#x60; | [optional] 
**category_ids** | **list[str]** | A list of tag IDs to associated with the kernel | [optional] 
**docker_image_pinning_type** | **str** | Which docker image to use for executing new versions going forward. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


