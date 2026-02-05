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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


