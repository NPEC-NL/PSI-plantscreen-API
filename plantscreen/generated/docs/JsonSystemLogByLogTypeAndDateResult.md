# JsonSystemLogByLogTypeAndDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_system_log_by_log_type_and_date_result** | [**List[SystemLog]**](SystemLog.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_system_log_by_log_type_and_date_result import JsonSystemLogByLogTypeAndDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSystemLogByLogTypeAndDateResult from a JSON string
json_system_log_by_log_type_and_date_result_instance = JsonSystemLogByLogTypeAndDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonSystemLogByLogTypeAndDateResult.to_json())

# convert the object into a dict
json_system_log_by_log_type_and_date_result_dict = json_system_log_by_log_type_and_date_result_instance.to_dict()
# create an instance of JsonSystemLogByLogTypeAndDateResult from a dict
json_system_log_by_log_type_and_date_result_from_dict = JsonSystemLogByLogTypeAndDateResult.from_dict(json_system_log_by_log_type_and_date_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


