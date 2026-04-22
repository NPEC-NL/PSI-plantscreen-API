# JsonIrPlantParamResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_ir_plant_param_result** | [**List[StatisticPlantParameter]**](StatisticPlantParameter.md) |  | [optional] 
**result** | [**List[StatisticPlantParameter]**](StatisticPlantParameter.md)| alias for **json_ir_plant_param_result**  | 

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
from plantscreen.models.json_ir_plant_param_result import JsonIrPlantParamResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIrPlantParamResult from a JSON string
json_ir_plant_param_result_instance = JsonIrPlantParamResult.from_json(json)
# print the JSON string representation of the object
print(JsonIrPlantParamResult.to_json())

# convert the object into a dict
json_ir_plant_param_result_dict = json_ir_plant_param_result_instance.to_dict()
# create an instance of JsonIrPlantParamResult from a dict
json_ir_plant_param_result_from_dict = JsonIrPlantParamResult.from_dict(json_ir_plant_param_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


