# JsonTrayTypeByTrayIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_tray_type_by_tray_id_result** | [**TrayType**](TrayType.md) |  | [optional] 
**result** | [**TrayType**](TrayType.md)| alias for **json_tray_type_by_tray_id_result**  | 

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
from plantscreen.models.json_tray_type_by_tray_id_result import JsonTrayTypeByTrayIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonTrayTypeByTrayIDResult from a JSON string
json_tray_type_by_tray_id_result_instance = JsonTrayTypeByTrayIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonTrayTypeByTrayIDResult.to_json())

# convert the object into a dict
json_tray_type_by_tray_id_result_dict = json_tray_type_by_tray_id_result_instance.to_dict()
# create an instance of JsonTrayTypeByTrayIDResult from a dict
json_tray_type_by_tray_id_result_from_dict = JsonTrayTypeByTrayIDResult.from_dict(json_tray_type_by_tray_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


