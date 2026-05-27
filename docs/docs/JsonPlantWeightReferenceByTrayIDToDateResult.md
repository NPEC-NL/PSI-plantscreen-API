# JsonPlantWeightReferenceByTrayIDToDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_plant_weight_reference_by_tray_idto_date_result** | [**List[PlantWeightReference]**](PlantWeightReference.md) |  | [optional] 
**result** | [**List[PlantWeightReference]**](PlantWeightReference.md)| alias for **json_plant_weight_reference_by_tray_idto_date_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_plant_weight_reference_by_tray_idto_date_result import JsonPlantWeightReferenceByTrayIDToDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPlantWeightReferenceByTrayIDToDateResult from a JSON string
json_plant_weight_reference_by_tray_idto_date_result_instance = JsonPlantWeightReferenceByTrayIDToDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonPlantWeightReferenceByTrayIDToDateResult.to_json())

# convert the object into a dict
json_plant_weight_reference_by_tray_idto_date_result_dict = json_plant_weight_reference_by_tray_idto_date_result_instance.to_dict()
# create an instance of JsonPlantWeightReferenceByTrayIDToDateResult from a dict
json_plant_weight_reference_by_tray_idto_date_result_from_dict = JsonPlantWeightReferenceByTrayIDToDateResult.from_dict(json_plant_weight_reference_by_tray_idto_date_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


