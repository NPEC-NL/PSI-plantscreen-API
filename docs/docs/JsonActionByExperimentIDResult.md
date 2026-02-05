# JsonActionByExperimentIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_action_by_experiment_id_result** | [**List[Action]**](Action.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_action_by_experiment_id_result import JsonActionByExperimentIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonActionByExperimentIDResult from a JSON string
json_action_by_experiment_id_result_instance = JsonActionByExperimentIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonActionByExperimentIDResult.to_json())

# convert the object into a dict
json_action_by_experiment_id_result_dict = json_action_by_experiment_id_result_instance.to_dict()
# create an instance of JsonActionByExperimentIDResult from a dict
json_action_by_experiment_id_result_from_dict = JsonActionByExperimentIDResult.from_dict(json_action_by_experiment_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


