# SpectrumValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spectrum_device_id** | **int** |  | [optional] 
**spectrum_path** | **str** | filetype | [optional] 
**spectrum_record_date** | **datetime** |  | [optional] 


## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
**spectrum_device**|[**int**](SpectrumDevice.md)|spectrum_device_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.spectrum_values import SpectrumValues

# TODO update the JSON string below
json = "{}"
# create an instance of SpectrumValues from a JSON string
spectrum_values_instance = SpectrumValues.from_json(json)
# print the JSON string representation of the object
print(SpectrumValues.to_json())

# convert the object into a dict
spectrum_values_dict = spectrum_values_instance.to_dict()
# create an instance of SpectrumValues from a dict
spectrum_values_from_dict = SpectrumValues.from_dict(spectrum_values_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


