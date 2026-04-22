# JsonRgbMeasureExtendedDataResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_rgb_measure_extended_data_result** | [**MeasureExtendedData**](MeasureExtendedData.md) |  | [optional] 
**result** | [**MeasureExtendedData**](MeasureExtendedData.md)| alias for **json_rgb_measure_extended_data_result**  | 

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
## Example

```python
from plantscreen.models.json_rgb_measure_extended_data_result import JsonRgbMeasureExtendedDataResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRgbMeasureExtendedDataResult from a JSON string
json_rgb_measure_extended_data_result_instance = JsonRgbMeasureExtendedDataResult.from_json(json)
# print the JSON string representation of the object
print(JsonRgbMeasureExtendedDataResult.to_json())

# convert the object into a dict
json_rgb_measure_extended_data_result_dict = json_rgb_measure_extended_data_result_instance.to_dict()
# create an instance of JsonRgbMeasureExtendedDataResult from a dict
json_rgb_measure_extended_data_result_from_dict = JsonRgbMeasureExtendedDataResult.from_dict(json_rgb_measure_extended_data_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


