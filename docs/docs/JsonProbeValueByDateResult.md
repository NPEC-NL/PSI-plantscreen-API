# JsonProbeValueByDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_probe_value_by_date_result** | [**List[ProbeValue]**](ProbeValue.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_probe_value_by_date_result import JsonProbeValueByDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonProbeValueByDateResult from a JSON string
json_probe_value_by_date_result_instance = JsonProbeValueByDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonProbeValueByDateResult.to_json())

# convert the object into a dict
json_probe_value_by_date_result_dict = json_probe_value_by_date_result_instance.to_dict()
# create an instance of JsonProbeValueByDateResult from a dict
json_probe_value_by_date_result_from_dict = JsonProbeValueByDateResult.from_dict(json_probe_value_by_date_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


