# JsonIrPlantMaskResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_ir_plant_mask_result** | [**List[PlantMask]**](PlantMask.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_ir_plant_mask_result import JsonIrPlantMaskResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIrPlantMaskResult from a JSON string
json_ir_plant_mask_result_instance = JsonIrPlantMaskResult.from_json(json)
# print the JSON string representation of the object
print(JsonIrPlantMaskResult.to_json())

# convert the object into a dict
json_ir_plant_mask_result_dict = json_ir_plant_mask_result_instance.to_dict()
# create an instance of JsonIrPlantMaskResult from a dict
json_ir_plant_mask_result_from_dict = JsonIrPlantMaskResult.from_dict(json_ir_plant_mask_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


