# Probe200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_probe_result** | [**List[Probe]**](Probe.md) |  | [optional] 
**json_probe_by_id_result** | [**Probe**](Probe.md) |  | [optional] 

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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


