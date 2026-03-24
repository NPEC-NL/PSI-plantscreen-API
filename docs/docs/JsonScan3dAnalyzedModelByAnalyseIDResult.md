# JsonScan3dAnalyzedModelByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_scan3d_analyzed_model_by_analyse_id_result** | [**List[Scan3DAnalyzedModel]**](Scan3DAnalyzedModel.md) |  | [optional] 
**result** | [**List[Scan3DAnalyzedModel]**](Scan3DAnalyzedModel.md)| alias for **json_scan3d_analyzed_model_by_analyse_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
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
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


