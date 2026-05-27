# ActionGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_protocol_id** | **int** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**group_caption** | **str** |  | [optional] 
**group_id** | **int** |  | [optional] 
**group_repeating_protocol** | **str** |  | [optional] 


## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------
**experiment**|[**int**](Experiment.md)|experiment_id

### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.action_group import ActionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ActionGroup from a JSON string
action_group_instance = ActionGroup.from_json(json)
# print the JSON string representation of the object
print(ActionGroup.to_json())

# convert the object into a dict
action_group_dict = action_group_instance.to_dict()
# create an instance of ActionGroup from a dict
action_group_from_dict = ActionGroup.from_dict(action_group_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


