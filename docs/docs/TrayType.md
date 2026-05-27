# TrayType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** |  | [optional] 
**type_info** | **str** |  | [optional] 
**type_mask_bottom** | **str** |  | [optional] 
**type_mask_side** | **str** |  | [optional] 
**type_mask_top** | **str** |  | [optional] 
**type_mask_under_side** | **str** |  | [optional] 
**type_name** | **str** |  | [optional] 
**type_size_x** | **int** |  | [optional] 
**type_size_y** | **int** |  | [optional] 
**type_size_z** | **int** |  | [optional] 


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
## Example

```python
from plantscreen.models.tray_type import TrayType

# TODO update the JSON string below
json = "{}"
# create an instance of TrayType from a JSON string
tray_type_instance = TrayType.from_json(json)
# print the JSON string representation of the object
print(TrayType.to_json())

# convert the object into a dict
tray_type_dict = tray_type_instance.to_dict()
# create an instance of TrayType from a dict
tray_type_from_dict = TrayType.from_dict(tray_type_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


