# JsonRgbMeasureExtendedDataByIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_rgb_measure_extended_data_by_id_result** | [**MeasureExtendedData**](MeasureExtendedData.md) |  | [optional] 
**result** | [**MeasureExtendedData**](MeasureExtendedData.md)| alias for **json_rgb_measure_extended_data_by_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_rgb_measure_extended_data_by_id_result import JsonRgbMeasureExtendedDataByIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRgbMeasureExtendedDataByIDResult from a JSON string
json_rgb_measure_extended_data_by_id_result_instance = JsonRgbMeasureExtendedDataByIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonRgbMeasureExtendedDataByIDResult.to_json())

# convert the object into a dict
json_rgb_measure_extended_data_by_id_result_dict = json_rgb_measure_extended_data_by_id_result_instance.to_dict()
# create an instance of JsonRgbMeasureExtendedDataByIDResult from a dict
json_rgb_measure_extended_data_by_id_result_from_dict = JsonRgbMeasureExtendedDataByIDResult.from_dict(json_rgb_measure_extended_data_by_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


