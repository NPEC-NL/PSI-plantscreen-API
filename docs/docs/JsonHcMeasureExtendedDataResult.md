# JsonHcMeasureExtendedDataResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_measure_extended_data_result** | [**MeasureExtendedData**](MeasureExtendedData.md) |  | [optional] 
**result** | [**MeasureExtendedData**](MeasureExtendedData.md)| alias for **json_hc_measure_extended_data_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_hc_measure_extended_data_result import JsonHcMeasureExtendedDataResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcMeasureExtendedDataResult from a JSON string
json_hc_measure_extended_data_result_instance = JsonHcMeasureExtendedDataResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcMeasureExtendedDataResult.to_json())

# convert the object into a dict
json_hc_measure_extended_data_result_dict = json_hc_measure_extended_data_result_instance.to_dict()
# create an instance of JsonHcMeasureExtendedDataResult from a dict
json_hc_measure_extended_data_result_from_dict = JsonHcMeasureExtendedDataResult.from_dict(json_hc_measure_extended_data_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


