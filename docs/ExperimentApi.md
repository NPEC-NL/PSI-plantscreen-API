# swagger_client.ExperimentApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiment**](ExperimentApi.md#experiment) | **GET** /Experiment | Returns one experiment by experiment ID.
[**experiment_date**](ExperimentApi.md#experiment_date) | **GET** /Experiment/Date | Returns all experiments whose rounds took place between defined times. Times is entered as the start and end time of the required interval. All experiments with at least one round between these times will be returned.
[**experiment_id**](ExperimentApi.md#experiment_id) | **GET** /ExperimentID | Returns a list of all experiment IDs in the database.
[**experiment_owner**](ExperimentApi.md#experiment_owner) | **GET** /Experiment/Owner | Returns all experiments that belong to the user defined by ID.
[**note_experiment**](ExperimentApi.md#note_experiment) | **GET** /Note/Experiment | Returns the experiment notes that the user saved for the experiment defined by ID.
[**owner**](ExperimentApi.md#owner) | **GET** /Owner | Returns the owner(s) of the experiment by ID.
[**owner_id**](ExperimentApi.md#owner_id) | **GET** /OwnerID | Returns a list of all experiment owner IDs in the database.

# **experiment**
> JsonExperimentResult experiment(id)

Returns one experiment by experiment ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExperimentApi()
id = 56 # int | experimentID

try:
    # Returns one experiment by experiment ID.
    api_response = api_instance.experiment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonExperimentResult**](JsonExperimentResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_date**
> JsonExperimentByDateResult experiment_date(start, stop)

Returns all experiments whose rounds took place between defined times. Times is entered as the start and end time of the required interval. All experiments with at least one round between these times will be returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExperimentApi()
start = '2013-10-20T19:20:30+01:00' # datetime | dateStart
stop = '2013-10-20T19:20:30+01:00' # datetime | dateStop

try:
    # Returns all experiments whose rounds took place between defined times. Times is entered as the start and end time of the required interval. All experiments with at least one round between these times will be returned.
    api_response = api_instance.experiment_date(start, stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| dateStart | 
 **stop** | **datetime**| dateStop | 

### Return type

[**JsonExperimentByDateResult**](JsonExperimentByDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_id**
> JsonExperimentIDResult experiment_id()

Returns a list of all experiment IDs in the database.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExperimentApi()

try:
    # Returns a list of all experiment IDs in the database.
    api_response = api_instance.experiment_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonExperimentIDResult**](JsonExperimentIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_owner**
> JsonExperimentByOwnerResult experiment_owner(id)

Returns all experiments that belong to the user defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExperimentApi()
id = 56 # int | ownerID

try:
    # Returns all experiments that belong to the user defined by ID.
    api_response = api_instance.experiment_owner(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ownerID | 

### Return type

[**JsonExperimentByOwnerResult**](JsonExperimentByOwnerResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_experiment**
> JsonNoteResult note_experiment(id)

Returns the experiment notes that the user saved for the experiment defined by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExperimentApi()
id = 56 # int | experimentID

try:
    # Returns the experiment notes that the user saved for the experiment defined by ID.
    api_response = api_instance.note_experiment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->note_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| experimentID | 

### Return type

[**JsonNoteResult**](JsonNoteResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **owner**
> JsonOwnerResult owner(ids)

Returns the owner(s) of the experiment by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExperimentApi()
ids = [56] # list[int] | ownerIDs TODO is this multiple?

try:
    # Returns the owner(s) of the experiment by ID.
    api_response = api_instance.owner(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| ownerIDs TODO is this multiple? | 

### Return type

[**JsonOwnerResult**](JsonOwnerResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **owner_id**
> JsonOwnerIDResult owner_id()

Returns a list of all experiment owner IDs in the database.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExperimentApi()

try:
    # Returns a list of all experiment owner IDs in the database.
    api_response = api_instance.owner_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->owner_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonOwnerIDResult**](JsonOwnerIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

