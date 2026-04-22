# JsonSystemProfileActiveResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_system_profile_active_result** | [**SystemProfile**](SystemProfile.md) |  | [optional] 
**result** | [**SystemProfile**](SystemProfile.md)| alias for **json_system_profile_active_result**  | 

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
from plantscreen.models.json_system_profile_active_result import JsonSystemProfileActiveResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSystemProfileActiveResult from a JSON string
json_system_profile_active_result_instance = JsonSystemProfileActiveResult.from_json(json)
# print the JSON string representation of the object
print(JsonSystemProfileActiveResult.to_json())

# convert the object into a dict
json_system_profile_active_result_dict = json_system_profile_active_result_instance.to_dict()
# create an instance of JsonSystemProfileActiveResult from a dict
json_system_profile_active_result_from_dict = JsonSystemProfileActiveResult.from_dict(json_system_profile_active_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


