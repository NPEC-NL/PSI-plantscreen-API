# plantscreen.ProbeApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**probe**](ProbeApi.md#probe) | **GET** /Probe | If called without ID it returns all probeIDs, when called with it returns one environment probe of that probe ID.
[**probe_value_date**](ProbeApi.md#probe_value_date) | **GET** /Probe/Value/Date | Returns all probe values measured between times. Times is entered as the start and end time of the required interval.
[**probe_value_date_probe**](ProbeApi.md#probe_value_date_probe) | **GET** /Probe/Value/Date/Probe | Returns all probe values for probe defined by probe ID measured between times. Times is entered as the start and end time of the required interval.


# **probe**
> Probe200Response probe(id=id)

If called without ID it returns all probeIDs, when called with it returns one environment probe of that probe ID.

### Example


```python
import plantscreen
from plantscreen.models.probe200_response import Probe200Response
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
    api_instance = plantscreen.ProbeApi(api_client)
    id = 56 # int | probeID. Two versions, with and without parameter (optional)

    try:
        # If called without ID it returns all probeIDs, when called with it returns one environment probe of that probe ID.
        api_response = api_instance.probe(id=id)
        print("The response of ProbeApi->probe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProbeApi->probe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| probeID. Two versions, with and without parameter | [optional] 

### Return type

[**Probe200Response**](Probe200Response.md)

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

# **probe_value_date**
> JsonProbeValueByDateResult probe_value_date(start, stop)

Returns all probe values measured between times. Times is entered as the start and end time of the required interval.

### Example


```python
import plantscreen
from plantscreen.models.json_probe_value_by_date_result import JsonProbeValueByDateResult
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
    api_instance = plantscreen.ProbeApi(api_client)
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns all probe values measured between times. Times is entered as the start and end time of the required interval.
        api_response = api_instance.probe_value_date(start, stop)
        print("The response of ProbeApi->probe_value_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProbeApi->probe_value_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonProbeValueByDateResult**](JsonProbeValueByDateResult.md)

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

# **probe_value_date_probe**
> JsonProbeValueByIDAndDateResult probe_value_date_probe(id, start, stop)

Returns all probe values for probe defined by probe ID measured between times. Times is entered as the start and end time of the required interval.

### Example


```python
import plantscreen
from plantscreen.models.json_probe_value_by_id_and_date_result import JsonProbeValueByIDAndDateResult
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
    api_instance = plantscreen.ProbeApi(api_client)
    id = 56 # int | probeID
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns all probe values for probe defined by probe ID measured between times. Times is entered as the start and end time of the required interval.
        api_response = api_instance.probe_value_date_probe(id, start, stop)
        print("The response of ProbeApi->probe_value_date_probe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProbeApi->probe_value_date_probe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| probeID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonProbeValueByIDAndDateResult**](JsonProbeValueByIDAndDateResult.md)

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

