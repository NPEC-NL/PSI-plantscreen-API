# swagger_client.BufferApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_buffer_history**](BufferApi.md#get_buffer_history) | **GET** /Buffer/History | Returns one buffer history state defined by buffer state ID.
[**get_buffer_history_date**](BufferApi.md#get_buffer_history_date) | **GET** /Buffer/History/Date | Returns buffer history states between times. Times is entered as the start and end time of the required interval.

# **get_buffer_history**
> JsonBufferHistoryResult get_buffer_history(id)

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
    api_response = api_instance.get_buffer_history(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BufferApi->get_buffer_history: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buffer_history_date**
> JsonBufferHistoryByDateResult get_buffer_history_date(start, stop)

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
    api_response = api_instance.get_buffer_history_date(start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BufferApi->get_buffer_history_date: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

