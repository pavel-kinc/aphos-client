import math
import sys
import unittest
import io

from aphos_openapi import aphos
from aphos_openapi.model.space_object import SpaceObject
from aphos_openapi.models.coordinates import Coordinates


class TestAphosModule(unittest.TestCase):
    _STAR_IDS = ["605-025126", "604-024943", "805-031770", "781-038863"]
    _CATALOG = "UCAC4"

    def test_get_catalogs(self):
        catalogs = aphos.get_catalogs()
        assert len(catalogs) > 2
        assert "UCAC4" in catalogs

    def test_get_object(self):
        object = aphos.get_object(self._STAR_IDS[0])
        same_object = aphos.get_object(self._STAR_IDS[0], "UCAC4")
        assert object == same_object

        assert aphos.get_object("NONEXISTENT-123") is None
        assert aphos.get_object(self._STAR_IDS[0], "NONEXISTENTCAT-987") is None

    def test_get_objects_by_params(self):
        stars = aphos.get_objects_by_params()
        assert len(stars) >= 100
        stars = aphos.get_objects_by_params(
            coordinates=Coordinates("21h41m55.291s +71d18m41.12s", 7, 'h', 'm'), catalog="UCAC4")
        assert len(stars) >= 3
        stars = aphos.get_objects_by_params(name="GK Cep", catalog="UCAC4")
        assert len(stars) == 1

    def test_get_objects_by_params_expected(self):
        stars = aphos.get_objects_by_params(object_id=self._STAR_IDS[0], catalog="UCAC4")
        assert len(stars) == 1
        stars[0].fluxes_count = 0
        expected = SpaceObject(id='605-025126', declination='+30°57\'03.59"',
                               right_asc='05h48m24.012s', name='', catalog='UCAC4',
                               magnitude=13.71, fluxes_count=0)
        assert expected == stars[0]

    def test_get_var_cmp_by_ids(self):
        var_cmp = aphos.get_var_cmp_by_ids(self._STAR_IDS[2], self._STAR_IDS[3])
        i = 0
        broke = False
        while i < len(var_cmp.data):
            if len(var_cmp.data[i].apertures[0]) > 1:
                broke = True
                break
            i += 1
        assert broke is True

    def test_get_var_cmp_by_ids_fields(self):
        var_cmp = aphos.get_var_cmp_by_ids(self._STAR_IDS[2], self._STAR_IDS[3])
        assert var_cmp.data[0].night.ap_to_be_used == "auto"
        assert var_cmp.data[0].night.cmp_ap_to_be_used == "auto"
        assert var_cmp.comparison.id == self._STAR_IDS[3]
        if var_cmp.data[0].magnitude > -50:
            var = var_cmp.data[0].ap_auto
            cmp = var_cmp.data[0].cmp_ap_auto
            res_mag = -2.5 * math.log(float(var) / float(cmp), 10)
            self.assertAlmostEqual(res_mag, var_cmp.data[0].magnitude, delta=0.001)

    def test_get_user(self):
        user = aphos.get_user("Pavel")
        if user is not None:
            assert user.description.lower().startswith("dev")

    def test_get_user_not_found(self):
        user = aphos.get_user("NonExistentUser987123")
        assert user is None

    def test_resolve_name_aphos(self):
        # uses aphos.get_objects_by_params() with coordinates

        assert len(aphos.resolve_name_aphos("2MASS J05482401+3057036")) >= 1
        assert len(aphos.resolve_name_aphos("UCAC4 605-025126")) >= 1

    def test_resolve_name_aphos_specific(self):
        """
        Test if aphos correctly sends back star with id and catalog
        (uses aphos.get_objects_by_params() with coordinates)
        """
        id = "605-025126"
        catalog = "UCAC4"
        assert stars_found("GSC 02405-01886", id, catalog)
        assert stars_found("2MASS J05482401+3057036", id, catalog)
        assert stars_found("UCAC4 605-025126", id, catalog)
        assert stars_found("Gaia DR2 3444802885109154944", id, catalog)

    def test_resolve_name_aphos_star_does_not_exist(self):
        stars_aphos = aphos.resolve_name_aphos("Random string - 416462")
        assert stars_aphos is None

    def test_upload_files_fail_directory(self):
        res = aphos._upload_files("tests/files/csv_only_incorrect")
        for fail in res:
            # filename has incorrect in it
            assert "incorrect" in fail[0]
            # if the upload was success
            assert not fail[1]
            assert fail[2] == "400"

    def test_upload_files_fail_file(self):
        res = aphos._upload_files("tests/files/csv_only_incorrect/test1_incorrect.csv")
        assert len(res) == 1
        fail = res[0]
        assert "incorrect" in fail[0]
        assert not fail[1]
        assert fail[2] == "400"

    def test_info(self):
        capture_stdout = io.StringIO()
        sys.stdout = capture_stdout
        aphos.info()
        sys.stdout = sys.__stdout__
        value = capture_stdout.getvalue().lower()
        assert "version" in value
        assert "help" in value
        assert "https://" in value


def stars_found(star_name: str, expected_id: str, expected_cat: str) -> bool:
    """
    Function for trying to find star in APhoS.

    Args:
        star_name: name of star/space object to search
        expected_id: expected id of aphos spaceobject
        expected_cat: expected catalog of aphos spaceobject

    Returns: True if searched star is in final list of possible stars in APhoS

    """
    stars_aphos = aphos.resolve_name_aphos(star_name)
    if stars_aphos is not None:
        for star in stars_aphos:
            if star.id == expected_id and star.catalog == expected_cat:
                return True
    return False

# o = get_object("604-024943")
# o.id
# print(o)
# print(type(o))
# k=get_object("604-024734")
# k = get_var_cmp_by_ids("805-031770", "781-038863")  # not saturated
# date = aphos_openapi.datetime.date(2021,11, 6)
# set_var_cmp_apertures(k, date, 5, 5)
# pprint(k)

# info()
# l = get_var_cmp_by_ids("805-031770", "807-030174")  # saturated
# set_var_cmp_apertures(l, aphos_openapi.datetime.date(2021,11, 6),5,6)
# pprint(l)
# set_var_cmp_apertures(l, aphos_openapi.datetime.date(2021,11, 6))
# print(l)
# g = GraphData(l,users=["xkrutak"], exclude=True,saturated=True)
# g.graph()
# print(g)
# pprint(l)
# date = aphos_openapi.datetime.date(2021,11, 6)
# set_var_cmp_apertures(l, date, 9, 9)
# pprint(l)
# pprint(c)
# c = Coordinates(right_asc="21:41:55.291", declination="71:18:41.12", radius=0.05)
# pprint(c)

# coords = Coordinates("21h41m55.291s +71d18m41.12s", 10, 'h', 'm')
# print(coords)
# c=get_objects_by_params(coordinates=coords)
# pprint(c)

# k = get_var_cmp_by_ids("605-025126", "604-024943", "UCAC4", "UCAC4")  # not saturated
# print(k)
# VarCmp getvarcmpbyids
# VAR vs CMP (orig vs ref)
# pprint(k)
# date = aphos_openapi.datetime.date(2022,3, 22)
# set_var_cmp_apertures(k, date, 0, 9)
# pprint(k)
# incorect = get_object("sdfsdf")
# print(k)
# k = GraphData(k, users=["xkrutak"], exclude=False, saturated=False)
# k.graph()
# k.composite_graph()
# k.phase_graph(2455957.5, 1.209373)
# print(k)
# k.to_file("./graphDataTest/data4.csv")
# pprint(k)
# k = GraphData("./graphDataTest/data4.csv")
# print(k)
# k.composite_graph()
# print(Coordinates(_SkyCoord.from_name("UCAC4 604-024937"),0.05))
# k.phase_graph(2455957.5, 1.209373)
# k.graph()
# k.composite_graph()
# k.phase_graph()

# print(resolve_name_aphos("USNO-B1.0 1211-0102048"))
# print(resolve_name_aphos("SKY# 9445")[0].declination)
# print("ajajaj")
# b = get_objects_by_params(coordinates=Coordinates("21h41m55.291s +71d18m41.12s", 0.05, 'h', 'd'))
# pprint(b)
# pprint(b)

# c = get_objects_by_params(min_mag=17.1, catalog="USNO-B1.0", max_mag=20)
# print("before c?")
# d = get_objects_by_params(min_mag=16.1, catalog="USNO-B1.0", max_mag=20)
# e = get_objects_by_params(min_mag=16.3, catalog="USNO-B1.0", max_mag=20)
# f = get_objects_by_params(min_mag=16.15, catalog="USNO-B1.0", max_mag=20)
# print("smth")
# pprint(c.get())
# print("after c")
# pprint(d.get())
# pprint(e.get())
# pprint(f.get())
# l = get_var_cmp_by_ids("805-031770", "807-030174")  # saturated
# pprint(l)
# pprint(get_user("kekw"))
# print(type(get_catalogs()))
# print(upload_files("csv_tests"))
# info()

# print(Coordinates("20 54 05.689 -37 01 17.38",10, 'h', 'm'))
# print(Coordinates("20:54:05.689-37:01:17.38",0.05, 'h'))
# print(Coordinates("17h15-17d10m", 0.05))
# print(Coordinates("275d11m15.6954s+17d59m59.876s", 0.05))
# print(Coordinates("12.34567h-17.87654d", 0.05))
# print(Coordinates("350.123456d-17.33333d", 0.05))
# print(parse_radius(25, 's'))
# coords = Coordinates("20 54 05.689 -37 01 17.38", 0.05)
# print(coords)
