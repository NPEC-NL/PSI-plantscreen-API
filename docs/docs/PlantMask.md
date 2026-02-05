# PlantMask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**device_pid** | **str** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**mask_is_leaf** | **bool** |  | [optional] 
**measure_angle** | **int** |  | [optional] 
**measure_date** | **datetime** |  | [optional] 
**measure_id** | **int** |  | [optional] 
**plant_mask_path** | **str** | filetype | [optional] 
**round_id** | **int** |  | [optional] 
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 

## Example

```python
from plantscreen.models.plant_mask import PlantMask

# TODO update the JSON string below
json = "{}"
# create an instance of PlantMask from a JSON string
plant_mask_instance = PlantMask.from_json(json)
# print the JSON string representation of the object
print(PlantMask.to_json())

# convert the object into a dict
plant_mask_dict = plant_mask_instance.to_dict()
# create an instance of PlantMask from a dict
plant_mask_from_dict = PlantMask.from_dict(plant_mask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


