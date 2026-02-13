# JsonHcParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_param_result** | [**Parameter**](Parameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_hc_param_result import JsonHcParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcParamResult from a JSON string
json_hc_param_result_instance = JsonHcParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcParamResult.to_json())

# convert the object into a dict
json_hc_param_result_dict = json_hc_param_result_instance.to_dict()
# create an instance of JsonHcParamResult from a dict
json_hc_param_result_from_dict = JsonHcParamResult.from_dict(json_hc_param_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


