# JsonIrUsedParamByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_ir_used_param_by_analyse_id_result** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**result** | [**List[Parameter]**](Parameter.md)| alias for **json_ir_used_param_by_analyse_id_result**  | 

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
from plantscreen.models.json_ir_used_param_by_analyse_id_result import JsonIrUsedParamByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIrUsedParamByAnalyseIDResult from a JSON string
json_ir_used_param_by_analyse_id_result_instance = JsonIrUsedParamByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonIrUsedParamByAnalyseIDResult.to_json())

# convert the object into a dict
json_ir_used_param_by_analyse_id_result_dict = json_ir_used_param_by_analyse_id_result_instance.to_dict()
# create an instance of JsonIrUsedParamByAnalyseIDResult from a dict
json_ir_used_param_by_analyse_id_result_from_dict = JsonIrUsedParamByAnalyseIDResult.from_dict(json_ir_used_param_by_analyse_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


