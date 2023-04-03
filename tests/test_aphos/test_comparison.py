import datetime
import json
import math
import unittest

from aphos_openapi import aphos
from aphos_openapi.model.comparison_object import ComparisonObject

_file_json = "tests/files/comparison.json"
_saturated_json = "tests/files/comparison_saturated.json"


class TestComparison(unittest.TestCase):
    def test_comparison_fields(self):
        cmp = get_cmp(False)
        for data in cmp.data:
            mag = -2.5 * \
                  math.log(float(data.ap_auto) / float(data.cmp_ap_auto), 10)
            self.assertAlmostEqual(mag, data.magnitude, delta=0.001)
            assert data.night.ap_to_be_used == "auto"
            assert data.night.cmp_ap_to_be_used == "auto"

        for data in cmp.data:
            var_sq = (data.ap_auto_dev / float(data.ap_auto)) ** 2
            cmp_sq = (data.cmp_ap_auto_dev / float(data.cmp_ap_auto)) ** 2

            self.assertAlmostEqual(aphos._DEV_CONSTANT * ((var_sq + cmp_sq) ** 0.5),
                                   data.deviation, delta=0.0001)

    def test_comparison_saturated_values(self):
        cmp = get_cmp(True)
        for data in cmp.data:
            assert data.magnitude == float('-inf')
            assert data.deviation is None

    def test_comparison_date_formats(self):
        cmp = get_cmp(False)
        for data in cmp.data:
            try:
                datetime.datetime.strptime(data.night.first_date_of_the_night, '%d-%m-%Y')
            except ValueError:
                self.fail("Date should be in format DD-MM-YYYY")
            try:
                datetime.datetime.fromisoformat(data.exp_middle)
            except ValueError:
                self.fail("Date should be in iso format")


def get_cmp(saturated) -> ComparisonObject:
    base = _file_json
    if saturated:
        base = _saturated_json
    with open(base, 'r') as file:
        json_dict = json.load(file)
    return ComparisonObject(**json_dict)