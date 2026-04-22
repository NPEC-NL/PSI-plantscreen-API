# MscLightSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | [optional] 
**light_set_caption** | **str** |  | [optional] 
**light_set_id** | **int** |  | [optional] 
**light_set_pid_name** | **str** |  | [optional] 
**light_set_valid** | **bool** |  | [optional] 


## Links

### 1:1 Relationships
Name | Model | Linked Via
------------ | ------------- | -------------


### Implicit Relationships
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------

### Parameterized Relationships
Name | Model | API | Operation | Parameters
------------ | ------------- | ------------- | ------------- | -------------
## Example

```python
from plantscreen.models.msc_light_set import MscLightSet

# TODO update the JSON string below
json = "{}"
# create an instance of MscLightSet from a JSON string
msc_light_set_instance = MscLightSet.from_json(json)
# print the JSON string representation of the object
print(MscLightSet.to_json())

# convert the object into a dict
msc_light_set_dict = msc_light_set_instance.to_dict()
# create an instance of MscLightSet from a dict
msc_light_set_from_dict = MscLightSet.from_dict(msc_light_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


