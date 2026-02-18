# JsonTrayByRoundIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_tray_by_round_id_result** | [**List[Tray]**](Tray.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_tray_by_round_id_result import JsonTrayByRoundIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonTrayByRoundIDResult from a JSON string
json_tray_by_round_id_result_instance = JsonTrayByRoundIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonTrayByRoundIDResult.to_json())

# convert the object into a dict
json_tray_by_round_id_result_dict = json_tray_by_round_id_result_instance.to_dict()
# create an instance of JsonTrayByRoundIDResult from a dict
json_tray_by_round_id_result_from_dict = JsonTrayByRoundIDResult.from_dict(json_tray_by_round_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


