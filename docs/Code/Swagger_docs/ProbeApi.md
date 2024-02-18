# swagger_client.ProbeApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**probe**](ProbeApi.md#probe) | **GET** /Probe | If called without ID it returns all probeIDs, when called with it returns one environment probe of that probe ID.
[**probe_value_date**](ProbeApi.md#probe_value_date) | **GET** /Probe/Value/Date | Returns all probe values measured between times. Times is entered as the start and end time of the required interval.
[**probe_value_date_probe**](ProbeApi.md#probe_value_date_probe) | **GET** /Probe/Value/Date/Probe | Returns all probe values for probe defined by probe ID measured between times. Times is entered as the start and end time of the required interval.

# **probe**
> InlineResponse2001 probe(id=id)

If called without ID it returns all probeIDs, when called with it returns one environment probe of that probe ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProbeApi()
id = 56 # int | probeID. Two versions, with and without parameter (optional)

try:
    # If called without ID it returns all probeIDs, when called with it returns one environment probe of that probe ID.
    api_response = api_instance.probe(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProbeApi->probe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| probeID. Two versions, with and without parameter | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **probe_value_date**
> JsonProbeValueByDateResult probe_value_date(start, stop)

Returns all probe values measured between times. Times is entered as the start and end time of the required interval.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProbeApi()
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns all probe values measured between times. Times is entered as the start and end time of the required interval.
    api_response = api_instance.probe_value_date(start, stop)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **probe_value_date_probe**
> JsonProbeValueByIDAndDateResult probe_value_date_probe(id, start, stop)

Returns all probe values for probe defined by probe ID measured between times. Times is entered as the start and end time of the required interval.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProbeApi()
id = 56 # int | probeID
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns all probe values for probe defined by probe ID measured between times. Times is entered as the start and end time of the required interval.
    api_response = api_instance.probe_value_date_probe(id, start, stop)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

