# aphos_openapi.UserApi

All URIs are relative to *http://localhost:8009*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logged_user**](UserApi.md#get_logged_user) | **GET** /api/user/current | Get current logged-in user for session
[**get_user_by_username**](UserApi.md#get_user_by_username) | **GET** /api/user/{name} | Find user by username


# **get_logged_user**
> User get_logged_user()

Get current logged-in user for session

Returns a user or null

### Example


```python
import time
import aphos_openapi
from aphos_openapi.api import user_api
from aphos_openapi.model.error_message import ErrorMessage
from aphos_openapi.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8009
# See configuration.py for a list of all supported configuration parameters.
configuration = aphos_openapi.Configuration(
    host = "http://localhost:8009"
)


# Enter a context with an instance of the API client
with aphos_openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current logged-in user for session
        api_response = api_instance.get_logged_user()
        pprint(api_response)
    except aphos_openapi.ApiException as e:
        print("Exception when calling UserApi->get_logged_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_username**
> User get_user_by_username(name)

Find user by username

Returns a user

### Example


```python
import time
import aphos_openapi
from aphos_openapi.api import user_api
from aphos_openapi.model.error_message import ErrorMessage
from aphos_openapi.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8009
# See configuration.py for a list of all supported configuration parameters.
configuration = aphos_openapi.Configuration(
    host = "http://localhost:8009"
)


# Enter a context with an instance of the API client
with aphos_openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    name = "name_example" # str | Find user by username

    # example passing only required values which don't have defaults set
    try:
        # Find user by username
        api_response = api_instance.get_user_by_username(name)
        pprint(api_response)
    except aphos_openapi.ApiException as e:
        print("Exception when calling UserApi->get_user_by_username: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Find user by username |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid username supplied |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

