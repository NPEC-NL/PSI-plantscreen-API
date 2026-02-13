# JsonDeviceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_device_result** | [**Device**](Device.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_device_result import JsonDeviceResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDeviceResult from a JSON string
json_device_result_instance = JsonDeviceResult.from_json(json)
# print the JSON string representation of the object
print(JsonDeviceResult.to_json())

# convert the object into a dict
json_device_result_dict = json_device_result_instance.to_dict()
# create an instance of JsonDeviceResult from a dict
json_device_result_from_dict = JsonDeviceResult.from_dict(json_device_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


