# plantscreen.Scan3dApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scan3d**](Scan3dApi.md#scan3d) | **GET** /Scan3d/Imaging | Returns 3D imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**scan3d_analysed_model_analyse**](Scan3dApi.md#scan3d_analysed_model_analyse) | **GET** /Scan3d/AnalyzedModel/Analyse | Returns the analyzed 3D data as a triangulated 3D model defined by analyse ID.
[**scan3d_analyzed_model**](Scan3dApi.md#scan3d_analyzed_model) | **GET** /Scan3d/AnalyzedModel | Returns the analyzed 3D data as a triangulated 3D model defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**scan3d_analyzed_model_measure**](Scan3dApi.md#scan3d_analyzed_model_measure) | **GET** /Scan3d/AnalyzedModel/Measure | Returns the analyzed 3D data as a triangulated 3D model defined by scan 3D measure ID.
[**scan3d_imaging_extended_data**](Scan3dApi.md#scan3d_imaging_extended_data) | **GET** /Scan3d/Imaging/ExtendedData | Returns 3D extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**scan3d_imaging_extended_data_measure**](Scan3dApi.md#scan3d_imaging_extended_data_measure) | **GET** /Scan3d/Imaging/ExtendedData/Measure | Returns 3D imaging extended data by scan 3D measure ID.
[**scan3d_imaging_measure**](Scan3dApi.md#scan3d_imaging_measure) | **GET** /Scan3d/Imaging/Measure | Returns 3D imaging data by scan 3D measure ID.
[**scan3d_leaf_param**](Scan3dApi.md#scan3d_leaf_param) | **GET** /Scan3d/Leaf/Param | Returns the 3D local leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**scan3d_leaf_param_analyse**](Scan3dApi.md#scan3d_leaf_param_analyse) | **GET** /Scan3d/Leaf/Param/Analyse | Returns the 3D local leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
[**scan3d_param**](Scan3dApi.md#scan3d_param) | **GET** /Scan3d/Param | Returns one 3D parameter by parameter ID.
[**scan3d_param_used**](Scan3dApi.md#scan3d_param_used) | **GET** /Scan3d/Param/Used | Returns the 3D plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**scan3d_param_used_analyse**](Scan3dApi.md#scan3d_param_used_analyse) | **GET** /Scan3d/Param/Used/Analyse | Returns the 3D plant and leaf parameters used in the analysis defined by analyse ID.
[**scan3d_plant_param**](Scan3dApi.md#scan3d_plant_param) | **GET** /Scan3d/Plant/Param | Returns the 3D plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
[**scan3d_plant_param_analyse**](Scan3dApi.md#scan3d_plant_param_analyse) | **GET** /Scan3d/Plant/Param/Analyse | Returns the 3D plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.


# **scan3d**
> JsonScan3dImagingResult scan3d(device_id, round_id, tray_id)

Returns 3D imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_imaging_result import JsonScan3dImagingResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    device_id = 56 # int | deviceID
    round_id = 56 # int | roundID
    tray_id = 56 # int | trayID

    try:
        # Returns 3D imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
        api_response = api_instance.scan3d(device_id, round_id, tray_id)
        print("The response of Scan3dApi->scan3d:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonScan3dImagingResult**](JsonScan3dImagingResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_analysed_model_analyse**
> JsonScan3dAnalyzedModelByAnalyseIDResult scan3d_analysed_model_analyse(id)

Returns the analyzed 3D data as a triangulated 3D model defined by analyse ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_analyzed_model_by_analyse_id_result import JsonScan3dAnalyzedModelByAnalyseIDResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    id = 56 # int | analyseID

    try:
        # Returns the analyzed 3D data as a triangulated 3D model defined by analyse ID.
        api_response = api_instance.scan3d_analysed_model_analyse(id)
        print("The response of Scan3dApi->scan3d_analysed_model_analyse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_analysed_model_analyse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 

### Return type

[**JsonScan3dAnalyzedModelByAnalyseIDResult**](JsonScan3dAnalyzedModelByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_analyzed_model**
> JsonScan3dAnalyzedModelResult scan3d_analyzed_model(device_id, round_id, tray_id)

Returns the analyzed 3D data as a triangulated 3D model defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_analyzed_model_result import JsonScan3dAnalyzedModelResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    device_id = 56 # int | deviceID
    round_id = 56 # int | roundID
    tray_id = 56 # int | trayID

    try:
        # Returns the analyzed 3D data as a triangulated 3D model defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
        api_response = api_instance.scan3d_analyzed_model(device_id, round_id, tray_id)
        print("The response of Scan3dApi->scan3d_analyzed_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_analyzed_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonScan3dAnalyzedModelResult**](JsonScan3dAnalyzedModelResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_analyzed_model_measure**
> JsonScan3dAnalyzedModelByMeasureIDResult scan3d_analyzed_model_measure(id)

Returns the analyzed 3D data as a triangulated 3D model defined by scan 3D measure ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_analyzed_model_by_measure_id_result import JsonScan3dAnalyzedModelByMeasureIDResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    id = 56 # int | measureID

    try:
        # Returns the analyzed 3D data as a triangulated 3D model defined by scan 3D measure ID.
        api_response = api_instance.scan3d_analyzed_model_measure(id)
        print("The response of Scan3dApi->scan3d_analyzed_model_measure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_analyzed_model_measure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonScan3dAnalyzedModelByMeasureIDResult**](JsonScan3dAnalyzedModelByMeasureIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_imaging_extended_data**
> JsonScan3dMeasureExtendedDataResult scan3d_imaging_extended_data(device_id, round_id, tray_id)

Returns 3D extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_measure_extended_data_result import JsonScan3dMeasureExtendedDataResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    device_id = 56 # int | deviceID
    round_id = 56 # int | roundID
    tray_id = 56 # int | trayID

    try:
        # Returns 3D extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
        api_response = api_instance.scan3d_imaging_extended_data(device_id, round_id, tray_id)
        print("The response of Scan3dApi->scan3d_imaging_extended_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_imaging_extended_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonScan3dMeasureExtendedDataResult**](JsonScan3dMeasureExtendedDataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_imaging_extended_data_measure**
> JsonScan3dMeasureExtendedDataByIDResult scan3d_imaging_extended_data_measure(id)

Returns 3D imaging extended data by scan 3D measure ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_measure_extended_data_by_id_result import JsonScan3dMeasureExtendedDataByIDResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    id = 56 # int | measureID

    try:
        # Returns 3D imaging extended data by scan 3D measure ID.
        api_response = api_instance.scan3d_imaging_extended_data_measure(id)
        print("The response of Scan3dApi->scan3d_imaging_extended_data_measure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_imaging_extended_data_measure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonScan3dMeasureExtendedDataByIDResult**](JsonScan3dMeasureExtendedDataByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_imaging_measure**
> JsonScan3dImagingByIDResult scan3d_imaging_measure(id)

Returns 3D imaging data by scan 3D measure ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_imaging_by_id_result import JsonScan3dImagingByIDResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    id = 56 # int | measureID

    try:
        # Returns 3D imaging data by scan 3D measure ID.
        api_response = api_instance.scan3d_imaging_measure(id)
        print("The response of Scan3dApi->scan3d_imaging_measure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_imaging_measure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonScan3dImagingByIDResult**](JsonScan3dImagingByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_leaf_param**
> JsonScan3dLeafParamResult scan3d_leaf_param(device_id, round_id, tray_id, param_id)

Returns the 3D local leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_leaf_param_result import JsonScan3dLeafParamResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    device_id = 56 # int | deviceID
    round_id = 56 # int | roundID
    tray_id = 56 # int | trayID
    param_id = 56 # int | paramID

    try:
        # Returns the 3D local leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
        api_response = api_instance.scan3d_leaf_param(device_id, round_id, tray_id, param_id)
        print("The response of Scan3dApi->scan3d_leaf_param:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_leaf_param: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonScan3dLeafParamResult**](JsonScan3dLeafParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_leaf_param_analyse**
> JsonScan3dLeafParamByAnalyseIDResult scan3d_leaf_param_analyse(id, param_id)

Returns the 3D local leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_leaf_param_by_analyse_id_result import JsonScan3dLeafParamByAnalyseIDResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    id = 56 # int | analyseID
    param_id = 56 # int | ParamID

    try:
        # Returns the 3D local leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
        api_response = api_instance.scan3d_leaf_param_analyse(id, param_id)
        print("The response of Scan3dApi->scan3d_leaf_param_analyse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_leaf_param_analyse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonScan3dLeafParamByAnalyseIDResult**](JsonScan3dLeafParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_param**
> JsonScan3dParamResult scan3d_param(id)

Returns one 3D parameter by parameter ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_param_result import JsonScan3dParamResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    id = 56 # int | paramID

    try:
        # Returns one 3D parameter by parameter ID.
        api_response = api_instance.scan3d_param(id)
        print("The response of Scan3dApi->scan3d_param:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_param: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| paramID | 

### Return type

[**JsonScan3dParamResult**](JsonScan3dParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_param_used**
> JsonScan3dUsedParamResult scan3d_param_used(device_id, round_id, tray_id)

Returns the 3D plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_used_param_result import JsonScan3dUsedParamResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    device_id = 56 # int | deviceID
    round_id = 56 # int | roundID
    tray_id = 56 # int | trayID

    try:
        # Returns the 3D plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
        api_response = api_instance.scan3d_param_used(device_id, round_id, tray_id)
        print("The response of Scan3dApi->scan3d_param_used:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_param_used: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonScan3dUsedParamResult**](JsonScan3dUsedParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_param_used_analyse**
> JsonScan3dUsedParamByAnalyseIDResult scan3d_param_used_analyse(id)

Returns the 3D plant and leaf parameters used in the analysis defined by analyse ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_used_param_by_analyse_id_result import JsonScan3dUsedParamByAnalyseIDResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    id = 56 # int | analyseID

    try:
        # Returns the 3D plant and leaf parameters used in the analysis defined by analyse ID.
        api_response = api_instance.scan3d_param_used_analyse(id)
        print("The response of Scan3dApi->scan3d_param_used_analyse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_param_used_analyse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 

### Return type

[**JsonScan3dUsedParamByAnalyseIDResult**](JsonScan3dUsedParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_plant_param**
> JsonScan3dPlantParamResult scan3d_plant_param(device_id, round_id, tray_id, param_id)

Returns the 3D plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_plant_param_result import JsonScan3dPlantParamResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    device_id = 56 # int | deviceID
    round_id = 56 # int | roundID
    tray_id = 56 # int | trayID
    param_id = 56 # int | paramID

    try:
        # Returns the 3D plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
        api_response = api_instance.scan3d_plant_param(device_id, round_id, tray_id, param_id)
        print("The response of Scan3dApi->scan3d_plant_param:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_plant_param: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 
 **param_id** | **int**| paramID | 

### Return type

[**JsonScan3dPlantParamResult**](JsonScan3dPlantParamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan3d_plant_param_analyse**
> JsonScan3dPlantParamByAnalyseIDResult scan3d_plant_param_analyse(id, param_id)

Returns the 3D plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scan3d_plant_param_by_analyse_id_result import JsonScan3dPlantParamByAnalyseIDResult
from plantscreen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44339
# See configuration.py for a list of all supported configuration parameters.
configuration = plantscreen.Configuration(
    host = "https://localhost:44339"
)


# Enter a context with an instance of the API client
with plantscreen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plantscreen.Scan3dApi(api_client)
    id = 56 # int | analyseID
    param_id = 56 # int | ParamID

    try:
        # Returns the 3D plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
        api_response = api_instance.scan3d_plant_param_analyse(id, param_id)
        print("The response of Scan3dApi->scan3d_plant_param_analyse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Scan3dApi->scan3d_plant_param_analyse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| analyseID | 
 **param_id** | **int**| ParamID | 

### Return type

[**JsonScan3dPlantParamByAnalyseIDResult**](JsonScan3dPlantParamByAnalyseIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

