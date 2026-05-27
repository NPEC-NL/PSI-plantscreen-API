# JsonPlantByTrayIDAndDatesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_plant_by_tray_id_and_dates_result** | [**List[Plant]**](Plant.md) |  | [optional] 
**result** | [**List[Plant]**](Plant.md)| alias for **json_plant_by_tray_id_and_dates_result**  | 

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
from plantscreen.models.json_plant_by_tray_id_and_dates_result import JsonPlantByTrayIDAndDatesResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPlantByTrayIDAndDatesResult from a JSON string
json_plant_by_tray_id_and_dates_result_instance = JsonPlantByTrayIDAndDatesResult.from_json(json)
# print the JSON string representation of the object
print(JsonPlantByTrayIDAndDatesResult.to_json())

# convert the object into a dict
json_plant_by_tray_id_and_dates_result_dict = json_plant_by_tray_id_and_dates_result_instance.to_dict()
# create an instance of JsonPlantByTrayIDAndDatesResult from a dict
json_plant_by_tray_id_and_dates_result_from_dict = JsonPlantByTrayIDAndDatesResult.from_dict(json_plant_by_tray_id_and_dates_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


