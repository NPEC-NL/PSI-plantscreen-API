# JsonIrUsedParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_ir_used_param_result** | [**List[Parameter]**](Parameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_ir_used_param_result import JsonIrUsedParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIrUsedParamResult from a JSON string
json_ir_used_param_result_instance = JsonIrUsedParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonIrUsedParamResult.to_json())

# convert the object into a dict
json_ir_used_param_result_dict = json_ir_used_param_result_instance.to_dict()
# create an instance of JsonIrUsedParamResult from a dict
json_ir_used_param_result_from_dict = JsonIrUsedParamResult.from_dict(json_ir_used_param_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


