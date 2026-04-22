# JsonFcLeafParamByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_fc_leaf_param_by_analyse_id_result** | [**List[LeafParameter]**](LeafParameter.md) |  | [optional] 
**result** | [**List[LeafParameter]**](LeafParameter.md)| alias for **json_fc_leaf_param_by_analyse_id_result**  | 

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
from plantscreen.models.json_fc_leaf_param_by_analyse_id_result import JsonFcLeafParamByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFcLeafParamByAnalyseIDResult from a JSON string
json_fc_leaf_param_by_analyse_id_result_instance = JsonFcLeafParamByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonFcLeafParamByAnalyseIDResult.to_json())

# convert the object into a dict
json_fc_leaf_param_by_analyse_id_result_dict = json_fc_leaf_param_by_analyse_id_result_instance.to_dict()
# create an instance of JsonFcLeafParamByAnalyseIDResult from a dict
json_fc_leaf_param_by_analyse_id_result_from_dict = JsonFcLeafParamByAnalyseIDResult.from_dict(json_fc_leaf_param_by_analyse_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


