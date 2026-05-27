# Experiment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**experiment_info** | **str** |  | [optional] 
**experiment_name** | **str** |  | [optional] 
**experiment_status** | **str** |  | [optional] 
**owner_id** | **int** |  | [optional] 
**status_changed_date** | **datetime** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**owner**|[**Owner**](Owner.md)|owner_id

### Implicit Relationships

All the listed relationships are available as properties on the model instance

Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------
rounds | List[[**Round**](Round.md)] | RoundApi |  | **ExperimentID->id**
round_orders | List[[**RoundOrder**](RoundOrder.md)] | RoundApi |  | **ExperimentID->id**
notes | List[[**ExperimentNote**](ExperimentNote.md)] | ExperimentApi |  | **ExperimentID->id**
actions | List[[**Action**](Action.md)] | ActionApi |  | **ExperimentID->id**
unfinished_actions | List[[**Action**](Action.md)] | ActionApi |  | **ExperimentID->id**

### Parameterized Relationships

All the listed relationships are available as methods on the model instance.

Parameters written in **bold** are taken automatically from the model instance, when calling the method you have to
supply the non-bold parameters

Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
rounds_by_date | List[[**Round**](Round.md)] | RoundApi | RoundDateExperiment | **ExperimentID->id**, start->start, stop->stop
round_orders_by_date | List[[**RoundOrder**](RoundOrder.md)] | RoundApi | RoundOrderDateExperiment | **ExperimentID->id**, start->start, stop->stop
## Example

```python
from plantscreen.models.experiment import Experiment

# TODO update the JSON string below
json = "{}"
# create an instance of Experiment from a JSON string
experiment_instance = Experiment.from_json(json)
# print the JSON string representation of the object
print(Experiment.to_json())

# convert the object into a dict
experiment_dict = experiment_instance.to_dict()
# create an instance of Experiment from a dict
experiment_from_dict = Experiment.from_dict(experiment_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


