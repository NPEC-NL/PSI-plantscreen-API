# JsonFcMeasureExtendedDataByIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_fc_measure_extended_data_by_id_result** | [**MeasureExtendedData**](MeasureExtendedData.md) |  | [optional] 
**result** | [**MeasureExtendedData**](MeasureExtendedData.md)| alias for **json_fc_measure_extended_data_by_id_result**  | 

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
from plantscreen.models.json_fc_measure_extended_data_by_id_result import JsonFcMeasureExtendedDataByIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFcMeasureExtendedDataByIDResult from a JSON string
json_fc_measure_extended_data_by_id_result_instance = JsonFcMeasureExtendedDataByIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonFcMeasureExtendedDataByIDResult.to_json())

# convert the object into a dict
json_fc_measure_extended_data_by_id_result_dict = json_fc_measure_extended_data_by_id_result_instance.to_dict()
# create an instance of JsonFcMeasureExtendedDataByIDResult from a dict
json_fc_measure_extended_data_by_id_result_from_dict = JsonFcMeasureExtendedDataByIDResult.from_dict(json_fc_measure_extended_data_by_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


