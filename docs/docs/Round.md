# Round


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **int** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**round_date_start** | **datetime** |  | [optional] 
**round_date_stop** | **datetime** |  | [optional] 
**round_done** | **bool** |  | [optional] 
**round_id** | **int** |  | [optional] 
**round_protocol_path** | **str** | filetype | [optional] 
**round_status** | **str** |  | [optional] 

## Example

```python
from plantscreen.models.round import Round

# TODO update the JSON string below
json = "{}"
# create an instance of Round from a JSON string
round_instance = Round.from_json(json)
# print the JSON string representation of the object
print(Round.to_json())

# convert the object into a dict
round_dict = round_instance.to_dict()
# create an instance of Round from a dict
round_from_dict = Round.from_dict(round_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


