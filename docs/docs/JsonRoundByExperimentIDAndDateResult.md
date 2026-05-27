# JsonRoundByExperimentIDAndDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_round_by_experiment_id_and_date_result** | [**List[Round]**](Round.md) |  | [optional] 
**result** | [**List[Round]**](Round.md)| alias for **json_round_by_experiment_id_and_date_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_round_by_experiment_id_and_date_result import JsonRoundByExperimentIDAndDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRoundByExperimentIDAndDateResult from a JSON string
json_round_by_experiment_id_and_date_result_instance = JsonRoundByExperimentIDAndDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonRoundByExperimentIDAndDateResult.to_json())

# convert the object into a dict
json_round_by_experiment_id_and_date_result_dict = json_round_by_experiment_id_and_date_result_instance.to_dict()
# create an instance of JsonRoundByExperimentIDAndDateResult from a dict
json_round_by_experiment_id_and_date_result_from_dict = JsonRoundByExperimentIDAndDateResult.from_dict(json_round_by_experiment_id_and_date_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


