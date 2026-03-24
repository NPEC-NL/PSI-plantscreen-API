# JsonScalesMeasureResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_scales_measure_result** | [**List[ScalesData]**](ScalesData.md) |  | [optional] 
**result** | [**List[ScalesData]**](ScalesData.md)| alias for **json_scales_measure_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_scales_measure_result import JsonScalesMeasureResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonScalesMeasureResult from a JSON string
json_scales_measure_result_instance = JsonScalesMeasureResult.from_json(json)
# print the JSON string representation of the object
print(JsonScalesMeasureResult.to_json())

# convert the object into a dict
json_scales_measure_result_dict = json_scales_measure_result_instance.to_dict()
# create an instance of JsonScalesMeasureResult from a dict
json_scales_measure_result_from_dict = JsonScalesMeasureResult.from_dict(json_scales_measure_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


