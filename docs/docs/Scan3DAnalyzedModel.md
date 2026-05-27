# Scan3DAnalyzedModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyse_id** | **int** |  | [optional] 
**analysed_model_path** | **str** | filetype | [optional] 
**device_id** | **int** |  | [optional] 
**device_pid** | **str** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**measure_date** | **datetime** |  | [optional] 
**measure_id** | **int** |  | [optional] 
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 
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
from plantscreen.models.scan3_d_analyzed_model import Scan3DAnalyzedModel

# TODO update the JSON string below
json = "{}"
# create an instance of Scan3DAnalyzedModel from a JSON string
scan3_d_analyzed_model_instance = Scan3DAnalyzedModel.from_json(json)
# print the JSON string representation of the object
print(Scan3DAnalyzedModel.to_json())

# convert the object into a dict
scan3_d_analyzed_model_dict = scan3_d_analyzed_model_instance.to_dict()
# create an instance of Scan3DAnalyzedModel from a dict
scan3_d_analyzed_model_from_dict = Scan3DAnalyzedModel.from_dict(scan3_d_analyzed_model_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


