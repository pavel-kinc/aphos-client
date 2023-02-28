# aphos_openapi.SpaceObjectApi

All URIs are relative to *http://localhost:8009*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_space_objects_by_params**](SpaceObjectApi.md#find_space_objects_by_params) | **GET** /api/spaceObject/findByParams | Finds space objects by multiple data
[**get_comparison_by_identificators**](SpaceObjectApi.md#get_comparison_by_identificators) | **GET** /api/spaceObject/comparison | Comparison object of 2 SpaceObjects
[**get_space_object_by_id**](SpaceObjectApi.md#get_space_object_by_id) | **GET** /api/spaceObject/find | Find space object by ID and catalog


# **find_space_objects_by_params**
> [SpaceObject] find_space_objects_by_params()

Finds space objects by multiple data

No additional data is mandatory, but maximum object count is 100

### Example


```python
import time
import aphos_openapi
from aphos_openapi.api import space_object_api
from aphos_openapi.model.space_object import SpaceObject
from aphos_openapi.model.error_message import ErrorMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8009
# See configuration.py for a list of all supported configuration parameters.
configuration = aphos_openapi.Configuration(
    host = "http://localhost:8009"
)


# Enter a context with an instance of the API client
with aphos_openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = space_object_api.SpaceObjectApi(api_client)
    object_id = "objectId_example" # str | Find object based on it's ID in given catalog (optional)
    catalog = "UCAC4" # str | Catalog of space object to return   Default is UCAC4 (optional)
    name = "name_example" # str | Find object by it's name (optional)
    coordinates = "coordinates_example" # str | Filter by coordinates (optional)
    min_mag = "0" # str | Find objects based on min magnitude (optional) if omitted the server will use the default value of "0"
    max_mag = "15" # str | Find objects based on max magnitude (optional) if omitted the server will use the default value of "15"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Finds space objects by multiple data
        api_response = api_instance.find_space_objects_by_params(object_id=object_id, catalog=catalog, name=name, coordinates=coordinates, min_mag=min_mag, max_mag=max_mag)
        pprint(api_response)
    except aphos_openapi.ApiException as e:
        print("Exception when calling SpaceObjectApi->find_space_objects_by_params: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Find object based on it&#39;s ID in given catalog | [optional]
 **catalog** | **str**| Catalog of space object to return   Default is UCAC4 | [optional]
 **name** | **str**| Find object by it&#39;s name | [optional]
 **coordinates** | **str**| Filter by coordinates | [optional]
 **min_mag** | **str**| Find objects based on min magnitude | [optional] if omitted the server will use the default value of "0"
 **max_mag** | **str**| Find objects based on max magnitude | [optional] if omitted the server will use the default value of "15"

### Return type

[**[SpaceObject]**](SpaceObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid values |  -  |
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comparison_by_identificators**
> ComparisonObject get_comparison_by_identificators(original_id, reference_id)

Comparison object of 2 SpaceObjects

Returns a fluxes comparison object, maximum fluxes count is 2000

### Example


```python
import time
import aphos_openapi
from aphos_openapi.api import space_object_api
from aphos_openapi.model.error_message import ErrorMessage
from aphos_openapi.model.comparison_object import ComparisonObject
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8009
# See configuration.py for a list of all supported configuration parameters.
configuration = aphos_openapi.Configuration(
    host = "http://localhost:8009"
)


# Enter a context with an instance of the API client
with aphos_openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = space_object_api.SpaceObjectApi(api_client)
    original_id = "originalId_example" # str | ID of space object to return
    reference_id = "referenceId_example" # str | ID of space object to return
    original_cat = "UCAC4" # str | Catalog of space object to return (optional)
    reference_cat = "UCAC4" # str | Catalog of space object to return (optional)

    # example passing only required values which don't have defaults set
    try:
        # Comparison object of 2 SpaceObjects
        api_response = api_instance.get_comparison_by_identificators(original_id, reference_id)
        pprint(api_response)
    except aphos_openapi.ApiException as e:
        print("Exception when calling SpaceObjectApi->get_comparison_by_identificators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Comparison object of 2 SpaceObjects
        api_response = api_instance.get_comparison_by_identificators(original_id, reference_id, original_cat=original_cat, reference_cat=reference_cat)
        pprint(api_response)
    except aphos_openapi.ApiException as e:
        print("Exception when calling SpaceObjectApi->get_comparison_by_identificators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_id** | **str**| ID of space object to return |
 **reference_id** | **str**| ID of space object to return |
 **original_cat** | **str**| Catalog of space object to return | [optional]
 **reference_cat** | **str**| Catalog of space object to return | [optional]

### Return type

[**ComparisonObject**](ComparisonObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Space object not found |  -  |
**400** | Invalid catalogs or ID supplied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_object_by_id**
> SpaceObjectWithFluxes get_space_object_by_id(space_object_id)

Find space object by ID and catalog

Returns a space object with fluxes, maximum fluxes count is 2000

### Example


```python
import time
import aphos_openapi
from aphos_openapi.api import space_object_api
from aphos_openapi.model.error_message import ErrorMessage
from aphos_openapi.model.space_object_with_fluxes import SpaceObjectWithFluxes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8009
# See configuration.py for a list of all supported configuration parameters.
configuration = aphos_openapi.Configuration(
    host = "http://localhost:8009"
)


# Enter a context with an instance of the API client
with aphos_openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = space_object_api.SpaceObjectApi(api_client)
    space_object_id = "spaceObjectId_example" # str | ID of space object to return
    catalog = "UCAC4" # str | Catalog of space object to return   Default is UCAC4 (optional)

    # example passing only required values which don't have defaults set
    try:
        # Find space object by ID and catalog
        api_response = api_instance.get_space_object_by_id(space_object_id)
        pprint(api_response)
    except aphos_openapi.ApiException as e:
        print("Exception when calling SpaceObjectApi->get_space_object_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find space object by ID and catalog
        api_response = api_instance.get_space_object_by_id(space_object_id, catalog=catalog)
        pprint(api_response)
    except aphos_openapi.ApiException as e:
        print("Exception when calling SpaceObjectApi->get_space_object_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_object_id** | **str**| ID of space object to return |
 **catalog** | **str**| Catalog of space object to return   Default is UCAC4 | [optional]

### Return type

[**SpaceObjectWithFluxes**](SpaceObjectWithFluxes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Space object not found |  -  |
**400** | Invalid catalog or ID supplied |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

