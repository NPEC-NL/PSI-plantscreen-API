# JsonScan3dLeafParamByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_scan3d_leaf_param_by_analyse_id_result** | [**List[LeafParameter]**](LeafParameter.md) |  | [optional] 
**result** | [**List[LeafParameter]**](LeafParameter.md)| alias for **json_scan3d_leaf_param_by_analyse_id_result**  | 

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
from plantscreen.models.json_scan3d_leaf_param_by_analyse_id_result import JsonScan3dLeafParamByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonScan3dLeafParamByAnalyseIDResult from a JSON string
json_scan3d_leaf_param_by_analyse_id_result_instance = JsonScan3dLeafParamByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonScan3dLeafParamByAnalyseIDResult.to_json())

# convert the object into a dict
json_scan3d_leaf_param_by_analyse_id_result_dict = json_scan3d_leaf_param_by_analyse_id_result_instance.to_dict()
# create an instance of JsonScan3dLeafParamByAnalyseIDResult from a dict
json_scan3d_leaf_param_by_analyse_id_result_from_dict = JsonScan3dLeafParamByAnalyseIDResult.from_dict(json_scan3d_leaf_param_by_analyse_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


