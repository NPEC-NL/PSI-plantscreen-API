# plantscreen.swagger_client.FcApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fc_imaging**](FcApi.md#fc_imaging) | **GET** /Fc/Imaging | Returns FluorCam imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**fc_imaging_extended_data**](FcApi.md#fc_imaging_extended_data) | **GET** /Fc/Imaging/ExtendedData | Returns FluorCam extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)
[**fc_imaging_extended_data_measure**](FcApi.md#fc_imaging_extended_data_measure) | **GET** /Fc/Imaging/ExtendedData/Measure | Returns FluorCam imaging extended data by FC measure ID. (Only available for field systems.)
[**fc_imaging_measure**](FcApi.md#fc_imaging_measure) | **GET** /Fc/Imaging/Measure | Returns FluorCam imaging data by FC measure ID.
[**fc_leaf_param**](FcApi.md#fc_leaf_param) | **GET** /Fc/Leaf/Param | Returns the FluorCam leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**fc_leaf_param_analyse**](FcApi.md#fc_leaf_param_analyse) | **GET** /Fc/Leaf/Param/Analyse | Returns the FluorCam leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**fc_param**](FcApi.md#fc_param) | **GET** /Fc/Param | Returns one FluorCam parameter by parameter ID.
[**fc_param_image**](FcApi.md#fc_param_image) | **GET** /Fc/Param/Image | Returns the FluorCam parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**fc_param_image_analyse**](FcApi.md#fc_param_image_analyse) | **GET** /Fc/Param/Image/Analyse | Returns the FluorCam parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**fc_param_used**](FcApi.md#fc_param_used) | **GET** /Fc/Param/Used | Returns the FluorCam plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**fc_plant_mask**](FcApi.md#fc_plant_mask) | **GET** /Fc/Plant/Mask | Returns FluorCam plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**fc_plant_mask_measure**](FcApi.md#fc_plant_mask_measure) | **GET** /Fc/Plant/Mask/Measure | Returns the FluorCam plant mask created for the measured tray defined by FC measure ID.
[**fc_plant_param**](FcApi.md#fc_plant_param) | **GET** /Fc/Plant/Param | Returns the FluorCam plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**fc_plant_param_analyse**](FcApi.md#fc_plant_param_analyse) | **GET** /Fc/Plant/Param/Analyse | Returns the FluorCam plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**i_fc_param_used_analyse**](FcApi.md#i_fc_param_used_analyse) | **GET** /Fc/Param/Used/Analyse | Returns the FluorCam plant and leaf parameters used in the analysis defined by analyse ID.

# **fc_imaging**
> JsonFcImagingResult fc_imaging(device_id, round_id, tray_id)

Returns FluorCam imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns FluorCam imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.fc_imaging(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_imaging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonFcImagingResult**](JsonFcImagingResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_imaging_extended_data**
> JsonFcMeasureExtendedDataResult fc_imaging_extended_data(device_id, round_id, tray_id)

Returns FluorCam extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns FluorCam extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)
    api_response = api_instance.fc_imaging_extended_data(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_imaging_extended_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonFcMeasureExtendedDataResult**](JsonFcMeasureExtendedDataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_imaging_extended_data_measure**
> JsonFcMeasureExtendedDataByIDResult fc_imaging_extended_data_measure(id)

Returns FluorCam imaging extended data by FC measure ID. (Only available for field systems.)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
id = 56 # int | measureID

try:
    # Returns FluorCam imaging extended data by FC measure ID. (Only available for field systems.)
    api_response = api_instance.fc_imaging_extended_data_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_imaging_extended_data_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonFcMeasureExtendedDataByIDResult**](JsonFcMeasureExtendedDataByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_imaging_measure**
> JsonFcImagingByIDResult fc_imaging_measure(id)

Returns FluorCam imaging data by FC measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
id = 56 # int | measureID

try:
    # Returns FluorCam imaging data by FC measure ID.
    api_response = api_instance.fc_imaging_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_imaging_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonFcImagingByIDResult**](JsonFcImagingByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_leaf_param**
> JsonFcLeafParamResult fc_leaf_param(device_id, round_id, tray_id, param_id)

Returns the FluorCam leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the FluorCam leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.fc_leaf_param(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_leaf_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonFcLeafParamResult**](JsonFcLeafParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_leaf_param_analyse**
> JsonFcLeafParamByAnalyseIDResult fc_leaf_param_analyse(id, param_id)

Returns the FluorCam leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the FluorCam leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.fc_leaf_param_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_leaf_param_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonFcLeafParamByAnalyseIDResult**](JsonFcLeafParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_param**
> JsonFcParamResult fc_param(id)

Returns one FluorCam parameter by parameter ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
id = 56 # int | paramID

try:
    # Returns one FluorCam parameter by parameter ID.
    api_response = api_instance.fc_param(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| paramID | 

### Return type

[**JsonFcParamResult**](JsonFcParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_param_image**
> JsonFcParameterImageResult fc_param_image(device_id, round_id, tray_id, param_id)

Returns the FluorCam parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the FluorCam parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.fc_param_image(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_param_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonFcParameterImageResult**](JsonFcParameterImageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_param_image_analyse**
> JsonFcParameterImageByAnalyseIDResult fc_param_image_analyse(id, param_id)

Returns the FluorCam parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
id = 56 # int | analyseID
param_id = 56 # int | paramID

try:
    # Returns the FluorCam parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.fc_param_image_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_param_image_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonFcParameterImageByAnalyseIDResult**](JsonFcParameterImageByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_param_used**
> JsonFcUsedParamResult fc_param_used(device_id, round_id, tray_id)

Returns the FluorCam plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns the FluorCam plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.fc_param_used(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_param_used: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonFcUsedParamResult**](JsonFcUsedParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_plant_mask**
> JsonFcPlantMaskResult fc_plant_mask(device_id, round_id, tray_id)

Returns FluorCam plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns FluorCam plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.fc_plant_mask(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_plant_mask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonFcPlantMaskResult**](JsonFcPlantMaskResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_plant_mask_measure**
> JsonFcPlantMaskByMeasureIDResult fc_plant_mask_measure(id)

Returns the FluorCam plant mask created for the measured tray defined by FC measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
id = 56 # int | measureID

try:
    # Returns the FluorCam plant mask created for the measured tray defined by FC measure ID.
    api_response = api_instance.fc_plant_mask_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_plant_mask_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonFcPlantMaskByMeasureIDResult**](JsonFcPlantMaskByMeasureIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_plant_param**
> JsonFcPlantParamResult fc_plant_param(device_id, round_id, tray_id, param_id)

Returns the FluorCam plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the FluorCam plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.fc_plant_param(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_plant_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonFcPlantParamResult**](JsonFcPlantParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_plant_param_analyse**
> JsonFcPlantParamByAnalyseIDResult fc_plant_param_analyse(id, param_id)

Returns the FluorCam plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the FluorCam plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.fc_plant_param_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->fc_plant_param_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonFcPlantParamByAnalyseIDResult**](JsonFcPlantParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_fc_param_used_analyse**
> JsonFcUsedParamByAnalyseIDResult i_fc_param_used_analyse(id)

Returns the FluorCam plant and leaf parameters used in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.FcApi()
id = 56 # int | analyseID

try:
    # Returns the FluorCam plant and leaf parameters used in the analysis defined by analyse ID.
    api_response = api_instance.i_fc_param_used_analyse(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcApi->i_fc_param_used_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 

### Return type

[**JsonFcUsedParamByAnalyseIDResult**](JsonFcUsedParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

