# swagger_client.FileApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file**](FileApi.md#file) | **GET** /file | Returns the streamed file located in the data file storage by defined path.

# **file**
> file(path)

Returns the streamed file located in the data file storage by defined path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileApi()
path = '2013-10-20T19:20:30+01:00' # datetime | fileStoragePath

try:
    # Returns the streamed file located in the data file storage by defined path.
    api_instance.file(path)
except ApiException as e:
    print("Exception when calling FileApi->file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **datetime**| fileStoragePath | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

