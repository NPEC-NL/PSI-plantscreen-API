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

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**action**|[**Action**](Action.md)|action_id**experiment**|[**Experiment**](Experiment.md)|experiment_id**round**|[**Round**](Round.md)|round_id

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


