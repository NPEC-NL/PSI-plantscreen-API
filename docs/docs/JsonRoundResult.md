# JsonRoundResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_round_result** | [**Round**](Round.md) |  | [optional] 
**result** | [**Round**](Round.md)| alias for **json_round_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------
****|[**Round**](RoundOrder.md)|order****|[**Round**](ActionGroup.md)|action_group****|[**Round**](ActionProtocol.md)|action_protocol****|[**Round**](Tray.md)|trays****|[**Round**](PlantHeight.md)|plant_heights****|[**Round**](SystemLog.md)|system_logs

### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_round_result import JsonRoundResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRoundResult from a JSON string
json_round_result_instance = JsonRoundResult.from_json(json)
# print the JSON string representation of the object
print(JsonRoundResult.to_json())

# convert the object into a dict
json_round_result_dict = json_round_result_instance.to_dict()
# create an instance of JsonRoundResult from a dict
json_round_result_from_dict = JsonRoundResult.from_dict(json_round_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


