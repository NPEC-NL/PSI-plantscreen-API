# JsonScan3dUsedParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_scan3d_used_param_result** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**result** | [**List[Parameter]**](Parameter.md)| alias for **json_scan3d_used_param_result**  | 

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
from plantscreen.models.json_scan3d_used_param_result import JsonScan3dUsedParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonScan3dUsedParamResult from a JSON string
json_scan3d_used_param_result_instance = JsonScan3dUsedParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonScan3dUsedParamResult.to_json())

# convert the object into a dict
json_scan3d_used_param_result_dict = json_scan3d_used_param_result_instance.to_dict()
# create an instance of JsonScan3dUsedParamResult from a dict
json_scan3d_used_param_result_from_dict = JsonScan3dUsedParamResult.from_dict(json_scan3d_used_param_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


