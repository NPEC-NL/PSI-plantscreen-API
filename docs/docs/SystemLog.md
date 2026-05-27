# SystemLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **int** |  | [optional] 
**log_date** | **datetime** |  | [optional] 
**log_id** | **int** |  | [optional] 
**log_tag** | **str** |  | [optional] 
**log_text** | **str** |  | [optional] 
**log_type** | **str** |  | [optional] 
**round_id** | **int** |  | [optional] 
**tray_barcode** | **str** |  | [optional] 
**tray_id** | **int** |  | [optional] 
**tray_profile_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**experiment**|[**Experiment**](Experiment.md)|experiment_id**round**|[**Round**](Round.md)|round_id**tray**|[**Tray**](Tray.md)|tray_id**tray_profile**|[**TrayProfile**](TrayProfile.md)|tray_profile_id

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
from plantscreen.models.system_log import SystemLog

# TODO update the JSON string below
json = "{}"
# create an instance of SystemLog from a JSON string
system_log_instance = SystemLog.from_json(json)
# print the JSON string representation of the object
print(SystemLog.to_json())

# convert the object into a dict
system_log_dict = system_log_instance.to_dict()
# create an instance of SystemLog from a dict
system_log_from_dict = SystemLog.from_dict(system_log_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


