# JsonSprayActionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_spray_action_result** | [**List[SprayAction]**](SprayAction.md) |  | [optional] 
**result** | [**List[SprayAction]**](SprayAction.md)| alias for **json_spray_action_result**  | 

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
from plantscreen.models.json_spray_action_result import JsonSprayActionResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSprayActionResult from a JSON string
json_spray_action_result_instance = JsonSprayActionResult.from_json(json)
# print the JSON string representation of the object
print(JsonSprayActionResult.to_json())

# convert the object into a dict
json_spray_action_result_dict = json_spray_action_result_instance.to_dict()
# create an instance of JsonSprayActionResult from a dict
json_spray_action_result_from_dict = JsonSprayActionResult.from_dict(json_spray_action_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


