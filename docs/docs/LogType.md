# LogType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_type** | **str** |  | [optional] 


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
system_logs_by_daterange | List[[**SystemLog**](SystemLog.md)] | SystemLogApi | SystemLogDateLogType | **LogType->type**, start->start, stop->stop
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
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


