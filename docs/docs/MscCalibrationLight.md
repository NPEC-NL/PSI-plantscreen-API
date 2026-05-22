# MscCalibrationLight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calibration_id** | **int** |  | [optional] 
**calibration_light_id** | **int** |  | [optional] 
**calibration_light_level** | **int** |  | [optional] 
**light_caption** | **str** |  | [optional] 
**light_id** | **int** |  | [optional] 
**light_set_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------


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
from plantscreen.models.msc_calibration_light import MscCalibrationLight

# TODO update the JSON string below
json = "{}"
# create an instance of MscCalibrationLight from a JSON string
msc_calibration_light_instance = MscCalibrationLight.from_json(json)
# print the JSON string representation of the object
print(MscCalibrationLight.to_json())

# convert the object into a dict
msc_calibration_light_dict = msc_calibration_light_instance.to_dict()
# create an instance of MscCalibrationLight from a dict
msc_calibration_light_from_dict = MscCalibrationLight.from_dict(msc_calibration_light_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


