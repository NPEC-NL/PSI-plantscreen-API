# JsonActionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_action_result** | [**Action**](Action.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_action_result import JsonActionResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonActionResult from a JSON string
json_action_result_instance = JsonActionResult.from_json(json)
# print the JSON string representation of the object
print(JsonActionResult.to_json())

# convert the object into a dict
json_action_result_dict = json_action_result_instance.to_dict()
# create an instance of JsonActionResult from a dict
json_action_result_from_dict = JsonActionResult.from_dict(json_action_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


