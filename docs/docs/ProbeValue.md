# ProbeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probe_id** | **int** |  | [optional] 
**probe_name** | **str** |  | [optional] 
**probe_unit** | **str** |  | [optional] 
**probe_value** | **float** |  | [optional] 
**record_date** | **datetime** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**probe**|[**Probe**](Probe.md)|probe_id

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
from plantscreen.models.probe_value import ProbeValue

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeValue from a JSON string
probe_value_instance = ProbeValue.from_json(json)
# print the JSON string representation of the object
print(ProbeValue.to_json())

# convert the object into a dict
probe_value_dict = probe_value_instance.to_dict()
# create an instance of ProbeValue from a dict
probe_value_from_dict = ProbeValue.from_dict(probe_value_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


