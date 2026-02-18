# JsonRgbPlantParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_rgb_plant_param_result** | [**List[PlantParameter]**](PlantParameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_rgb_plant_param_result import JsonRgbPlantParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRgbPlantParamResult from a JSON string
json_rgb_plant_param_result_instance = JsonRgbPlantParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonRgbPlantParamResult.to_json())

# convert the object into a dict
json_rgb_plant_param_result_dict = json_rgb_plant_param_result_instance.to_dict()
# create an instance of JsonRgbPlantParamResult from a dict
json_rgb_plant_param_result_from_dict = JsonRgbPlantParamResult.from_dict(json_rgb_plant_param_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


