# swagger_client.RgbApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rgb_greening_mask_image**](RgbApi.md#rgb_greening_mask_image) | **GET** /Rgb/Greening/Mask/Image | Returns RGB greening data data masked by the plant mask for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. The greening mask image is created by greening analysis, therefore it is only available if greening analysis has been performed on the required data.
[**rgb_greening_mask_image_measure**](RgbApi.md#rgb_greening_mask_image_measure) | **GET** /Rgb/Greening/Mask/Image/Measure | Returns RGB greening data masked by the plant mask defined by RGB measure ID. The greening mask image is created by greening analysis, therefore it is only available if greening analysis has been performed on the required data.
[**rgb_imaging**](RgbApi.md#rgb_imaging) | **GET** /Rgb/Imaging | Returns FluorCam imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**rgb_imaging_extended_data**](RgbApi.md#rgb_imaging_extended_data) | **GET** /Rgb/Imaging/ExtendedData | Returns RGB extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)
[**rgb_imaging_extended_data_measure**](RgbApi.md#rgb_imaging_extended_data_measure) | **GET** /Rgb/Imaging/ExtendedData/Measure | Returns RGB imaging extended data by RGB measure ID. (Only available for field systems.)
[**rgb_imaging_measure**](RgbApi.md#rgb_imaging_measure) | **GET** /Rgb/Imaging/Measure | Returns RGB imaging data by RGB measure ID.
[**rgb_leaf_param**](RgbApi.md#rgb_leaf_param) | **GET** /Rgb/Leaf/Param | Returns the RGB leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**rgb_leaf_param_analyse**](RgbApi.md#rgb_leaf_param_analyse) | **GET** /Rgb/Leaf/Param/Analyse | Returns the RGB leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**rgb_leaf_param_color**](RgbApi.md#rgb_leaf_param_color) | **GET** /Rgb/Leaf/Param/Color | Returns the RGB greening leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**rgb_leaf_param_color_analyse**](RgbApi.md#rgb_leaf_param_color_analyse) | **GET** /Rgb/Leaf/Param/Color/Analyse | Returns the RGB greening leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID (for greening analysis).
[**rgb_param**](RgbApi.md#rgb_param) | **GET** /Rgb/Param | Returns one RGB morfo parameter by parameter ID.
[**rgb_param_color_used**](RgbApi.md#rgb_param_color_used) | **GET** /Rgb/Param/Color/Used | Returns the greening RGB plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**rgb_param_color_used_analyse**](RgbApi.md#rgb_param_color_used_analyse) | **GET** /Rgb/Param/Color/Used/Analyse | Returns the greening RGB plant and leaf parameters used in the greening analysis defined by analyse ID (for greening analysis).
[**rgb_param_used**](RgbApi.md#rgb_param_used) | **GET** /Rgb/Param/Used | Returns the RGB plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**rgb_param_used_analyse**](RgbApi.md#rgb_param_used_analyse) | **GET** /Rgb/Param/Used/Analyse | Returns the RGB plant and leaf parameters used in the analysis defined by analyse ID.
[**rgb_plant_mask**](RgbApi.md#rgb_plant_mask) | **GET** /Rgb/Plant/Mask | Returns RGB plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**rgb_plant_mask_measure**](RgbApi.md#rgb_plant_mask_measure) | **GET** /Rgb/Plant/Mask/Measure | Returns the RGB plant mask created for the measured tray defined by RGB measure ID.
[**rgb_plant_param**](RgbApi.md#rgb_plant_param) | **GET** /Rgb/Plant/Param | Returns the RGB plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**rgb_plant_param_analyse**](RgbApi.md#rgb_plant_param_analyse) | **GET** /Rgb/Plant/Param/Analyse | Returns the RGB plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**rgb_plant_param_color**](RgbApi.md#rgb_plant_param_color) | **GET** /Rgb/Plant/Param/Color | Returns the RGB greening plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**rgb_plant_param_color_analyse**](RgbApi.md#rgb_plant_param_color_analyse) | **GET** /Rgb/Plant/Param/Color/Analyse | Returns the RGB greening plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID (for greening analysis).

# **rgb_greening_mask_image**
> JsonRgbGreeningMaskImageResult rgb_greening_mask_image(device_id, round_id, tray_id)

Returns RGB greening data data masked by the plant mask for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. The greening mask image is created by greening analysis, therefore it is only available if greening analysis has been performed on the required data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns RGB greening data data masked by the plant mask for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. The greening mask image is created by greening analysis, therefore it is only available if greening analysis has been performed on the required data.
    api_response = api_instance.rgb_greening_mask_image(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_greening_mask_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonRgbGreeningMaskImageResult**](JsonRgbGreeningMaskImageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_greening_mask_image_measure**
> JsonRgbGreeningMaskImageByMeasureIDResult rgb_greening_mask_image_measure(id)

Returns RGB greening data masked by the plant mask defined by RGB measure ID. The greening mask image is created by greening analysis, therefore it is only available if greening analysis has been performed on the required data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | measureID

try:
    # Returns RGB greening data masked by the plant mask defined by RGB measure ID. The greening mask image is created by greening analysis, therefore it is only available if greening analysis has been performed on the required data.
    api_response = api_instance.rgb_greening_mask_image_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_greening_mask_image_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonRgbGreeningMaskImageByMeasureIDResult**](JsonRgbGreeningMaskImageByMeasureIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_imaging**
> JsonRgbImagingResult rgb_imaging(device_id, round_id, tray_id)

Returns FluorCam imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns FluorCam imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.rgb_imaging(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_imaging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonRgbImagingResult**](JsonRgbImagingResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_imaging_extended_data**
> JsonRgbMeasureExtendedDataResult rgb_imaging_extended_data(device_id, round_id, tray_id)

Returns RGB extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns RGB extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)
    api_response = api_instance.rgb_imaging_extended_data(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_imaging_extended_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonRgbMeasureExtendedDataResult**](JsonRgbMeasureExtendedDataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_imaging_extended_data_measure**
> JsonRgbMeasureExtendedDataByIDResult rgb_imaging_extended_data_measure(id)

Returns RGB imaging extended data by RGB measure ID. (Only available for field systems.)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | measureID

try:
    # Returns RGB imaging extended data by RGB measure ID. (Only available for field systems.)
    api_response = api_instance.rgb_imaging_extended_data_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_imaging_extended_data_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonRgbMeasureExtendedDataByIDResult**](JsonRgbMeasureExtendedDataByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_imaging_measure**
> JsonRgbImagingByIDResult rgb_imaging_measure(id)

Returns RGB imaging data by RGB measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | measureID

try:
    # Returns RGB imaging data by RGB measure ID.
    api_response = api_instance.rgb_imaging_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_imaging_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonRgbImagingByIDResult**](JsonRgbImagingByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_leaf_param**
> JsonRgbLeafParamResult rgb_leaf_param(device_id, round_id, tray_id, param_id)

Returns the RGB leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the RGB leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.rgb_leaf_param(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_leaf_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonRgbLeafParamResult**](JsonRgbLeafParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_leaf_param_analyse**
> JsonRgbLeafParamByAnalyseIDResult rgb_leaf_param_analyse(id, param_id)

Returns the RGB leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the RGB leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.rgb_leaf_param_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_leaf_param_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonRgbLeafParamByAnalyseIDResult**](JsonRgbLeafParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_leaf_param_color**
> JsonRgbLeafParamColorResult rgb_leaf_param_color(device_id, round_id, tray_id, param_id)

Returns the RGB greening leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the RGB greening leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.rgb_leaf_param_color(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_leaf_param_color: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonRgbLeafParamColorResult**](JsonRgbLeafParamColorResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_leaf_param_color_analyse**
> JsonRgbLeafParamColorByAnalyseIDResult rgb_leaf_param_color_analyse(id, param_id)

Returns the RGB greening leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID (for greening analysis).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the RGB greening leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID (for greening analysis).
    api_response = api_instance.rgb_leaf_param_color_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_leaf_param_color_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonRgbLeafParamColorByAnalyseIDResult**](JsonRgbLeafParamColorByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_param**
> JsonRgbParamResult rgb_param(id)

Returns one RGB morfo parameter by parameter ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | paramID

try:
    # Returns one RGB morfo parameter by parameter ID.
    api_response = api_instance.rgb_param(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| paramID | 

### Return type

[**JsonRgbParamResult**](JsonRgbParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_param_color_used**
> JsonRgbUsedParamColorResult rgb_param_color_used(device_id, round_id, tray_id)

Returns the greening RGB plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns the greening RGB plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.rgb_param_color_used(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_param_color_used: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonRgbUsedParamColorResult**](JsonRgbUsedParamColorResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_param_color_used_analyse**
> JsonRgbUsedParamColorByAnalyseIDResult rgb_param_color_used_analyse(id)

Returns the greening RGB plant and leaf parameters used in the greening analysis defined by analyse ID (for greening analysis).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | analyseID

try:
    # Returns the greening RGB plant and leaf parameters used in the greening analysis defined by analyse ID (for greening analysis).
    api_response = api_instance.rgb_param_color_used_analyse(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_param_color_used_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 

### Return type

[**JsonRgbUsedParamColorByAnalyseIDResult**](JsonRgbUsedParamColorByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_param_used**
> JsonRgbcUsedParamsResult rgb_param_used(device_id, round_id, tray_id)

Returns the RGB plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns the RGB plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.rgb_param_used(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_param_used: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonRgbcUsedParamsResult**](JsonRgbcUsedParamsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_param_used_analyse**
> JsonRgbUsedParamByAnalyseIDResult rgb_param_used_analyse(id)

Returns the RGB plant and leaf parameters used in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | analyseID

try:
    # Returns the RGB plant and leaf parameters used in the analysis defined by analyse ID.
    api_response = api_instance.rgb_param_used_analyse(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_param_used_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 

### Return type

[**JsonRgbUsedParamByAnalyseIDResult**](JsonRgbUsedParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_plant_mask**
> JsonRgbPlantMaskResult rgb_plant_mask(device_id, round_id, tray_id)

Returns RGB plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns RGB plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.rgb_plant_mask(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_plant_mask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonRgbPlantMaskResult**](JsonRgbPlantMaskResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_plant_mask_measure**
> JsonRgbPlantMaskByMeasureIDResult rgb_plant_mask_measure(id)

Returns the RGB plant mask created for the measured tray defined by RGB measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | measureID

try:
    # Returns the RGB plant mask created for the measured tray defined by RGB measure ID.
    api_response = api_instance.rgb_plant_mask_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_plant_mask_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonRgbPlantMaskByMeasureIDResult**](JsonRgbPlantMaskByMeasureIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_plant_param**
> JsonRgbPlantParamResult rgb_plant_param(device_id, round_id, tray_id, param_id)

Returns the RGB plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the RGB plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.rgb_plant_param(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_plant_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonRgbPlantParamResult**](JsonRgbPlantParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_plant_param_analyse**
> JsonRgbPlantParamByAnalyseIDResult rgb_plant_param_analyse(id, param_id)

Returns the RGB plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the RGB plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.rgb_plant_param_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_plant_param_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonRgbPlantParamByAnalyseIDResult**](JsonRgbPlantParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_plant_param_color**
> JsonRgbPlantParamColorResult rgb_plant_param_color(device_id, round_id, tray_id, param_id)

Returns the RGB greening plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the RGB greening plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.rgb_plant_param_color(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_plant_param_color: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonRgbPlantParamColorResult**](JsonRgbPlantParamColorResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rgb_plant_param_color_analyse**
> JsonRgbPlantParamColorByAnalyseIDResult rgb_plant_param_color_analyse(id, param_id)

Returns the RGB greening plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID (for greening analysis).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RgbApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the RGB greening plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID (for greening analysis).
    api_response = api_instance.rgb_plant_param_color_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RgbApi->rgb_plant_param_color_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonRgbPlantParamColorByAnalyseIDResult**](JsonRgbPlantParamColorByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

