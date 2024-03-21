# ModelInstanceUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overview** | **str** | The overview of the model instance (markdown) | [optional] 
**usage** | **str** | The description of how to use the model instance (markdown) | [optional] 
**license_name** | **str** | The license that should be associated with the model instance | [optional] [default to 'Apache 2.0']
**fine_tunable** | **bool** | Whether the model instance is fine tunable | [optional] [default to True]
**training_data** | **list[str]** | A list of training data (urls or names) | [optional] 
**model_instance_type** | **str** | Whether the model instance is a base model, external variant, internal variant, or unspecified | [optional] 
**base_model_instance** | **str** | If this is an internal variant, the &#x60;{owner-slug}/{model-slug}/{framework}/{instance-slug}&#x60; of the base model instance | [optional] 
**external_base_model_url** | **int** | If this is an external variant, a URL to the base model | [optional] 
**update_mask** | **str** | Describes which fields to update | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


