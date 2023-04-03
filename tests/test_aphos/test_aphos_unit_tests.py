import json
import math
import unittest
from unittest.mock import patch

from aphos_openapi import aphos, ApiException
from aphos_openapi.model.comparison_object import ComparisonObject
from aphos_openapi.model.user import User

_file_json = "tests/files/comparison.json"
_saturated_json = "tests/files/comparison_saturated.json"


class TestAphosUnitTests(unittest.TestCase):
    @patch('aphos_openapi.api.user_api.UserApi')
    def test_get_user_mock(self, MockApi):
        MockApi().get_user_by_username.return_value = User("ExistingUser", "Amateur")
        user = aphos.get_user("mock")
        MockApi().get_user_by_username.assert_called_once_with("mock")
        assert user.description == "Amateur"

    @patch('aphos_openapi.api.user_api.UserApi')
    def test_get_user_mock_not_found(self, MockApi):
        MockApi().get_user_by_username.side_effect = ApiException(status=404)
        assert aphos.get_user("NONEXISTENT-123") is None

    def test_set_var_cmp_apertures_magnitude_values(self):
        cmp = get_cmp(False)
        aphos.set_var_cmp_apertures(cmp, None, 4, 7)

        for data in cmp.data:
            assert data.night.ap_to_be_used == '4'
            assert data.night.cmp_ap_to_be_used == '7'
            # test for correct magnitude
            mag = -2.5 * \
                  math.log(float(data.apertures[4]) / float(data.cmp_apertures[7]), 10)
            self.assertAlmostEqual(mag, data.magnitude, delta=0.001)
            assert mag < -0.1

    def test_set_var_cmp_apertures_deviation_values(self):
        """
        Test set_var_cmp_apertures and its changes,
        tests for changes in ComparisonObject based on this function.
        """
        # testing comparison got from json
        cmp = get_cmp(False)
        for data in cmp.data:
            for i in range(3):
                # setting deviations (indexes 0-2) to 'random' values other than 0
                data.aperture_devs[i] = float(data.apertures[i]) % 400
                data.cmp_aperture_devs[i] = float(data.cmp_apertures[i]) % 400
        assert cmp.data[0].deviation == 0
        aphos.set_var_cmp_apertures(cmp, None, 0, 0)
        # deviation should not be 0
        assert cmp.data[0].deviation != 0
        # test correct values for each flux (deviation)
        for data in cmp.data:
            var_sq = (data.aperture_devs[0] / float(data.apertures[0])) ** 2
            cmp_sq = (data.cmp_aperture_devs[0] / float(data.cmp_apertures[0])) ** 2
            self.assertAlmostEqual(aphos._DEV_CONSTANT * ((var_sq + cmp_sq) ** 0.5),
                                   data.deviation, delta=0.0001)
        # set back to default
        aphos.set_var_cmp_apertures(cmp)
        assert cmp.data[2].deviation == 0

    def test_set_var_cmp_apertures_default(self):
        cmp = get_cmp(False)
        expected = get_cmp(False)
        # java sends random amount of float numbers, so cannot just ==
        aphos.set_var_cmp_apertures(expected)
        aphos.set_var_cmp_apertures(cmp, None, 2, 3)
        assert expected != cmp
        aphos.set_var_cmp_apertures(cmp)
        assert expected == cmp

    def test_set_var_cmp_apertures_saturated(self):
        cmp = get_cmp(True)
        cmp.data[0].magnitude = 0.5
        cmp.data[1].deviation = 0.1
        aphos.set_var_cmp_apertures(cmp, None, 2, 3)
        for data in cmp.data:
            assert data.magnitude == float('-inf')
            assert data.deviation is None

    @patch('aphos_openapi.api.space_object_api.SpaceObjectApi')
    def test_upload_files(self, MockApi):
        # only one file
        MockApi().upload_csv.return_value = "Files uploaded"
        res = aphos._upload_files("tests/files/csv_tests/test1.csv")
        assert res == [("tests/files/csv_tests/test1.csv", True, "Files uploaded")]


def get_cmp(saturated) -> ComparisonObject:
    base = _file_json
    if saturated:
        base = _saturated_json
    with open(base, 'r') as file:
        json_dict = json.load(file)
    return ComparisonObject(**json_dict)
