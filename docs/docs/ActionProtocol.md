# ActionProtocol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **int** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**protocol_body** | **str** |  | [optional] 
**protocol_date_changed** | **datetime** |  | [optional] 
**protocol_id** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 


## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------
**action**|[**int**](Action.md)|action_id**experiment**|[**int**](Experiment.md)|experiment_id**round**|[**int**](Round.md)|round_id

### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.action_protocol import ActionProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of ActionProtocol from a JSON string
action_protocol_instance = ActionProtocol.from_json(json)
# print the JSON string representation of the object
print(ActionProtocol.to_json())

# convert the object into a dict
action_protocol_dict = action_protocol_instance.to_dict()
# create an instance of ActionProtocol from a dict
action_protocol_from_dict = ActionProtocol.from_dict(action_protocol_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


