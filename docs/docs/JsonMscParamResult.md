# JsonMscParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_param_result** | [**Parameter**](Parameter.md) |  | [optional] 
**result** | [**Parameter**](Parameter.md)| alias for **json_msc_param_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_msc_param_result import JsonMscParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscParamResult from a JSON string
json_msc_param_result_instance = JsonMscParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscParamResult.to_json())

# convert the object into a dict
json_msc_param_result_dict = json_msc_param_result_instance.to_dict()
# create an instance of JsonMscParamResult from a dict
json_msc_param_result_from_dict = JsonMscParamResult.from_dict(json_msc_param_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


