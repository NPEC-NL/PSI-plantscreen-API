# JsonSpectrumDeviceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_spectrum_device_result** | [**SpectrumDevice**](SpectrumDevice.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_spectrum_device_result import JsonSpectrumDeviceResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSpectrumDeviceResult from a JSON string
json_spectrum_device_result_instance = JsonSpectrumDeviceResult.from_json(json)
# print the JSON string representation of the object
print(JsonSpectrumDeviceResult.to_json())

# convert the object into a dict
json_spectrum_device_result_dict = json_spectrum_device_result_instance.to_dict()
# create an instance of JsonSpectrumDeviceResult from a dict
json_spectrum_device_result_from_dict = JsonSpectrumDeviceResult.from_dict(json_spectrum_device_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


