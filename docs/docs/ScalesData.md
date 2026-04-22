# ScalesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_pid** | **str** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**measure_date** | **datetime** |  | [optional] 
**measure_id** | **int** |  | [optional] 
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**plant_weight** | **float** |  | [optional] 
**round_id** | **int** |  | [optional] 
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 
**tray_area** | **str** |  | [optional] 
**tray_profile_id** | **int** |  | [optional] 
**watered** | **bool** |  | [optional] 


## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
**action**|[**int**](Action.md)|action_id**device**|[**int**](Device.md)|device_id**experiment**|[**int**](Experiment.md)|experiment_id**plant**|[**int**](Plant.md)|plant_id**round**|[**int**](Round.md)|round_id**tray**|[**int**](Tray.md)|tray_id**tray_profile**|[**int**](TrayProfile.md)|tray_profile_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.scales_data import ScalesData

# TODO update the JSON string below
json = "{}"
# create an instance of ScalesData from a JSON string
scales_data_instance = ScalesData.from_json(json)
# print the JSON string representation of the object
print(ScalesData.to_json())

# convert the object into a dict
scales_data_dict = scales_data_instance.to_dict()
# create an instance of ScalesData from a dict
scales_data_from_dict = ScalesData.from_dict(scales_data_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


