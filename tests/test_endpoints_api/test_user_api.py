"""
    APhoS

    This is Amateur Photometric Survey (APhoS) Application Programming Interface.   # noqa: E501

    The version of the OpenAPI document: 1.0.5
    Contact: pavelkinc230@gmail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

from aphos_openapi.api.user_api import UserApi  # noqa: E501
from aphos_openapi.model.user import User


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs
    basic testing of endpoints"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        del self.api

    def test_get_user_by_username(self):
        """Test case for get_user_by_username

        Find user by username  # noqa: E501
        """
        user = self.api.get_user_by_username("Pavel")
        assert type(user) == User
        assert "developer" in user.description.lower()


if __name__ == '__main__':
    unittest.main()
