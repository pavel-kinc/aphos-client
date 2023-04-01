import unittest
import pickle

from aphos_openapi.model.comparison_object import ComparisonObject
from aphos_openapi import aphos
from pprint import pprint


class TestGraphData(unittest.TestCase):
    _file_name = "comparison.pickle"

    # File comparison.pkl was created like this
    # cmp = aphos.get_var_cmp_by_ids("605-025126", "604-024943", "UCAC4", "UCAC4")
    # with open(self._file_name, 'wb') as file:
    #    pickle.dump(cmp, file)

    #def test_graph_data(self):
    #    cmp = aphos.get_var_cmp_by_ids("605-025126", "604-024943", "UCAC4", "UCAC4")
    #    star = cmp.data
    #    with open(self._file_name, 'wb') as file:
    #        pickle.dump(star, file)
    #    with open(self._file_name, 'rb') as file:
    #        res = pickle.load(file)
    #    pprint(res)
