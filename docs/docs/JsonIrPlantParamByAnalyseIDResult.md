# JsonIrPlantParamByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_ir_plant_param_by_analyse_id_result** | [**List[StatisticPlantParameter]**](StatisticPlantParameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_ir_plant_param_by_analyse_id_result import JsonIrPlantParamByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIrPlantParamByAnalyseIDResult from a JSON string
json_ir_plant_param_by_analyse_id_result_instance = JsonIrPlantParamByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonIrPlantParamByAnalyseIDResult.to_json())

# convert the object into a dict
json_ir_plant_param_by_analyse_id_result_dict = json_ir_plant_param_by_analyse_id_result_instance.to_dict()
# create an instance of JsonIrPlantParamByAnalyseIDResult from a dict
json_ir_plant_param_by_analyse_id_result_from_dict = JsonIrPlantParamByAnalyseIDResult.from_dict(json_ir_plant_param_by_analyse_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


