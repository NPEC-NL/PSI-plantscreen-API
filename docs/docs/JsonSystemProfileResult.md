# JsonSystemProfileResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_system_profile_result** | [**SystemProfile**](SystemProfile.md) |  | [optional] 
**result** | [**SystemProfile**](SystemProfile.md)| alias for **json_system_profile_result**  | 

## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
****|[**SystemProfile**](Device.md)|devices

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.json_system_profile_result import JsonSystemProfileResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSystemProfileResult from a JSON string
json_system_profile_result_instance = JsonSystemProfileResult.from_json(json)
# print the JSON string representation of the object
print(JsonSystemProfileResult.to_json())

# convert the object into a dict
json_system_profile_result_dict = json_system_profile_result_instance.to_dict()
# create an instance of JsonSystemProfileResult from a dict
json_system_profile_result_from_dict = JsonSystemProfileResult.from_dict(json_system_profile_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


