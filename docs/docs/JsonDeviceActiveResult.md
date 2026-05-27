# JsonDeviceActiveResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_device_active_result** | [**List[Device]**](Device.md) |  | [optional] 
**result** | [**List[Device]**](Device.md)| alias for **json_device_active_result**  | 

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
from plantscreen.models.json_device_active_result import JsonDeviceActiveResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDeviceActiveResult from a JSON string
json_device_active_result_instance = JsonDeviceActiveResult.from_json(json)
# print the JSON string representation of the object
print(JsonDeviceActiveResult.to_json())

# convert the object into a dict
json_device_active_result_dict = json_device_active_result_instance.to_dict()
# create an instance of JsonDeviceActiveResult from a dict
json_device_active_result_from_dict = JsonDeviceActiveResult.from_dict(json_device_active_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


