# JsonPlantByTrayProfileIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_plant_by_tray_profile_id_result** | [**List[Plant]**](Plant.md) |  | [optional] 
**result** | [**List[Plant]**](Plant.md)| alias for **json_plant_by_tray_profile_id_result**  | 

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
from plantscreen.models.json_plant_by_tray_profile_id_result import JsonPlantByTrayProfileIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPlantByTrayProfileIDResult from a JSON string
json_plant_by_tray_profile_id_result_instance = JsonPlantByTrayProfileIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonPlantByTrayProfileIDResult.to_json())

# convert the object into a dict
json_plant_by_tray_profile_id_result_dict = json_plant_by_tray_profile_id_result_instance.to_dict()
# create an instance of JsonPlantByTrayProfileIDResult from a dict
json_plant_by_tray_profile_id_result_from_dict = JsonPlantByTrayProfileIDResult.from_dict(json_plant_by_tray_profile_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


