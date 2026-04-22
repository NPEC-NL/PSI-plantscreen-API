# JsonRoundOrderByExperimentIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_round_order_by_experiment_id_result** | [**List[RoundOrder]**](RoundOrder.md) |  | [optional] 
**result** | [**List[RoundOrder]**](RoundOrder.md)| alias for **json_round_order_by_experiment_id_result**  | 

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
from plantscreen.models.json_round_order_by_experiment_id_result import JsonRoundOrderByExperimentIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRoundOrderByExperimentIDResult from a JSON string
json_round_order_by_experiment_id_result_instance = JsonRoundOrderByExperimentIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonRoundOrderByExperimentIDResult.to_json())

# convert the object into a dict
json_round_order_by_experiment_id_result_dict = json_round_order_by_experiment_id_result_instance.to_dict()
# create an instance of JsonRoundOrderByExperimentIDResult from a dict
json_round_order_by_experiment_id_result_from_dict = JsonRoundOrderByExperimentIDResult.from_dict(json_round_order_by_experiment_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


