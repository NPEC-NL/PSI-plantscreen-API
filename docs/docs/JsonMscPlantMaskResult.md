# JsonMscPlantMaskResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_plant_mask_result** | [**List[PlantMask]**](PlantMask.md) |  | [optional] 
**result** | [**List[PlantMask]**](PlantMask.md)| alias for **json_msc_plant_mask_result**  | 

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
from plantscreen.models.json_msc_plant_mask_result import JsonMscPlantMaskResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscPlantMaskResult from a JSON string
json_msc_plant_mask_result_instance = JsonMscPlantMaskResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscPlantMaskResult.to_json())

# convert the object into a dict
json_msc_plant_mask_result_dict = json_msc_plant_mask_result_instance.to_dict()
# create an instance of JsonMscPlantMaskResult from a dict
json_msc_plant_mask_result_from_dict = JsonMscPlantMaskResult.from_dict(json_msc_plant_mask_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


