# FcImaging


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
**protocol_path** | **str** | filetype | [optional] 
**round_id** | **int** |  | [optional] 
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 
**tray_profile_id** | **int** |  | [optional] 
**tar_path** | **str** | filetype | [optional] 

## Example

```python
from plantscreen.models.fc_imaging import FcImaging

# TODO update the JSON string below
json = "{}"
# create an instance of FcImaging from a JSON string
fc_imaging_instance = FcImaging.from_json(json)
# print the JSON string representation of the object
print(FcImaging.to_json())

# convert the object into a dict
fc_imaging_dict = fc_imaging_instance.to_dict()
# create an instance of FcImaging from a dict
fc_imaging_from_dict = FcImaging.from_dict(fc_imaging_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


