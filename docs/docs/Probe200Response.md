# Probe200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_probe_result** | [**List[Probe]**](Probe.md) |  | 
**json_probe_by_id_result** | [**Probe**](Probe.md) |  | 


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
from plantscreen.models.probe200_response import Probe200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Probe200Response from a JSON string
probe200_response_instance = Probe200Response.from_json(json)
# print the JSON string representation of the object
print(Probe200Response.to_json())

# convert the object into a dict
probe200_response_dict = probe200_response_instance.to_dict()
# create an instance of Probe200Response from a dict
probe200_response_from_dict = Probe200Response.from_dict(probe200_response_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


