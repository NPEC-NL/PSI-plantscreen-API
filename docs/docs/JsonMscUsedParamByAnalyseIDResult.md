# JsonMscUsedParamByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_used_param_by_analyse_id_result** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**result** | [**List[Parameter]**](Parameter.md)| alias for **json_msc_used_param_by_analyse_id_result**  | 

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
from plantscreen.models.json_msc_used_param_by_analyse_id_result import JsonMscUsedParamByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscUsedParamByAnalyseIDResult from a JSON string
json_msc_used_param_by_analyse_id_result_instance = JsonMscUsedParamByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscUsedParamByAnalyseIDResult.to_json())

# convert the object into a dict
json_msc_used_param_by_analyse_id_result_dict = json_msc_used_param_by_analyse_id_result_instance.to_dict()
# create an instance of JsonMscUsedParamByAnalyseIDResult from a dict
json_msc_used_param_by_analyse_id_result_from_dict = JsonMscUsedParamByAnalyseIDResult.from_dict(json_msc_used_param_by_analyse_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


