import os
import unittest
import json


from aphos_openapi.model.comparison_object import ComparisonObject
from aphos_openapi import aphos
from pprint import pprint


class TestGraphData(unittest.TestCase):
    _file_name = "comparison.json"
    #_file_name = "HALO.txt"

    # File comparison.pkl was created like this
    # cmp = aphos.get_var_cmp_by_ids("605-025126", "604-024943", "UCAC4", "UCAC4")
    # with open(self._file_name, 'wb') as file:
    #    pickle.dump(cmp, file)

    #def test_graph_data(self):
        #cmp = aphos.get_var_cmp_by_ids("605-025126", "604-024943", "UCAC4", "UCAC4")
        #json_dict = cmp._data_store
        #js = json.loads(json_dict)
        #print(type(js))
        #comparison_json = json.dumps(json_dict, default=lambda key: key.__dict__)
        #print(type(comparison_json))
        #with open(self._file_name, "w") as file:
        #    #file.write(json.dumps(str(json_dict)))
        #    file.write(str(json_dict))
        #with open(self._file_name, 'r') as file:
        #    random_dict = json.load(file)
            #random_dict = file.read()


        #print(type(random_dict))
        #print(dict(random_dict))
        #cmp2 = ComparisonObject(**json_dict)
        #print(cmp2.variable)
        #pprint(json_str)
        #pprint(dict(cmp._data_store))

    def test_graph_data_json(self):
        #cmp = aphos.get_var_cmp_by_ids("805-031770", "781-038863", "UCAC4", "UCAC4")
        #json_dict = cmp._data_store
        #js = json.loads(json_dict)
        #print(type(js))
        # normally there would be key.__dict__ but generated objects have interesting structure
        #print(type(json_dict["variable"]))
        #comparison_json = json.dumps(json_dict, default=lambda key: key._data_store)

        #print(type(comparison_json))
        #with open(self._file_name, "w") as file:
        #    file.write(comparison_json)
        with open(self._file_name, 'r') as file:
            random_dict = json.load(file)
        #print(type(random_dict))
        cmp2 = ComparisonObject(**random_dict)
        assert type(cmp2) == ComparisonObject
        #print(cmp2)

