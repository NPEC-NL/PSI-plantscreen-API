# JsonScalesMeasureByIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_scales_measure_by_id_result** | [**ScalesData**](ScalesData.md) |  | [optional] 
**result** | [**ScalesData**](ScalesData.md)| alias for **json_scales_measure_by_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_scales_measure_by_id_result import JsonScalesMeasureByIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonScalesMeasureByIDResult from a JSON string
json_scales_measure_by_id_result_instance = JsonScalesMeasureByIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonScalesMeasureByIDResult.to_json())

# convert the object into a dict
json_scales_measure_by_id_result_dict = json_scales_measure_by_id_result_instance.to_dict()
# create an instance of JsonScalesMeasureByIDResult from a dict
json_scales_measure_by_id_result_from_dict = JsonScalesMeasureByIDResult.from_dict(json_scales_measure_by_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


