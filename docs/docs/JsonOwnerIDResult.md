# JsonOwnerIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_owner_id_result** | [**List[OwnerIDWrapper]**](OwnerIDWrapper.md) |  | [optional] 
**result** | [**List[OwnerIDWrapper]**](OwnerIDWrapper.md)| alias for **json_owner_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
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
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


