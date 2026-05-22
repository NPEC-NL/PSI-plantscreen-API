# JsonBufferHistoryByDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_buffer_history_by_date_result** | [**List[BufferHistory]**](BufferHistory.md) |  | [optional] 
**result** | [**List[BufferHistory]**](BufferHistory.md)| alias for **json_buffer_history_by_date_result**  | 

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
from plantscreen.models.json_buffer_history_by_date_result import JsonBufferHistoryByDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonBufferHistoryByDateResult from a JSON string
json_buffer_history_by_date_result_instance = JsonBufferHistoryByDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonBufferHistoryByDateResult.to_json())

# convert the object into a dict
json_buffer_history_by_date_result_dict = json_buffer_history_by_date_result_instance.to_dict()
# create an instance of JsonBufferHistoryByDateResult from a dict
json_buffer_history_by_date_result_from_dict = JsonBufferHistoryByDateResult.from_dict(json_buffer_history_by_date_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


