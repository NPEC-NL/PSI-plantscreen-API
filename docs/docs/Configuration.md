# Configuration XML Models


## Item

Name | Type
------------- | -------------
**z** | **int**
**x_shift** | **int**
**y_shift** | **int**


## CenterShift

Name | Type
------------- | -------------
**items** | **List[Item]**


## Configuration

Name | Type
------------- | -------------
**windowing_mode** | **int**
**extract_lines** | **int**
**focus** | **int**
**width** | **int**
**height** | **int**
**default_z** | **int**
**mask_center_x** | **int**
**mask_center_y** | **int**
**barrel** | **float**
**mask_rotation** | **float**
**z_conversion** | **int**
**ratio_coefficient** | **float**
**backward_fec** | **bool**
**fixed_x** | **bool**
**fixed_x_px_mm_ratio** | **float**
**fixed_y** | **bool**
**fixed_y_px_mm_ratio** | **float**
**center_shift** | **CenterShift**
**scan_lines** | **int**
**position_start** | **int**
**position_end** | **int**
**scan_speed** | **int**
**move_speed** | **int**
**scan_axis** | **str**
**heating_temp_diff** | **float**
**heating_time** | **int**


---
[Back to top](#) | [Back to API Endpoints](../API_endpoints.md) | [Back to CompleteAPIClient](../CompleteAPIClient.md) | [Back to README](../README.md)
