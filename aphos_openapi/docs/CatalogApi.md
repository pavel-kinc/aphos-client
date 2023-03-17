# aphos_openapi.CatalogApi

All URIs are relative to *http://localhost:8009*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalogs**](CatalogApi.md#get_catalogs) | **GET** /api/catalog/getCatalogs | Find all catalogs


# **get_catalogs**
> [str] get_catalogs()

Find all catalogs

Returns catalogs

### Example


```python
import time
import aphos_openapi
from aphos_openapi.api import catalog_api
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
    api_instance = catalog_api.CatalogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find all catalogs
        api_response = api_instance.get_catalogs()
        pprint(api_response)
    except aphos_openapi.ApiException as e:
        print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

