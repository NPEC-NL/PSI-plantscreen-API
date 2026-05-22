# ProfileIDWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **int** |  | [optional] 


## Links

### 1:1 Relationships

All the listed relationships are available as properties on the model instance

Name | Model | Linked Via
------------ | ------------- | -------------


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
from plantscreen.models.profile_id_wrapper import ProfileIDWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileIDWrapper from a JSON string
profile_id_wrapper_instance = ProfileIDWrapper.from_json(json)
# print the JSON string representation of the object
print(ProfileIDWrapper.to_json())

# convert the object into a dict
profile_id_wrapper_dict = profile_id_wrapper_instance.to_dict()
# create an instance of ProfileIDWrapper from a dict
profile_id_wrapper_from_dict = ProfileIDWrapper.from_dict(profile_id_wrapper_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


