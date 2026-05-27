# HcImaging


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
**calibration_white_header_path** | **str** | filetype | [optional] 
**calibration_white_content_path** | **str** | filetype | [optional] 
**calibration_dark_header_path** | **str** | filetype | [optional] 
**calibration_dark_content_path** | **str** | filetype | [optional] 
**data_content_path** | **str** | filetype | [optional] 
**data_header_path** | **str** | filetype | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**action**|[**Action**](Action.md)|action_id**device**|[**Device**](Device.md)|device_id**experiment**|[**Experiment**](Experiment.md)|experiment_id**round**|[**Round**](Round.md)|round_id**tray**|[**Tray**](Tray.md)|tray_id**tray_profile**|[**TrayProfile**](TrayProfile.md)|tray_profile_id

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
from plantscreen.models.hc_imaging import HcImaging

# TODO update the JSON string below
json = "{}"
# create an instance of HcImaging from a JSON string
hc_imaging_instance = HcImaging.from_json(json)
# print the JSON string representation of the object
print(HcImaging.to_json())

# convert the object into a dict
hc_imaging_dict = hc_imaging_instance.to_dict()
# create an instance of HcImaging from a dict
hc_imaging_from_dict = HcImaging.from_dict(hc_imaging_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


