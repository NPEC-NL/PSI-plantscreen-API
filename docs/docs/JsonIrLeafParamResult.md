# JsonIrLeafParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_ir_leaf_param_result** | [**List[StatisticLeafParameter]**](StatisticLeafParameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_ir_leaf_param_result import JsonIrLeafParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIrLeafParamResult from a JSON string
json_ir_leaf_param_result_instance = JsonIrLeafParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonIrLeafParamResult.to_json())

# convert the object into a dict
json_ir_leaf_param_result_dict = json_ir_leaf_param_result_instance.to_dict()
# create an instance of JsonIrLeafParamResult from a dict
json_ir_leaf_param_result_from_dict = JsonIrLeafParamResult.from_dict(json_ir_leaf_param_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


