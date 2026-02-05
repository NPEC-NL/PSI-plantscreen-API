# RoundOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 

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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


