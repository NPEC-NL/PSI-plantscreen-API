# JsonOwnerIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_owner_id_result** | [**List[OwnerIDWrapper]**](OwnerIDWrapper.md) |  | [optional] 
**result** | [**List[OwnerIDWrapper]**](OwnerIDWrapper.md)| alias for **json_owner_id_result**  | 

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
from plantscreen.models.json_owner_id_result import JsonOwnerIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonOwnerIDResult from a JSON string
json_owner_id_result_instance = JsonOwnerIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonOwnerIDResult.to_json())

# convert the object into a dict
json_owner_id_result_dict = json_owner_id_result_instance.to_dict()
# create an instance of JsonOwnerIDResult from a dict
json_owner_id_result_from_dict = JsonOwnerIDResult.from_dict(json_owner_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


