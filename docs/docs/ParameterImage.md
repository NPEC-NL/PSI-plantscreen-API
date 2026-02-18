# ParameterImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyse_id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_pid** | **str** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**measure_angle** | **int** |  | [optional] 
**measure_id** | **int** |  | [optional] 
**parameter_id** | **int** |  | [optional] 
**parameter_image_path** | **str** | filetype | [optional] 
**parameter_name** | **str** |  | [optional] 
**round_id** | **int** |  | [optional] 
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 

## Example

```python
from plantscreen.models.parameter_image import ParameterImage

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterImage from a JSON string
parameter_image_instance = ParameterImage.from_json(json)
# print the JSON string representation of the object
print(ParameterImage.to_json())

# convert the object into a dict
parameter_image_dict = parameter_image_instance.to_dict()
# create an instance of ParameterImage from a dict
parameter_image_from_dict = ParameterImage.from_dict(parameter_image_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


