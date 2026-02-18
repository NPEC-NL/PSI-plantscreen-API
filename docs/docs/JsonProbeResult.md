# JsonProbeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_probe_result** | [**List[Probe]**](Probe.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_probe_result import JsonProbeResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonProbeResult from a JSON string
json_probe_result_instance = JsonProbeResult.from_json(json)
# print the JSON string representation of the object
print(JsonProbeResult.to_json())

# convert the object into a dict
json_probe_result_dict = json_probe_result_instance.to_dict()
# create an instance of JsonProbeResult from a dict
json_probe_result_from_dict = JsonProbeResult.from_dict(json_probe_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


