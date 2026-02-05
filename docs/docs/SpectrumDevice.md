# SpectrumDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spectrum_device_id** | **int** |  | [optional] 
**spectrum_device_serial** | **str** |  | [optional] 
**spectrum_device_wavelengths_json** | [**SpectrumDeviceWavelengthsJSONWrapper**](SpectrumDeviceWavelengthsJSONWrapper.md) |  | [optional] 

## Example

```python
from plantscreen.models.spectrum_device import SpectrumDevice

# TODO update the JSON string below
json = "{}"
# create an instance of SpectrumDevice from a JSON string
spectrum_device_instance = SpectrumDevice.from_json(json)
# print the JSON string representation of the object
print(SpectrumDevice.to_json())

# convert the object into a dict
spectrum_device_dict = spectrum_device_instance.to_dict()
# create an instance of SpectrumDevice from a dict
spectrum_device_from_dict = SpectrumDevice.from_dict(spectrum_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


