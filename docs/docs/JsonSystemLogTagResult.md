# JsonSystemLogTagResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_system_log_tag_result** | [**List[LogTag]**](LogTag.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_system_log_tag_result import JsonSystemLogTagResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSystemLogTagResult from a JSON string
json_system_log_tag_result_instance = JsonSystemLogTagResult.from_json(json)
# print the JSON string representation of the object
print(JsonSystemLogTagResult.to_json())

# convert the object into a dict
json_system_log_tag_result_dict = json_system_log_tag_result_instance.to_dict()
# create an instance of JsonSystemLogTagResult from a dict
json_system_log_tag_result_from_dict = JsonSystemLogTagResult.from_dict(json_system_log_tag_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


