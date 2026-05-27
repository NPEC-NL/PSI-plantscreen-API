# JsonSystemProfileIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_system_profile_id_result** | [**List[ProfileIDWrapper]**](ProfileIDWrapper.md) |  | [optional] 
**result** | [**List[ProfileIDWrapper]**](ProfileIDWrapper.md)| alias for **json_system_profile_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_system_profile_id_result import JsonSystemProfileIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSystemProfileIDResult from a JSON string
json_system_profile_id_result_instance = JsonSystemProfileIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonSystemProfileIDResult.to_json())

# convert the object into a dict
json_system_profile_id_result_dict = json_system_profile_id_result_instance.to_dict()
# create an instance of JsonSystemProfileIDResult from a dict
json_system_profile_id_result_from_dict = JsonSystemProfileIDResult.from_dict(json_system_profile_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


