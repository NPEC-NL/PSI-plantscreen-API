# TrayProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_date_start** | **datetime** |  | [optional] 
**profile_date_stop** | **datetime** |  | [optional] 
**profile_id** | **int** |  | [optional] 
**profile_name** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**tray**|[**Tray**](Tray.md)|tray_id

### Implicit Relationships

All the listed relationships are available as properties on the model instance

Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------
tray_type | [**TrayType**](TrayType.md) | TrayApi |  | **ProfileID->id**
plants | List[[**Plant**](Plant.md)] | PlantApi |  | **ProfileID->id**

### Parameterized Relationships

All the listed relationships are available as methods on the model instance.

Parameters written in **bold** are taken automatically from the model instance, when calling the method you have to
supply the non-bold parameters

Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.tray_profile import TrayProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TrayProfile from a JSON string
tray_profile_instance = TrayProfile.from_json(json)
# print the JSON string representation of the object
print(TrayProfile.to_json())

# convert the object into a dict
tray_profile_dict = tray_profile_instance.to_dict()
# create an instance of TrayProfile from a dict
tray_profile_from_dict = TrayProfile.from_dict(tray_profile_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


