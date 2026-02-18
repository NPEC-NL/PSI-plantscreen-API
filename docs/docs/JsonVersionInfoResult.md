# JsonVersionInfoResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_version_info_result** | [**VersionInfo**](VersionInfo.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_version_info_result import JsonVersionInfoResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonVersionInfoResult from a JSON string
json_version_info_result_instance = JsonVersionInfoResult.from_json(json)
# print the JSON string representation of the object
print(JsonVersionInfoResult.to_json())

# convert the object into a dict
json_version_info_result_dict = json_version_info_result_instance.to_dict()
# create an instance of JsonVersionInfoResult from a dict
json_version_info_result_from_dict = JsonVersionInfoResult.from_dict(json_version_info_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


