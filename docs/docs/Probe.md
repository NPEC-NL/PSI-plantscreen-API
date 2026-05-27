# Probe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probe_family** | **str** |  | [optional] 
**probe_id** | **int** |  | [optional] 
**probe_name** | **str** |  | [optional] 
**probe_placement** | **str** |  | [optional] 
**probe_unit** | **str** |  | [optional] 
**probe_variable** | **str** |  | [optional] 


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
values_by_date | List[[**ProbeValue**](ProbeValue.md)] | ProbeApi | ProbeValueDateProbe | **ProbeID->id**, start->start, stop->stop
## Example

```python
from plantscreen.models.probe import Probe

# TODO update the JSON string below
json = "{}"
# create an instance of Probe from a JSON string
probe_instance = Probe.from_json(json)
# print the JSON string representation of the object
print(Probe.to_json())

# convert the object into a dict
probe_dict = probe_instance.to_dict()
# create an instance of Probe from a dict
probe_from_dict = Probe.from_dict(probe_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


