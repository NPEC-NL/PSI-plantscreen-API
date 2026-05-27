# JsonSystemLogTypeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_system_log_type_result** | [**List[LogType]**](LogType.md) |  | [optional] 
**result** | [**List[LogType]**](LogType.md)| alias for **json_system_log_type_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_system_log_type_result import JsonSystemLogTypeResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSystemLogTypeResult from a JSON string
json_system_log_type_result_instance = JsonSystemLogTypeResult.from_json(json)
# print the JSON string representation of the object
print(JsonSystemLogTypeResult.to_json())

# convert the object into a dict
json_system_log_type_result_dict = json_system_log_type_result_instance.to_dict()
# create an instance of JsonSystemLogTypeResult from a dict
json_system_log_type_result_from_dict = JsonSystemLogTypeResult.from_dict(json_system_log_type_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


