# plantscreen.swagger_client.MscApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**msc_calibration**](MscApi.md#msc_calibration) | **GET** /Msc/Calibration | Returns one Multispectral calibration for individual groups of lights with information about the exposure and gain of the camera defined by calibration ID.
[**msc_calibration_light**](MscApi.md#msc_calibration_light) | **GET** /Msc/CalibrationLight | Returns one light output setting for light group calibration defined by calibration light ID. TODO There are two versions, with and without parameters but one gives array back, one single value?
[**msc_calibration_light_set**](MscApi.md#msc_calibration_light_set) | **GET** /Msc/Calibration/LightSet | Returns the Multispectral calibration for individual groups of lights with information about the exposure and gain of the camera defined by light set ID.
[**msc_imaging**](MscApi.md#msc_imaging) | **GET** /Msc/Imaging | Returns Multispectral imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**msc_imaging_extended_data**](MscApi.md#msc_imaging_extended_data) | **GET** /Msc/Imaging/ExtendedData | Returns Multispectral extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)
[**msc_imaging_extended_data_measure**](MscApi.md#msc_imaging_extended_data_measure) | **GET** /Msc/Imaging/ExtendedData/Measure | Returns Multispectral imaging extended data by MSC measure ID. (Only available for field systems.)
[**msc_imaging_measure**](MscApi.md#msc_imaging_measure) | **GET** /Msc/Imaging/Measure | Returns Multispectral imaging data by MSC measure ID.
[**msc_leaf_param**](MscApi.md#msc_leaf_param) | **GET** /Msc/Leaf/Param | Returns the Multispectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**msc_leaf_param_analyse**](MscApi.md#msc_leaf_param_analyse) | **GET** /Msc/Leaf/Param/Analyse | Returns the Multispectral statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**msc_light_set**](MscApi.md#msc_light_set) | **GET** /Msc/LightSet | Returns one set of the lights for multispectral camera service defined by light set ID.
[**msc_light_set_used**](MscApi.md#msc_light_set_used) | **GET** /Msc/LightSet/Used | Returns the sets of the lights for multispectral camera service used in the measure for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**msc_param**](MscApi.md#msc_param) | **GET** /Msc/Param | Returns one Multispectral parameter by parameter ID.
[**msc_param_image**](MscApi.md#msc_param_image) | **GET** /Msc/Param/Image | Returns the Multispectral parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**msc_param_image_analyse**](MscApi.md#msc_param_image_analyse) | **GET** /Msc/Param/Image/Analyse | Returns the Multispectral parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**msc_param_used**](MscApi.md#msc_param_used) | **GET** /Msc/Param/Used | Returns the Multispectral plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**msc_param_used_analyse**](MscApi.md#msc_param_used_analyse) | **GET** /Msc/Param/Used/Analyse | Returns Multispectral used plant parameters by analyse ID.
[**msc_plant_mask**](MscApi.md#msc_plant_mask) | **GET** /Msc/Plant/Mask | Returns Multispectral plant mask by device, round and tray ID.
[**msc_plant_mask_measure**](MscApi.md#msc_plant_mask_measure) | **GET** /Msc/Plant/Mask/Measure | Returns the Multispectral plant mask created for the measured tray defined by MSC measure ID.
[**msc_plant_param**](MscApi.md#msc_plant_param) | **GET** /Msc/Plant/Param | Returns the Multispectral statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**msc_plant_param_analyse**](MscApi.md#msc_plant_param_analyse) | **GET** /Msc/Plant/Param/Analyse | Returns the Multispectral plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

# **msc_calibration**
> JsonMscCalibrationResult msc_calibration(id)

Returns one Multispectral calibration for individual groups of lights with information about the exposure and gain of the camera defined by calibration ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | calibrationID

try:
    # Returns one Multispectral calibration for individual groups of lights with information about the exposure and gain of the camera defined by calibration ID.
    api_response = api_instance.msc_calibration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_calibration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| calibrationID | 

### Return type

[**JsonMscCalibrationResult**](JsonMscCalibrationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_calibration_light**
> JsonMscCalibrationLightByIDResult msc_calibration_light(id=id)

Returns one light output setting for light group calibration defined by calibration light ID. TODO There are two versions, with and without parameters but one gives array back, one single value?

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | calibrationLightID. Two versions, with and without parameter (optional)

try:
    # Returns one light output setting for light group calibration defined by calibration light ID. TODO There are two versions, with and without parameters but one gives array back, one single value?
    api_response = api_instance.msc_calibration_light(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_calibration_light: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| calibrationLightID. Two versions, with and without parameter | [optional] 

### Return type

[**JsonMscCalibrationLightByIDResult**](JsonMscCalibrationLightByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_calibration_light_set**
> JsonMscCalibrationByLightSetIDResult msc_calibration_light_set(id)

Returns the Multispectral calibration for individual groups of lights with information about the exposure and gain of the camera defined by light set ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | lightSetID

try:
    # Returns the Multispectral calibration for individual groups of lights with information about the exposure and gain of the camera defined by light set ID.
    api_response = api_instance.msc_calibration_light_set(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_calibration_light_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| lightSetID | 

### Return type

[**JsonMscCalibrationByLightSetIDResult**](JsonMscCalibrationByLightSetIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_imaging**
> JsonMscImagingResult msc_imaging(device_id, round_id, tray_id)

Returns Multispectral imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns Multispectral imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.msc_imaging(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_imaging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonMscImagingResult**](JsonMscImagingResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_imaging_extended_data**
> JsonMscMeasureExtendedDataResult msc_imaging_extended_data(device_id, round_id, tray_id)

Returns Multispectral extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns Multispectral extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)
    api_response = api_instance.msc_imaging_extended_data(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_imaging_extended_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonMscMeasureExtendedDataResult**](JsonMscMeasureExtendedDataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_imaging_extended_data_measure**
> JsonMscMeasureExtendedDataByIDResult msc_imaging_extended_data_measure(id)

Returns Multispectral imaging extended data by MSC measure ID. (Only available for field systems.)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | measureID

try:
    # Returns Multispectral imaging extended data by MSC measure ID. (Only available for field systems.)
    api_response = api_instance.msc_imaging_extended_data_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_imaging_extended_data_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonMscMeasureExtendedDataByIDResult**](JsonMscMeasureExtendedDataByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_imaging_measure**
> JsonMscImagingByIDResult msc_imaging_measure(id)

Returns Multispectral imaging data by MSC measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | measureID

try:
    # Returns Multispectral imaging data by MSC measure ID.
    api_response = api_instance.msc_imaging_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_imaging_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonMscImagingByIDResult**](JsonMscImagingByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_leaf_param**
> JsonMscLeafParamResult msc_leaf_param(device_id, round_id, tray_id, param_id)

Returns the Multispectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the Multispectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.msc_leaf_param(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_leaf_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonMscLeafParamResult**](JsonMscLeafParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_leaf_param_analyse**
> JsonMscLeafParamByAnalyseIDResult msc_leaf_param_analyse(id, param_id)

Returns the Multispectral statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | analyseID
param_id = 56 # int | paramID

try:
    # Returns the Multispectral statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.msc_leaf_param_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_leaf_param_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonMscLeafParamByAnalyseIDResult**](JsonMscLeafParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_light_set**
> JsonMscLightSetResult msc_light_set(id)

Returns one set of the lights for multispectral camera service defined by light set ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | lightSetID

try:
    # Returns one set of the lights for multispectral camera service defined by light set ID.
    api_response = api_instance.msc_light_set(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_light_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| lightSetID | 

### Return type

[**JsonMscLightSetResult**](JsonMscLightSetResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_light_set_used**
> JsonMscLightSetUsedResult msc_light_set_used(device_id, round_id, tray_id)

Returns the sets of the lights for multispectral camera service used in the measure for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns the sets of the lights for multispectral camera service used in the measure for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.msc_light_set_used(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_light_set_used: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonMscLightSetUsedResult**](JsonMscLightSetUsedResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_param**
> JsonMscParamResult msc_param(id)

Returns one Multispectral parameter by parameter ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | paramID

try:
    # Returns one Multispectral parameter by parameter ID.
    api_response = api_instance.msc_param(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| paramID | 

### Return type

[**JsonMscParamResult**](JsonMscParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_param_image**
> JsonMscParameterImageResult msc_param_image(device_id, round_id, tray_id, param_id)

Returns the Multispectral parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the Multispectral parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.msc_param_image(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_param_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonMscParameterImageResult**](JsonMscParameterImageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_param_image_analyse**
> JsonMscParameterImageByAnalyseIDResult msc_param_image_analyse(id, param_id)

Returns the Multispectral parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the Multispectral parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.msc_param_image_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_param_image_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonMscParameterImageByAnalyseIDResult**](JsonMscParameterImageByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_param_used**
> JsonMscUsedParamResult msc_param_used(device_id, round_id, tray_id)

Returns the Multispectral plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns the Multispectral plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.msc_param_used(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_param_used: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonMscUsedParamResult**](JsonMscUsedParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_param_used_analyse**
> JsonMscUsedParamByAnalyseIDResult msc_param_used_analyse(id)

Returns Multispectral used plant parameters by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | analyseID

try:
    # Returns Multispectral used plant parameters by analyse ID.
    api_response = api_instance.msc_param_used_analyse(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_param_used_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 

### Return type

[**JsonMscUsedParamByAnalyseIDResult**](JsonMscUsedParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_plant_mask**
> JsonMscPlantMaskResult msc_plant_mask(device_id, round_id, tray_id)

Returns Multispectral plant mask by device, round and tray ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns Multispectral plant mask by device, round and tray ID.
    api_response = api_instance.msc_plant_mask(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_plant_mask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonMscPlantMaskResult**](JsonMscPlantMaskResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_plant_mask_measure**
> JsonMscPlantMaskByMeasureIDResult msc_plant_mask_measure(id)

Returns the Multispectral plant mask created for the measured tray defined by MSC measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | measureID

try:
    # Returns the Multispectral plant mask created for the measured tray defined by MSC measure ID.
    api_response = api_instance.msc_plant_mask_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_plant_mask_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonMscPlantMaskByMeasureIDResult**](JsonMscPlantMaskByMeasureIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_plant_param**
> JsonMscPlantParamResult msc_plant_param(device_id, round_id, tray_id, param_id)

Returns the Multispectral statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the Multispectral statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.msc_plant_param(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_plant_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonMscPlantParamResult**](JsonMscPlantParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **msc_plant_param_analyse**
> JsonMscPlantParamByAnalyseIDResult msc_plant_param_analyse(id, param_id)

Returns the Multispectral plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.MscApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the Multispectral plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.msc_plant_param_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MscApi->msc_plant_param_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonMscPlantParamByAnalyseIDResult**](JsonMscPlantParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

