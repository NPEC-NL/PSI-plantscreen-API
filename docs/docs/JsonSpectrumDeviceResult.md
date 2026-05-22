# JsonSpectrumDeviceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_spectrum_device_result** | [**SpectrumDevice**](SpectrumDevice.md) |  | [optional] 
**result** | [**SpectrumDevice**](SpectrumDevice.md)| alias for **json_spectrum_device_result**  | 

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


