# Action


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_date_start** | **datetime** |  | [optional] 
**action_done** | **bool** |  | [optional] 
**action_group_id** | **int** |  | [optional] 
**action_id** | **int** |  | [optional] 
**action_running** | **bool** |  | [optional] 
**action_status** | **str** |  | [optional] 
**experiment_id** | **int** |  | [optional] 


## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------
**action_group**|[**int**](ActionGroup.md)|action_group_id**experiment**|[**int**](Experiment.md)|experiment_id

### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print(Action.to_json())

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_from_dict = Action.from_dict(action_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


