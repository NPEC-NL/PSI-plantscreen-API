# plantscreen.DeviceApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device**](DeviceApi.md#device) | **GET** /Device | Returns one device by device ID.
[**device_active**](DeviceApi.md#device_active) | **GET** /Device/Active | Returns all active devices that have not ended validity.
[**device_profile**](DeviceApi.md#device_profile) | **GET** /Device/Profile | Returns all devices that contains the system profile defined by ID.


# **device**
> JsonDeviceResult device(id)

Returns one device by device ID.

### Example


```python
import plantscreen
from plantscreen.models.json_device_result import JsonDeviceResult
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
    api_instance = plantscreen.DeviceApi(api_client)
    id = 56 # int | deviceID

    try:
        # Returns one device by device ID.
        api_response = api_instance.device(id)
        print("The response of DeviceApi->device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| deviceID | 

### Return type

[**JsonDeviceResult**](JsonDeviceResult.md)

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

# **device_active**
> JsonDeviceActiveResult device_active()

Returns all active devices that have not ended validity.

### Example


```python
import plantscreen
from plantscreen.models.json_device_active_result import JsonDeviceActiveResult
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
    api_instance = plantscreen.DeviceApi(api_client)

    try:
        # Returns all active devices that have not ended validity.
        api_response = api_instance.device_active()
        print("The response of DeviceApi->device_active:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->device_active: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JsonDeviceActiveResult**](JsonDeviceActiveResult.md)

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

# **device_profile**
> JsonDeviceByProfileIDResult device_profile(id)

Returns all devices that contains the system profile defined by ID.

### Example


```python
import plantscreen
from plantscreen.models.json_device_by_profile_id_result import JsonDeviceByProfileIDResult
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
    api_instance = plantscreen.DeviceApi(api_client)
    id = 56 # int | profileID

    try:
        # Returns all devices that contains the system profile defined by ID.
        api_response = api_instance.device_profile(id)
        print("The response of DeviceApi->device_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->device_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| profileID | 

### Return type

[**JsonDeviceByProfileIDResult**](JsonDeviceByProfileIDResult.md)

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

