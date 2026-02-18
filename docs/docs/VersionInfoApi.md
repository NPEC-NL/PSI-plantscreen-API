# plantscreen.VersionInfoApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_info**](VersionInfoApi.md#version_info) | **GET** /VersionInfo | Returns version of the database and the PlantScreen Data REST API used


# **version_info**
> JsonVersionInfoResult version_info()

Returns version of the database and the PlantScreen Data REST API used

### Example


```python
import plantscreen
from plantscreen.models.json_version_info_result import JsonVersionInfoResult
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
    api_instance = plantscreen.VersionInfoApi(api_client)

    try:
        # Returns version of the database and the PlantScreen Data REST API used
        api_response = api_instance.version_info()
        print("The response of VersionInfoApi->version_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionInfoApi->version_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JsonVersionInfoResult**](JsonVersionInfoResult.md)

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

