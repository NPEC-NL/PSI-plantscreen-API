# JsonIrImagingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_ir_imaging_result** | [**List[Imaging]**](Imaging.md) |  | [optional] 
**result** | [**List[Imaging]**](Imaging.md)| alias for **json_ir_imaging_result**  | 

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
from plantscreen.models.json_ir_imaging_result import JsonIrImagingResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIrImagingResult from a JSON string
json_ir_imaging_result_instance = JsonIrImagingResult.from_json(json)
# print the JSON string representation of the object
print(JsonIrImagingResult.to_json())

# convert the object into a dict
json_ir_imaging_result_dict = json_ir_imaging_result_instance.to_dict()
# create an instance of JsonIrImagingResult from a dict
json_ir_imaging_result_from_dict = JsonIrImagingResult.from_dict(json_ir_imaging_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


