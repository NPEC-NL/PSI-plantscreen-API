# plantscreen.RoundApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**round**](RoundApi.md#round) | **GET** /Round | Returns one round by round ID.
[**round_date_experiment**](RoundApi.md#round_date_experiment) | **GET** /Round/Date/Experiment | Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.
[**round_experiment**](RoundApi.md#round_experiment) | **GET** /Round/Experiment | Returns all rounds measured in the experiment defined by ID.
[**round_order_date_experiment**](RoundApi.md#round_order_date_experiment) | **GET** /RoundOrder/Date/Experiment | Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.
[**round_order_experiment**](RoundApi.md#round_order_experiment) | **GET** /RoundOrder/Experiment | Returns all rounds measured in the experiment defined by ID.
[**round_order_round**](RoundApi.md#round_order_round) | **GET** /RoundOrder/Round | Returns the round order in the experiment by round ID.


# **round**
> JsonRoundResult round(id)

Returns one round by round ID.

### Example


```python
import plantscreen
from plantscreen.models.json_round_result import JsonRoundResult
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
    api_instance = plantscreen.RoundApi(api_client)
    id = 56 # int | roundID

    try:
        # Returns one round by round ID.
        api_response = api_instance.round(id)
        print("The response of RoundApi->round:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundApi->round: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonRoundResult**](JsonRoundResult.md)

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

# **round_date_experiment**
> JsonRoundByExperimentIDAndDateResult round_date_experiment(id, start, stop)

Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.

### Example


```python
import plantscreen
from plantscreen.models.json_round_by_experiment_id_and_date_result import JsonRoundByExperimentIDAndDateResult
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
    api_instance = plantscreen.RoundApi(api_client)
    id = 56 # int | experimentID
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.
        api_response = api_instance.round_date_experiment(id, start, stop)
        print("The response of RoundApi->round_date_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundApi->round_date_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonRoundByExperimentIDAndDateResult**](JsonRoundByExperimentIDAndDateResult.md)

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

# **round_experiment**
> JsonRoundByExperimentIDResult round_experiment(id)

Returns all rounds measured in the experiment defined by ID.

### Example


```python
import plantscreen
from plantscreen.models.json_round_by_experiment_id_result import JsonRoundByExperimentIDResult
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
    api_instance = plantscreen.RoundApi(api_client)
    id = 56 # int | experimentID

    try:
        # Returns all rounds measured in the experiment defined by ID.
        api_response = api_instance.round_experiment(id)
        print("The response of RoundApi->round_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundApi->round_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonRoundByExperimentIDResult**](JsonRoundByExperimentIDResult.md)

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

# **round_order_date_experiment**
> JsonRoundOrderByExperimentIDAndDateResult round_order_date_experiment(id, start, stop)

Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.

### Example


```python
import plantscreen
from plantscreen.models.json_round_order_by_experiment_id_and_date_result import JsonRoundOrderByExperimentIDAndDateResult
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
    api_instance = plantscreen.RoundApi(api_client)
    id = 56 # int | experimentID
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.
        api_response = api_instance.round_order_date_experiment(id, start, stop)
        print("The response of RoundApi->round_order_date_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundApi->round_order_date_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonRoundOrderByExperimentIDAndDateResult**](JsonRoundOrderByExperimentIDAndDateResult.md)

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

# **round_order_experiment**
> JsonRoundOrderByExperimentIDResult round_order_experiment(id)

Returns all rounds measured in the experiment defined by ID.

### Example


```python
import plantscreen
from plantscreen.models.json_round_order_by_experiment_id_result import JsonRoundOrderByExperimentIDResult
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
    api_instance = plantscreen.RoundApi(api_client)
    id = 56 # int | experimentID

    try:
        # Returns all rounds measured in the experiment defined by ID.
        api_response = api_instance.round_order_experiment(id)
        print("The response of RoundApi->round_order_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundApi->round_order_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonRoundOrderByExperimentIDResult**](JsonRoundOrderByExperimentIDResult.md)

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

# **round_order_round**
> JsonRoundOrderResult round_order_round(id)

Returns the round order in the experiment by round ID.

### Example


```python
import plantscreen
from plantscreen.models.json_round_order_result import JsonRoundOrderResult
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
    api_instance = plantscreen.RoundApi(api_client)
    id = 56 # int | roundID

    try:
        # Returns the round order in the experiment by round ID.
        api_response = api_instance.round_order_round(id)
        print("The response of RoundApi->round_order_round:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundApi->round_order_round: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonRoundOrderResult**](JsonRoundOrderResult.md)

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

