# JsonRgbUsedParamColorResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_rgb_used_param_color_result** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**result** | [**List[Parameter]**](Parameter.md)| alias for **json_rgb_used_param_color_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_rgb_used_param_color_result import JsonRgbUsedParamColorResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRgbUsedParamColorResult from a JSON string
json_rgb_used_param_color_result_instance = JsonRgbUsedParamColorResult.from_json(json)
# print the JSON string representation of the object
print(JsonRgbUsedParamColorResult.to_json())

# convert the object into a dict
json_rgb_used_param_color_result_dict = json_rgb_used_param_color_result_instance.to_dict()
# create an instance of JsonRgbUsedParamColorResult from a dict
json_rgb_used_param_color_result_from_dict = JsonRgbUsedParamColorResult.from_dict(json_rgb_used_param_color_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


