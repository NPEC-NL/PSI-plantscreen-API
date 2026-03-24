# JsonHcParameterImageByAnalyseIDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_hc_parameter_image_by_analyse_id_result** | [**ParameterImage**](ParameterImage.md) |  | [optional] 
**result** | [**ParameterImage**](ParameterImage.md)| alias for **json_hc_parameter_image_by_analyse_id_result**  | 

## Links

### 1:1
Name | Model | Linked Via
------------ | ------------- | -------------


### 1:n
Name | Model | API | Operation | Parameter
------------ | ------------- | ------------- | ------------- | -------------


## Example

```python
from plantscreen.models.json_hc_parameter_image_by_analyse_id_result import JsonHcParameterImageByAnalyseIDResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonHcParameterImageByAnalyseIDResult from a JSON string
json_hc_parameter_image_by_analyse_id_result_instance = JsonHcParameterImageByAnalyseIDResult.from_json(json)
# print the JSON string representation of the object
print(JsonHcParameterImageByAnalyseIDResult.to_json())

# convert the object into a dict
json_hc_parameter_image_by_analyse_id_result_dict = json_hc_parameter_image_by_analyse_id_result_instance.to_dict()
# create an instance of JsonHcParameterImageByAnalyseIDResult from a dict
json_hc_parameter_image_by_analyse_id_result_from_dict = JsonHcParameterImageByAnalyseIDResult.from_dict(json_hc_parameter_image_by_analyse_id_result_dict)
```
[Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)


