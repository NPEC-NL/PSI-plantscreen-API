# HcRgbImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**device_pid** | **str** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**measure_angle** | **int** |  | [optional] 
**measure_id** | **int** |  | [optional] 
**rgb_image_path** | **str** | filetype | [optional] 
**round_id** | **int** |  | [optional] 
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
**device**|[**int**](Device.md)|device_id**experiment**|[**int**](Experiment.md)|experiment_id**round**|[**int**](Round.md)|round_id**tray**|[**int**](Tray.md)|tray_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.hc_rgb_image import HcRgbImage

# TODO update the JSON string below
json = "{}"
# create an instance of HcRgbImage from a JSON string
hc_rgb_image_instance = HcRgbImage.from_json(json)
# print the JSON string representation of the object
print(HcRgbImage.to_json())

# convert the object into a dict
hc_rgb_image_dict = hc_rgb_image_instance.to_dict()
# create an instance of HcRgbImage from a dict
hc_rgb_image_from_dict = HcRgbImage.from_dict(hc_rgb_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


