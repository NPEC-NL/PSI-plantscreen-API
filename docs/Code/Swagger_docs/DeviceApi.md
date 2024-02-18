# swagger_client.DeviceApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device**](DeviceApi.md#device) | **GET** /Device | Returns one device by device ID.
[**device_active**](DeviceApi.md#device_active) | **GET** /Device/Active | Returns all active devices that have not ended validity.
[**device_profile**](DeviceApi.md#device_profile) | **GET** /Device/Profile | Returns all devices that contains the system profile defined by ID.

# **device**
> JsonDeviceResult device(id)

Returns one device by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()
id = 56 # int | deviceID

try:
    # Returns one device by device ID.
    api_response = api_instance.device(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| deviceID | 

### Return type

[**JsonDeviceResult**](JsonDeviceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **device_active**
> JsonDeviceActiveResult device_active()

Returns all active devices that have not ended validity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()

try:
    # Returns all active devices that have not ended validity.
    api_response = api_instance.device_active()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_active: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonDeviceActiveResult**](JsonDeviceActiveResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **device_profile**
> JsonDeviceByProfileIDResult device_profile(id)

Returns all devices that contains the system profile defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()
id = 56 # int | profileID

try:
    # Returns all devices that contains the system profile defined by ID.
    api_response = api_instance.device_profile(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| profileID | 

### Return type

[**JsonDeviceByProfileIDResult**](JsonDeviceByProfileIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

