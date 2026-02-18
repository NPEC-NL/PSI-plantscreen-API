# JsonHcPlantParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_plant_param_result** | [**List[StatisticPlantParameter]**](StatisticPlantParameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_hc_plant_param_result import JsonHcPlantParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcPlantParamResult from a JSON string
json_hc_plant_param_result_instance = JsonHcPlantParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcPlantParamResult.to_json())

# convert the object into a dict
json_hc_plant_param_result_dict = json_hc_plant_param_result_instance.to_dict()
# create an instance of JsonHcPlantParamResult from a dict
json_hc_plant_param_result_from_dict = JsonHcPlantParamResult.from_dict(json_hc_plant_param_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


