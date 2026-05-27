# RoundOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**experiment**|[**Experiment**](Experiment.md)|experiment_id**round**|[**Round**](Round.md)|round_id

### Implicit Relationships

All the listed relationships are available as properties on the model instance

Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships

All the listed relationships are available as methods on the model instance.

Parameters written in **bold** are taken automatically from the model instance, when calling the method you have to
supply the non-bold parameters

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


