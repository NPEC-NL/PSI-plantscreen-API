# JsonTrayResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_tray_result** | [**Tray**](Tray.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_tray_result import JsonTrayResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonTrayResult from a JSON string
json_tray_result_instance = JsonTrayResult.from_json(json)
# print the JSON string representation of the object
print(JsonTrayResult.to_json())

# convert the object into a dict
json_tray_result_dict = json_tray_result_instance.to_dict()
# create an instance of JsonTrayResult from a dict
json_tray_result_from_dict = JsonTrayResult.from_dict(json_tray_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


