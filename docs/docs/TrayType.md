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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


