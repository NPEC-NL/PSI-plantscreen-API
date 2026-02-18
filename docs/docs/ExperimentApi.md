# plantscreen.ExperimentApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiment**](ExperimentApi.md#experiment) | **GET** /Experiment | Returns one experiment by experiment ID.
[**experiment_date**](ExperimentApi.md#experiment_date) | **GET** /Experiment/Date | Returns all experiments whose rounds took place between defined times. Times is entered as the start and end time of the required interval. All experiments with at least one round between these times will be returned.
[**experiment_id**](ExperimentApi.md#experiment_id) | **GET** /ExperimentID | Returns a list of all experiment IDs in the database.
[**experiment_owner**](ExperimentApi.md#experiment_owner) | **GET** /Experiment/Owner | Returns all experiments that belong to the user defined by ID.
[**note_experiment**](ExperimentApi.md#note_experiment) | **GET** /Note/Experiment | Returns the experiment notes that the user saved for the experiment defined by ID.
[**owner**](ExperimentApi.md#owner) | **GET** /Owner | Returns the owner(s) of the experiment by owner ID.
[**owner_id**](ExperimentApi.md#owner_id) | **GET** /OwnerID | Returns a list of all experiment owner IDs in the database.


# **experiment**
> JsonExperimentResult experiment(id)

Returns one experiment by experiment ID.

### Example


```python
import plantscreen
from plantscreen.models.json_experiment_result import JsonExperimentResult
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
    api_instance = plantscreen.ExperimentApi(api_client)
    id = 56 # int | experimentID

    try:
        # Returns one experiment by experiment ID.
        api_response = api_instance.experiment(id)
        print("The response of ExperimentApi->experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonExperimentResult**](JsonExperimentResult.md)

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

# **experiment_date**
> JsonExperimentByDateResult experiment_date(start, stop)

Returns all experiments whose rounds took place between defined times. Times is entered as the start and end time of the required interval. All experiments with at least one round between these times will be returned.

### Example


```python
import plantscreen
from plantscreen.models.json_experiment_by_date_result import JsonExperimentByDateResult
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
    api_instance = plantscreen.ExperimentApi(api_client)
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns all experiments whose rounds took place between defined times. Times is entered as the start and end time of the required interval. All experiments with at least one round between these times will be returned.
        api_response = api_instance.experiment_date(start, stop)
        print("The response of ExperimentApi->experiment_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonExperimentByDateResult**](JsonExperimentByDateResult.md)

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

# **experiment_id**
> JsonExperimentIDResult experiment_id()

Returns a list of all experiment IDs in the database.

### Example


```python
import plantscreen
from plantscreen.models.json_experiment_id_result import JsonExperimentIDResult
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
    api_instance = plantscreen.ExperimentApi(api_client)

    try:
        # Returns a list of all experiment IDs in the database.
        api_response = api_instance.experiment_id()
        print("The response of ExperimentApi->experiment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JsonExperimentIDResult**](JsonExperimentIDResult.md)

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

# **experiment_owner**
> JsonExperimentByOwnerResult experiment_owner(id)

Returns all experiments that belong to the user defined by ID.

### Example


```python
import plantscreen
from plantscreen.models.json_experiment_by_owner_result import JsonExperimentByOwnerResult
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
    api_instance = plantscreen.ExperimentApi(api_client)
    id = 56 # int | ownerID

    try:
        # Returns all experiments that belong to the user defined by ID.
        api_response = api_instance.experiment_owner(id)
        print("The response of ExperimentApi->experiment_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ownerID | 

### Return type

[**JsonExperimentByOwnerResult**](JsonExperimentByOwnerResult.md)

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

# **note_experiment**
> JsonNoteResult note_experiment(id)

Returns the experiment notes that the user saved for the experiment defined by ID.

### Example


```python
import plantscreen
from plantscreen.models.json_note_result import JsonNoteResult
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
    api_instance = plantscreen.ExperimentApi(api_client)
    id = 56 # int | experimentID

    try:
        # Returns the experiment notes that the user saved for the experiment defined by ID.
        api_response = api_instance.note_experiment(id)
        print("The response of ExperimentApi->note_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->note_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonNoteResult**](JsonNoteResult.md)

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

# **owner**
> JsonOwnerResult owner(ids)

Returns the owner(s) of the experiment by owner ID.

### Example


```python
import plantscreen
from plantscreen.models.json_owner_result import JsonOwnerResult
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
    api_instance = plantscreen.ExperimentApi(api_client)
    ids = [56] # List[int] | List of Owner IDs

    try:
        # Returns the owner(s) of the experiment by owner ID.
        api_response = api_instance.owner(ids)
        print("The response of ExperimentApi->owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| List of Owner IDs | 

### Return type

[**JsonOwnerResult**](JsonOwnerResult.md)

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

# **owner_id**
> JsonOwnerIDResult owner_id()

Returns a list of all experiment owner IDs in the database.

### Example


```python
import plantscreen
from plantscreen.models.json_owner_id_result import JsonOwnerIDResult
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
    api_instance = plantscreen.ExperimentApi(api_client)

    try:
        # Returns a list of all experiment owner IDs in the database.
        api_response = api_instance.owner_id()
        print("The response of ExperimentApi->owner_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->owner_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JsonOwnerIDResult**](JsonOwnerIDResult.md)

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

