# JsonRgbImagingByIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_rgb_imaging_by_id_result** | [**Imaging**](Imaging.md) |  | [optional] 
**result** | [**Imaging**](Imaging.md)| alias for **json_rgb_imaging_by_id_result**  | 

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
from plantscreen.models.json_rgb_imaging_by_id_result import JsonRgbImagingByIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRgbImagingByIDResult from a JSON string
json_rgb_imaging_by_id_result_instance = JsonRgbImagingByIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonRgbImagingByIDResult.to_json())

# convert the object into a dict
json_rgb_imaging_by_id_result_dict = json_rgb_imaging_by_id_result_instance.to_dict()
# create an instance of JsonRgbImagingByIDResult from a dict
json_rgb_imaging_by_id_result_from_dict = JsonRgbImagingByIDResult.from_dict(json_rgb_imaging_by_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


