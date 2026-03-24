# MscCalibration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calibration_date** | **datetime** |  | [optional] 
**calibration_id** | **int** |  | [optional] 
**calibration_image_path** | **str** | filetype | [optional] 
**camera_exposure** | **int** |  | [optional] 
**camera_gain** | **int** |  | [optional] 
**light_set_id** | **int** |  | [optional] 


## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.msc_calibration import MscCalibration

# TODO update the JSON string below
json = "{}"
# create an instance of MscCalibration from a JSON string
msc_calibration_instance = MscCalibration.from_json(json)
# print the JSON string representation of the object
print(MscCalibration.to_json())

# convert the object into a dict
msc_calibration_dict = msc_calibration_instance.to_dict()
# create an instance of MscCalibration from a dict
msc_calibration_from_dict = MscCalibration.from_dict(msc_calibration_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


