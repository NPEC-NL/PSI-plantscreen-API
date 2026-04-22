# JsonExperimentByDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_experiment_by_date_result** | [**List[Experiment]**](Experiment.md) |  | [optional] 
**result** | [**List[Experiment]**](Experiment.md)| alias for **json_experiment_by_date_result**  | 

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
from plantscreen.models.json_experiment_by_date_result import JsonExperimentByDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonExperimentByDateResult from a JSON string
json_experiment_by_date_result_instance = JsonExperimentByDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonExperimentByDateResult.to_json())

# convert the object into a dict
json_experiment_by_date_result_dict = json_experiment_by_date_result_instance.to_dict()
# create an instance of JsonExperimentByDateResult from a dict
json_experiment_by_date_result_from_dict = JsonExperimentByDateResult.from_dict(json_experiment_by_date_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


