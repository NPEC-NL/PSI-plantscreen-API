# JsonMscCalibrationLightResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_calibration_light_result** | [**List[MscCalibrationLight]**](MscCalibrationLight.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_msc_calibration_light_result import JsonMscCalibrationLightResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscCalibrationLightResult from a JSON string
json_msc_calibration_light_result_instance = JsonMscCalibrationLightResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscCalibrationLightResult.to_json())

# convert the object into a dict
json_msc_calibration_light_result_dict = json_msc_calibration_light_result_instance.to_dict()
# create an instance of JsonMscCalibrationLightResult from a dict
json_msc_calibration_light_result_from_dict = JsonMscCalibrationLightResult.from_dict(json_msc_calibration_light_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


