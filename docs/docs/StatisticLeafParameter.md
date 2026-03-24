# StatisticLeafParameter


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

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------
**device**|[**int**](Device.md)|device_id**experiment**|[**int**](Experiment.md)|experiment_id**plant**|[**int**](Plant.md)|plant_id**round**|[**int**](Round.md)|round_id**tray**|[**int**](Tray.md)|tray_id

### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.statistic_leaf_parameter import StatisticLeafParameter

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticLeafParameter from a JSON string
statistic_leaf_parameter_instance = StatisticLeafParameter.from_json(json)
# print the JSON string representation of the object
print(StatisticLeafParameter.to_json())

# convert the object into a dict
statistic_leaf_parameter_dict = statistic_leaf_parameter_instance.to_dict()
# create an instance of StatisticLeafParameter from a dict
statistic_leaf_parameter_from_dict = StatisticLeafParameter.from_dict(statistic_leaf_parameter_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


