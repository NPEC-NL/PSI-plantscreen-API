# Plant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plant_barcode** | **str** |  | [optional] 
**plant_id** | **int** |  | [optional] 
**plant_info** | **str** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**tray_area** | **str** |  | [optional] 

## Example

```python
from plantscreen.models.plant import Plant

# TODO update the JSON string below
json = "{}"
# create an instance of Plant from a JSON string
plant_instance = Plant.from_json(json)
# print the JSON string representation of the object
print(Plant.to_json())

# convert the object into a dict
plant_dict = plant_instance.to_dict()
# create an instance of Plant from a dict
plant_from_dict = Plant.from_dict(plant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


