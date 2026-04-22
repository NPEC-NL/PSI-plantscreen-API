# JsonTrayResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_tray_result** | [**Tray**](Tray.md) |  | [optional] 
**result** | [**Tray**](Tray.md)| alias for **json_tray_result**  | 

## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
****|[**Tray**](TrayProfile.md)|tray_profile****|[**Tray**](ScalesMapping.md)|scales_mapping****|[**Tray**](Plant.md)|plants****|[**Tray**](PlantWeightReference.md)|plant_reference_weights****|[**Tray**](SystemLog.md)|system_logs

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


