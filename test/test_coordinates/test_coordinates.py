import unittest
from astropy.coordinates import SkyCoord
from aphos_openapi.models import coordinates
from aphos_openapi.models.coordinates import Coordinates
import json


class TestCoordinates(unittest.TestCase):
    def test_parse_coordinates(self):
        self.assertEqual(coordinates.parse_coordinates("20 54 05.6891 +37 01 17.38", 'h'),
                         ("20:54:05.689", "37:01:17.38"))
        # longer RA + skycoord
        self.assertEqual(coordinates.parse_coordinates(SkyCoord("20h54m05.689219s-37d01m17.38s")),
                         ("20:54:05.689", "-37:01:17.38"))

    def test_parse_radius(self):
        delta = 0.0001
        self.assertAlmostEqual(coordinates.parse_radius(0.05), 0.05, delta=delta)
        self.assertAlmostEqual(coordinates.parse_radius(0.05, 'random'), 0.05, delta=delta)
        self.assertAlmostEqual(coordinates.parse_radius(3, 'm'), 0.05, delta=delta)
        self.assertAlmostEqual(coordinates.parse_radius(180, 's'), 0.05, delta=delta)
        self.assertAlmostEqual(coordinates.parse_radius(200, 's'), 0.05555, delta=delta)
        self.assertAlmostEqual(coordinates.parse_radius(8, 'm'), 0.13333, delta=delta)

    def test_coordinates_constructor(self):
        try:
            Coordinates("20 54 05.689 -37 01 17.38", 10, 'h', 'm')
            Coordinates("20:54:05.689-37:01:17.38", 0.05, 'h')
            Coordinates("17h15-17d10m", 0.05)
            Coordinates("275d11m15.6954s+17d59m59.876s", 0.05)
            Coordinates("12.34567h-17.87654d", 0.05)
            Coordinates("350.123456d-17.33333d", 0.05)
        except ValueError:
            self.fail("Constructor not taking correct formats")

    def test_coordinates_constructor_bad_format(self):
        with self.assertRaises(ValueError):
            Coordinates("20h54m05.689s-37 01 17.38", 0.05)
        with self.assertRaises(ValueError):
            Coordinates("20h54m05.689s-37a01b17.38c", 0.05)


    def test_coordinates_equality(self):
        test_coord = Coordinates("21h41m55.291s+71d18m41.12s", 0.133333)
        coords = [Coordinates("21h41m55.291s +71d18m41.12s", 8, radius_unit='m'),
                  Coordinates("21 41 55.291 +71 18 41.12", 0.1333333),
                  Coordinates(SkyCoord("21h41m55.291s +71d18m41.12s"), 0.1333333),
                  Coordinates("21.698691944444448h +71.31142223d", 0.1333333),
                  Coordinates("21:41:55.291 +71:18:41.12", 0.1333333),
                  Coordinates("325.48037916666664d +71.31142223d", 0.1333333),
                  Coordinates("325 28 49.365 +71 18 41.12", 8, 'd', 'm')]
        for coord in coords:
            assert test_coord == coord

    def test_coordinates_not_equal(self):
        test_coord1 = Coordinates("21h41m55.291s+71d18m41.12s", 0.05)
        test_coord2 = Coordinates("21h41m55.391s+71d18m41.12s", 0.05)
        assert test_coord1 != test_coord2

    def test_coordinates_json_format(self):
        coord = Coordinates("21h41m55.291s+71d18m41.12s", 0.133333)
        coord_dict = coord.__dict__
        coord_str = str(Coordinates("21h41m55.291s+71d18m41.12s", 0.133333))
        json_dict = dict(json.loads(coord_str))
        assert set(coord_dict.keys()) == set(json_dict.keys())
        assert coord_dict == json_dict
