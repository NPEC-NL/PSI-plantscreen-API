# SpectrumDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spectrum_device_id** | **int** |  | [optional] 
**spectrum_device_serial** | **str** |  | [optional] 
**spectrum_device_wavelengths_json** | [**SpectrumDeviceWavelengthsJSONWrapper**](SpectrumDeviceWavelengthsJSONWrapper.md) |  | [optional] 


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
values_by_date | List[[**object**](SpectrumValues.md)] | SpectrumDeviceApi | SpectrumValuesDateDevice | SpectrumDeviceID->id, start->start, stop->stop
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
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


