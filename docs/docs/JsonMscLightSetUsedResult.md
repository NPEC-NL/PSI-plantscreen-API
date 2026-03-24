# JsonMscLightSetUsedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_light_set_used_result** | [**List[MscLightSet]**](MscLightSet.md) |  | [optional] 
**result** | [**List[MscLightSet]**](MscLightSet.md)| alias for **json_msc_light_set_used_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_msc_light_set_used_result import JsonMscLightSetUsedResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscLightSetUsedResult from a JSON string
json_msc_light_set_used_result_instance = JsonMscLightSetUsedResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscLightSetUsedResult.to_json())

# convert the object into a dict
json_msc_light_set_used_result_dict = json_msc_light_set_used_result_instance.to_dict()
# create an instance of JsonMscLightSetUsedResult from a dict
json_msc_light_set_used_result_from_dict = JsonMscLightSetUsedResult.from_dict(json_msc_light_set_used_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


