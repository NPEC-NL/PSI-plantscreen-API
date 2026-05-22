# JsonTrayResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_tray_result** | [**Tray**](Tray.md) |  | [optional] 
**result** | [**Tray**](Tray.md)| alias for **json_tray_result**  | 

## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
****|[**TrayProfile**](TrayProfile.md)|tray_profile****|[**ScalesMapping**](ScalesMapping.md)|scales_mapping****|[**Plant**](Plant.md)|plants****|[**PlantWeightReference**](PlantWeightReference.md)|plant_reference_weights****|[**SystemLog**](SystemLog.md)|system_logs

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
from plantscreen.models.json_tray_result import JsonTrayResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonTrayResult from a JSON string
json_tray_result_instance = JsonTrayResult.from_json(json)
# print the JSON string representation of the object
print(JsonTrayResult.to_json())

# convert the object into a dict
json_tray_result_dict = json_tray_result_instance.to_dict()
# create an instance of JsonTrayResult from a dict
json_tray_result_from_dict = JsonTrayResult.from_dict(json_tray_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


