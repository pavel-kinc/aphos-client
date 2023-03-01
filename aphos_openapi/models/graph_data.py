from aphos_openapi.model.comparison_object import ComparisonObject as _Comp
from astropy.time import Time as _Time
import pprint as _pprint


class GraphData:
    def __init__(self, comparison, users=None, exclude=False, saturated=False):
        if type(comparison) != str:
            self.data_list = from_comparison(comparison, users, exclude, saturated)
        else:
            self.data_list = from_file(comparison, users, exclude, saturated)

    def __repr__(self):
        return str(self)


class DMD:
    def __init__(self, date, mag, dev):
        self.date = date
        self.magnitude = mag
        self.deviation = dev

    def __str__(self):
        return f'{self.date}, {self.magnitude}, {self.deviation}'

    def __repr__(self):
        return str(self)


def from_comparison(comparison: _Comp, users, exclude, saturated):
    res = []
    for flux in comparison.data:
        if not saturated and (flux.ap_auto == "saturated" or flux.ref_ap_auto == "saturated"):
            continue
        if users is not None:
            if flux.username in users:
                if exclude:
                    continue
                else:
                    date = _Time(flux.exp_middle).mjd
                    res.append(DMD(date, flux.magnitude, flux.deviation))
        date = _Time(flux.exp_middle).mjd
        res.append(DMD(date, flux.magnitude, flux.deviation))
    return res


def from_file(comparison, users, exclude, saturated):
    return []
