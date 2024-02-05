# swagger_client.ProfileApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile**](ProfileApi.md#profile) | **GET** /Profile | Returns one system profile by profile ID.
[**profile_active**](ProfileApi.md#profile_active) | **GET** /Profile/Active | Returns the active system profile.
[**profile_id**](ProfileApi.md#profile_id) | **GET** /ProfileID | Returns a list of all system profile IDs in the database

# **profile**
> JsonSystemProfileResult profile(id)

Returns one system profile by profile ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProfileApi()
id = 56 # int | profileID

try:
    # Returns one system profile by profile ID.
    api_response = api_instance.profile(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| profileID | 

### Return type

[**JsonSystemProfileResult**](JsonSystemProfileResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_active**
> JsonSystemProfileActiveResult profile_active()

Returns the active system profile.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProfileApi()

try:
    # Returns the active system profile.
    api_response = api_instance.profile_active()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->profile_active: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonSystemProfileActiveResult**](JsonSystemProfileActiveResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_id**
> JsonSystemProfileIDResult profile_id()

Returns a list of all system profile IDs in the database

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProfileApi()

try:
    # Returns a list of all system profile IDs in the database
    api_response = api_instance.profile_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->profile_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonSystemProfileIDResult**](JsonSystemProfileIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

