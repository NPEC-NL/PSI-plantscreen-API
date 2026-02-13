# SpectrumDeviceWavelengthsJSONWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[float]** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**s_const** | **str** |  | [optional] 

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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


