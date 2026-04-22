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
Name | Model | Linked Via
------------ | ------------- | -------------
**tray_type**|[**int**](TrayType.md)|tray_type_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------
tray_profile | [**object**](TrayProfile.md) | TrayApi |  | TrayID->id
scales_mapping | [**object**](ScalesMapping.md) | TrayApi |  | TrayID->id
plants | List[[**object**](Plant.md)] | PlantApi |  | TrayID->id
plant_reference_weights | List[[**object**](PlantWeightReference.md)] | ScalesApi |  | TrayID->id
system_logs | List[[**object**](SystemLog.md)] | SystemLogApi |  | TrayID->id

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
tray_profile_used_by_daterange | List[[**object**](TrayProfile.md)] | TrayApi | TrayProfileUsedTray | TrayID->id, start->start, stop->stop
tray_profile_used_at_time | List[[**object**](TrayProfile.md)] | TrayApi | TrayProfileToDateTray | TrayID->id, date->date
plants_by_daterange | List[[**object**](Plant.md)] | PlantApi | PlantTrayProfileTray | TrayID->id, start->start, stop->stop
plant_reference_weights_at_time | List[[**object**](PlantWeightReference.md)] | ScalesApi | ScalesWeightReferenceToDateTray | TrayID->id, date->date
system_logs_by_daterange | List[[**object**](SystemLog.md)] | SystemLogApi | SystemLogDateTray | TrayID->id, start->start, stop->stop
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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


