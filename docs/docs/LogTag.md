# LogTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_tag** | **str** |  | [optional] 


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
system_logs_by_daterange | List[[**SystemLog**](SystemLog.md)] | SystemLogApi | SystemLogDateLogTag | **LogTag->tag**, start->start, stop->stop
## Example

```python
from plantscreen.models.log_tag import LogTag

# TODO update the JSON string below
json = "{}"
# create an instance of LogTag from a JSON string
log_tag_instance = LogTag.from_json(json)
# print the JSON string representation of the object
print(LogTag.to_json())

# convert the object into a dict
log_tag_dict = log_tag_instance.to_dict()
# create an instance of LogTag from a dict
log_tag_from_dict = LogTag.from_dict(log_tag_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


