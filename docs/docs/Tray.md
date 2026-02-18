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


