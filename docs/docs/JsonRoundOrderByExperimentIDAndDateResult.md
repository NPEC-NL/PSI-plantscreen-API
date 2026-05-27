# JsonRoundOrderByExperimentIDAndDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_round_order_by_experiment_id_and_date_result** | [**List[RoundOrder]**](RoundOrder.md) |  | [optional] 
**result** | [**List[RoundOrder]**](RoundOrder.md)| alias for **json_round_order_by_experiment_id_and_date_result**  | 

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
from plantscreen.models.json_round_order_by_experiment_id_and_date_result import JsonRoundOrderByExperimentIDAndDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRoundOrderByExperimentIDAndDateResult from a JSON string
json_round_order_by_experiment_id_and_date_result_instance = JsonRoundOrderByExperimentIDAndDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonRoundOrderByExperimentIDAndDateResult.to_json())

# convert the object into a dict
json_round_order_by_experiment_id_and_date_result_dict = json_round_order_by_experiment_id_and_date_result_instance.to_dict()
# create an instance of JsonRoundOrderByExperimentIDAndDateResult from a dict
json_round_order_by_experiment_id_and_date_result_from_dict = JsonRoundOrderByExperimentIDAndDateResult.from_dict(json_round_order_by_experiment_id_and_date_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


