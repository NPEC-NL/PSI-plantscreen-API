# Scan3DImaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_pid** | **str** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**measure_angle** | **int** |  | [optional] 
**measure_date** | **datetime** |  | [optional] 
**measure_height** | **int** |  | [optional] 
**measure_id** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 
**tray_profile_id** | **int** |  | [optional] 
**scan3_d_model_path** | **str** | filetype | [optional] 


## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
**action**|[**int**](Action.md)|action_id**device**|[**int**](Device.md)|device_id**experiment**|[**int**](Experiment.md)|experiment_id**round**|[**int**](Round.md)|round_id**tray**|[**int**](Tray.md)|tray_id**tray_profile**|[**int**](TrayProfile.md)|tray_profile_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.scan3_d_imaging import Scan3DImaging

# TODO update the JSON string below
json = "{}"
# create an instance of Scan3DImaging from a JSON string
scan3_d_imaging_instance = Scan3DImaging.from_json(json)
# print the JSON string representation of the object
print(Scan3DImaging.to_json())

# convert the object into a dict
scan3_d_imaging_dict = scan3_d_imaging_instance.to_dict()
# create an instance of Scan3DImaging from a dict
scan3_d_imaging_from_dict = Scan3DImaging.from_dict(scan3_d_imaging_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


