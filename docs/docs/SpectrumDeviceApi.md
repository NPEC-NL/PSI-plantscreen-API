# plantscreen.SpectrumDeviceApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spectrum_device**](SpectrumDeviceApi.md#spectrum_device) | **GET** /SpectrumDevice | Returns one spectrum device by spectrum device ID.
[**spectrum_device_id**](SpectrumDeviceApi.md#spectrum_device_id) | **GET** /SpectrumDeviceID | Returns a list of all spectrum device IDs in the database.
[**spectrum_values_date_device**](SpectrumDeviceApi.md#spectrum_values_date_device) | **GET** /Spectrum/Values/Date/Device | Returns spectrum values for spectrum device defined by spectrum device ID measured between times. Times is entered as the start and end time of the required interval.


# **spectrum_device**
> JsonSpectrumDeviceResult spectrum_device(id)

Returns one spectrum device by spectrum device ID.

### Example


```python
import plantscreen
from plantscreen.models.json_spectrum_device_result import JsonSpectrumDeviceResult
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
    api_instance = plantscreen.SpectrumDeviceApi(api_client)
    id = 56 # int | spectrumDeviceID

    try:
        # Returns one spectrum device by spectrum device ID.
        api_response = api_instance.spectrum_device(id)
        print("The response of SpectrumDeviceApi->spectrum_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpectrumDeviceApi->spectrum_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| spectrumDeviceID | 

### Return type

[**JsonSpectrumDeviceResult**](JsonSpectrumDeviceResult.md)

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

# **spectrum_device_id**
> JsonSpectrumDeviceIDResult spectrum_device_id()

Returns a list of all spectrum device IDs in the database.

### Example


```python
import plantscreen
from plantscreen.models.json_spectrum_device_id_result import JsonSpectrumDeviceIDResult
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
    api_instance = plantscreen.SpectrumDeviceApi(api_client)

    try:
        # Returns a list of all spectrum device IDs in the database.
        api_response = api_instance.spectrum_device_id()
        print("The response of SpectrumDeviceApi->spectrum_device_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpectrumDeviceApi->spectrum_device_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JsonSpectrumDeviceIDResult**](JsonSpectrumDeviceIDResult.md)

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

# **spectrum_values_date_device**
> JsonSpectrumValuesResult spectrum_values_date_device(id, start, stop)

Returns spectrum values for spectrum device defined by spectrum device ID measured between times. Times is entered as the start and end time of the required interval.

### Example


```python
import plantscreen
from plantscreen.models.json_spectrum_values_result import JsonSpectrumValuesResult
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
    api_instance = plantscreen.SpectrumDeviceApi(api_client)
    id = 56 # int | spectrumDeviceID
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns spectrum values for spectrum device defined by spectrum device ID measured between times. Times is entered as the start and end time of the required interval.
        api_response = api_instance.spectrum_values_date_device(id, start, stop)
        print("The response of SpectrumDeviceApi->spectrum_values_date_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpectrumDeviceApi->spectrum_values_date_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| spectrumDeviceID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonSpectrumValuesResult**](JsonSpectrumValuesResult.md)

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

