# MscCalibrationLight200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_calibration_light_by_id_result** | [**MscCalibrationLight**](MscCalibrationLight.md) |  | [optional] 
**json_msc_calibration_light_result** | [**List[MscCalibrationLight]**](MscCalibrationLight.md) |  | [optional] 


## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------


### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
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


