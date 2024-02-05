# plantscreen.swagger_client.VersionInfoApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_info**](VersionInfoApi.md#version_info) | **GET** /VersionInfo | Returns version of the database and the PlantScreen Data REST API used

# **version_info**
> JsonVersionInfoResult version_info()

Returns version of the database and the PlantScreen Data REST API used

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.VersionInfoApi()

try:
    # Returns version of the database and the PlantScreen Data REST API used
    api_response = api_instance.version_info()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

