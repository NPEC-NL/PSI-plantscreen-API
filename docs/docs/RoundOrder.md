# RoundOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
**experiment**|[**int**](Experiment.md)|experiment_id**round**|[**int**](Round.md)|round_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.round_order import RoundOrder

# TODO update the JSON string below
json = "{}"
# create an instance of RoundOrder from a JSON string
round_order_instance = RoundOrder.from_json(json)
# print the JSON string representation of the object
print(RoundOrder.to_json())

# convert the object into a dict
round_order_dict = round_order_instance.to_dict()
# create an instance of RoundOrder from a dict
round_order_from_dict = RoundOrder.from_dict(round_order_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


