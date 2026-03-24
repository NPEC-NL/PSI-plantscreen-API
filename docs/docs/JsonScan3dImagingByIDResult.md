# JsonScan3dImagingByIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_scan3d_imaging_by_id_result** | [**Scan3DImaging**](Scan3DImaging.md) |  | [optional] 
**result** | [**Scan3DImaging**](Scan3DImaging.md)| alias for **json_scan3d_imaging_by_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_scan3d_imaging_by_id_result import JsonScan3dImagingByIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonScan3dImagingByIDResult from a JSON string
json_scan3d_imaging_by_id_result_instance = JsonScan3dImagingByIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonScan3dImagingByIDResult.to_json())

# convert the object into a dict
json_scan3d_imaging_by_id_result_dict = json_scan3d_imaging_by_id_result_instance.to_dict()
# create an instance of JsonScan3dImagingByIDResult from a dict
json_scan3d_imaging_by_id_result_from_dict = JsonScan3dImagingByIDResult.from_dict(json_scan3d_imaging_by_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


