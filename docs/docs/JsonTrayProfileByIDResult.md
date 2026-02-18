# JsonTrayProfileByIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_tray_profile_by_id_result** | [**TrayProfile**](TrayProfile.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_tray_profile_by_id_result import JsonTrayProfileByIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonTrayProfileByIDResult from a JSON string
json_tray_profile_by_id_result_instance = JsonTrayProfileByIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonTrayProfileByIDResult.to_json())

# convert the object into a dict
json_tray_profile_by_id_result_dict = json_tray_profile_by_id_result_instance.to_dict()
# create an instance of JsonTrayProfileByIDResult from a dict
json_tray_profile_by_id_result_from_dict = JsonTrayProfileByIDResult.from_dict(json_tray_profile_by_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


