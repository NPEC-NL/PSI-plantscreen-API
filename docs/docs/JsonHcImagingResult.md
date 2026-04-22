# JsonHcImagingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_imaging_result** | [**List[HcImaging]**](HcImaging.md) |  | [optional] 
**result** | [**List[HcImaging]**](HcImaging.md)| alias for **json_hc_imaging_result**  | 

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
from plantscreen.models.json_hc_imaging_result import JsonHcImagingResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcImagingResult from a JSON string
json_hc_imaging_result_instance = JsonHcImagingResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcImagingResult.to_json())

# convert the object into a dict
json_hc_imaging_result_dict = json_hc_imaging_result_instance.to_dict()
# create an instance of JsonHcImagingResult from a dict
json_hc_imaging_result_from_dict = JsonHcImagingResult.from_dict(json_hc_imaging_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


