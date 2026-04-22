# JsonFcPlantMaskByMeasureIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_fc_plant_mask_by_measure_id_result** | [**PlantMask**](PlantMask.md) |  | [optional] 
**result** | [**PlantMask**](PlantMask.md)| alias for **json_fc_plant_mask_by_measure_id_result**  | 

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
from plantscreen.models.json_fc_plant_mask_by_measure_id_result import JsonFcPlantMaskByMeasureIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFcPlantMaskByMeasureIDResult from a JSON string
json_fc_plant_mask_by_measure_id_result_instance = JsonFcPlantMaskByMeasureIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonFcPlantMaskByMeasureIDResult.to_json())

# convert the object into a dict
json_fc_plant_mask_by_measure_id_result_dict = json_fc_plant_mask_by_measure_id_result_instance.to_dict()
# create an instance of JsonFcPlantMaskByMeasureIDResult from a dict
json_fc_plant_mask_by_measure_id_result_from_dict = JsonFcPlantMaskByMeasureIDResult.from_dict(json_fc_plant_mask_by_measure_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


