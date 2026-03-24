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

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------
**tray_type**|[**int**](TrayType.md)|tray_type_id

### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------
tray_profile | List[[**object**](TrayProfile.md)]] | TrayApi |  | TrayIDscales_mapping | List[[**object**](ScalesMapping.md)]] | TrayApi |  | TrayIDplants | List[[**object**](Plant.md)]] | PlantApi |  | TrayIDplant_reference_weights | List[[**object**](PlantWeightReference.md)]] | ScalesApi |  | TrayIDsystem_logs | List[[**object**](SystemLog.md)]] | SystemLogApi |  | TrayID

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


