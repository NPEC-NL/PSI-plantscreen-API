# JsonMscCalibrationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_calibration_result** | [**MscCalibration**](MscCalibration.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_msc_calibration_result import JsonMscCalibrationResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscCalibrationResult from a JSON string
json_msc_calibration_result_instance = JsonMscCalibrationResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscCalibrationResult.to_json())

# convert the object into a dict
json_msc_calibration_result_dict = json_msc_calibration_result_instance.to_dict()
# create an instance of JsonMscCalibrationResult from a dict
json_msc_calibration_result_from_dict = JsonMscCalibrationResult.from_dict(json_msc_calibration_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


