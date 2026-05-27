# JsonSpectrumValuesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_spectrum_values_result** | [**List[SpectrumValues]**](SpectrumValues.md) |  | [optional] 
**result** | [**List[SpectrumValues]**](SpectrumValues.md)| alias for **json_spectrum_values_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_spectrum_values_result import JsonSpectrumValuesResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSpectrumValuesResult from a JSON string
json_spectrum_values_result_instance = JsonSpectrumValuesResult.from_json(json)
# print the JSON string representation of the object
print(JsonSpectrumValuesResult.to_json())

# convert the object into a dict
json_spectrum_values_result_dict = json_spectrum_values_result_instance.to_dict()
# create an instance of JsonSpectrumValuesResult from a dict
json_spectrum_values_result_from_dict = JsonSpectrumValuesResult.from_dict(json_spectrum_values_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


