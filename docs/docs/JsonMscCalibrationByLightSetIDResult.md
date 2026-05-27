# JsonMscCalibrationByLightSetIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_calibration_by_light_set_id_result** | [**MscCalibration**](MscCalibration.md) |  | [optional] 
**result** | [**MscCalibration**](MscCalibration.md)| alias for **json_msc_calibration_by_light_set_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_msc_calibration_by_light_set_id_result import JsonMscCalibrationByLightSetIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscCalibrationByLightSetIDResult from a JSON string
json_msc_calibration_by_light_set_id_result_instance = JsonMscCalibrationByLightSetIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscCalibrationByLightSetIDResult.to_json())

# convert the object into a dict
json_msc_calibration_by_light_set_id_result_dict = json_msc_calibration_by_light_set_id_result_instance.to_dict()
# create an instance of JsonMscCalibrationByLightSetIDResult from a dict
json_msc_calibration_by_light_set_id_result_from_dict = JsonMscCalibrationByLightSetIDResult.from_dict(json_msc_calibration_by_light_set_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


