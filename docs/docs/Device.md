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
Name | Model | Linked Via
------------ | ------------- | -------------
**system_profile**|[**int**](SystemProfile.md)|profile_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


