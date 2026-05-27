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
Name | Model | Linked Via
------------ | ------------- | -------------
**tray_type**|[**int**](TrayType.md)|tray_type_id

### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
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


