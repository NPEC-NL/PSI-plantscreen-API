# JsonHcParameterImageResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_parameter_image_result** | [**List[ParameterImage]**](ParameterImage.md) |  | [optional] 
**result** | [**List[ParameterImage]**](ParameterImage.md)| alias for **json_hc_parameter_image_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_hc_parameter_image_result import JsonHcParameterImageResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcParameterImageResult from a JSON string
json_hc_parameter_image_result_instance = JsonHcParameterImageResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcParameterImageResult.to_json())

# convert the object into a dict
json_hc_parameter_image_result_dict = json_hc_parameter_image_result_instance.to_dict()
# create an instance of JsonHcParameterImageResult from a dict
json_hc_parameter_image_result_from_dict = JsonHcParameterImageResult.from_dict(json_hc_parameter_image_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


