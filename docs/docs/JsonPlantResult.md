# JsonPlantResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_plant_result** | [**List[Plant]**](Plant.md) |  | [optional] 
**result** | [**List[Plant]**](Plant.md)| alias for **json_plant_result**  | 

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
from plantscreen.models.json_plant_result import JsonPlantResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPlantResult from a JSON string
json_plant_result_instance = JsonPlantResult.from_json(json)
# print the JSON string representation of the object
print(JsonPlantResult.to_json())

# convert the object into a dict
json_plant_result_dict = json_plant_result_instance.to_dict()
# create an instance of JsonPlantResult from a dict
json_plant_result_from_dict = JsonPlantResult.from_dict(json_plant_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


