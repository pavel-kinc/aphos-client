from aphos_openapi.model.comparison_object import ComparisonObject as _Comp
from astropy.time import Time as _Time
import pprint as _pprint
import csv as _csv
import os as _os
import matplotlib.pyplot as _plt
#import numpy as _np


class GraphData:
    def __init__(self, comparison, users=None, exclude=False, saturated=False):
        if type(comparison) != str:
            self.data_list = from_comparison(comparison, users, exclude, saturated)
        else:
            self.data_list = from_file(comparison, saturated)

    def __repr__(self):
        return _pprint.pformat(self.data_list)

    def to_file(self, path):
        _os.makedirs(_os.path.dirname(path), exist_ok=True)
        with open(path, 'w', newline='') as file:
            writer = _csv.writer(file, delimiter=' ')
            for data in self.data_list:
                writer.writerow(data)

    def graph(self):
        a,b,c = zip(*self.data_list)
        _plt.title("Light curve of star")
        _plt.xlabel("Julian Date")
        _plt.ylabel("Magnitude")
        _plt.scatter(a,b)
        _plt.show()

class DMD:
    def __init__(self, date, mag, dev):
        self.date = date
        self.magnitude = mag
        self.deviation = dev

    def __str__(self):
        return f'{self.date}, {self.magnitude}, {self.deviation}'

    def __repr__(self):
        return str(self)

    def __iter__(self):
        for val in self.__dict__.values():
            yield val


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


def from_file(comparison, saturated):
    res = []
    with open(comparison, 'r', newline='') as file:
        reader = _csv.reader(file, delimiter=' ')
        for row in reader:
            if row[2] == float('-inf') and not saturated:
                continue
            res.append(DMD(float(row[0]), float(row[1]), float(row[2])))
    return res
