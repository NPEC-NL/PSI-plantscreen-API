# plantscreen.SystemLogApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_log_date_log_tag**](SystemLogApi.md#system_log_date_log_tag) | **GET** /SystemLog/Date/LogTag | Returns important events as system logs by log tag between defined times. Times is entered as the start and end time of the required interval.
[**system_log_date_log_type**](SystemLogApi.md#system_log_date_log_type) | **GET** /SystemLog/Date/LogType | Returns important events as system logs by log type between defined times. Times is entered as the start and end time of the required interval.
[**system_log_date_round**](SystemLogApi.md#system_log_date_round) | **GET** /SystemLog/Date/Round | Returns important events as system logs by round ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the round.
[**system_log_date_tray**](SystemLogApi.md#system_log_date_tray) | **GET** /SystemLog/Date/Tray | Returns important events as system logs by tray ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the tray.
[**system_log_log_tag**](SystemLogApi.md#system_log_log_tag) | **GET** /SystemLog/LogTag | Returns a list of all used system log tag.
[**system_log_log_type**](SystemLogApi.md#system_log_log_type) | **GET** /SystemLog/LogType | Returns a list of all used system log types.
[**system_log_round**](SystemLogApi.md#system_log_round) | **GET** /SystemLog/Round | Returns important events as system logs by round ID. System logs are only optionally assigned to the round.
[**system_log_tray**](SystemLogApi.md#system_log_tray) | **GET** /SystemLog/Tray | Returns important events as system logs by tray ID. System logs are only optionally assigned to the tray.


# **system_log_date_log_tag**
> JsonSystemLogByLogTagAndDateResult system_log_date_log_tag(tag, start, stop)

Returns important events as system logs by log tag between defined times. Times is entered as the start and end time of the required interval.

### Example


```python
import plantscreen
from plantscreen.models.json_system_log_by_log_tag_and_date_result import JsonSystemLogByLogTagAndDateResult
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
    api_instance = plantscreen.SystemLogApi(api_client)
    tag = 'tag_example' # str | tag
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns important events as system logs by log tag between defined times. Times is entered as the start and end time of the required interval.
        api_response = api_instance.system_log_date_log_tag(tag, start, stop)
        print("The response of SystemLogApi->system_log_date_log_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemLogApi->system_log_date_log_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| tag | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonSystemLogByLogTagAndDateResult**](JsonSystemLogByLogTagAndDateResult.md)

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

# **system_log_date_log_type**
> JsonSystemLogByLogTypeAndDateResult system_log_date_log_type(type, start, stop)

Returns important events as system logs by log type between defined times. Times is entered as the start and end time of the required interval.

### Example


```python
import plantscreen
from plantscreen.models.json_system_log_by_log_type_and_date_result import JsonSystemLogByLogTypeAndDateResult
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
    api_instance = plantscreen.SystemLogApi(api_client)
    type = 'type_example' # str | type
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns important events as system logs by log type between defined times. Times is entered as the start and end time of the required interval.
        api_response = api_instance.system_log_date_log_type(type, start, stop)
        print("The response of SystemLogApi->system_log_date_log_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemLogApi->system_log_date_log_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonSystemLogByLogTypeAndDateResult**](JsonSystemLogByLogTypeAndDateResult.md)

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

# **system_log_date_round**
> JsonSystemLogByRoundIDAndDateResult system_log_date_round(id, start, stop)

Returns important events as system logs by round ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the round.

### Example


```python
import plantscreen
from plantscreen.models.json_system_log_by_round_id_and_date_result import JsonSystemLogByRoundIDAndDateResult
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
    api_instance = plantscreen.SystemLogApi(api_client)
    id = 56 # int | roundID
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns important events as system logs by round ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the round.
        api_response = api_instance.system_log_date_round(id, start, stop)
        print("The response of SystemLogApi->system_log_date_round:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemLogApi->system_log_date_round: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_log_date_tray**
> JsonSystemLogByTrayIDAndDateResult system_log_date_tray(id, start, stop)

Returns important events as system logs by tray ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the tray.

### Example


```python
import plantscreen
from plantscreen.models.json_system_log_by_tray_id_and_date_result import JsonSystemLogByTrayIDAndDateResult
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
    api_instance = plantscreen.SystemLogApi(api_client)
    id = 56 # int | trayID
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns important events as system logs by tray ID between defined times. Times is entered as the start and end time of the required interval. System logs are only optionally assigned to the tray.
        api_response = api_instance.system_log_date_tray(id, start, stop)
        print("The response of SystemLogApi->system_log_date_tray:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemLogApi->system_log_date_tray: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_log_log_tag**
> JsonSystemLogTagResult system_log_log_tag()

Returns a list of all used system log tag.

### Example


```python
import plantscreen
from plantscreen.models.json_system_log_tag_result import JsonSystemLogTagResult
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
    api_instance = plantscreen.SystemLogApi(api_client)

    try:
        # Returns a list of all used system log tag.
        api_response = api_instance.system_log_log_tag()
        print("The response of SystemLogApi->system_log_log_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemLogApi->system_log_log_tag: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_log_log_type**
> JsonSystemLogTypeResult system_log_log_type()

Returns a list of all used system log types.

### Example


```python
import plantscreen
from plantscreen.models.json_system_log_type_result import JsonSystemLogTypeResult
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
    api_instance = plantscreen.SystemLogApi(api_client)

    try:
        # Returns a list of all used system log types.
        api_response = api_instance.system_log_log_type()
        print("The response of SystemLogApi->system_log_log_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemLogApi->system_log_log_type: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_log_round**
> JsonSystemLogByRoundIDResult system_log_round(id)

Returns important events as system logs by round ID. System logs are only optionally assigned to the round.

### Example


```python
import plantscreen
from plantscreen.models.json_system_log_by_round_id_result import JsonSystemLogByRoundIDResult
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
    api_instance = plantscreen.SystemLogApi(api_client)
    id = 56 # int | roundID

    try:
        # Returns important events as system logs by round ID. System logs are only optionally assigned to the round.
        api_response = api_instance.system_log_round(id)
        print("The response of SystemLogApi->system_log_round:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemLogApi->system_log_round: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_log_tray**
> JsonSystemLogByTrayIDResult system_log_tray(id)

Returns important events as system logs by tray ID. System logs are only optionally assigned to the tray.

### Example


```python
import plantscreen
from plantscreen.models.json_system_log_by_tray_id_result import JsonSystemLogByTrayIDResult
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
    api_instance = plantscreen.SystemLogApi(api_client)
    id = 56 # int | trayID

    try:
        # Returns important events as system logs by tray ID. System logs are only optionally assigned to the tray.
        api_response = api_instance.system_log_tray(id)
        print("The response of SystemLogApi->system_log_tray:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemLogApi->system_log_tray: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

