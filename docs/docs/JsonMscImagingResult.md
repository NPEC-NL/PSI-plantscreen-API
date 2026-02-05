# JsonMscImagingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_imaging_result** | [**List[Imaging]**](Imaging.md) |  | [optional] 

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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


