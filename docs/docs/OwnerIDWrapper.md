# OwnerIDWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **float** |  | [optional] 


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
from plantscreen.models.owner_id_wrapper import OwnerIDWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerIDWrapper from a JSON string
owner_id_wrapper_instance = OwnerIDWrapper.from_json(json)
# print the JSON string representation of the object
print(OwnerIDWrapper.to_json())

# convert the object into a dict
owner_id_wrapper_dict = owner_id_wrapper_instance.to_dict()
# create an instance of OwnerIDWrapper from a dict
owner_id_wrapper_from_dict = OwnerIDWrapper.from_dict(owner_id_wrapper_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


