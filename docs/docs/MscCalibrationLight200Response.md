# MscCalibrationLight200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_calibration_light_by_id_result** | [**MscCalibrationLight**](MscCalibrationLight.md) |  | 
**json_msc_calibration_light_result** | [**List[MscCalibrationLight]**](MscCalibrationLight.md) |  | 


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
from plantscreen.models.msc_calibration_light200_response import MscCalibrationLight200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MscCalibrationLight200Response from a JSON string
msc_calibration_light200_response_instance = MscCalibrationLight200Response.from_json(json)
# print the JSON string representation of the object
print(MscCalibrationLight200Response.to_json())

# convert the object into a dict
msc_calibration_light200_response_dict = msc_calibration_light200_response_instance.to_dict()
# create an instance of MscCalibrationLight200Response from a dict
msc_calibration_light200_response_from_dict = MscCalibrationLight200Response.from_dict(msc_calibration_light200_response_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


