# JsonMscImagingByIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_imaging_by_id_result** | [**List[Imaging]**](Imaging.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_msc_imaging_by_id_result import JsonMscImagingByIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscImagingByIDResult from a JSON string
json_msc_imaging_by_id_result_instance = JsonMscImagingByIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscImagingByIDResult.to_json())

# convert the object into a dict
json_msc_imaging_by_id_result_dict = json_msc_imaging_by_id_result_instance.to_dict()
# create an instance of JsonMscImagingByIDResult from a dict
json_msc_imaging_by_id_result_from_dict = JsonMscImagingByIDResult.from_dict(json_msc_imaging_by_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


