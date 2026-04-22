# JsonSystemLogByTrayIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_system_log_by_tray_id_result** | [**List[SystemLog]**](SystemLog.md) |  | [optional] 
**result** | [**List[SystemLog]**](SystemLog.md)| alias for **json_system_log_by_tray_id_result**  | 

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
from plantscreen.models.json_system_log_by_tray_id_result import JsonSystemLogByTrayIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSystemLogByTrayIDResult from a JSON string
json_system_log_by_tray_id_result_instance = JsonSystemLogByTrayIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonSystemLogByTrayIDResult.to_json())

# convert the object into a dict
json_system_log_by_tray_id_result_dict = json_system_log_by_tray_id_result_instance.to_dict()
# create an instance of JsonSystemLogByTrayIDResult from a dict
json_system_log_by_tray_id_result_from_dict = JsonSystemLogByTrayIDResult.from_dict(json_system_log_by_tray_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


