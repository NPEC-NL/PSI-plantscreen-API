# plantscreen.ScalesApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scales_plant_weight**](ScalesApi.md#scales_plant_weight) | **GET** /Scales/PlantWeight | Returns scales data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**scales_plant_weight_measure**](ScalesApi.md#scales_plant_weight_measure) | **GET** /Scales/PlantWeight/Measure | Returns scales data by measure ID.
[**scales_weight_reference_plant**](ScalesApi.md#scales_weight_reference_plant) | **GET** /Scales/WeightReference/Plant | Returns plant weight reference data by plant ID. The weight is in units of grams
[**scales_weight_reference_to_date_tray**](ScalesApi.md#scales_weight_reference_to_date_tray) | **GET** /Scales/WeightReference/ToDate/Tray | Returns plant weight reference data by plant ID. The weight is in units of grams
[**scales_weight_reference_tray**](ScalesApi.md#scales_weight_reference_tray) | **GET** /Scales/WeightReference/Tray | Returns plant weight reference data by tray ID. The weight is in units of grams


# **scales_plant_weight**
> JsonScalesMeasureResult scales_plant_weight(device_id, round_id, tray_id)

Returns scales data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scales_measure_result import JsonScalesMeasureResult
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
    api_instance = plantscreen.ScalesApi(api_client)
    device_id = 56 # int | deviceID
    round_id = 56 # int | roundID
    tray_id = 56 # int | trayID

    try:
        # Returns scales data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
        api_response = api_instance.scales_plant_weight(device_id, round_id, tray_id)
        print("The response of ScalesApi->scales_plant_weight:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScalesApi->scales_plant_weight: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonScalesMeasureResult**](JsonScalesMeasureResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)

# **scales_plant_weight_measure**
> JsonScalesMeasureByIDResult scales_plant_weight_measure(id)

Returns scales data by measure ID.

### Example


```python
import plantscreen
from plantscreen.models.json_scales_measure_by_id_result import JsonScalesMeasureByIDResult
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
    api_instance = plantscreen.ScalesApi(api_client)
    id = 56 # int | measureID

    try:
        # Returns scales data by measure ID.
        api_response = api_instance.scales_plant_weight_measure(id)
        print("The response of ScalesApi->scales_plant_weight_measure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScalesApi->scales_plant_weight_measure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonScalesMeasureByIDResult**](JsonScalesMeasureByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)

# **scales_weight_reference_plant**
> JsonPlantWeightReferenceByPlantIDResult scales_weight_reference_plant(id)

Returns plant weight reference data by plant ID. The weight is in units of grams

### Example


```python
import plantscreen
from plantscreen.models.json_plant_weight_reference_by_plant_id_result import JsonPlantWeightReferenceByPlantIDResult
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
    api_instance = plantscreen.ScalesApi(api_client)
    id = 56 # int | plantID

    try:
        # Returns plant weight reference data by plant ID. The weight is in units of grams
        api_response = api_instance.scales_weight_reference_plant(id)
        print("The response of ScalesApi->scales_weight_reference_plant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScalesApi->scales_weight_reference_plant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| plantID | 

### Return type

[**JsonPlantWeightReferenceByPlantIDResult**](JsonPlantWeightReferenceByPlantIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)

# **scales_weight_reference_to_date_tray**
> JsonPlantWeightReferenceByTrayIDToDateResult scales_weight_reference_to_date_tray(id, var_date)

Returns plant weight reference data by plant ID. The weight is in units of grams

### Example


```python
import plantscreen
from plantscreen.models.json_plant_weight_reference_by_tray_idto_date_result import JsonPlantWeightReferenceByTrayIDToDateResult
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
    api_instance = plantscreen.ScalesApi(api_client)
    id = 56 # int | trayID
    var_date = '2013-10-20T19:20:30+01:00' # datetime | toDate

    try:
        # Returns plant weight reference data by plant ID. The weight is in units of grams
        api_response = api_instance.scales_weight_reference_to_date_tray(id, var_date)
        print("The response of ScalesApi->scales_weight_reference_to_date_tray:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScalesApi->scales_weight_reference_to_date_tray: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 
 **var_date** | **datetime**| toDate | 

### Return type

[**JsonPlantWeightReferenceByTrayIDToDateResult**](JsonPlantWeightReferenceByTrayIDToDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)

# **scales_weight_reference_tray**
> JsonPlantWeightReferenceByTrayIDResult scales_weight_reference_tray(id)

Returns plant weight reference data by tray ID. The weight is in units of grams

### Example


```python
import plantscreen
from plantscreen.models.json_plant_weight_reference_by_tray_id_result import JsonPlantWeightReferenceByTrayIDResult
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
    api_instance = plantscreen.ScalesApi(api_client)
    id = 56 # int | trayID

    try:
        # Returns plant weight reference data by tray ID. The weight is in units of grams
        api_response = api_instance.scales_weight_reference_tray(id)
        print("The response of ScalesApi->scales_weight_reference_tray:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScalesApi->scales_weight_reference_tray: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 

### Return type

[**JsonPlantWeightReferenceByTrayIDResult**](JsonPlantWeightReferenceByTrayIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [Back to API Endpoints](../API_endpoints.md) [Back to Models](../Models.md) [[Back to README]](../README.md)

