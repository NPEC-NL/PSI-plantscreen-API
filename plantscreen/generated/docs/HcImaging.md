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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


