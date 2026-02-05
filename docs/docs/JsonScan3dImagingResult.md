# JsonScan3dImagingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_scan3d_imaging_result** | [**List[Scan3DImaging]**](Scan3DImaging.md) |  | [optional] 

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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


