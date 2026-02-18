# JsonMscMeasureExtendedDataResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_measure_extended_data_result** | [**MeasureExtendedData**](MeasureExtendedData.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_msc_measure_extended_data_result import JsonMscMeasureExtendedDataResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscMeasureExtendedDataResult from a JSON string
json_msc_measure_extended_data_result_instance = JsonMscMeasureExtendedDataResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscMeasureExtendedDataResult.to_json())

# convert the object into a dict
json_msc_measure_extended_data_result_dict = json_msc_measure_extended_data_result_instance.to_dict()
# create an instance of JsonMscMeasureExtendedDataResult from a dict
json_msc_measure_extended_data_result_from_dict = JsonMscMeasureExtendedDataResult.from_dict(json_msc_measure_extended_data_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


