# JsonDeviceByProfileIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_device_by_profile_id_result** | [**List[Device]**](Device.md) |  | [optional] 
**result** | [**List[Device]**](Device.md)| alias for **json_device_by_profile_id_result**  | 

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
from plantscreen.models.json_device_by_profile_id_result import JsonDeviceByProfileIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDeviceByProfileIDResult from a JSON string
json_device_by_profile_id_result_instance = JsonDeviceByProfileIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonDeviceByProfileIDResult.to_json())

# convert the object into a dict
json_device_by_profile_id_result_dict = json_device_by_profile_id_result_instance.to_dict()
# create an instance of JsonDeviceByProfileIDResult from a dict
json_device_by_profile_id_result_from_dict = JsonDeviceByProfileIDResult.from_dict(json_device_by_profile_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


