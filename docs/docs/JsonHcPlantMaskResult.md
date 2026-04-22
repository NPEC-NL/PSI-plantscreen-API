# JsonHcPlantMaskResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_plant_mask_result** | [**List[PlantMask]**](PlantMask.md) |  | [optional] 
**result** | [**List[PlantMask]**](PlantMask.md)| alias for **json_hc_plant_mask_result**  | 

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
from plantscreen.models.json_hc_plant_mask_result import JsonHcPlantMaskResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcPlantMaskResult from a JSON string
json_hc_plant_mask_result_instance = JsonHcPlantMaskResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcPlantMaskResult.to_json())

# convert the object into a dict
json_hc_plant_mask_result_dict = json_hc_plant_mask_result_instance.to_dict()
# create an instance of JsonHcPlantMaskResult from a dict
json_hc_plant_mask_result_from_dict = JsonHcPlantMaskResult.from_dict(json_hc_plant_mask_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


