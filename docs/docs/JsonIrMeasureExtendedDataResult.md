# JsonIrMeasureExtendedDataResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_ir_measure_extended_data_result** | [**MeasureExtendedData**](MeasureExtendedData.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_ir_measure_extended_data_result import JsonIrMeasureExtendedDataResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIrMeasureExtendedDataResult from a JSON string
json_ir_measure_extended_data_result_instance = JsonIrMeasureExtendedDataResult.from_json(json)
# print the JSON string representation of the object
print(JsonIrMeasureExtendedDataResult.to_json())

# convert the object into a dict
json_ir_measure_extended_data_result_dict = json_ir_measure_extended_data_result_instance.to_dict()
# create an instance of JsonIrMeasureExtendedDataResult from a dict
json_ir_measure_extended_data_result_from_dict = JsonIrMeasureExtendedDataResult.from_dict(json_ir_measure_extended_data_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


