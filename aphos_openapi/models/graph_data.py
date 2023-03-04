import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox as _Box

from aphos_openapi.model.comparison_object import ComparisonObject as _Comp
from astropy.time import Time as _Time
import pprint as _pprint
import csv as _csv
import os as _os
import matplotlib.pyplot as _plt
from matplotlib.widgets import CheckButtons
import math as _math

# import numpy as _np


_JD_SHRT_SUB = 2400000



class GraphData:
    def __init__(self, comparison, users=None, exclude=False, saturated=False):
        if type(comparison) != str:
            self.data_list = from_comparison(comparison, users, exclude, saturated)
            info = [comparison.original.id, comparison.original.catalog,
                    comparison.reference.id, comparison.reference.catalog]
        else:
            info, self.data_list = from_file(comparison, users, exclude, saturated)
        self.original, self.orig_catalog, self.reference, self.ref_catalog = info

    def __repr__(self):
        return _pprint.pformat(self.__dict__)

    def to_file(self, path):
        _os.makedirs(_os.path.dirname(path), exist_ok=True)
        with open(path, 'w', newline='') as file:
            writer = _csv.writer(file, delimiter=' ')
            writer.writerow(["Original ID", self.original])
            writer.writerow(["Original Catalog", self.orig_catalog])
            writer.writerow(["Reference ID", self.reference])
            writer.writerow(["Reference Catalog", self.ref_catalog])
            for data in self.data_list:
                writer.writerow(data)

    def graph(self):
        d = dict()
        fig, ax = _plt.subplots(figsize=(11, 7))
        fig.subplots_adjust(right=0.8)
        _plt.title(f"Light curve of {self.original} {self.orig_catalog} to {self.reference} {self.ref_catalog}")
        _plt.xlabel("Julian Date")
        _plt.ylabel("Magnitude")
        for a,b,c,u in self.data_list:
            key = u[0:15]
            d.setdefault(key,[]).append((a,b,c))
        errs=[]
        for key, val in d.items():
            a,b,c = zip(*val)
            ax.plot(a, b, "o", label=key)
            errs.append(ax.errorbar(a, b, yerr=c, fmt=" ", color="#1f77b4", visible=False))
        box = deviations(_plt, ax, errs)
        legend = ax.legend(loc='upper left', title="Username", bbox_to_anchor=(1, 0, 0.07, 1))
        if len(errs) > 10:
            scroll(fig, legend)

        _plt.show()

    def composite_graph(self):
        d = dict()
        fig, ax = _plt.subplots(figsize=(11, 7))
        _plt.title(f"Composed night light curve of {self.original} {self.orig_catalog} "
                   f"to {self.reference} {self.ref_catalog}")
        _plt.xlabel("Julian Date - floating point")
        _plt.ylabel("Magnitude")
        fig.subplots_adjust(right=0.8)
        errs = []
        for a, b, c,_ in self.data_list:
            key = _math.floor(a)
            d.setdefault(key, []).append((a % 1, b, c))
        for key, val in d.items():
            time = _Time(key+_JD_SHRT_SUB, format='jd')
            a, b, c = zip(*val)
            ax.plot(a, b, "o", label=time.strftime('%Y-%m-%d'))
            errs.append(ax.errorbar(a, b, yerr=c, fmt=" ",color="#1f77b4", visible=False))
        legend = ax.legend(loc='upper left', title="First day of night", bbox_to_anchor=(1, 0, 0.07, 1))
        if len(errs) > 10:
            scroll(fig, legend)
        box = deviations(_plt, ax, errs)
        _plt.show()


class DMDU:
    def __init__(self, date, mag, dev, user):
        self.date = date
        self.magnitude = mag
        self.deviation = dev
        self.user = user

    def __str__(self):
        return f'{self.date}, {self.magnitude}, {self.deviation}, {self.user}'

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
                continue
        date = _Time(flux.exp_middle).jd - _JD_SHRT_SUB
        res.append(DMDU(date, flux.magnitude, flux.deviation, flux.username))
    return res


def from_file(comparison,users, exclude, saturated):
    info= []
    res = []
    with open(comparison, 'r', newline='') as file:
        reader = _csv.reader(file, delimiter=' ')
        for row in reader:
            if len(row) < 3:
                info.append(row[1])
                continue
            if row[2] == float('-inf') and not saturated:
                continue
            if users is not None:
                if row[3] in users:
                    if exclude:
                        continue
                else:
                    continue
            res.append(DMDU(float(row[0]), float(row[1]), float(row[2]), row[3]))
    return info, res


def deviations(plot, ax, errors):
    button = plot.axes([0.01, 0.03, 0.18, 0.05], frameon=False)
    box = CheckButtons(button, ["show with deviations"], [False])

    def set_devs(label):
        for error in errors:
            for bar in error.lines[2]:
                bar.set_visible(not bar.get_visible())
            plot.draw()

    box.on_clicked(set_devs)
    return box

def scroll(fig, legend):
    d = {"down": 40, "up": -40}

    def legend_scroll(evt):
        if legend.contains(evt):
            bbox = legend.get_bbox_to_anchor()
            bbox = _Box.from_bounds(bbox.x0, bbox.y0 + d[evt.button], bbox.width, bbox.height)
            tr = legend.axes.transAxes.inverted()
            legend.set_bbox_to_anchor(bbox.transformed(tr))
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("scroll_event", legend_scroll)
