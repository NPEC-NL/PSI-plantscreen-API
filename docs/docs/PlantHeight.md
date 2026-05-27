# PlantHeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **int** |  | [optional] 
**height_date** | **datetime** |  | [optional] 
**height_value** | **int** |  | [optional] 
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**round_id** | **int** |  | [optional] 


## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------
**experiment**|[**int**](Experiment.md)|experiment_id**plant**|[**int**](Plant.md)|plant_id**round**|[**int**](Round.md)|round_id

### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.plant_height import PlantHeight

# TODO update the JSON string below
json = "{}"
# create an instance of PlantHeight from a JSON string
plant_height_instance = PlantHeight.from_json(json)
# print the JSON string representation of the object
print(PlantHeight.to_json())

# convert the object into a dict
plant_height_dict = plant_height_instance.to_dict()
# create an instance of PlantHeight from a dict
plant_height_from_dict = PlantHeight.from_dict(plant_height_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


