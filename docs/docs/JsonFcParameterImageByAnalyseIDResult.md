# JsonFcParameterImageByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_fc_parameter_image_by_analyse_id_result** | [**ParameterImage**](ParameterImage.md) |  | [optional] 
**result** | [**ParameterImage**](ParameterImage.md)| alias for **json_fc_parameter_image_by_analyse_id_result**  | 

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
from plantscreen.models.json_fc_parameter_image_by_analyse_id_result import JsonFcParameterImageByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFcParameterImageByAnalyseIDResult from a JSON string
json_fc_parameter_image_by_analyse_id_result_instance = JsonFcParameterImageByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonFcParameterImageByAnalyseIDResult.to_json())

# convert the object into a dict
json_fc_parameter_image_by_analyse_id_result_dict = json_fc_parameter_image_by_analyse_id_result_instance.to_dict()
# create an instance of JsonFcParameterImageByAnalyseIDResult from a dict
json_fc_parameter_image_by_analyse_id_result_from_dict = JsonFcParameterImageByAnalyseIDResult.from_dict(json_fc_parameter_image_by_analyse_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


