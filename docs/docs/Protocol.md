# Protocol XML Models


## Frame

Name | Type
------------- | -------------
**angle** | **Optional[int]**


## Light

Name | Type
------------- | -------------
**name** | **str**
**value** | **int**


## SetLight

Name | Type
------------- | -------------
**lights** | **List[Light]**


## TrayLoad

Name | Type
------------- | -------------
**row** | **int**
**count** | **int**


## ProtocolInner

Name | Type
------------- | -------------
**name** | **Optional[str]**
**value** | **Optional[str]**


## Offset

Name | Type
------------- | -------------
**value** | **int**


## Delay

Name | Type
------------- | -------------
**value** | **str**


## IR1

Name | Type
------------- | -------------
**height** | **str**
**offset** | **int**
**protocol** | **ProtocolInner**
**delay** | **str**


## PlantMask

Name | Type
------------- | -------------
**formula** | **Optional[str]**
**threshold** | **Optional[float]**
**median_filter_size** | **Optional[int]**
**min_size** | **Optional[int]**
**min_hole_size** | **Optional[int]**
**crop_objects_on_borders** | **Optional[bool]**
**crop_objects_on_borders_min_preserve_size** | **Optional[int]**
**use_reflection_reduction** | **Optional[bool]**
**skip_bad_exposed_points** | **Optional[bool]**


## RGBS

Name | Type
------------- | -------------
**height** | **Optional[str]**
**offset** | **Optional[int]**
**frame** | **Optional['Frame']**
**delay** | **Optional[str]**
**plant_mask** | **Optional[PlantMask]**


## Rgb

Name | Type
------------- | -------------
**red** | **Optional[int]**
**green** | **Optional[int]**
**blue** | **Optional[int]**
**brighten_multiplier** | **Optional[int]**


## Parameters

Name | Type
------------- | -------------
**parameter** | **Optional[str]**


## Values

Name | Type
------------- | -------------
**wl_surrounding** | **Optional[int]**
**min_valid_pixels_percentage** | **Optional[int]**


## SWIR

Name | Type
------------- | -------------
**height** | **Optional[str]**
**offset** | **Optional[int]**
**delay** | **Optional[str]**
**rgb** | **Optional[Rgb]**
**parameters** | **Optional[Parameters]**
**values** | **Optional[Values]**


## Analyse

Name | Type
------------- | -------------
**mask_erosion_level** | **Optional[int]**
**rgbs** | **Optional['RGBS']**
**swir** | **Optional['SWIR']**


## Prescription

Name | Type
------------- | -------------
**id** | **Optional[int]**
**name** | **Optional[str]**
**ir1** | **Optional[IR1]**
**rgbs** | **Optional[RGBS]**
**swir** | **Optional[SWIR]**
**analyse** | **Optional[Analyse]**


## Batch

Name | Type
------------- | -------------
**name** | **str**
**pid** | **int**
**date** | **str**


## Tray

Name | Type
------------- | -------------
**sid** | **str**
**id** | **int**
**pid** | **int**


## Measure

Name | Type
------------- | -------------
**adapt_time** | **Optional[str]**
**prescription** | **Optional[Prescription]**
**batches** | **Optional[List[Batch]]**
**trays** | **Optional[List[Tray]]**


## Protocol

Name | Type
------------- | -------------
**set_lights** | **Optional[List[SetLight]]**
**tray_load** | **Optional[TrayLoad]**
**measure** | **Optional[Measure]**


---
[Back to top](#) [Back to API Endpoints](../API_endpoints.md) [Back to CompleteAPIClient](../CompleteAPIClient.md) [Back to README](../README.md)
