# JsonMscLeafParamByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_leaf_param_by_analyse_id_result** | [**List[StatisticLeafParameter]**](StatisticLeafParameter.md) |  | [optional] 
**result** | [**List[StatisticLeafParameter]**](StatisticLeafParameter.md)| alias for **json_msc_leaf_param_by_analyse_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_msc_leaf_param_by_analyse_id_result import JsonMscLeafParamByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscLeafParamByAnalyseIDResult from a JSON string
json_msc_leaf_param_by_analyse_id_result_instance = JsonMscLeafParamByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscLeafParamByAnalyseIDResult.to_json())

# convert the object into a dict
json_msc_leaf_param_by_analyse_id_result_dict = json_msc_leaf_param_by_analyse_id_result_instance.to_dict()
# create an instance of JsonMscLeafParamByAnalyseIDResult from a dict
json_msc_leaf_param_by_analyse_id_result_from_dict = JsonMscLeafParamByAnalyseIDResult.from_dict(json_msc_leaf_param_by_analyse_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


