# SprayAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_pid** | **str** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**liquid_amount** | **int** |  | [optional] 
**liquid_name** | **str** |  | [optional] 
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**round_id** | **int** |  | [optional] 
**spray_action_date** | **datetime** |  | [optional] 
**spray_action_id** | **int** |  | [optional] 
**spray_time** | **int** |  | [optional] 
**tray_area** | **str** |  | [optional] 
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 
**tray_profile_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**action**|[**Action**](Action.md)|action_id**device**|[**Device**](Device.md)|device_id**experiment**|[**Experiment**](Experiment.md)|experiment_id**plant**|[**Plant**](Plant.md)|plant_id**round**|[**Round**](Round.md)|round_id**tray**|[**Tray**](Tray.md)|tray_id**tray_profile**|[**TrayProfile**](TrayProfile.md)|tray_profile_id

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
from plantscreen.models.spray_action import SprayAction

# TODO update the JSON string below
json = "{}"
# create an instance of SprayAction from a JSON string
spray_action_instance = SprayAction.from_json(json)
# print the JSON string representation of the object
print(SprayAction.to_json())

# convert the object into a dict
spray_action_dict = spray_action_instance.to_dict()
# create an instance of SprayAction from a dict
spray_action_from_dict = SprayAction.from_dict(spray_action_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


