# JsonTrayTypeByTrayProfileIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_tray_type_by_tray_profile_id_result** | [**TrayType**](TrayType.md) |  | [optional] 
**result** | [**TrayType**](TrayType.md)| alias for **json_tray_type_by_tray_profile_id_result**  | 

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
from plantscreen.models.json_tray_type_by_tray_profile_id_result import JsonTrayTypeByTrayProfileIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonTrayTypeByTrayProfileIDResult from a JSON string
json_tray_type_by_tray_profile_id_result_instance = JsonTrayTypeByTrayProfileIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonTrayTypeByTrayProfileIDResult.to_json())

# convert the object into a dict
json_tray_type_by_tray_profile_id_result_dict = json_tray_type_by_tray_profile_id_result_instance.to_dict()
# create an instance of JsonTrayTypeByTrayProfileIDResult from a dict
json_tray_type_by_tray_profile_id_result_from_dict = JsonTrayTypeByTrayProfileIDResult.from_dict(json_tray_type_by_tray_profile_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


