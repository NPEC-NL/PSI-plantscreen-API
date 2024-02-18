# swagger_client.ScalesApi

All URIs are relative to *https://localhost:44339/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scales_plant_weight**](ScalesApi.md#scales_plant_weight) | **GET** /Scales/PlantWeight | Returns scales data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
[**scales_plant_weight_measure**](ScalesApi.md#scales_plant_weight_measure) | **GET** /Scales/PlantWeight/Measure | Returns scales data by measure ID.
[**scales_weight_reference_plant**](ScalesApi.md#scales_weight_reference_plant) | **GET** /Scales/WeightReference/Plant | Returns plant weight reference data by plant ID. The weight is in units of grams
[**scales_weight_reference_to_date_tray**](ScalesApi.md#scales_weight_reference_to_date_tray) | **GET** /Scales/WeightReference/ToDate/Tray | Returns plant weight reference data by plant ID. The weight is in units of grams
[**scales_weight_reference_tray**](ScalesApi.md#scales_weight_reference_tray) | **GET** /Scales/WeightReference/Tray | Returns plant weight reference data by tray ID. The weight is in units of grams

# **scales_plant_weight**
> JsonScalesMeasureResult scales_plant_weight(device_id, round_id, tray_id)

Returns scales data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScalesApi()
device_id = 56 # int | deviceID
round_id = 56 # int | roundID
tray_id = 56 # int | trayID

try:
    # Returns scales data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    api_response = api_instance.scales_plant_weight(device_id, round_id, tray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScalesApi->scales_plant_weight: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceID | 
 **round_id** | **int**| roundID | 
 **tray_id** | **int**| trayID | 

### Return type

[**JsonScalesMeasureResult**](JsonScalesMeasureResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **scales_plant_weight_measure**
> JsonScalesMeasureByIDResult scales_plant_weight_measure(id)

Returns scales data by measure ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScalesApi()
id = 56 # int | measureID

try:
    # Returns scales data by measure ID.
    api_response = api_instance.scales_plant_weight_measure(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScalesApi->scales_plant_weight_measure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| measureID | 

### Return type

[**JsonScalesMeasureByIDResult**](JsonScalesMeasureByIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **scales_weight_reference_plant**
> JsonPlantWeightReferenceByPlantIDResult scales_weight_reference_plant(id)

Returns plant weight reference data by plant ID. The weight is in units of grams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScalesApi()
id = 56 # int | plantID

try:
    # Returns plant weight reference data by plant ID. The weight is in units of grams
    api_response = api_instance.scales_weight_reference_plant(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScalesApi->scales_weight_reference_plant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| plantID | 

### Return type

[**JsonPlantWeightReferenceByPlantIDResult**](JsonPlantWeightReferenceByPlantIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **scales_weight_reference_to_date_tray**
> JsonPlantWeightReferenceByTrayIDToDateResult scales_weight_reference_to_date_tray(id, _date)

Returns plant weight reference data by plant ID. The weight is in units of grams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScalesApi()
id = 56 # int | trayID
_date = '2013-10-20T19:20:30+01:00' # datetime | toDate

try:
    # Returns plant weight reference data by plant ID. The weight is in units of grams
    api_response = api_instance.scales_weight_reference_to_date_tray(id, _date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScalesApi->scales_weight_reference_to_date_tray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 
 **_date** | **datetime**| toDate | 

### Return type

[**JsonPlantWeightReferenceByTrayIDToDateResult**](JsonPlantWeightReferenceByTrayIDToDateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

# **scales_weight_reference_tray**
> JsonPlantWeightReferenceByTrayIDResult scales_weight_reference_tray(id)

Returns plant weight reference data by tray ID. The weight is in units of grams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScalesApi()
id = 56 # int | trayID

try:
    # Returns plant weight reference data by tray ID. The weight is in units of grams
    api_response = api_instance.scales_weight_reference_tray(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScalesApi->scales_weight_reference_tray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trayID | 

### Return type

[**JsonPlantWeightReferenceByTrayIDResult**](JsonPlantWeightReferenceByTrayIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../swagger_file.md#documentation-for-api-endpoints) [[Back to Model list]](../swagger_file.md#documentation-for-models) [[Back to README]](../swagger_file.md)

