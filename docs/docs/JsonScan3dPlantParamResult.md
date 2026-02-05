# JsonScan3dPlantParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_scan3d_plant_param_result** | [**List[PlantParameter]**](PlantParameter.md) |  | [optional] 

## Example

```python
from plantscreen.models.json_scan3d_plant_param_result import JsonScan3dPlantParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonScan3dPlantParamResult from a JSON string
json_scan3d_plant_param_result_instance = JsonScan3dPlantParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonScan3dPlantParamResult.to_json())

# convert the object into a dict
json_scan3d_plant_param_result_dict = json_scan3d_plant_param_result_instance.to_dict()
# create an instance of JsonScan3dPlantParamResult from a dict
json_scan3d_plant_param_result_from_dict = JsonScan3dPlantParamResult.from_dict(json_scan3d_plant_param_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


