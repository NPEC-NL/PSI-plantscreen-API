# JsonScan3dImagingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_scan3d_imaging_result** | [**List[Scan3DImaging]**](Scan3DImaging.md) |  | [optional] 
**result** | [**List[Scan3DImaging]**](Scan3DImaging.md)| alias for **json_scan3d_imaging_result**  | 

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
from plantscreen.models.json_scan3d_imaging_result import JsonScan3dImagingResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonScan3dImagingResult from a JSON string
json_scan3d_imaging_result_instance = JsonScan3dImagingResult.from_json(json)
# print the JSON string representation of the object
print(JsonScan3dImagingResult.to_json())

# convert the object into a dict
json_scan3d_imaging_result_dict = json_scan3d_imaging_result_instance.to_dict()
# create an instance of JsonScan3dImagingResult from a dict
json_scan3d_imaging_result_from_dict = JsonScan3dImagingResult.from_dict(json_scan3d_imaging_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


