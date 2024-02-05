# swagger_client.ActionApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action**](ActionApi.md#action) | **GET** /Action | Returns one scheduled action by action ID.
[**action_experiment**](ActionApi.md#action_experiment) | **GET** /Action/Experiment | Returns all scheduled actions in the experiment defined by ID.
[**action_group**](ActionApi.md#action_group) | **GET** /Action/Group | Returns one group of scheduled actions by action group ID.
[**action_group_round**](ActionApi.md#action_group_round) | **GET** /Action/Group/Round | Returns one group of scheduled actions to which a round defined by ID belongs.
[**action_not_done_experiment**](ActionApi.md#action_not_done_experiment) | **GET** /Action/NotDone/Experiment | Returns all unfinished scheduled actions (with pending and running action state) in the experiment defined by ID.
[**action_protocol**](ActionApi.md#action_protocol) | **GET** /Action/Protocol | Returns one protocol of scheduled action by protocol ID.
[**action_protocol_round**](ActionApi.md#action_protocol_round) | **GET** /Action/Protocol/Round | Returns one group of scheduled actions that belong to round defined by ID.

# **action**
> JsonActionResult action(id)

Returns one scheduled action by action ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
id = 56 # int | actionID

try:
    # Returns one scheduled action by action ID.
    api_response = api_instance.action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| actionID | 

### Return type

[**JsonActionResult**](JsonActionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_experiment**
> JsonActionByExperimentIDResult action_experiment(id)

Returns all scheduled actions in the experiment defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
id = 56 # int | experimentID

try:
    # Returns all scheduled actions in the experiment defined by ID.
    api_response = api_instance.action_experiment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->action_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonActionByExperimentIDResult**](JsonActionByExperimentIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_group**
> JsonActionGroupResult action_group(id)

Returns one group of scheduled actions by action group ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
id = 56 # int | groupID

try:
    # Returns one group of scheduled actions by action group ID.
    api_response = api_instance.action_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->action_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| groupID | 

### Return type

[**JsonActionGroupResult**](JsonActionGroupResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_group_round**
> JsonActionGroupByRoundIDResult action_group_round(id)

Returns one group of scheduled actions to which a round defined by ID belongs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
id = 56 # int | roundID

try:
    # Returns one group of scheduled actions to which a round defined by ID belongs.
    api_response = api_instance.action_group_round(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->action_group_round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonActionGroupByRoundIDResult**](JsonActionGroupByRoundIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_not_done_experiment**
> JsonActionByExperimentIDNotDoneResult action_not_done_experiment(id)

Returns all unfinished scheduled actions (with pending and running action state) in the experiment defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
id = 56 # int | experimentID

try:
    # Returns all unfinished scheduled actions (with pending and running action state) in the experiment defined by ID.
    api_response = api_instance.action_not_done_experiment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->action_not_done_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonActionByExperimentIDNotDoneResult**](JsonActionByExperimentIDNotDoneResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_protocol**
> JsonActionProtocolResult action_protocol(id)

Returns one protocol of scheduled action by protocol ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
id = 56 # int | protocolID

try:
    # Returns one protocol of scheduled action by protocol ID.
    api_response = api_instance.action_protocol(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->action_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| protocolID | 

### Return type

[**JsonActionProtocolResult**](JsonActionProtocolResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_protocol_round**
> JsonActionProtocolByRoundIDResult action_protocol_round(id)

Returns one group of scheduled actions that belong to round defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
id = 56 # int | roundID

try:
    # Returns one group of scheduled actions that belong to round defined by ID.
    api_response = api_instance.action_protocol_round(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->action_protocol_round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonActionProtocolByRoundIDResult**](JsonActionProtocolByRoundIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

