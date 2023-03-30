"""
    APhoS

    This is Amateur Photometric Survey (APhoS) Application Programming Interface.   # noqa: E501

    The version of the OpenAPI document: 1.0.5
    Contact: pavelkinc230@gmail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import aphos_openapi
from aphos_openapi.api.flux_api import FluxApi  # noqa: E501


class TestFluxApi(unittest.TestCase):
    """FluxApi unit test stubs"""

    def setUp(self):
        self.api = FluxApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_comparison_by_identificators(self):
        """Test case for get_comparison_by_identificators

        Comparison object of 2 SpaceObjects  # noqa: E501
        """
        pass

    def test_get_space_object_by_id(self):
        """Test case for get_space_object_by_id

        Find space object by ID and catalog  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()