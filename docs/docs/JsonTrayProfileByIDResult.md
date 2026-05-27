# JsonTrayProfileByIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_tray_profile_by_id_result** | [**TrayProfile**](TrayProfile.md) |  | [optional] 
**result** | [**TrayProfile**](TrayProfile.md)| alias for **json_tray_profile_by_id_result**  | 

## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
****|[**TrayType**](TrayType.md)|tray_type****|[**Plant**](Plant.md)|plants

### Implicit Relationships

All the listed relationships are available as properties on the model instance

Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships

All the listed relationships are available as methods on the model instance.

Parameters written in **bold** are taken automatically from the model instance, when calling the method you have to
supply the non-bold parameters

Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
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


