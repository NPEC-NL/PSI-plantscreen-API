# JsonPlantByTrayIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_plant_by_tray_id_result** | [**List[Plant]**](Plant.md) |  | [optional] 
**result** | [**List[Plant]**](Plant.md)| alias for **json_plant_by_tray_id_result**  | 

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
from plantscreen.models.json_plant_by_tray_id_result import JsonPlantByTrayIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPlantByTrayIDResult from a JSON string
json_plant_by_tray_id_result_instance = JsonPlantByTrayIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonPlantByTrayIDResult.to_json())

# convert the object into a dict
json_plant_by_tray_id_result_dict = json_plant_by_tray_id_result_instance.to_dict()
# create an instance of JsonPlantByTrayIDResult from a dict
json_plant_by_tray_id_result_from_dict = JsonPlantByTrayIDResult.from_dict(json_plant_by_tray_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


