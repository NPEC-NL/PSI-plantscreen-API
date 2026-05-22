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


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**device**|[**Device**](Device.md)|device_id**experiment**|[**Experiment**](Experiment.md)|experiment_id**round**|[**Round**](Round.md)|round_id**tray**|[**Tray**](Tray.md)|tray_id

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
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


