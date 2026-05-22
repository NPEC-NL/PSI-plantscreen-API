# BufferHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buffer_occasion** | **str** |  | [optional] 
**buffer_state_date** | **datetime** |  | [optional] 
**buffer_state_id** | **int** |  | [optional] 
**buffer_state_path** | **str** | filetype | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------


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
from plantscreen.models.buffer_history import BufferHistory

# TODO update the JSON string below
json = "{}"
# create an instance of BufferHistory from a JSON string
buffer_history_instance = BufferHistory.from_json(json)
# print the JSON string representation of the object
print(BufferHistory.to_json())

# convert the object into a dict
buffer_history_dict = buffer_history_instance.to_dict()
# create an instance of BufferHistory from a dict
buffer_history_from_dict = BufferHistory.from_dict(buffer_history_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


