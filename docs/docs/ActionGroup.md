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

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
**experiment**|[**int**](Experiment.md)|experiment_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


