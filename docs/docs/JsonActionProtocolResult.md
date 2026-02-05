# JsonActionProtocolResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_action_protocol_result** | [**ActionProtocol**](ActionProtocol.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_action_protocol_result import JsonActionProtocolResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonActionProtocolResult from a JSON string
json_action_protocol_result_instance = JsonActionProtocolResult.from_json(json)
# print the JSON string representation of the object
print(JsonActionProtocolResult.to_json())

# convert the object into a dict
json_action_protocol_result_dict = json_action_protocol_result_instance.to_dict()
# create an instance of JsonActionProtocolResult from a dict
json_action_protocol_result_from_dict = JsonActionProtocolResult.from_dict(json_action_protocol_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


