# ExperimentNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **int** |  | [optional] 
**note_created_date** | **datetime** |  | [optional] 
**note_id** | **int** |  | [optional] 
**note_text** | **str** |  | [optional] 
**owner_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**experiment**|[**Experiment**](Experiment.md)|experiment_id**owner**|[**Owner**](Owner.md)|owner_id

### Implicit Relationships

All the listed relationships are available as properties on the model instance

Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships

All the listed relationships are available as methods on the model instance.

Parameters written in **bold** are taken automatically from the model instance, when calling the method you have to
supply the non-bold parameters

Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.experiment_note import ExperimentNote

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentNote from a JSON string
experiment_note_instance = ExperimentNote.from_json(json)
# print the JSON string representation of the object
print(ExperimentNote.to_json())

# convert the object into a dict
experiment_note_dict = experiment_note_instance.to_dict()
# create an instance of ExperimentNote from a dict
experiment_note_from_dict = ExperimentNote.from_dict(experiment_note_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


