# LeafParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyse_id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_pid** | **str** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**leaf_index** | **int** |  | [optional] 
**measure_angle** | **int** |  | [optional] 
**measure_id** | **int** |  | [optional] 
**parameter_id** | **int** |  | [optional] 
**parameter_name** | **str** |  | [optional] 
**parameter_value** | **float** |  | [optional] 
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**round_id** | **int** |  | [optional] 
**tray_area** | **str** |  | [optional] 
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------
**device**|[**int**](Device.md)|device_id**experiment**|[**int**](Experiment.md)|experiment_id**plant**|[**int**](Plant.md)|plant_id**round**|[**int**](Round.md)|round_id**tray**|[**int**](Tray.md)|tray_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.leaf_parameter import LeafParameter

# TODO update the JSON string below
json = "{}"
# create an instance of LeafParameter from a JSON string
leaf_parameter_instance = LeafParameter.from_json(json)
# print the JSON string representation of the object
print(LeafParameter.to_json())

# convert the object into a dict
leaf_parameter_dict = leaf_parameter_instance.to_dict()
# create an instance of LeafParameter from a dict
leaf_parameter_from_dict = LeafParameter.from_dict(leaf_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


