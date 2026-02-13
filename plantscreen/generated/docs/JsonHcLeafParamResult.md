# JsonHcLeafParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_leaf_param_result** | [**List[StatisticLeafParameter]**](StatisticLeafParameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_hc_leaf_param_result import JsonHcLeafParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcLeafParamResult from a JSON string
json_hc_leaf_param_result_instance = JsonHcLeafParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcLeafParamResult.to_json())

# convert the object into a dict
json_hc_leaf_param_result_dict = json_hc_leaf_param_result_instance.to_dict()
# create an instance of JsonHcLeafParamResult from a dict
json_hc_leaf_param_result_from_dict = JsonHcLeafParamResult.from_dict(json_hc_leaf_param_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


