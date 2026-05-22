# PlantLeaf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaf_index** | **int** |  | [optional] 
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**plant**|[**Plant**](Plant.md)|plant_id**tray**|[**Tray**](Tray.md)|tray_id

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
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


