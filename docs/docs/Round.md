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

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**action**|[**Action**](Action.md)|action_id**experiment**|[**Experiment**](Experiment.md)|experiment_id

### Implicit Relationships

All the listed relationships are available as properties on the model instance

Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------
order | [**RoundOrder**](RoundOrder.md) | RoundApi |  | **RoundID->id**
action_group | [**ActionGroup**](ActionGroup.md) | ActionApi |  | **RoundID->id**
action_protocol | [**ActionProtocol**](ActionProtocol.md) | ActionApi |  | **RoundID->id**
trays | List[[**Tray**](Tray.md)] | TrayApi |  | **RoundID->id**
plant_heights | List[[**PlantHeight**](PlantHeight.md)] | RoundApi |  | **RoundID->id**
system_logs | List[[**SystemLog**](SystemLog.md)] | SystemLogApi |  | **RoundID->id**

### Parameterized Relationships

All the listed relationships are available as methods on the model instance.

Parameters written in **bold** are taken automatically from the model instance, when calling the method you have to
supply the non-bold parameters

Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
system_logs_by_daterange | List[[**SystemLog**](SystemLog.md)] | SystemLogApi | SystemLogDateRound | **RoundID->id**, start->start, stop->stop
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
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


