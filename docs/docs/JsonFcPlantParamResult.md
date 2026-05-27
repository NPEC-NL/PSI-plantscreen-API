# JsonFcPlantParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_fc_plant_param_result** | [**List[PlantParameter]**](PlantParameter.md) |  | [optional] 
**result** | [**List[PlantParameter]**](PlantParameter.md)| alias for **json_fc_plant_param_result**  | 

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
from plantscreen.models.json_fc_plant_param_result import JsonFcPlantParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFcPlantParamResult from a JSON string
json_fc_plant_param_result_instance = JsonFcPlantParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonFcPlantParamResult.to_json())

# convert the object into a dict
json_fc_plant_param_result_dict = json_fc_plant_param_result_instance.to_dict()
# create an instance of JsonFcPlantParamResult from a dict
json_fc_plant_param_result_from_dict = JsonFcPlantParamResult.from_dict(json_fc_plant_param_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


