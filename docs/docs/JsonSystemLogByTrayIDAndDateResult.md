# JsonSystemLogByTrayIDAndDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_system_log_by_tray_id_and_date_result** | [**List[SystemLog]**](SystemLog.md) |  | [optional] 
**result** | [**List[SystemLog]**](SystemLog.md)| alias for **json_system_log_by_tray_id_and_date_result**  | 

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
from plantscreen.models.json_system_log_by_tray_id_and_date_result import JsonSystemLogByTrayIDAndDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSystemLogByTrayIDAndDateResult from a JSON string
json_system_log_by_tray_id_and_date_result_instance = JsonSystemLogByTrayIDAndDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonSystemLogByTrayIDAndDateResult.to_json())

# convert the object into a dict
json_system_log_by_tray_id_and_date_result_dict = json_system_log_by_tray_id_and_date_result_instance.to_dict()
# create an instance of JsonSystemLogByTrayIDAndDateResult from a dict
json_system_log_by_tray_id_and_date_result_from_dict = JsonSystemLogByTrayIDAndDateResult.from_dict(json_system_log_by_tray_id_and_date_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


