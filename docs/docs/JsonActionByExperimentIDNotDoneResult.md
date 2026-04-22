# JsonActionByExperimentIDNotDoneResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_action_by_experiment_id_not_done_result** | [**List[Action]**](Action.md) |  | [optional] 
**result** | [**List[Action]**](Action.md)| alias for **json_action_by_experiment_id_not_done_result**  | 

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
from plantscreen.models.json_action_by_experiment_id_not_done_result import JsonActionByExperimentIDNotDoneResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonActionByExperimentIDNotDoneResult from a JSON string
json_action_by_experiment_id_not_done_result_instance = JsonActionByExperimentIDNotDoneResult.from_json(json)
# print the JSON string representation of the object
print(JsonActionByExperimentIDNotDoneResult.to_json())

# convert the object into a dict
json_action_by_experiment_id_not_done_result_dict = json_action_by_experiment_id_not_done_result_instance.to_dict()
# create an instance of JsonActionByExperimentIDNotDoneResult from a dict
json_action_by_experiment_id_not_done_result_from_dict = JsonActionByExperimentIDNotDoneResult.from_dict(json_action_by_experiment_id_not_done_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


