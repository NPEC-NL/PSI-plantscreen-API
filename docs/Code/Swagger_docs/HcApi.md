# swagger_client.HcApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hc_imaging**](HcApi.md#hc_imaging) | **GET** /Hc/Imaging | Returns Hyperspectral imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**hc_imaging_extended_data**](HcApi.md#hc_imaging_extended_data) | **GET** /Hc/Imaging/ExtendedData | Returns Hyperspectral extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**hc_imaging_extended_data_measure**](HcApi.md#hc_imaging_extended_data_measure) | **GET** /Hc/Imaging/ExtendedData/Measure | Returns Hyperspectral imaging extended data by HC measure ID.
[**hc_imaging_measure**](HcApi.md#hc_imaging_measure) | **GET** /Hc/Imaging/Measure | Returns Hyperspectral imaging data by HC measure ID.
[**hc_leaf_param**](HcApi.md#hc_leaf_param) | **GET** /Hc/Leaf/Param | Returns the Hyperspectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**hc_leaf_param_analyse**](HcApi.md#hc_leaf_param_analyse) | **GET** /Hc/Leaf/Param/Analyse | Returns the Hyperspectral statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**hc_param**](HcApi.md#hc_param) | **GET** /Hc/Param | Returns one Hyperspectral parameter by parameter ID.
[**hc_param_image**](HcApi.md#hc_param_image) | **GET** /Hc/Param/Image | Returns the Hyperspectral parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**hc_param_image_analyse**](HcApi.md#hc_param_image_analyse) | **GET** /Hc/Param/Image/Analyse | Returns the Hyperspectral parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**hc_param_used**](HcApi.md#hc_param_used) | **GET** /Hc/Param/Used | Returns the Hyperspectral plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**hc_param_used_analyse**](HcApi.md#hc_param_used_analyse) | **GET** /Hc/Param/Used/Analyse | Returns the Hyperspectral plant and leaf parameters used in the analysis defined by analyse ID.
[**hc_plant_mask**](HcApi.md#hc_plant_mask) | **GET** /Hc/Plant/Mask | Returns Hyperspectral plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**hc_plant_mask_measure**](HcApi.md#hc_plant_mask_measure) | **GET** /Hc/Plant/Mask/Measure | Returns the Hyperspectral plant mask created for the measured tray defined by HC measure ID.
[**hc_plant_param**](HcApi.md#hc_plant_param) | **GET** /Hc/Plant/Param | Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**hc_plant_param_analyse**](HcApi.md#hc_plant_param_analyse) | **GET** /Hc/Plant/Param/Analyse | Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**hc_rgb_image**](HcApi.md#hc_rgb_image) | **GET** /Hc/Rgb/Image | Returns the Hyperspectral RGB image created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. The Hyperspectral RGB image is created by analysis, therefore it is only available if analysis has been performed on the required data.
[**hc_rgb_image_measure**](HcApi.md#hc_rgb_image_measure) | **GET** /Hc/Rgb/Image/Measure | Returns the Hyperspectral RGB image created for the measured tray by HC measure ID. The Hyperspectral RGB image is created by analysis, therefore it is only available if analysis has been performed on the required data.

# **hc_imaging**
> JsonHcImagingResult hc_imaging(device_id, round_id, tray_id)

Returns Hyperspectral imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns Hyperspectral imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.hc_imaging(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_imaging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonHcImagingResult**](JsonHcImagingResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_imaging_extended_data**
> JsonHcMeasureExtendedDataResult hc_imaging_extended_data(device_id, round_id, tray_id)

Returns Hyperspectral extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns Hyperspectral extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.hc_imaging_extended_data(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_imaging_extended_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonHcMeasureExtendedDataResult**](JsonHcMeasureExtendedDataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_imaging_extended_data_measure**
> JsonHcMeasureExtendedDataByIDResult hc_imaging_extended_data_measure(id)

Returns Hyperspectral imaging extended data by HC measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
id = 56 # int | measureID

try:
    # Returns Hyperspectral imaging extended data by HC measure ID.
    api_response = api_instance.hc_imaging_extended_data_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_imaging_extended_data_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonHcMeasureExtendedDataByIDResult**](JsonHcMeasureExtendedDataByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_imaging_measure**
> JsonHcImagingByIDResult hc_imaging_measure(id)

Returns Hyperspectral imaging data by HC measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
id = 56 # int | measureID

try:
    # Returns Hyperspectral imaging data by HC measure ID.
    api_response = api_instance.hc_imaging_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_imaging_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonHcImagingByIDResult**](JsonHcImagingByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_leaf_param**
> JsonHcLeafParamResult hc_leaf_param(device_id, round_id, tray_id, param_id)

Returns the Hyperspectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the Hyperspectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.hc_leaf_param(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_leaf_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonHcLeafParamResult**](JsonHcLeafParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_leaf_param_analyse**
> JsonHcLeafParamByAnalyseIDResult hc_leaf_param_analyse(id, param_id)

Returns the Hyperspectral statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the Hyperspectral statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.hc_leaf_param_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_leaf_param_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonHcLeafParamByAnalyseIDResult**](JsonHcLeafParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_param**
> JsonHcParamResult hc_param(id)

Returns one Hyperspectral parameter by parameter ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
id = 56 # int | paramID

try:
    # Returns one Hyperspectral parameter by parameter ID.
    api_response = api_instance.hc_param(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| paramID | 

### Return type

[**JsonHcParamResult**](JsonHcParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_param_image**
> JsonHcParameterImageResult hc_param_image(device_id, round_id, tray_id, param_id)

Returns the Hyperspectral parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the Hyperspectral parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.hc_param_image(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_param_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonHcParameterImageResult**](JsonHcParameterImageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_param_image_analyse**
> JsonHcParameterImageByAnalyseIDResult hc_param_image_analyse(id, param_id)

Returns the Hyperspectral parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the Hyperspectral parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.hc_param_image_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_param_image_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonHcParameterImageByAnalyseIDResult**](JsonHcParameterImageByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_param_used**
> JsonHcUsedParamResult hc_param_used(device_id, round_id, tray_id)

Returns the Hyperspectral plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns the Hyperspectral plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.hc_param_used(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_param_used: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonHcUsedParamResult**](JsonHcUsedParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_param_used_analyse**
> JsonHcUsedParamByAnalyseIDResult hc_param_used_analyse(id)

Returns the Hyperspectral plant and leaf parameters used in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
id = 56 # int | analyseID

try:
    # Returns the Hyperspectral plant and leaf parameters used in the analysis defined by analyse ID.
    api_response = api_instance.hc_param_used_analyse(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_param_used_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 

### Return type

[**JsonHcUsedParamByAnalyseIDResult**](JsonHcUsedParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_plant_mask**
> JsonHcPlantMaskResult hc_plant_mask(device_id, round_id, tray_id)

Returns Hyperspectral plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns Hyperspectral plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.hc_plant_mask(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_plant_mask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonHcPlantMaskResult**](JsonHcPlantMaskResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_plant_mask_measure**
> JsonHcPlantMaskByMeasureIDResult hc_plant_mask_measure(id)

Returns the Hyperspectral plant mask created for the measured tray defined by HC measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
id = 56 # int | measureID

try:
    # Returns the Hyperspectral plant mask created for the measured tray defined by HC measure ID.
    api_response = api_instance.hc_plant_mask_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_plant_mask_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonHcPlantMaskByMeasureIDResult**](JsonHcPlantMaskByMeasureIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_plant_param**
> JsonHcPlantParamResult hc_plant_param(device_id, round_id, tray_id, param_id)

Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.hc_plant_param(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_plant_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonHcPlantParamResult**](JsonHcPlantParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_plant_param_analyse**
> JsonHcPlantParamByAnalyseIDResult hc_plant_param_analyse(id, param_id)

Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.hc_plant_param_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_plant_param_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonHcPlantParamByAnalyseIDResult**](JsonHcPlantParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_rgb_image**
> JsonHcRgbImageResult hc_rgb_image(device_id, round_id, tray_id)

Returns the Hyperspectral RGB image created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. The Hyperspectral RGB image is created by analysis, therefore it is only available if analysis has been performed on the required data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns the Hyperspectral RGB image created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. The Hyperspectral RGB image is created by analysis, therefore it is only available if analysis has been performed on the required data.
    api_response = api_instance.hc_rgb_image(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_rgb_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonHcRgbImageResult**](JsonHcRgbImageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **hc_rgb_image_measure**
> JsonHcRgbImageByMeasureIDResult hc_rgb_image_measure(id)

Returns the Hyperspectral RGB image created for the measured tray by HC measure ID. The Hyperspectral RGB image is created by analysis, therefore it is only available if analysis has been performed on the required data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HcApi()
id = 56 # int | measureID

try:
    # Returns the Hyperspectral RGB image created for the measured tray by HC measure ID. The Hyperspectral RGB image is created by analysis, therefore it is only available if analysis has been performed on the required data.
    api_response = api_instance.hc_rgb_image_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HcApi->hc_rgb_image_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonHcRgbImageByMeasureIDResult**](JsonHcRgbImageByMeasureIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

