# swagger_client.TrayApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scales_mapping_tray**](TrayApi.md#scales_mapping_tray) | **GET** /ScalesMapping/Tray | Returns a scales mapping for tray defined by ID.
[**tray**](TrayApi.md#tray) | **GET** /Tray | Returns one tray by tray ID.
[**tray_profile**](TrayApi.md#tray_profile) | **GET** /TrayProfile | Returns one tray profile by tray profile ID.
[**tray_profile_to_date_tray**](TrayApi.md#tray_profile_to_date_tray) | **GET** /TrayProfile/ToDate/Tray | Returns one tray profile to which tray defined by ID was assigned on the defined time.
[**tray_profile_tray**](TrayApi.md#tray_profile_tray) | **GET** /TrayProfile/Tray | Returns one tray profile to which tray defined by ID is assigned.
[**tray_profile_used_tray**](TrayApi.md#tray_profile_used_tray) | **GET** /TrayProfile/Used/Tray | Returns tray profiles to which tray defined by ID was assigned between defined times. Times is entered as the start and end time of the required interval. All tray profiles assigned to tray between these times will be returned.
[**tray_round**](TrayApi.md#tray_round) | **GET** /Tray/Round | Returns all trays measured in the round defined by ID.
[**tray_type**](TrayApi.md#tray_type) | **GET** /TrayType | Returns one tray type by tray type ID.
[**tray_type_tray**](TrayApi.md#tray_type_tray) | **GET** /TrayType/Tray | Returns one tray type which is assigned to the tray defined by ID.
[**tray_type_tray_profile**](TrayApi.md#tray_type_tray_profile) | **GET** /TrayType/TrayProfile | Returns one tray type which is assigned to the tray profile defined by ID.

# **scales_mapping_tray**
> JsonScalesMappingByTrayIDResult scales_mapping_tray(id)

Returns a scales mapping for tray defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrayApi()
id = 56 # int | trayID

try:
    # Returns a scales mapping for tray defined by ID.
    api_response = api_instance.scales_mapping_tray(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrayApi->scales_mapping_tray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 

### Return type

[**JsonScalesMappingByTrayIDResult**](JsonScalesMappingByTrayIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **tray**
> JsonTrayResult tray(id)

Returns one tray by tray ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrayApi()
id = 56 # int | trayID

try:
    # Returns one tray by tray ID.
    api_response = api_instance.tray(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrayApi->tray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 

### Return type

[**JsonTrayResult**](JsonTrayResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **tray_profile**
> JsonTrayProfileByIDResult tray_profile(id)

Returns one tray profile by tray profile ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrayApi()
id = 56 # int | profileID

try:
    # Returns one tray profile by tray profile ID.
    api_response = api_instance.tray_profile(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrayApi->tray_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| profileID | 

### Return type

[**JsonTrayProfileByIDResult**](JsonTrayProfileByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **tray_profile_to_date_tray**
> JsonTrayProfileByTrayIDToDateResult tray_profile_to_date_tray(id, _date)

Returns one tray profile to which tray defined by ID was assigned on the defined time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrayApi()
id = 56 # int | trayID
_date = '2013-10-20T19:20:30+01:00' # datetime | date

try:
    # Returns one tray profile to which tray defined by ID was assigned on the defined time.
    api_response = api_instance.tray_profile_to_date_tray(id, _date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrayApi->tray_profile_to_date_tray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 
 **_date** | **datetime**| date | 

### Return type

[**JsonTrayProfileByTrayIDToDateResult**](JsonTrayProfileByTrayIDToDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **tray_profile_tray**
> JsonTrayProfileByTrayIDResult tray_profile_tray(id)

Returns one tray profile to which tray defined by ID is assigned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrayApi()
id = 56 # int | trayID

try:
    # Returns one tray profile to which tray defined by ID is assigned.
    api_response = api_instance.tray_profile_tray(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrayApi->tray_profile_tray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 

### Return type

[**JsonTrayProfileByTrayIDResult**](JsonTrayProfileByTrayIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **tray_profile_used_tray**
> JsonUsedTrayProfileByTrayIDResult tray_profile_used_tray(id, start, stop)

Returns tray profiles to which tray defined by ID was assigned between defined times. Times is entered as the start and end time of the required interval. All tray profiles assigned to tray between these times will be returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrayApi()
id = 56 # int | trayID
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns tray profiles to which tray defined by ID was assigned between defined times. Times is entered as the start and end time of the required interval. All tray profiles assigned to tray between these times will be returned.
    api_response = api_instance.tray_profile_used_tray(id, start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrayApi->tray_profile_used_tray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonUsedTrayProfileByTrayIDResult**](JsonUsedTrayProfileByTrayIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **tray_round**
> JsonTrayByRoundIDResult tray_round(id)

Returns all trays measured in the round defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrayApi()
id = 56 # int | roundID

try:
    # Returns all trays measured in the round defined by ID.
    api_response = api_instance.tray_round(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrayApi->tray_round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonTrayByRoundIDResult**](JsonTrayByRoundIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **tray_type**
> JsonTrayTypeResult tray_type(id)

Returns one tray type by tray type ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrayApi()
id = 56 # int | typeID

try:
    # Returns one tray type by tray type ID.
    api_response = api_instance.tray_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrayApi->tray_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| typeID | 

### Return type

[**JsonTrayTypeResult**](JsonTrayTypeResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **tray_type_tray**
> JsonTrayTypeByTrayIDResult tray_type_tray(id)

Returns one tray type which is assigned to the tray defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrayApi()
id = 56 # int | trayID

try:
    # Returns one tray type which is assigned to the tray defined by ID.
    api_response = api_instance.tray_type_tray(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrayApi->tray_type_tray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 

### Return type

[**JsonTrayTypeByTrayIDResult**](JsonTrayTypeByTrayIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **tray_type_tray_profile**
> JsonTrayTypeByTrayProfileIDResult tray_type_tray_profile(id)

Returns one tray type which is assigned to the tray profile defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrayApi()
id = 56 # int | trayProfileID

try:
    # Returns one tray type which is assigned to the tray profile defined by ID.
    api_response = api_instance.tray_type_tray_profile(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrayApi->tray_type_tray_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayProfileID | 

### Return type

[**JsonTrayTypeByTrayProfileIDResult**](JsonTrayTypeByTrayProfileIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

