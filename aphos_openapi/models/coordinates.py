from astropy.coordinates import SkyCoord as _SkyCoord
from astropy import units as _u
from astropy.coordinates import Angle as _Angle
#import pprint as _pprint


class Coordinates:
    def __init__(self, coordinates, radius, default_unit='h', radius_unit='d'):
        self.rightAsc, self.declination = parse_coordinates(coordinates, default_unit)
        self.radius = parse_radius(radius, radius_unit)

    def __str__(self):
        #return _pprint.pformat(self.__dict__)
        return '{{"rightAsc": "{}",  "declination": "{}","radius": {}}}'\
            .format(self.rightAsc, self.declination, self.radius)



def parse_coordinates(coordinates, default_unit='h'):
    coordinates.strip()
    sign = '+'
    if '-' in coordinates:
        sign = '-'
    if coordinates.count(' ') > 1 or coordinates.count(':') > 1:
        coord_arr = coordinates.split(sign)
        coord_arr[0] = coord_arr[0].strip() + default_unit
        coord_arr[1] = sign + coord_arr[1].strip() + 'd'
        coordinates = coord_arr[0] + coord_arr[1]
    sky_coord = _SkyCoord(coordinates)
    return sky_coord.ra.to_string(unit=_u.hour, sep=':'), sky_coord.dec.to_string(unit=_u.degree, sep=':')


def parse_radius(radius, radius_unit):
    if radius_unit not in "ms" or len(radius_unit) > 1:
        return radius
    return _Angle(str(radius) + radius_unit).degree


#print(Coordinates("20 54 05.689 -37 01 17.38",10, 'h', 'm'))
#print(Coordinates("20:54:05.689-37:01:17.38",0.05, 'h'))
#print(Coordinates("17h15-17d10m", 0.05))
#print(Coordinates("275d11m15.6954s+17d59m59.876s", 0.05))
#print(Coordinates("12.34567h-17.87654d", 0.05))
#print(Coordinates("350.123456d-17.33333d", 0.05))
#print(parse_radius(25, 's'))
#coords = Coordinates("20 54 05.689 -37 01 17.38", 0.05)
#print(coords)
