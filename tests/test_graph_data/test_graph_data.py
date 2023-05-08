import os
import unittest
import json

from matplotlib.testing.compare import calculate_rms, compare_images
from matplotlib.testing.decorators import image_comparison

from aphos_openapi.model.comparison_object import ComparisonObject
from aphos_openapi import aphos
from pprint import pprint
import matplotlib.pyplot as plt  # type: ignore

from aphos_openapi.model.space_object import SpaceObject
from aphos_openapi.models.graph_data import GraphData


class TestGraphData(unittest.TestCase):
    _file_json = "tests/files/comparison.json"
    _csv_mock = "tests/files/test_data.csv"
    _csv_users = "tests/files/graph_data.csv"
    _path_new = "tests/files/to_create.csv"
    _JD_DATE_BASE = 2400000

    # cmp = aphos.get_var_cmp_by_ids("805-031770", "781-038863", "UCAC4", "UCAC4")
    # json_dict = cmp._data_store
    # # normally there would be key.__dict__ but generated objects have interesting structure
    # comparison_json = json.dumps(json_dict, default=lambda key: key._data_store)
    # with open(self._file_json, "w") as file:
    #    file.write(comparison_json)

    def test_graph_data_from_comparison_json(self):
        """
        Load json with comparison and basic tests.
        (create graphdata from saved comparison)
        """
        with open(self._file_json, 'r') as file:
            json_dict = json.load(file)
        cmp = ComparisonObject(**json_dict)
        assert type(cmp) == ComparisonObject
        assert type(cmp.variable) == SpaceObject
        assert cmp.variable.id == "805-031770"
        graph_data = GraphData(cmp)
        assert graph_data.comparison == "781-038863"

    def test_graph_data_from_file(self):
        graph_data = GraphData(self._csv_mock)
        assert graph_data.variable == "605-025126"
        assert graph_data.comparison == "604-024943"
        assert graph_data.var_catalog == "UCAC4"
        assert graph_data.cmp_catalog == "UCAC4"
        assert len(graph_data.data_list) > 500

        dmdu = graph_data.data_list[0]
        assert dmdu.date > self._JD_DATE_BASE
        assert 1.4 < dmdu.magnitude < 1.8
        assert 0 <= dmdu.deviation <= 0.1
        assert dmdu.user == "xkrutak"

    def test_graph_pick_users_from_file(self):
        users = ["pepa8", "pavel"]
        rest_of_users = ["xkrutak", "12345"]

        graph_data = GraphData(self._csv_users, users)
        for data in graph_data.data_list:
            assert data.user in users

        graph_data = GraphData(self._csv_users, users, exclude=True)
        for data in graph_data.data_list:
            assert data.user in rest_of_users

    def test_graph_pick_users_from_comparison(self):
        users = ["pepa8", "pavel"]
        rest_of_users = ["xkrutak", "12345"]

        with open(self._file_json, 'r') as file:
            json_dict = json.load(file)
        graph_data = GraphData(ComparisonObject(**json_dict), users)

        for data in graph_data.data_list:
            assert data.user in users

        with open(self._file_json, 'r') as file:
            json_dict = json.load(file)
        graph_data = GraphData(ComparisonObject(**json_dict), users, exclude=True)

        for data in graph_data.data_list:
            assert data.user in rest_of_users

    def test_graph_data_to_file(self):
        with open(self._file_json, 'r') as file:
            json_dict = json.load(file)
        graph_data = GraphData(ComparisonObject(**json_dict))
        graph_data.to_file(self._path_new)
        graph_data2 = GraphData(self._path_new)

        assert str(graph_data) == str(graph_data2)

        if os.path.exists(self._path_new):
            os.remove(self._path_new)

    def test_graph_data_graph_fig(self):
        with open(self._file_json, 'r') as file:
            json_dict = json.load(file)
        graph_data = GraphData(ComparisonObject(**json_dict))

        graph_data._create_graph()
        actual = "tests/files/actual_fig.png"
        plt.savefig(actual)
        s = compare_images("tests/files/fig.png", actual, 0.001)
        if os.path.exists(actual):
            os.remove(actual)

        # compare_images returns None, if equal
        assert s is None
        #plt.show()

    def test_graph_data_graph_axes(self):
        with open(self._file_json, 'r') as file:
            json_dict = json.load(file)
        graph_data = GraphData(ComparisonObject(**json_dict))
        values = dict()
        for d, m, _, _ in graph_data.data_list:
            values[d] = m

        plts, _ = graph_data._create_graph()
        #plt.show
        # 4 users in legend
        assert len(plts) == 4

        for plot in plts:
            # data for users
            x = plot.get_xdata()
            y = plot.get_ydata()
            # go through data and test if they match
            for i in range(len(x)):
                assert values[x[i]] == y[i]

    def test_graph_data_other_graphs(self):
        graph_data = GraphData(self._csv_users)
        try:
            graph_data._create_composite_graph()
            graph_data._create_phase_graph(2459800.5, 1.2)
        except:
            self.fail("Creating graphs should not result in exception")
