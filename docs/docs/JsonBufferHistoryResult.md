# JsonBufferHistoryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_buffer_history_result** | [**BufferHistory**](BufferHistory.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_buffer_history_result import JsonBufferHistoryResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonBufferHistoryResult from a JSON string
json_buffer_history_result_instance = JsonBufferHistoryResult.from_json(json)
# print the JSON string representation of the object
print(JsonBufferHistoryResult.to_json())

# convert the object into a dict
json_buffer_history_result_dict = json_buffer_history_result_instance.to_dict()
# create an instance of JsonBufferHistoryResult from a dict
json_buffer_history_result_from_dict = JsonBufferHistoryResult.from_dict(json_buffer_history_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


