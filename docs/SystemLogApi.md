# plantscreen.swagger_client.SystemLogApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_log_date_log_tag**](SystemLogApi.md#get_system_log_date_log_tag) | **GET** /SystemLog/Date/LogTag | Returns important events as system logs by log tag between defined times. Times is entered as the start and end time of the required interval.
[**get_system_log_date_log_type**](SystemLogApi.md#get_system_log_date_log_type) | **GET** /SystemLog/Date/LogType | Returns important events as system logs by log type between defined times. Times is entered as the start and end time of the required interval.
[**get_system_log_date_round**](SystemLogApi.md#get_system_log_date_round) | **GET** /SystemLog/Date/Round | Returns important events as system logs by round ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the round.
[**get_system_log_date_tray**](SystemLogApi.md#get_system_log_date_tray) | **GET** /SystemLog/Date/Tray | Returns important events as system logs by tray ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the tray.
[**get_system_log_log_tag**](SystemLogApi.md#get_system_log_log_tag) | **GET** /SystemLog/LogTag | Returns a list of all used system log tag.
[**get_system_log_log_type**](SystemLogApi.md#get_system_log_log_type) | **GET** /SystemLog/LogType | Returns a list of all used system log types.
[**get_system_log_round**](SystemLogApi.md#get_system_log_round) | **GET** /SystemLog/Round | Returns important events as system logs by round ID. System logs are only optionally assigned to the round.
[**get_system_log_tray**](SystemLogApi.md#get_system_log_tray) | **GET** /SystemLog/Tray | Returns important events as system logs by tray ID. System logs are only optionally assigned to the tray.

# **get_system_log_date_log_tag**
> JsonSystemLogByLogTagAndDateResult get_system_log_date_log_tag(tag, start, stop)

Returns important events as system logs by log tag between defined times. Times is entered as the start and end time of the required interval.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.SystemLogApi()
tag = 56 # int | tag
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns important events as system logs by log tag between defined times. Times is entered as the start and end time of the required interval.
    api_response = api_instance.get_system_log_date_log_tag(tag, start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLogApi->get_system_log_date_log_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **int**| tag | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonSystemLogByLogTagAndDateResult**](JsonSystemLogByLogTagAndDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_log_date_log_type**
> JsonSystemLogByLogTypeAndDateResult get_system_log_date_log_type(type, start, stop)

Returns important events as system logs by log type between defined times. Times is entered as the start and end time of the required interval.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.SystemLogApi()
type = 56 # int | type
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns important events as system logs by log type between defined times. Times is entered as the start and end time of the required interval.
    api_response = api_instance.get_system_log_date_log_type(type, start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLogApi->get_system_log_date_log_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **int**| type | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonSystemLogByLogTypeAndDateResult**](JsonSystemLogByLogTypeAndDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_log_date_round**
> JsonSystemLogByRoundIDAndDateResult get_system_log_date_round(id, start, stop)

Returns important events as system logs by round ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the round.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.SystemLogApi()
id = 56 # int | roundID
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns important events as system logs by round ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the round.
    api_response = api_instance.get_system_log_date_round(id, start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLogApi->get_system_log_date_round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonSystemLogByRoundIDAndDateResult**](JsonSystemLogByRoundIDAndDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_log_date_tray**
> JsonSystemLogByTrayIDAndDateResult get_system_log_date_tray(id, start, stop)

Returns important events as system logs by tray ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the tray.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.SystemLogApi()
id = 56 # int | trayID
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns important events as system logs by tray ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the tray.
    api_response = api_instance.get_system_log_date_tray(id, start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLogApi->get_system_log_date_tray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonSystemLogByTrayIDAndDateResult**](JsonSystemLogByTrayIDAndDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_log_log_tag**
> JsonSystemLogTagResult get_system_log_log_tag()

Returns a list of all used system log tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.SystemLogApi()

try:
    # Returns a list of all used system log tag.
    api_response = api_instance.get_system_log_log_tag()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLogApi->get_system_log_log_tag: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonSystemLogTagResult**](JsonSystemLogTagResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_log_log_type**
> JsonSystemLogTypeResult get_system_log_log_type()

Returns a list of all used system log types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.SystemLogApi()

try:
    # Returns a list of all used system log types.
    api_response = api_instance.get_system_log_log_type()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLogApi->get_system_log_log_type: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonSystemLogTypeResult**](JsonSystemLogTypeResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_log_round**
> JsonSystemLogByRoundIDResult get_system_log_round(id)

Returns important events as system logs by round ID. System logs are only optionally assigned to the round.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.SystemLogApi()
id = 56 # int | roundID

try:
    # Returns important events as system logs by round ID. System logs are only optionally assigned to the round.
    api_response = api_instance.get_system_log_round(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLogApi->get_system_log_round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonSystemLogByRoundIDResult**](JsonSystemLogByRoundIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_log_tray**
> JsonSystemLogByTrayIDResult get_system_log_tray(id)

Returns important events as system logs by tray ID. System logs are only optionally assigned to the tray.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.SystemLogApi()
id = 56 # int | trayID

try:
    # Returns important events as system logs by tray ID. System logs are only optionally assigned to the tray.
    api_response = api_instance.get_system_log_tray(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLogApi->get_system_log_tray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 

### Return type

[**JsonSystemLogByTrayIDResult**](JsonSystemLogByTrayIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

