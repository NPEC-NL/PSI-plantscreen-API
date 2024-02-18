# swagger_client.IrApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ir_imaging**](IrApi.md#ir_imaging) | **GET** /Ir/Imaging | Returns Thermal imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**ir_imaging_extended_data**](IrApi.md#ir_imaging_extended_data) | **GET** /Ir/Imaging/ExtendedData | Returns Thermal extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**ir_imaging_extended_data_measure**](IrApi.md#ir_imaging_extended_data_measure) | **GET** /Ir/Imaging/ExtendedData/Measure | Returns Thermal imaging extended data by IR measure ID.
[**ir_imaging_measure**](IrApi.md#ir_imaging_measure) | **GET** /Ir/Imaging/Measure | Returns Thermal imaging data by IR measure ID.
[**ir_leaf_param**](IrApi.md#ir_leaf_param) | **GET** /Ir/Leaf/Param | Returns the Thermal Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**ir_leaf_param_analyse**](IrApi.md#ir_leaf_param_analyse) | **GET** /Ir/Leaf/Param/Analyse | Returns the Thermal statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**ir_param**](IrApi.md#ir_param) | **GET** /Ir/Param | Returns one Thermal parameter by parameter ID.
[**ir_param_used**](IrApi.md#ir_param_used) | **GET** /Ir/Param/Used | Returns the Thermal plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**ir_param_used_analyse**](IrApi.md#ir_param_used_analyse) | **GET** /Ir/Param/Used/Analyse | Returns the Thermalplant and leaf parameters used in the analysis defined by analyse ID.
[**ir_plant_mask**](IrApi.md#ir_plant_mask) | **GET** /Ir/Plant/Mask | Returns Thermal plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**ir_plant_mask_image**](IrApi.md#ir_plant_mask_image) | **GET** /Ir/Plant/Mask/Image | Returns Thermal imaging data masked by the plant mask for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**ir_plant_mask_image_measure**](IrApi.md#ir_plant_mask_image_measure) | **GET** /Ir/Plant/Mask/Image/Measure | Returns Thermal imaging data masked by the plant mask defined by IR measure ID.
[**ir_plant_mask_measure**](IrApi.md#ir_plant_mask_measure) | **GET** /Ir/Plant/Mask/Measure | Returns the Thermal plant mask created for the measured tray defined by IR measure ID.
[**ir_plant_param**](IrApi.md#ir_plant_param) | **GET** /Ir/Plant/Param | Returns the Thermal statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**ir_plant_param_analyse**](IrApi.md#ir_plant_param_analyse) | **GET** /Ir/Plant/Param/Analyse | Returns the Thermal plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

# **ir_imaging**
> JsonIrImagingResult ir_imaging(device_id, round_id, tray_id)

Returns Thermal imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns Thermal imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.ir_imaging(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_imaging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonIrImagingResult**](JsonIrImagingResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_imaging_extended_data**
> JsonIrMeasureExtendedDataResult ir_imaging_extended_data(device_id, round_id, tray_id)

Returns Thermal extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns Thermal extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.ir_imaging_extended_data(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_imaging_extended_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonIrMeasureExtendedDataResult**](JsonIrMeasureExtendedDataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_imaging_extended_data_measure**
> JsonIrMeasureExtendedDataByIDResult ir_imaging_extended_data_measure(id)

Returns Thermal imaging extended data by IR measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
id = 56 # int | measureID

try:
    # Returns Thermal imaging extended data by IR measure ID.
    api_response = api_instance.ir_imaging_extended_data_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_imaging_extended_data_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonIrMeasureExtendedDataByIDResult**](JsonIrMeasureExtendedDataByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_imaging_measure**
> JsonIrImagingByIDResult ir_imaging_measure(id)

Returns Thermal imaging data by IR measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
id = 56 # int | measureID

try:
    # Returns Thermal imaging data by IR measure ID.
    api_response = api_instance.ir_imaging_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_imaging_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonIrImagingByIDResult**](JsonIrImagingByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_leaf_param**
> JsonIrLeafParamResult ir_leaf_param(device_id, round_id, tray_id, param_id)

Returns the Thermal Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the Thermal Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.ir_leaf_param(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_leaf_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonIrLeafParamResult**](JsonIrLeafParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_leaf_param_analyse**
> JsonIrLeafParamByAnalyseIDResult ir_leaf_param_analyse(id, param_id)

Returns the Thermal statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
id = 56 # int | analyseID
param_id = 56 # int | paramID

try:
    # Returns the Thermal statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.ir_leaf_param_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_leaf_param_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonIrLeafParamByAnalyseIDResult**](JsonIrLeafParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_param**
> JsonIrParamResult ir_param(id)

Returns one Thermal parameter by parameter ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
id = 56 # int | paramID

try:
    # Returns one Thermal parameter by parameter ID.
    api_response = api_instance.ir_param(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| paramID | 

### Return type

[**JsonIrParamResult**](JsonIrParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_param_used**
> JsonIrUsedParamResult ir_param_used(device_id, round_id, tray_id)

Returns the Thermal plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns the Thermal plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.ir_param_used(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_param_used: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonIrUsedParamResult**](JsonIrUsedParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_param_used_analyse**
> JsonIrUsedParamByAnalyseIDResult ir_param_used_analyse(id)

Returns the Thermalplant and leaf parameters used in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
id = 56 # int | analyseID

try:
    # Returns the Thermalplant and leaf parameters used in the analysis defined by analyse ID.
    api_response = api_instance.ir_param_used_analyse(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_param_used_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 

### Return type

[**JsonIrUsedParamByAnalyseIDResult**](JsonIrUsedParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_plant_mask**
> JsonIrPlantMaskResult ir_plant_mask(device_id, round_id, tray_id)

Returns Thermal plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns Thermal plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.ir_plant_mask(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_plant_mask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonIrPlantMaskResult**](JsonIrPlantMaskResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_plant_mask_image**
> JsonIrPlantMaskImageResult ir_plant_mask_image(device_id, round_id, tray_id)

Returns Thermal imaging data masked by the plant mask for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns Thermal imaging data masked by the plant mask for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.ir_plant_mask_image(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_plant_mask_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonIrPlantMaskImageResult**](JsonIrPlantMaskImageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_plant_mask_image_measure**
> JsonIrPlantMaskImageByMeasureIDResult ir_plant_mask_image_measure(id)

Returns Thermal imaging data masked by the plant mask defined by IR measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
id = 56 # int | measureID

try:
    # Returns Thermal imaging data masked by the plant mask defined by IR measure ID.
    api_response = api_instance.ir_plant_mask_image_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_plant_mask_image_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonIrPlantMaskImageByMeasureIDResult**](JsonIrPlantMaskImageByMeasureIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_plant_mask_measure**
> JsonIrPlantMaskByMeasureIDResult ir_plant_mask_measure(id)

Returns the Thermal plant mask created for the measured tray defined by IR measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
id = 56 # int | measureID

try:
    # Returns the Thermal plant mask created for the measured tray defined by IR measure ID.
    api_response = api_instance.ir_plant_mask_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_plant_mask_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonIrPlantMaskByMeasureIDResult**](JsonIrPlantMaskByMeasureIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_plant_param**
> JsonIrPlantParamResult ir_plant_param(device_id, round_id, tray_id, param_id)

Returns the Thermal statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID
param_id = 56 # int | paramID

try:
    # Returns the Thermal statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    api_response = api_instance.ir_plant_param(device_id, round_id, tray_id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_plant_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonIrPlantParamResult**](JsonIrPlantParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **ir_plant_param_analyse**
> JsonIrPlantParamByAnalyseIDResult ir_plant_param_analyse(id, param_id)

Returns the Thermal plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IrApi()
id = 56 # int | analyseID
param_id = 56 # int | ParamID

try:
    # Returns the Thermal plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    api_response = api_instance.ir_plant_param_analyse(id, param_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IrApi->ir_plant_param_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonIrPlantParamByAnalyseIDResult**](JsonIrPlantParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

