# JsonFcLeafParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_fc_leaf_param_result** | [**List[LeafParameter]**](LeafParameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_fc_leaf_param_result import JsonFcLeafParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFcLeafParamResult from a JSON string
json_fc_leaf_param_result_instance = JsonFcLeafParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonFcLeafParamResult.to_json())

# convert the object into a dict
json_fc_leaf_param_result_dict = json_fc_leaf_param_result_instance.to_dict()
# create an instance of JsonFcLeafParamResult from a dict
json_fc_leaf_param_result_from_dict = JsonFcLeafParamResult.from_dict(json_fc_leaf_param_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


