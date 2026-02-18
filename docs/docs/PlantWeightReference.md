# PlantWeightReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**reference_weight_date** | **datetime** |  | [optional] 
**reference_weight_value** | **float** |  | [optional] 

## Example

```python
from plantscreen.models.plant_weight_reference import PlantWeightReference

# TODO update the JSON string below
json = "{}"
# create an instance of PlantWeightReference from a JSON string
plant_weight_reference_instance = PlantWeightReference.from_json(json)
# print the JSON string representation of the object
print(PlantWeightReference.to_json())

# convert the object into a dict
plant_weight_reference_dict = plant_weight_reference_instance.to_dict()
# create an instance of PlantWeightReference from a dict
plant_weight_reference_from_dict = PlantWeightReference.from_dict(plant_weight_reference_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


