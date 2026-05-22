# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_caption** | **str** |  | [optional] 
**device_config** | **str** |  | [optional] 
**device_family** | **str** |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_name** | **str** |  | [optional] 
**device_pid** | **str** |  | [optional] 
**device_type** | **str** |  | [optional] 
**device_validity_start** | **datetime** |  | [optional] 
**device_validity_end** | **datetime** |  | [optional] 
**profile_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**system_profile**|[**SystemProfile**](SystemProfile.md)|profile_id

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
from plantscreen.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


