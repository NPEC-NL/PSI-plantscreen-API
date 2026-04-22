# JsonPlantHeightByRoundIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_plant_height_by_round_id_result** | [**List[PlantHeight]**](PlantHeight.md) |  | [optional] 
**result** | [**List[PlantHeight]**](PlantHeight.md)| alias for **json_plant_height_by_round_id_result**  | 

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
from plantscreen.models.json_plant_height_by_round_id_result import JsonPlantHeightByRoundIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPlantHeightByRoundIDResult from a JSON string
json_plant_height_by_round_id_result_instance = JsonPlantHeightByRoundIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonPlantHeightByRoundIDResult.to_json())

# convert the object into a dict
json_plant_height_by_round_id_result_dict = json_plant_height_by_round_id_result_instance.to_dict()
# create an instance of JsonPlantHeightByRoundIDResult from a dict
json_plant_height_by_round_id_result_from_dict = JsonPlantHeightByRoundIDResult.from_dict(json_plant_height_by_round_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


