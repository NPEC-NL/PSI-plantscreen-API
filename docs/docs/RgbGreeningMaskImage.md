# RgbGreeningMaskImage


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
**greening_picture_path** | **str** | filetype | [optional] 

## Example

```python
from plantscreen.models.rgb_greening_mask_image import RgbGreeningMaskImage

# TODO update the JSON string below
json = "{}"
# create an instance of RgbGreeningMaskImage from a JSON string
rgb_greening_mask_image_instance = RgbGreeningMaskImage.from_json(json)
# print the JSON string representation of the object
print(RgbGreeningMaskImage.to_json())

# convert the object into a dict
rgb_greening_mask_image_dict = rgb_greening_mask_image_instance.to_dict()
# create an instance of RgbGreeningMaskImage from a dict
rgb_greening_mask_image_from_dict = RgbGreeningMaskImage.from_dict(rgb_greening_mask_image_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


