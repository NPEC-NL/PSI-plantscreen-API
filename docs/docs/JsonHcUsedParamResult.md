# JsonHcUsedParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_used_param_result** | [**List[Parameter]**](Parameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_hc_used_param_result import JsonHcUsedParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcUsedParamResult from a JSON string
json_hc_used_param_result_instance = JsonHcUsedParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcUsedParamResult.to_json())

# convert the object into a dict
json_hc_used_param_result_dict = json_hc_used_param_result_instance.to_dict()
# create an instance of JsonHcUsedParamResult from a dict
json_hc_used_param_result_from_dict = JsonHcUsedParamResult.from_dict(json_hc_used_param_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


