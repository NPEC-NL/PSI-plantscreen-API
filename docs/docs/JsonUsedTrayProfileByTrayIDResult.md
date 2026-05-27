# JsonUsedTrayProfileByTrayIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_used_tray_profile_by_tray_id_result** | [**List[TrayProfile]**](TrayProfile.md) |  | [optional] 
**result** | [**List[TrayProfile]**](TrayProfile.md)| alias for **json_used_tray_profile_by_tray_id_result**  | 

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
from plantscreen.models.json_used_tray_profile_by_tray_id_result import JsonUsedTrayProfileByTrayIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUsedTrayProfileByTrayIDResult from a JSON string
json_used_tray_profile_by_tray_id_result_instance = JsonUsedTrayProfileByTrayIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonUsedTrayProfileByTrayIDResult.to_json())

# convert the object into a dict
json_used_tray_profile_by_tray_id_result_dict = json_used_tray_profile_by_tray_id_result_instance.to_dict()
# create an instance of JsonUsedTrayProfileByTrayIDResult from a dict
json_used_tray_profile_by_tray_id_result_from_dict = JsonUsedTrayProfileByTrayIDResult.from_dict(json_used_tray_profile_by_tray_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


