# Tray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 
**tray_info** | **str** |  | [optional] 
**tray_status** | **str** |  | [optional] 
**tray_status_changed** | **datetime** |  | [optional] 
**tray_type_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**tray_type**|[**TrayType**](TrayType.md)|tray_type_id

### Implicit Relationships

All the listed relationships are available as properties on the model instance

Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------
tray_profile | [**TrayProfile**](TrayProfile.md) | TrayApi |  | **TrayID->id**
scales_mapping | [**ScalesMapping**](ScalesMapping.md) | TrayApi |  | **TrayID->id**
plants | List[[**Plant**](Plant.md)] | PlantApi |  | **TrayID->id**
plant_reference_weights | List[[**PlantWeightReference**](PlantWeightReference.md)] | ScalesApi |  | **TrayID->id**
system_logs | List[[**SystemLog**](SystemLog.md)] | SystemLogApi |  | **TrayID->id**

### Parameterized Relationships

All the listed relationships are available as methods on the model instance.

Parameters written in **bold** are taken automatically from the model instance, when calling the method you have to
supply the non-bold parameters

Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
tray_profile_used_by_daterange | List[[**TrayProfile**](TrayProfile.md)] | TrayApi | TrayProfileUsedTray | **TrayID->id**, start->start, stop->stop
tray_profile_used_at_time | List[[**TrayProfile**](TrayProfile.md)] | TrayApi | TrayProfileToDateTray | **TrayID->id**, var_date->var_date
plants_by_daterange | List[[**Plant**](Plant.md)] | PlantApi | PlantTrayProfileTray | **TrayID->id**, start->start, stop->stop
plant_reference_weights_at_time | List[[**PlantWeightReference**](PlantWeightReference.md)] | ScalesApi | ScalesWeightReferenceToDateTray | **TrayID->id**, date->date
system_logs_by_daterange | List[[**SystemLog**](SystemLog.md)] | SystemLogApi | SystemLogDateTray | **TrayID->id**, start->start, stop->stop
## Example

```python
from plantscreen.models.tray import Tray

# TODO update the JSON string below
json = "{}"
# create an instance of Tray from a JSON string
tray_instance = Tray.from_json(json)
# print the JSON string representation of the object
print(Tray.to_json())

# convert the object into a dict
tray_dict = tray_instance.to_dict()
# create an instance of Tray from a dict
tray_from_dict = Tray.from_dict(tray_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


