# JsonMscImagingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_imaging_result** | [**List[Imaging]**](Imaging.md) |  | [optional] 
**result** | [**List[Imaging]**](Imaging.md)| alias for **json_msc_imaging_result**  | 

## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------


### Implicit Relationships

All the listed relationships are available as properties on the model instance

Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships

All the listed relationships are available as methods on the model instance.

Parameters written in **bold** are taken automatically from the model instance, when calling the method you have to
supply the non-bold parameters

Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.json_msc_imaging_result import JsonMscImagingResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscImagingResult from a JSON string
json_msc_imaging_result_instance = JsonMscImagingResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscImagingResult.to_json())

# convert the object into a dict
json_msc_imaging_result_dict = json_msc_imaging_result_instance.to_dict()
# create an instance of JsonMscImagingResult from a dict
json_msc_imaging_result_from_dict = JsonMscImagingResult.from_dict(json_msc_imaging_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


