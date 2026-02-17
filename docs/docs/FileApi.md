# plantscreen.FileApi

All URIs are relative to *https://localhost:44339*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file**](FileApi.md#file) | **GET** /file | Returns the streamed file located in the data file storage by defined path.
[**file_changelog**](FileApi.md#file_changelog) | **GET** /file/Changelog | Returns the changelog as a streamed text file. The changelog is a record of all notable changes made in individual versions of the API.


# **file**
> file(path)

Returns the streamed file located in the data file storage by defined path.

### Example


```python
import plantscreen
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
    api_instance = plantscreen.FileApi(api_client)
    path = 'path_example' # str | fileStoragePath

    try:
        # Returns the streamed file located in the data file storage by defined path.
        api_instance.file(path)
    except Exception as e:
        print("Exception when calling FileApi->file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| fileStoragePath | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_changelog**
> str file_changelog()

Returns the changelog as a streamed text file. The changelog is a record of all notable changes made in individual versions of the API.

### Example


```python
import plantscreen
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
    api_instance = plantscreen.FileApi(api_client)

    try:
        # Returns the changelog as a streamed text file. The changelog is a record of all notable changes made in individual versions of the API.
        api_response = api_instance.file_changelog()
        print("The response of FileApi->file_changelog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->file_changelog: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

