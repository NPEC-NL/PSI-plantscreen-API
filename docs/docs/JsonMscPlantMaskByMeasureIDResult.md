# JsonMscPlantMaskByMeasureIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_plant_mask_by_measure_id_result** | [**PlantMask**](PlantMask.md) |  | [optional] 
**result** | [**PlantMask**](PlantMask.md)| alias for **json_msc_plant_mask_by_measure_id_result**  | 

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
from plantscreen.models.json_msc_plant_mask_by_measure_id_result import JsonMscPlantMaskByMeasureIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscPlantMaskByMeasureIDResult from a JSON string
json_msc_plant_mask_by_measure_id_result_instance = JsonMscPlantMaskByMeasureIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscPlantMaskByMeasureIDResult.to_json())

# convert the object into a dict
json_msc_plant_mask_by_measure_id_result_dict = json_msc_plant_mask_by_measure_id_result_instance.to_dict()
# create an instance of JsonMscPlantMaskByMeasureIDResult from a dict
json_msc_plant_mask_by_measure_id_result_from_dict = JsonMscPlantMaskByMeasureIDResult.from_dict(json_msc_plant_mask_by_measure_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


