# JsonFcImagingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_fc_imaging_result** | [**List[FcImaging]**](FcImaging.md) |  | [optional] 
**result** | [**List[FcImaging]**](FcImaging.md)| alias for **json_fc_imaging_result**  | 

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
from plantscreen.models.json_fc_imaging_result import JsonFcImagingResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFcImagingResult from a JSON string
json_fc_imaging_result_instance = JsonFcImagingResult.from_json(json)
# print the JSON string representation of the object
print(JsonFcImagingResult.to_json())

# convert the object into a dict
json_fc_imaging_result_dict = json_fc_imaging_result_instance.to_dict()
# create an instance of JsonFcImagingResult from a dict
json_fc_imaging_result_from_dict = JsonFcImagingResult.from_dict(json_fc_imaging_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


