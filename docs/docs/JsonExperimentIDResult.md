# JsonExperimentIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_experiment_id_result** | [**List[ExperimentIDWrapper]**](ExperimentIDWrapper.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_experiment_id_result import JsonExperimentIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonExperimentIDResult from a JSON string
json_experiment_id_result_instance = JsonExperimentIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonExperimentIDResult.to_json())

# convert the object into a dict
json_experiment_id_result_dict = json_experiment_id_result_instance.to_dict()
# create an instance of JsonExperimentIDResult from a dict
json_experiment_id_result_from_dict = JsonExperimentIDResult.from_dict(json_experiment_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


