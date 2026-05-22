# ScalesMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_area** | **str** |  | [optional] 
**map_column** | **int** |  | [optional] 
**map_row** | **int** |  | [optional] 
**tray_type_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------
**tray_type**|[**TrayType**](TrayType.md)|tray_type_id

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
from plantscreen.models.scales_mapping import ScalesMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ScalesMapping from a JSON string
scales_mapping_instance = ScalesMapping.from_json(json)
# print the JSON string representation of the object
print(ScalesMapping.to_json())

# convert the object into a dict
scales_mapping_dict = scales_mapping_instance.to_dict()
# create an instance of ScalesMapping from a dict
scales_mapping_from_dict = ScalesMapping.from_dict(scales_mapping_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


