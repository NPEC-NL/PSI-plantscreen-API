# JsonIrImagingByIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_ir_imaging_by_id_result** | [**Imaging**](Imaging.md) |  | [optional] 
**result** | [**Imaging**](Imaging.md)| alias for **json_ir_imaging_by_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_ir_imaging_by_id_result import JsonIrImagingByIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIrImagingByIDResult from a JSON string
json_ir_imaging_by_id_result_instance = JsonIrImagingByIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonIrImagingByIDResult.to_json())

# convert the object into a dict
json_ir_imaging_by_id_result_dict = json_ir_imaging_by_id_result_instance.to_dict()
# create an instance of JsonIrImagingByIDResult from a dict
json_ir_imaging_by_id_result_from_dict = JsonIrImagingByIDResult.from_dict(json_ir_imaging_by_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


