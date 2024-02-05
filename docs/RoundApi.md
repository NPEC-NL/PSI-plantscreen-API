# plantscreen.swagger_client.RoundApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**round**](RoundApi.md#round) | **GET** /Round | Returns one round by round ID.
[**round_date_experiment**](RoundApi.md#round_date_experiment) | **GET** /Round/Date/Experiment | Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.
[**round_experiment**](RoundApi.md#round_experiment) | **GET** /Round/Experiment | Returns all rounds measured in the experiment defined by ID.
[**round_order_date_experiment**](RoundApi.md#round_order_date_experiment) | **GET** /RoundOrder/Date/Experiment | Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.
[**round_order_experiment**](RoundApi.md#round_order_experiment) | **GET** /RoundOrder/Experiment | Returns all rounds measured in the experiment defined by ID.
[**round_order_round**](RoundApi.md#round_order_round) | **GET** /RoundOrder/Round | Returns the round order in the experiment by round ID.

# **round**
> JsonRoundResult round(id)

Returns one round by round ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.RoundApi()
id = 56 # int | roundID

try:
    # Returns one round by round ID.
    api_response = api_instance.round(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoundApi->round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonRoundResult**](JsonRoundResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **round_date_experiment**
> JsonRoundByExperimentIDAndDateResult round_date_experiment(id, start, stop)

Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.RoundApi()
id = 56 # int | experimentID
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.
    api_response = api_instance.round_date_experiment(id, start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoundApi->round_date_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonRoundByExperimentIDAndDateResult**](JsonRoundByExperimentIDAndDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **round_experiment**
> JsonRoundByExperimentIDResult round_experiment(id)

Returns all rounds measured in the experiment defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.RoundApi()
id = 56 # int | experimentID

try:
    # Returns all rounds measured in the experiment defined by ID.
    api_response = api_instance.round_experiment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoundApi->round_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonRoundByExperimentIDResult**](JsonRoundByExperimentIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **round_order_date_experiment**
> JsonRoundOrderByExperimentIDAndDateResult round_order_date_experiment(id, start, stop)

Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.RoundApi()
id = 56 # int | experimentID
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns all rounds measured in the experiment defined by ID between defined times. Times is entered as the start and end time of the required interval.
    api_response = api_instance.round_order_date_experiment(id, start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoundApi->round_order_date_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonRoundOrderByExperimentIDAndDateResult**](JsonRoundOrderByExperimentIDAndDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **round_order_experiment**
> JsonRoundOrderByExperimentIDResult round_order_experiment(id)

Returns all rounds measured in the experiment defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.RoundApi()
id = 56 # int | experimentID

try:
    # Returns all rounds measured in the experiment defined by ID.
    api_response = api_instance.round_order_experiment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoundApi->round_order_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonRoundOrderByExperimentIDResult**](JsonRoundOrderByExperimentIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **round_order_round**
> JsonRoundOrderResult round_order_round(id)

Returns the round order in the experiment by round ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = plantscreen.swagger_client.RoundApi()
id = 56 # int | roundID

try:
    # Returns the round order in the experiment by round ID.
    api_response = api_instance.round_order_round(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoundApi->round_order_round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| roundID | 

### Return type

[**JsonRoundOrderResult**](JsonRoundOrderResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

