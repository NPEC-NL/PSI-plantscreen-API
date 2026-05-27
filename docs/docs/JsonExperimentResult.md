# JsonExperimentResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_experiment_result** | [**Experiment**](Experiment.md) |  | [optional] 
**result** | [**Experiment**](Experiment.md)| alias for **json_experiment_result**  | 

## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
****|[**Experiment**](Round.md)|rounds****|[**Experiment**](RoundOrder.md)|round_orders****|[**Experiment**](ExperimentNote.md)|notes****|[**Experiment**](Action.md)|actions****|[**Experiment**](Action.md)|unfinished_actions

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.json_experiment_result import JsonExperimentResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonExperimentResult from a JSON string
json_experiment_result_instance = JsonExperimentResult.from_json(json)
# print the JSON string representation of the object
print(JsonExperimentResult.to_json())

# convert the object into a dict
json_experiment_result_dict = json_experiment_result_instance.to_dict()
# create an instance of JsonExperimentResult from a dict
json_experiment_result_from_dict = JsonExperimentResult.from_dict(json_experiment_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


