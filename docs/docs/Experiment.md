# Experiment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**experiment_info** | **str** |  | [optional] 
**experiment_name** | **str** |  | [optional] 
**experiment_status** | **str** |  | [optional] 
**owner_id** | **int** |  | [optional] 
**status_changed_date** | **datetime** |  | [optional] 

## Example

```python
from plantscreen.models.experiment import Experiment

# TODO update the JSON string below
json = "{}"
# create an instance of Experiment from a JSON string
experiment_instance = Experiment.from_json(json)
# print the JSON string representation of the object
print(Experiment.to_json())

# convert the object into a dict
experiment_dict = experiment_instance.to_dict()
# create an instance of Experiment from a dict
experiment_from_dict = Experiment.from_dict(experiment_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


