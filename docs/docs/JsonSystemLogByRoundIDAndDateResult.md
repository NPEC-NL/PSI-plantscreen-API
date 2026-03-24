# JsonSystemLogByRoundIDAndDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_system_log_by_round_id_and_date_result** | [**List[SystemLog]**](SystemLog.md) |  | [optional] 
**result** | [**List[SystemLog]**](SystemLog.md)| alias for **json_system_log_by_round_id_and_date_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_system_log_by_round_id_and_date_result import JsonSystemLogByRoundIDAndDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSystemLogByRoundIDAndDateResult from a JSON string
json_system_log_by_round_id_and_date_result_instance = JsonSystemLogByRoundIDAndDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonSystemLogByRoundIDAndDateResult.to_json())

# convert the object into a dict
json_system_log_by_round_id_and_date_result_dict = json_system_log_by_round_id_and_date_result_instance.to_dict()
# create an instance of JsonSystemLogByRoundIDAndDateResult from a dict
json_system_log_by_round_id_and_date_result_from_dict = JsonSystemLogByRoundIDAndDateResult.from_dict(json_system_log_by_round_id_and_date_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


