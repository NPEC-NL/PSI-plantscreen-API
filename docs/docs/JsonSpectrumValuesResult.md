# JsonSpectrumValuesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_spectrum_values_result** | [**List[SpectrumValues]**](SpectrumValues.md) |  | [optional] 

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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


