# MeasureExtendedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**extended_data** | **str** |  | [optional] 
**measure_date** | **datetime** |  | [optional] 
**measure_id** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 
**tray_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**device**|[**Device**](Device.md)|device_id**round**|[**Round**](Round.md)|round_id**tray**|[**Tray**](Tray.md)|tray_id

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
from plantscreen.models.measure_extended_data import MeasureExtendedData

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureExtendedData from a JSON string
measure_extended_data_instance = MeasureExtendedData.from_json(json)
# print the JSON string representation of the object
print(MeasureExtendedData.to_json())

# convert the object into a dict
measure_extended_data_dict = measure_extended_data_instance.to_dict()
# create an instance of MeasureExtendedData from a dict
measure_extended_data_from_dict = MeasureExtendedData.from_dict(measure_extended_data_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


