# Tray_type XML Models


## TRectangleShape

Name | Type
------------- | -------------
**name** | **str**
**left** | **int**
**top** | **int**
**right** | **int**
**bottom** | **int**


## TMultiShapes

Name | Type
------------- | -------------
**rectangles** | **Optional[List[TRectangleShape]]**


## TLineShapes

_No fields found._


## TAnyShapes

Name | Type
------------- | -------------
**width** | **float**
**height** | **float**
**xratio** | **float**
**yratio** | **float**
**ps** | **float**
**psx** | **float**
**psy** | **float**
**t_line_shapes** | **Optional[TLineShapes]**
**t_multi_shapes** | **Optional[TMultiShapes]**


---
[Back to top](#) [Back to API Endpoints](../API_endpoints.md) [Back to CompleteAPIClient](../CompleteAPIClient.md) [Back to README](../README.md)
