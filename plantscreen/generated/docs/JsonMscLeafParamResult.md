# JsonMscLeafParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_leaf_param_result** | [**List[StatisticLeafParameter]**](StatisticLeafParameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_msc_leaf_param_result import JsonMscLeafParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscLeafParamResult from a JSON string
json_msc_leaf_param_result_instance = JsonMscLeafParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscLeafParamResult.to_json())

# convert the object into a dict
json_msc_leaf_param_result_dict = json_msc_leaf_param_result_instance.to_dict()
# create an instance of JsonMscLeafParamResult from a dict
json_msc_leaf_param_result_from_dict = JsonMscLeafParamResult.from_dict(json_msc_leaf_param_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


