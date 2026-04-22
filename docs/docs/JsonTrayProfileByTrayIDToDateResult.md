# JsonTrayProfileByTrayIDToDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_tray_profile_by_tray_idto_date_result** | [**TrayProfile**](TrayProfile.md) |  | [optional] 
**result** | [**TrayProfile**](TrayProfile.md)| alias for **json_tray_profile_by_tray_idto_date_result**  | 

## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
****|[**TrayProfile**](TrayType.md)|tray_type****|[**TrayProfile**](Plant.md)|plants

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.json_tray_profile_by_tray_idto_date_result import JsonTrayProfileByTrayIDToDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonTrayProfileByTrayIDToDateResult from a JSON string
json_tray_profile_by_tray_idto_date_result_instance = JsonTrayProfileByTrayIDToDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonTrayProfileByTrayIDToDateResult.to_json())

# convert the object into a dict
json_tray_profile_by_tray_idto_date_result_dict = json_tray_profile_by_tray_idto_date_result_instance.to_dict()
# create an instance of JsonTrayProfileByTrayIDToDateResult from a dict
json_tray_profile_by_tray_idto_date_result_from_dict = JsonTrayProfileByTrayIDToDateResult.from_dict(json_tray_profile_by_tray_idto_date_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


