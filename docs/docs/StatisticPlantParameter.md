# StatisticPlantParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyse_id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_pid** | **str** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**measure_angle** | **int** |  | [optional] 
**measure_id** | **int** |  | [optional] 
**parameter_avg** | **float** |  | [optional] 
**parameter_id** | **int** |  | [optional] 
**parameter_max** | **float** |  | [optional] 
**parameter_median** | **float** |  | [optional] 
**parameter_min** | **float** |  | [optional] 
**parameter_name** | **str** |  | [optional] 
**parameter_stddev** | **float** |  | [optional] 
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**round_id** | **int** |  | [optional] 
**tray_area** | **str** |  | [optional] 
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**device**|[**Device**](Device.md)|device_id**experiment**|[**Experiment**](Experiment.md)|experiment_id**plant**|[**Plant**](Plant.md)|plant_id**round**|[**Round**](Round.md)|round_id**tray**|[**Tray**](Tray.md)|tray_id

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
from plantscreen.models.statistic_plant_parameter import StatisticPlantParameter

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticPlantParameter from a JSON string
statistic_plant_parameter_instance = StatisticPlantParameter.from_json(json)
# print the JSON string representation of the object
print(StatisticPlantParameter.to_json())

# convert the object into a dict
statistic_plant_parameter_dict = statistic_plant_parameter_instance.to_dict()
# create an instance of StatisticPlantParameter from a dict
statistic_plant_parameter_from_dict = StatisticPlantParameter.from_dict(statistic_plant_parameter_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


