# JsonNoteResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_note_result** | [**List[ExperimentNote]**](ExperimentNote.md) |  | [optional] 
**result** | [**List[ExperimentNote]**](ExperimentNote.md)| alias for **json_note_result**  | 

## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------


### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.json_note_result import JsonNoteResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonNoteResult from a JSON string
json_note_result_instance = JsonNoteResult.from_json(json)
# print the JSON string representation of the object
print(JsonNoteResult.to_json())

# convert the object into a dict
json_note_result_dict = json_note_result_instance.to_dict()
# create an instance of JsonNoteResult from a dict
json_note_result_from_dict = JsonNoteResult.from_dict(json_note_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


