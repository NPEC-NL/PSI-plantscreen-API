# JsonScan3dAnalyzedModelByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_scan3d_analyzed_model_by_analyse_id_result** | [**List[Scan3DAnalyzedModel]**](Scan3DAnalyzedModel.md) |  | [optional] 
**result** | [**List[Scan3DAnalyzedModel]**](Scan3DAnalyzedModel.md)| alias for **json_scan3d_analyzed_model_by_analyse_id_result**  | 

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
from plantscreen.models.json_scan3d_analyzed_model_by_analyse_id_result import JsonScan3dAnalyzedModelByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonScan3dAnalyzedModelByAnalyseIDResult from a JSON string
json_scan3d_analyzed_model_by_analyse_id_result_instance = JsonScan3dAnalyzedModelByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonScan3dAnalyzedModelByAnalyseIDResult.to_json())

# convert the object into a dict
json_scan3d_analyzed_model_by_analyse_id_result_dict = json_scan3d_analyzed_model_by_analyse_id_result_instance.to_dict()
# create an instance of JsonScan3dAnalyzedModelByAnalyseIDResult from a dict
json_scan3d_analyzed_model_by_analyse_id_result_from_dict = JsonScan3dAnalyzedModelByAnalyseIDResult.from_dict(json_scan3d_analyzed_model_by_analyse_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


