# LogType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_type** | **str** |  | [optional] 


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
system_logs_by_daterange | List[[**object**](SystemLog.md)] | SystemLogApi | SystemLogDateLogType | LogType->type, start->start, stop->stop
## Example

```python
from plantscreen.models.log_type import LogType

# TODO update the JSON string below
json = "{}"
# create an instance of LogType from a JSON string
log_type_instance = LogType.from_json(json)
# print the JSON string representation of the object
print(LogType.to_json())

# convert the object into a dict
log_type_dict = log_type_instance.to_dict()
# create an instance of LogType from a dict
log_type_from_dict = LogType.from_dict(log_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


