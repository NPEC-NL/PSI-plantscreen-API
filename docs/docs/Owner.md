# Owner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_failed_date** | **datetime** |  | [optional] 
**last_name** | **str** |  | [optional] 
**last_success_login** | **datetime** |  | [optional] 
**login** | **str** |  | [optional] 
**owner_id** | **int** |  | [optional] 
**sms_phone_number** | **str** |  | [optional] 


## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------
experiments | List[[**object**](Experiment.md)]] | ExperimentApi |  | OwnerID

## Example

```python
from plantscreen.models.owner import Owner

# TODO update the JSON string below
json = "{}"
# create an instance of Owner from a JSON string
owner_instance = Owner.from_json(json)
# print the JSON string representation of the object
print(Owner.to_json())

# convert the object into a dict
owner_dict = owner_instance.to_dict()
# create an instance of Owner from a dict
owner_from_dict = Owner.from_dict(owner_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


