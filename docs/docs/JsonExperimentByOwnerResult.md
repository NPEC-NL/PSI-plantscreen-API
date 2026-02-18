# JsonExperimentByOwnerResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_experiment_by_owner_result** | [**List[Experiment]**](Experiment.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_experiment_by_owner_result import JsonExperimentByOwnerResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonExperimentByOwnerResult from a JSON string
json_experiment_by_owner_result_instance = JsonExperimentByOwnerResult.from_json(json)
# print the JSON string representation of the object
print(JsonExperimentByOwnerResult.to_json())

# convert the object into a dict
json_experiment_by_owner_result_dict = json_experiment_by_owner_result_instance.to_dict()
# create an instance of JsonExperimentByOwnerResult from a dict
json_experiment_by_owner_result_from_dict = JsonExperimentByOwnerResult.from_dict(json_experiment_by_owner_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


