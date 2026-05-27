# JsonHcRgbImageByMeasureIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_rgb_image_by_measure_id_result** | [**HcRgbImage**](HcRgbImage.md) |  | [optional] 
**result** | [**HcRgbImage**](HcRgbImage.md)| alias for **json_hc_rgb_image_by_measure_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_hc_rgb_image_by_measure_id_result import JsonHcRgbImageByMeasureIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcRgbImageByMeasureIDResult from a JSON string
json_hc_rgb_image_by_measure_id_result_instance = JsonHcRgbImageByMeasureIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcRgbImageByMeasureIDResult.to_json())

# convert the object into a dict
json_hc_rgb_image_by_measure_id_result_dict = json_hc_rgb_image_by_measure_id_result_instance.to_dict()
# create an instance of JsonHcRgbImageByMeasureIDResult from a dict
json_hc_rgb_image_by_measure_id_result_from_dict = JsonHcRgbImageByMeasureIDResult.from_dict(json_hc_rgb_image_by_measure_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


