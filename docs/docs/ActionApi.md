# plantscreen.ActionApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action**](ActionApi.md#action) | **GET** /Action | Returns one scheduled action by action ID.
[**action_experiment**](ActionApi.md#action_experiment) | **GET** /Action/Experiment | Returns all scheduled actions in the experiment defined by ID.
[**action_group**](ActionApi.md#action_group) | **GET** /Action/Group | Returns one group of scheduled actions by action group ID.
[**action_group_round**](ActionApi.md#action_group_round) | **GET** /Action/Group/Round | Returns one group of scheduled actions to which a round defined by ID belongs.
[**action_not_done_experiment**](ActionApi.md#action_not_done_experiment) | **GET** /Action/NotDone/Experiment | Returns all unfinished scheduled actions (with pending and running action state) in the experiment defined by ID.
[**action_protocol**](ActionApi.md#action_protocol) | **GET** /Action/Protocol | Returns one protocol of scheduled action by protocol ID.
[**action_protocol_round**](ActionApi.md#action_protocol_round) | **GET** /Action/Protocol/Round | Returns one group of scheduled actions that belong to round defined by ID.


# **action**
> JsonActionResult action(id)

Returns one scheduled action by action ID.

### Example


```python
import plantscreen
from plantscreen.models.json_action_result import JsonActionResult
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
    api_instance = plantscreen.ActionApi(api_client)
    id = 56 # int | actionID

    try:
        # Returns one scheduled action by action ID.
        api_response = api_instance.action(id)
        print("The response of ActionApi->action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionApi->action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| actionID | 

### Return type

[**JsonActionResult**](JsonActionResult.md)

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

# **action_experiment**
> JsonActionByExperimentIDResult action_experiment(id)

Returns all scheduled actions in the experiment defined by ID.

### Example


```python
import plantscreen
from plantscreen.models.json_action_by_experiment_id_result import JsonActionByExperimentIDResult
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
    api_instance = plantscreen.ActionApi(api_client)
    id = 56 # int | experimentID

    try:
        # Returns all scheduled actions in the experiment defined by ID.
        api_response = api_instance.action_experiment(id)
        print("The response of ActionApi->action_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionApi->action_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonActionByExperimentIDResult**](JsonActionByExperimentIDResult.md)

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

# **action_group**
> JsonActionGroupResult action_group(id)

Returns one group of scheduled actions by action group ID.

### Example


```python
import plantscreen
from plantscreen.models.json_action_group_result import JsonActionGroupResult
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
    api_instance = plantscreen.ActionApi(api_client)
    id = 56 # int | groupID

    try:
        # Returns one group of scheduled actions by action group ID.
        api_response = api_instance.action_group(id)
        print("The response of ActionApi->action_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionApi->action_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| groupID | 

### Return type

[**JsonActionGroupResult**](JsonActionGroupResult.md)

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

# **action_group_round**
> JsonActionGroupByRoundIDResult action_group_round(id)

Returns one group of scheduled actions to which a round defined by ID belongs.

### Example


```python
import plantscreen
from plantscreen.models.json_action_group_by_round_id_result import JsonActionGroupByRoundIDResult
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
    api_instance = plantscreen.ActionApi(api_client)
    id = 56 # int | roundID

    try:
        # Returns one group of scheduled actions to which a round defined by ID belongs.
        api_response = api_instance.action_group_round(id)
        print("The response of ActionApi->action_group_round:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionApi->action_group_round: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonActionGroupByRoundIDResult**](JsonActionGroupByRoundIDResult.md)

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

# **action_not_done_experiment**
> JsonActionByExperimentIDNotDoneResult action_not_done_experiment(id)

Returns all unfinished scheduled actions (with pending and running action state) in the experiment defined by ID.

### Example


```python
import plantscreen
from plantscreen.models.json_action_by_experiment_id_not_done_result import JsonActionByExperimentIDNotDoneResult
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
    api_instance = plantscreen.ActionApi(api_client)
    id = 56 # int | experimentID

    try:
        # Returns all unfinished scheduled actions (with pending and running action state) in the experiment defined by ID.
        api_response = api_instance.action_not_done_experiment(id)
        print("The response of ActionApi->action_not_done_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionApi->action_not_done_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonActionByExperimentIDNotDoneResult**](JsonActionByExperimentIDNotDoneResult.md)

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

# **action_protocol**
> JsonActionProtocolResult action_protocol(id)

Returns one protocol of scheduled action by protocol ID.

### Example


```python
import plantscreen
from plantscreen.models.json_action_protocol_result import JsonActionProtocolResult
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
    api_instance = plantscreen.ActionApi(api_client)
    id = 56 # int | protocolID

    try:
        # Returns one protocol of scheduled action by protocol ID.
        api_response = api_instance.action_protocol(id)
        print("The response of ActionApi->action_protocol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionApi->action_protocol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| protocolID | 

### Return type

[**JsonActionProtocolResult**](JsonActionProtocolResult.md)

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

# **action_protocol_round**
> JsonActionProtocolByRoundIDResult action_protocol_round(id)

Returns one group of scheduled actions that belong to round defined by ID.

### Example


```python
import plantscreen
from plantscreen.models.json_action_protocol_by_round_id_result import JsonActionProtocolByRoundIDResult
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
    api_instance = plantscreen.ActionApi(api_client)
    id = 56 # int | roundID

    try:
        # Returns one group of scheduled actions that belong to round defined by ID.
        api_response = api_instance.action_protocol_round(id)
        print("The response of ActionApi->action_protocol_round:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionApi->action_protocol_round: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonActionProtocolByRoundIDResult**](JsonActionProtocolByRoundIDResult.md)

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

