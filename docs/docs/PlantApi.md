# plantscreen.PlantApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plant**](PlantApi.md#plant) | **GET** /Plant | Returns a list of plants by the list of plant IDs.
[**plant_height_round**](PlantApi.md#plant_height_round) | **GET** /Plant/Height/Round | Returns all plant heights measured in the round defined by ID.
[**plant_leaf**](PlantApi.md#plant_leaf) | **GET** /Plant/Leaf | Returns all plant leaves for the plant assigned to the tray defined by the plant and tray ID.
[**plant_tray**](PlantApi.md#plant_tray) | **GET** /Plant/Tray | Returns list of plants which are assigned to the tray defined by ID.
[**plant_tray_profile**](PlantApi.md#plant_tray_profile) | **GET** /Plant/TrayProfile | Returns plants that were assigned to the tray profile defined by tray profile ID without time limit.
[**plant_tray_profile_tray**](PlantApi.md#plant_tray_profile_tray) | **GET** /Plant/TrayProfile/Tray | Returns plants that were assigned to the tray defined by tray ID between defined times. Times is entered as the start and end time of the required interval. All plants assigned to tray between these times will be returned.


# **plant**
> JsonPlantResult plant(ids)

Returns a list of plants by the list of plant IDs.

### Example


```python
import plantscreen
from plantscreen.models.json_plant_result import JsonPlantResult
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
    api_instance = plantscreen.PlantApi(api_client)
    ids = [56] # List[int] | plantIDs

    try:
        # Returns a list of plants by the list of plant IDs.
        api_response = api_instance.plant(ids)
        print("The response of PlantApi->plant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantApi->plant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| plantIDs | 

### Return type

[**JsonPlantResult**](JsonPlantResult.md)

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

# **plant_height_round**
> JsonPlantHeightByRoundIDResult plant_height_round(id)

Returns all plant heights measured in the round defined by ID.

### Example


```python
import plantscreen
from plantscreen.models.json_plant_height_by_round_id_result import JsonPlantHeightByRoundIDResult
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
    api_instance = plantscreen.PlantApi(api_client)
    id = 56 # int | roundID

    try:
        # Returns all plant heights measured in the round defined by ID.
        api_response = api_instance.plant_height_round(id)
        print("The response of PlantApi->plant_height_round:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantApi->plant_height_round: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonPlantHeightByRoundIDResult**](JsonPlantHeightByRoundIDResult.md)

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

# **plant_leaf**
> JsonPlantLeavesByPlantAndTrayIDResult plant_leaf(plant_id, tray_id)

Returns all plant leaves for the plant assigned to the tray defined by the plant and tray ID.

### Example


```python
import plantscreen
from plantscreen.models.json_plant_leaves_by_plant_and_tray_id_result import JsonPlantLeavesByPlantAndTrayIDResult
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
    api_instance = plantscreen.PlantApi(api_client)
    plant_id = 56 # int | plantID
    tray_id = 56 # int | trayID

    try:
        # Returns all plant leaves for the plant assigned to the tray defined by the plant and tray ID.
        api_response = api_instance.plant_leaf(plant_id, tray_id)
        print("The response of PlantApi->plant_leaf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantApi->plant_leaf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plant_id** | **int**| plantID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonPlantLeavesByPlantAndTrayIDResult**](JsonPlantLeavesByPlantAndTrayIDResult.md)

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

# **plant_tray**
> JsonPlantByTrayIDResult plant_tray(id)

Returns list of plants which are assigned to the tray defined by ID.

### Example


```python
import plantscreen
from plantscreen.models.json_plant_by_tray_id_result import JsonPlantByTrayIDResult
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
    api_instance = plantscreen.PlantApi(api_client)
    id = 56 # int | trayID

    try:
        # Returns list of plants which are assigned to the tray defined by ID.
        api_response = api_instance.plant_tray(id)
        print("The response of PlantApi->plant_tray:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantApi->plant_tray: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 

### Return type

[**JsonPlantByTrayIDResult**](JsonPlantByTrayIDResult.md)

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

# **plant_tray_profile**
> JsonPlantByTrayProfileIDResult plant_tray_profile(id)

Returns plants that were assigned to the tray profile defined by tray profile ID without time limit.

### Example


```python
import plantscreen
from plantscreen.models.json_plant_by_tray_profile_id_result import JsonPlantByTrayProfileIDResult
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
    api_instance = plantscreen.PlantApi(api_client)
    id = 56 # int | trayProfileID

    try:
        # Returns plants that were assigned to the tray profile defined by tray profile ID without time limit.
        api_response = api_instance.plant_tray_profile(id)
        print("The response of PlantApi->plant_tray_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantApi->plant_tray_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayProfileID | 

### Return type

[**JsonPlantByTrayProfileIDResult**](JsonPlantByTrayProfileIDResult.md)

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

# **plant_tray_profile_tray**
> JsonPlantByTrayIDAndDatesResult plant_tray_profile_tray(id, start, stop)

Returns plants that were assigned to the tray defined by tray ID between defined times. Times is entered as the start and end time of the required interval. All plants assigned to tray between these times will be returned.

### Example


```python
import plantscreen
from plantscreen.models.json_plant_by_tray_id_and_dates_result import JsonPlantByTrayIDAndDatesResult
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
    api_instance = plantscreen.PlantApi(api_client)
    id = 56 # int | trayID
    start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
    stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

    try:
        # Returns plants that were assigned to the tray defined by tray ID between defined times. Times is entered as the start and end time of the required interval. All plants assigned to tray between these times will be returned.
        api_response = api_instance.plant_tray_profile_tray(id, start, stop)
        print("The response of PlantApi->plant_tray_profile_tray:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantApi->plant_tray_profile_tray: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonPlantByTrayIDAndDatesResult**](JsonPlantByTrayIDAndDatesResult.md)

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

