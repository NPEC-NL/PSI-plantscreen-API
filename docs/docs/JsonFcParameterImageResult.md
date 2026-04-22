# JsonFcParameterImageResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_fc_parameter_image_result** | [**List[ParameterImage]**](ParameterImage.md) |  | [optional] 
**result** | [**List[ParameterImage]**](ParameterImage.md)| alias for **json_fc_parameter_image_result**  | 

## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------


### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.json_fc_parameter_image_result import JsonFcParameterImageResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFcParameterImageResult from a JSON string
json_fc_parameter_image_result_instance = JsonFcParameterImageResult.from_json(json)
# print the JSON string representation of the object
print(JsonFcParameterImageResult.to_json())

# convert the object into a dict
json_fc_parameter_image_result_dict = json_fc_parameter_image_result_instance.to_dict()
# create an instance of JsonFcParameterImageResult from a dict
json_fc_parameter_image_result_from_dict = JsonFcParameterImageResult.from_dict(json_fc_parameter_image_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


