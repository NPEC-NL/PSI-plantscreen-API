# JsonActionGroupResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_action_group_result** | [**ActionGroup**](ActionGroup.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_action_group_result import JsonActionGroupResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonActionGroupResult from a JSON string
json_action_group_result_instance = JsonActionGroupResult.from_json(json)
# print the JSON string representation of the object
print(JsonActionGroupResult.to_json())

# convert the object into a dict
json_action_group_result_dict = json_action_group_result_instance.to_dict()
# create an instance of JsonActionGroupResult from a dict
json_action_group_result_from_dict = JsonActionGroupResult.from_dict(json_action_group_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


