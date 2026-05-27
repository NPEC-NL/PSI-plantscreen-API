# JsonMscParameterImageByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_msc_parameter_image_by_analyse_id_result** | [**ParameterImage**](ParameterImage.md) |  | [optional] 
**result** | [**ParameterImage**](ParameterImage.md)| alias for **json_msc_parameter_image_by_analyse_id_result**  | 

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
from plantscreen.models.json_msc_parameter_image_by_analyse_id_result import JsonMscParameterImageByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMscParameterImageByAnalyseIDResult from a JSON string
json_msc_parameter_image_by_analyse_id_result_instance = JsonMscParameterImageByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonMscParameterImageByAnalyseIDResult.to_json())

# convert the object into a dict
json_msc_parameter_image_by_analyse_id_result_dict = json_msc_parameter_image_by_analyse_id_result_instance.to_dict()
# create an instance of JsonMscParameterImageByAnalyseIDResult from a dict
json_msc_parameter_image_by_analyse_id_result_from_dict = JsonMscParameterImageByAnalyseIDResult.from_dict(json_msc_parameter_image_by_analyse_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


