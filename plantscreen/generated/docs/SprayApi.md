# plantscreen.SprayApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spray_action**](SprayApi.md#spray_action) | **GET** /Spray/Action | Return spray action data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.


# **spray_action**
> JsonSprayActionResult spray_action(device_id, round_id, tray_id)

Return spray action data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example


```python
import plantscreen
from plantscreen.models.json_spray_action_result import JsonSprayActionResult
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
    api_instance = plantscreen.SprayApi(api_client)
    device_id = 56 # int | deviceID
    round_id = 56 # int | roundID
    tray_id = 56 # int | trayID

    try:
        # Return spray action data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
        api_response = api_instance.spray_action(device_id, round_id, tray_id)
        print("The response of SprayApi->spray_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SprayApi->spray_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonSprayActionResult**](JsonSprayActionResult.md)

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

