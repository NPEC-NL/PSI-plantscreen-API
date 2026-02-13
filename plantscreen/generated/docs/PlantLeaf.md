# PlantLeaf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaf_index** | **int** |  | [optional] 
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 

## Example

```python
from plantscreen.models.plant_leaf import PlantLeaf

# TODO update the JSON string below
json = "{}"
# create an instance of PlantLeaf from a JSON string
plant_leaf_instance = PlantLeaf.from_json(json)
# print the JSON string representation of the object
print(PlantLeaf.to_json())

# convert the object into a dict
plant_leaf_dict = plant_leaf_instance.to_dict()
# create an instance of PlantLeaf from a dict
plant_leaf_from_dict = PlantLeaf.from_dict(plant_leaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


