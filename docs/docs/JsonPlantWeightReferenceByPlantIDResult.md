# JsonPlantWeightReferenceByPlantIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_plant_weight_reference_by_plant_id_result** | [**PlantWeightReference**](PlantWeightReference.md) |  | [optional] 
**result** | [**PlantWeightReference**](PlantWeightReference.md)| alias for **json_plant_weight_reference_by_plant_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_plant_weight_reference_by_plant_id_result import JsonPlantWeightReferenceByPlantIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPlantWeightReferenceByPlantIDResult from a JSON string
json_plant_weight_reference_by_plant_id_result_instance = JsonPlantWeightReferenceByPlantIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonPlantWeightReferenceByPlantIDResult.to_json())

# convert the object into a dict
json_plant_weight_reference_by_plant_id_result_dict = json_plant_weight_reference_by_plant_id_result_instance.to_dict()
# create an instance of JsonPlantWeightReferenceByPlantIDResult from a dict
json_plant_weight_reference_by_plant_id_result_from_dict = JsonPlantWeightReferenceByPlantIDResult.from_dict(json_plant_weight_reference_by_plant_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


