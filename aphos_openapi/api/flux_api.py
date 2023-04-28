"""
    APhoS

    This is Amateur Photometric Survey (APhoS) Application Programming Interface.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: pavelkinc230@gmail.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from aphos_openapi.api_client import ApiClient, Endpoint as _Endpoint
from aphos_openapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from aphos_openapi.model.comparison_object import ComparisonObject
from aphos_openapi.model.error_message import ErrorMessage
from aphos_openapi.model.space_object_with_fluxes import SpaceObjectWithFluxes


class FluxApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_comparison_by_identificators_endpoint = _Endpoint(
            settings={
                'response_type': (ComparisonObject,),
                'auth': [],
                'endpoint_path': '/api/space-objects/comparison',
                'operation_id': 'get_comparison_by_identificators',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'original_id',
                    'reference_id',
                    'original_cat',
                    'reference_cat',
                ],
                'required': [
                    'original_id',
                    'reference_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'original_cat',
                    'reference_cat',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('original_cat',): {

                        "ALL_CATALOGUES": "All catalogues",
                        "UCAC4": "UCAC4",
                        "USNO-B1.0": "USNO-B1.0"
                    },
                    ('reference_cat',): {

                        "ALL_CATALOGUES": "All catalogues",
                        "UCAC4": "UCAC4",
                        "USNO-B1.0": "USNO-B1.0"
                    },
                },
                'openapi_types': {
                    'original_id':
                        (str,),
                    'reference_id':
                        (str,),
                    'original_cat':
                        (str,),
                    'reference_cat':
                        (str,),
                },
                'attribute_map': {
                    'original_id': 'originalId',
                    'reference_id': 'referenceId',
                    'original_cat': 'originalCat',
                    'reference_cat': 'referenceCat',
                },
                'location_map': {
                    'original_id': 'query',
                    'reference_id': 'query',
                    'original_cat': 'query',
                    'reference_cat': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_space_object_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (SpaceObjectWithFluxes,),
                'auth': [],
                'endpoint_path': '/api/space-objects/search',
                'operation_id': 'get_space_object_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'space_object_id',
                    'catalog',
                ],
                'required': [
                    'space_object_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'catalog',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('catalog',): {

                        "ALL_CATALOGUES": "All catalogues",
                        "UCAC4": "UCAC4",
                        "USNO-B1.0": "USNO-B1.0"
                    },
                },
                'openapi_types': {
                    'space_object_id':
                        (str,),
                    'catalog':
                        (str,),
                },
                'attribute_map': {
                    'space_object_id': 'spaceObjectId',
                    'catalog': 'catalog',
                },
                'location_map': {
                    'space_object_id': 'query',
                    'catalog': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.upload_csv_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [],
                'endpoint_path': '/api/space-objects/upload',
                'operation_id': 'upload_csv',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'file',
                ],
                'required': [
                    'file',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file':
                        (file_type,),
                },
                'attribute_map': {
                    'file': 'file',
                },
                'location_map': {
                    'file': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )

    def get_comparison_by_identificators(
        self,
        original_id,
        reference_id,
        **kwargs
    ):
        """Comparison object of 2 SpaceObjects  # noqa: E501

        Returns a fluxes comparison object, maximum fluxes count is 2000  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_comparison_by_identificators(original_id, reference_id, async_req=True)
        >>> result = thread.get()

        Args:
            original_id (str): ID of space object to return
            reference_id (str): ID of space object to return

        Keyword Args:
            original_cat (str): Catalog of space object to return. [optional]
            reference_cat (str): Catalog of space object to return. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ComparisonObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['original_id'] = \
            original_id
        kwargs['reference_id'] = \
            reference_id
        return self.get_comparison_by_identificators_endpoint.call_with_http_info(**kwargs)

    def get_space_object_by_id(
        self,
        space_object_id,
        **kwargs
    ):
        """Find space object by ID and catalog  # noqa: E501

        Returns a space object with fluxes, maximum fluxes count is 2000  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_space_object_by_id(space_object_id, async_req=True)
        >>> result = thread.get()

        Args:
            space_object_id (str): ID of space object to return

        Keyword Args:
            catalog (str): Catalog of space object to return   Default is UCAC4. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            SpaceObjectWithFluxes
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['space_object_id'] = \
            space_object_id
        return self.get_space_object_by_id_endpoint.call_with_http_info(**kwargs)

    def upload_csv(
        self,
        file,
        **kwargs
    ):
        """Upload file  # noqa: E501

        uploads file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_csv(file, async_req=True)
        >>> result = thread.get()

        Args:
            file (file_type):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['file'] = \
            file
        return self.upload_csv_endpoint.call_with_http_info(**kwargs)

