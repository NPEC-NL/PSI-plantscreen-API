# plantscreen.swagger_client.SprayApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_spray_action**](SprayApi.md#get_spray_action) | **GET** /Spray/Action | Return spray action data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

# **get_spray_action**
> JsonSprayActionResult get_spray_action(device_id, round_id, tray_id)

Return spray action data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.SprayApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Return spray action data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.get_spray_action(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SprayApi->get_spray_action: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

