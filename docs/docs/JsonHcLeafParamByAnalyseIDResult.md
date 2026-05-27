# JsonHcLeafParamByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_leaf_param_by_analyse_id_result** | [**List[StatisticLeafParameter]**](StatisticLeafParameter.md) |  | [optional] 
**result** | [**List[StatisticLeafParameter]**](StatisticLeafParameter.md)| alias for **json_hc_leaf_param_by_analyse_id_result**  | 

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
from plantscreen.models.json_hc_leaf_param_by_analyse_id_result import JsonHcLeafParamByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcLeafParamByAnalyseIDResult from a JSON string
json_hc_leaf_param_by_analyse_id_result_instance = JsonHcLeafParamByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcLeafParamByAnalyseIDResult.to_json())

# convert the object into a dict
json_hc_leaf_param_by_analyse_id_result_dict = json_hc_leaf_param_by_analyse_id_result_instance.to_dict()
# create an instance of JsonHcLeafParamByAnalyseIDResult from a dict
json_hc_leaf_param_by_analyse_id_result_from_dict = JsonHcLeafParamByAnalyseIDResult.from_dict(json_hc_leaf_param_by_analyse_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


