# JsonFcPlantParamByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_fc_plant_param_by_analyse_id_result** | [**List[PlantParameter]**](PlantParameter.md) |  | [optional] 
**result** | [**List[PlantParameter]**](PlantParameter.md)| alias for **json_fc_plant_param_by_analyse_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_fc_plant_param_by_analyse_id_result import JsonFcPlantParamByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFcPlantParamByAnalyseIDResult from a JSON string
json_fc_plant_param_by_analyse_id_result_instance = JsonFcPlantParamByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonFcPlantParamByAnalyseIDResult.to_json())

# convert the object into a dict
json_fc_plant_param_by_analyse_id_result_dict = json_fc_plant_param_by_analyse_id_result_instance.to_dict()
# create an instance of JsonFcPlantParamByAnalyseIDResult from a dict
json_fc_plant_param_by_analyse_id_result_from_dict = JsonFcPlantParamByAnalyseIDResult.from_dict(json_fc_plant_param_by_analyse_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


