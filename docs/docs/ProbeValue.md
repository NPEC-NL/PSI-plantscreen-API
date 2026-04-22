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
Name | Model | Linked Via
------------ | ------------- | -------------
**probe**|[**int**](Probe.md)|probe_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


