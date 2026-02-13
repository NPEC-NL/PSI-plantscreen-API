# JsonRgbLeafParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_rgb_leaf_param_result** | [**List[LeafParameter]**](LeafParameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_rgb_leaf_param_result import JsonRgbLeafParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRgbLeafParamResult from a JSON string
json_rgb_leaf_param_result_instance = JsonRgbLeafParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonRgbLeafParamResult.to_json())

# convert the object into a dict
json_rgb_leaf_param_result_dict = json_rgb_leaf_param_result_instance.to_dict()
# create an instance of JsonRgbLeafParamResult from a dict
json_rgb_leaf_param_result_from_dict = JsonRgbLeafParamResult.from_dict(json_rgb_leaf_param_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


