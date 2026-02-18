# ExperimentIDWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **int** |  | [optional] 

## Example

```python
from plantscreen.models.experiment_id_wrapper import ExperimentIDWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentIDWrapper from a JSON string
experiment_id_wrapper_instance = ExperimentIDWrapper.from_json(json)
# print the JSON string representation of the object
print(ExperimentIDWrapper.to_json())

# convert the object into a dict
experiment_id_wrapper_dict = experiment_id_wrapper_instance.to_dict()
# create an instance of ExperimentIDWrapper from a dict
experiment_id_wrapper_from_dict = ExperimentIDWrapper.from_dict(experiment_id_wrapper_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


