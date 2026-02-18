# plantscreen.ProfileApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile**](ProfileApi.md#profile) | **GET** /Profile | Returns one system profile by profile ID.
[**profile_active**](ProfileApi.md#profile_active) | **GET** /Profile/Active | Returns the active system profile.
[**profile_id**](ProfileApi.md#profile_id) | **GET** /ProfileID | Returns a list of all system profile IDs in the database


# **profile**
> JsonSystemProfileResult profile(id)

Returns one system profile by profile ID.

### Example


```python
import plantscreen
from plantscreen.models.json_system_profile_result import JsonSystemProfileResult
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
    api_instance = plantscreen.ProfileApi(api_client)
    id = 56 # int | profileID

    try:
        # Returns one system profile by profile ID.
        api_response = api_instance.profile(id)
        print("The response of ProfileApi->profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| profileID | 

### Return type

[**JsonSystemProfileResult**](JsonSystemProfileResult.md)

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

# **profile_active**
> JsonSystemProfileActiveResult profile_active()

Returns the active system profile.

### Example


```python
import plantscreen
from plantscreen.models.json_system_profile_active_result import JsonSystemProfileActiveResult
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
    api_instance = plantscreen.ProfileApi(api_client)

    try:
        # Returns the active system profile.
        api_response = api_instance.profile_active()
        print("The response of ProfileApi->profile_active:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->profile_active: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JsonSystemProfileActiveResult**](JsonSystemProfileActiveResult.md)

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

# **profile_id**
> JsonSystemProfileIDResult profile_id()

Returns a list of all system profile IDs in the database

### Example


```python
import plantscreen
from plantscreen.models.json_system_profile_id_result import JsonSystemProfileIDResult
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
    api_instance = plantscreen.ProfileApi(api_client)

    try:
        # Returns a list of all system profile IDs in the database
        api_response = api_instance.profile_id()
        print("The response of ProfileApi->profile_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->profile_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JsonSystemProfileIDResult**](JsonSystemProfileIDResult.md)

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

