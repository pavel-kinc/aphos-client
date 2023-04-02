import unittest
from astropy.coordinates import SkyCoord
from aphos_openapi.models import coordinates
from aphos_openapi.models.coordinates import Coordinates
import json

from aphos_openapi import aphos


class TestCoordinates(unittest.TestCase):

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
