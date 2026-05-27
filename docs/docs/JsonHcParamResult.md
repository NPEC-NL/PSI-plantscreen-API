# JsonHcParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_param_result** | [**Parameter**](Parameter.md) |  | [optional] 
**result** | [**Parameter**](Parameter.md)| alias for **json_hc_param_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_hc_param_result import JsonHcParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcParamResult from a JSON string
json_hc_param_result_instance = JsonHcParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcParamResult.to_json())

# convert the object into a dict
json_hc_param_result_dict = json_hc_param_result_instance.to_dict()
# create an instance of JsonHcParamResult from a dict
json_hc_param_result_from_dict = JsonHcParamResult.from_dict(json_hc_param_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


