"""
    APhoS

    This is Amateur Photometric Survey (APhoS) Application Programming Interface.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: pavelkinc230@gmail.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from aphos_openapi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from aphos_openapi.exceptions import ApiAttributeError


def lazy_import():
    from aphos_openapi.model.night import Night
    globals()['Night'] = Night


class FluxData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'right_asc': (str,),  # noqa: E501
            'dec': (str,),  # noqa: E501
            'ap_auto': (str,),  # noqa: E501
            'ap_auto_dev': (float,),  # noqa: E501
            'apertures': ([str],),  # noqa: E501
            'aperture_devs': ([float],),  # noqa: E501
            'magnitude': (float,),  # noqa: E501
            'deviation': (float,),  # noqa: E501
            'username': (str,),  # noqa: E501
            'night': (Night,),  # noqa: E501
            'exp_middle': (str,),  # noqa: E501
            'cmp_ap_auto': (str,),  # noqa: E501
            'cmp_ap_auto_dev': (float,),  # noqa: E501
            'cmp_apertures': ([str],),  # noqa: E501
            'cmp_aperture_devs': ([float],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'right_asc': 'rightAsc',  # noqa: E501
        'dec': 'dec',  # noqa: E501
        'ap_auto': 'apAuto',  # noqa: E501
        'ap_auto_dev': 'apAutoDev',  # noqa: E501
        'apertures': 'apertures',  # noqa: E501
        'aperture_devs': 'apertureDevs',  # noqa: E501
        'magnitude': 'magnitude',  # noqa: E501
        'deviation': 'deviation',  # noqa: E501
        'username': 'username',  # noqa: E501
        'night': 'night',  # noqa: E501
        'exp_middle': 'expMiddle',  # noqa: E501
        'cmp_ap_auto': 'cmpApAuto',  # noqa: E501
        'cmp_ap_auto_dev': 'cmpApAutoDev',  # noqa: E501
        'cmp_apertures': 'cmpApertures',  # noqa: E501
        'cmp_aperture_devs': 'cmpApertureDevs',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, right_asc, dec, ap_auto, ap_auto_dev, apertures, aperture_devs, magnitude, deviation, username, night, exp_middle, cmp_ap_auto, cmp_ap_auto_dev, cmp_apertures, cmp_aperture_devs, *args, **kwargs):  # noqa: E501
        """FluxData - a model defined in OpenAPI

        Args:
            right_asc (str):
            dec (str):
            ap_auto (str):
            ap_auto_dev (float):
            apertures ([str]):
            aperture_devs ([float]):
            magnitude (float):
            deviation (float):
            username (str):
            night (Night):
            exp_middle (str):
            cmp_ap_auto (str):
            cmp_ap_auto_dev (float):
            cmp_apertures ([str]):
            cmp_aperture_devs ([float]):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.right_asc = right_asc
        self.dec = dec
        self.ap_auto = ap_auto
        self.ap_auto_dev = ap_auto_dev
        self.apertures = apertures
        self.aperture_devs = aperture_devs
        self.magnitude = magnitude
        self.deviation = deviation
        self.username = username
        self.night = night
        self.exp_middle = exp_middle
        self.cmp_ap_auto = cmp_ap_auto
        self.cmp_ap_auto_dev = cmp_ap_auto_dev
        self.cmp_apertures = cmp_apertures
        self.cmp_aperture_devs = cmp_aperture_devs
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, right_asc, dec, ap_auto, ap_auto_dev, apertures, aperture_devs, magnitude, deviation, username, night, exp_middle, cmp_ap_auto, cmp_ap_auto_dev, cmp_apertures, cmp_aperture_devs, *args, **kwargs):  # noqa: E501
        """FluxData - a model defined in OpenAPI

        Args:
            right_asc (str):
            dec (str):
            ap_auto (str):
            ap_auto_dev (float):
            apertures ([str]):
            aperture_devs ([float]):
            magnitude (float):
            deviation (float):
            username (str):
            night (Night):
            exp_middle (str):
            cmp_ap_auto (str):
            cmp_ap_auto_dev (float):
            cmp_apertures ([str]):
            cmp_aperture_devs ([float]):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.right_asc = right_asc
        self.dec = dec
        self.ap_auto = ap_auto
        self.ap_auto_dev = ap_auto_dev
        self.apertures = apertures
        self.aperture_devs = aperture_devs
        self.magnitude = magnitude
        self.deviation = deviation
        self.username = username
        self.night = night
        self.exp_middle = exp_middle
        self.cmp_ap_auto = cmp_ap_auto
        self.cmp_ap_auto_dev = cmp_ap_auto_dev
        self.cmp_apertures = cmp_apertures
        self.cmp_aperture_devs = cmp_aperture_devs
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
