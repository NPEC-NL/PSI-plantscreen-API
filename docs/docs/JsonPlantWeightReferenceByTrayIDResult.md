# JsonPlantWeightReferenceByTrayIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_plant_weight_reference_by_tray_id_result** | [**List[PlantWeightReference]**](PlantWeightReference.md) |  | [optional] 
**result** | [**List[PlantWeightReference]**](PlantWeightReference.md)| alias for **json_plant_weight_reference_by_tray_id_result**  | 

## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------


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
from plantscreen.models.json_plant_weight_reference_by_tray_id_result import JsonPlantWeightReferenceByTrayIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPlantWeightReferenceByTrayIDResult from a JSON string
json_plant_weight_reference_by_tray_id_result_instance = JsonPlantWeightReferenceByTrayIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonPlantWeightReferenceByTrayIDResult.to_json())

# convert the object into a dict
json_plant_weight_reference_by_tray_id_result_dict = json_plant_weight_reference_by_tray_id_result_instance.to_dict()
# create an instance of JsonPlantWeightReferenceByTrayIDResult from a dict
json_plant_weight_reference_by_tray_id_result_from_dict = JsonPlantWeightReferenceByTrayIDResult.from_dict(json_plant_weight_reference_by_tray_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


