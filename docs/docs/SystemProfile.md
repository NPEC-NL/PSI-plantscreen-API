# SystemProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_active** | **bool** |  | [optional] 
**profile_id** | **int** |  | [optional] 
**profile_info** | **str** |  | [optional] 
**profile_name** | **str** |  | [optional] 
**system_hw_config** | **str** |  | [optional] 

## Example

```python
from plantscreen.models.system_profile import SystemProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SystemProfile from a JSON string
system_profile_instance = SystemProfile.from_json(json)
# print the JSON string representation of the object
print(SystemProfile.to_json())

# convert the object into a dict
system_profile_dict = system_profile_instance.to_dict()
# create an instance of SystemProfile from a dict
system_profile_from_dict = SystemProfile.from_dict(system_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


