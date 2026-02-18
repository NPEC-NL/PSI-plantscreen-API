# JsonTrayProfileByTrayIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_tray_profile_by_tray_id_result** | [**List[TrayProfile]**](TrayProfile.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_tray_profile_by_tray_id_result import JsonTrayProfileByTrayIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonTrayProfileByTrayIDResult from a JSON string
json_tray_profile_by_tray_id_result_instance = JsonTrayProfileByTrayIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonTrayProfileByTrayIDResult.to_json())

# convert the object into a dict
json_tray_profile_by_tray_id_result_dict = json_tray_profile_by_tray_id_result_instance.to_dict()
# create an instance of JsonTrayProfileByTrayIDResult from a dict
json_tray_profile_by_tray_id_result_from_dict = JsonTrayProfileByTrayIDResult.from_dict(json_tray_profile_by_tray_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


