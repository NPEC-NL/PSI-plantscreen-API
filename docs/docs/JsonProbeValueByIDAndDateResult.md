# JsonProbeValueByIDAndDateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_probe_value_by_id_and_date_result** | [**List[ProbeValue]**](ProbeValue.md) |  | [optional] 
**result** | [**List[ProbeValue]**](ProbeValue.md)| alias for **json_probe_value_by_id_and_date_result**  | 

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
from plantscreen.models.json_probe_value_by_id_and_date_result import JsonProbeValueByIDAndDateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonProbeValueByIDAndDateResult from a JSON string
json_probe_value_by_id_and_date_result_instance = JsonProbeValueByIDAndDateResult.from_json(json)
# print the JSON string representation of the object
print(JsonProbeValueByIDAndDateResult.to_json())

# convert the object into a dict
json_probe_value_by_id_and_date_result_dict = json_probe_value_by_id_and_date_result_instance.to_dict()
# create an instance of JsonProbeValueByIDAndDateResult from a dict
json_probe_value_by_id_and_date_result_from_dict = JsonProbeValueByIDAndDateResult.from_dict(json_probe_value_by_id_and_date_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


