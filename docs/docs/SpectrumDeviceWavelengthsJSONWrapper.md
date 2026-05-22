# SpectrumDeviceWavelengthsJSONWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[float]** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**s_const** | **str** |  | [optional] 


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
from plantscreen.models.spectrum_device_wavelengths_json_wrapper import SpectrumDeviceWavelengthsJSONWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SpectrumDeviceWavelengthsJSONWrapper from a JSON string
spectrum_device_wavelengths_json_wrapper_instance = SpectrumDeviceWavelengthsJSONWrapper.from_json(json)
# print the JSON string representation of the object
print(SpectrumDeviceWavelengthsJSONWrapper.to_json())

# convert the object into a dict
spectrum_device_wavelengths_json_wrapper_dict = spectrum_device_wavelengths_json_wrapper_instance.to_dict()
# create an instance of SpectrumDeviceWavelengthsJSONWrapper from a dict
spectrum_device_wavelengths_json_wrapper_from_dict = SpectrumDeviceWavelengthsJSONWrapper.from_dict(spectrum_device_wavelengths_json_wrapper_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


