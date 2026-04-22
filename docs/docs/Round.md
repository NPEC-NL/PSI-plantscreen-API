# Round


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **int** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**round_date_start** | **datetime** |  | [optional] 
**round_date_stop** | **datetime** |  | [optional] 
**round_done** | **bool** |  | [optional] 
**round_id** | **int** |  | [optional] 
**round_protocol_path** | **str** | filetype | [optional] 
**round_status** | **str** |  | [optional] 


## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
**action**|[**int**](Action.md)|action_id**experiment**|[**int**](Experiment.md)|experiment_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------
order | [**object**](RoundOrder.md) | RoundApi |  | RoundID->id
action_group | [**object**](ActionGroup.md) | ActionApi |  | RoundID->id
action_protocol | [**object**](ActionProtocol.md) | ActionApi |  | RoundID->id
trays | List[[**object**](Tray.md)] | TrayApi |  | RoundID->id
plant_heights | List[[**object**](PlantHeight.md)] | RoundApi |  | RoundID->id
system_logs | List[[**object**](SystemLog.md)] | SystemLogApi |  | RoundID->id

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
system_logs_by_daterange | List[[**object**](SystemLog.md)] | SystemLogApi | SystemLogDateRound | RoundID->id, start->start, stop->stop
## Example

```python
from plantscreen.models.round import Round

# TODO update the JSON string below
json = "{}"
# create an instance of Round from a JSON string
round_instance = Round.from_json(json)
# print the JSON string representation of the object
print(Round.to_json())

# convert the object into a dict
round_dict = round_instance.to_dict()
# create an instance of Round from a dict
round_from_dict = Round.from_dict(round_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


