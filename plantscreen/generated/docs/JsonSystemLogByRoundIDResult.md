# JsonSystemLogByRoundIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_system_log_by_round_id_result** | [**List[SystemLog]**](SystemLog.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_system_log_by_round_id_result import JsonSystemLogByRoundIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSystemLogByRoundIDResult from a JSON string
json_system_log_by_round_id_result_instance = JsonSystemLogByRoundIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonSystemLogByRoundIDResult.to_json())

# convert the object into a dict
json_system_log_by_round_id_result_dict = json_system_log_by_round_id_result_instance.to_dict()
# create an instance of JsonSystemLogByRoundIDResult from a dict
json_system_log_by_round_id_result_from_dict = JsonSystemLogByRoundIDResult.from_dict(json_system_log_by_round_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


