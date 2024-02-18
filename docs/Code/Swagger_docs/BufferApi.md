# swagger_client.BufferApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buffer_history**](BufferApi.md#buffer_history) | **GET** /Buffer/History | Returns one buffer history state defined by buffer state ID.
[**buffer_history_date**](BufferApi.md#buffer_history_date) | **GET** /Buffer/History/Date | Returns buffer history states between times. Times is entered as the start and end time of the required interval.

# **buffer_history**
> JsonBufferHistoryResult buffer_history(id)

Returns one buffer history state defined by buffer state ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BufferApi()
id = 56 # int | bufferStateID

try:
    # Returns one buffer history state defined by buffer state ID.
    api_response = api_instance.buffer_history(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BufferApi->buffer_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| bufferStateID | 

### Return type

[**JsonBufferHistoryResult**](JsonBufferHistoryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **buffer_history_date**
> JsonBufferHistoryByDateResult buffer_history_date(start, stop)

Returns buffer history states between times. Times is entered as the start and end time of the required interval.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BufferApi()
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns buffer history states between times. Times is entered as the start and end time of the required interval.
    api_response = api_instance.buffer_history_date(start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BufferApi->buffer_history_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonBufferHistoryByDateResult**](JsonBufferHistoryByDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

