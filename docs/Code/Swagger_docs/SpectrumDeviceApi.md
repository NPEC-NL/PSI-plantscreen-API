# swagger_client.SpectrumDeviceApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spectrum_device**](SpectrumDeviceApi.md#spectrum_device) | **GET** /SpectrumDevice | Returns one spectrum device by spectrum device ID.
[**spectrum_device_id**](SpectrumDeviceApi.md#spectrum_device_id) | **GET** /SpectrumDeviceID | Returns a list of all spectrum device IDs in the database.
[**spectrum_values_date_device**](SpectrumDeviceApi.md#spectrum_values_date_device) | **GET** /Spectrum/Values/Date/Device | Returns spectrum values for spectrum device defined by spectrum device ID measured between times. Times is entered as the start and end time of the required interval.

# **spectrum_device**
> JsonSpectrumDeviceResult spectrum_device(id)

Returns one spectrum device by spectrum device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpectrumDeviceApi()
id = 56 # int | spectrumDeviceID

try:
    # Returns one spectrum device by spectrum device ID.
    api_response = api_instance.spectrum_device(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpectrumDeviceApi->spectrum_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| spectrumDeviceID | 

### Return type

[**JsonSpectrumDeviceResult**](JsonSpectrumDeviceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **spectrum_device_id**
> JsonSpectrumDeviceIDResult spectrum_device_id()

Returns a list of all spectrum device IDs in the database.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpectrumDeviceApi()

try:
    # Returns a list of all spectrum device IDs in the database.
    api_response = api_instance.spectrum_device_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpectrumDeviceApi->spectrum_device_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonSpectrumDeviceIDResult**](JsonSpectrumDeviceIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **spectrum_values_date_device**
> JsonSpectrumValuesResult spectrum_values_date_device(id, start, stop)

Returns spectrum values for spectrum device defined by spectrum device ID measured between times. Times is entered as the start and end time of the required interval.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpectrumDeviceApi()
id = 56 # int | spectrumDeviceID
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns spectrum values for spectrum device defined by spectrum device ID measured between times. Times is entered as the start and end time of the required interval.
    api_response = api_instance.spectrum_values_date_device(id, start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpectrumDeviceApi->spectrum_values_date_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| spectrumDeviceID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonSpectrumValuesResult**](JsonSpectrumValuesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

