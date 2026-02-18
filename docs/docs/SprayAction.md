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


