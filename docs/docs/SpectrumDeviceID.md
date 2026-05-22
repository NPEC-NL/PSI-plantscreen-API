# SpectrumDeviceID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spectrum_device_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**spectrum_device**|[**SpectrumDevice**](SpectrumDevice.md)|spectrum_device_id

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
from plantscreen.models.spectrum_device_id import SpectrumDeviceID

# TODO update the JSON string below
json = "{}"
# create an instance of SpectrumDeviceID from a JSON string
spectrum_device_id_instance = SpectrumDeviceID.from_json(json)
# print the JSON string representation of the object
print(SpectrumDeviceID.to_json())

# convert the object into a dict
spectrum_device_id_dict = spectrum_device_id_instance.to_dict()
# create an instance of SpectrumDeviceID from a dict
spectrum_device_id_from_dict = SpectrumDeviceID.from_dict(spectrum_device_id_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


