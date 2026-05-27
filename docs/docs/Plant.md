# Plant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**plant_info** | **str** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**tray_area** | **str** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------


### Implicit Relationships

All the listed relationships are available as properties on the model instance

Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------
reference_weight | [**PlantWeightReference**](PlantWeightReference.md) | ScalesApi |  | **PlantID->id**

### Parameterized Relationships

All the listed relationships are available as methods on the model instance.

Parameters written in **bold** are taken automatically from the model instance, when calling the method you have to
supply the non-bold parameters

Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.plant import Plant

# TODO update the JSON string below
json = "{}"
# create an instance of Plant from a JSON string
plant_instance = Plant.from_json(json)
# print the JSON string representation of the object
print(Plant.to_json())

# convert the object into a dict
plant_dict = plant_instance.to_dict()
# create an instance of Plant from a dict
plant_from_dict = Plant.from_dict(plant_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


