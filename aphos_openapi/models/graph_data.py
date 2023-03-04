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
        a, b, c = zip(*self.data_list)
        fig, ax = _plt.subplots(figsize=(11, 7))
        _plt.title("Light curve of star")
        _plt.xlabel("Julian Date")
        _plt.ylabel("Magnitude")
        dot, = ax.plot(a, b, 'o', label="dot")
        error = ax.errorbar(a, b, yerr=c, fmt=" ", label="error", ecolor="#1f77b4", visible=False)
        box = deviations(_plt, ax, [error])
        scroll(fig, box)

        _plt.show()

    def composite_graph(self):
        d = dict()
        fig, ax = _plt.subplots(figsize=(11, 7))
        _plt.title("Light curve of star - compare nights")
        _plt.xlabel("Julian Date - floating point")
        _plt.ylabel("Magnitude")
        fig.subplots_adjust(right=0.8)
        errs = []
        for a, b, c in self.data_list:
            key = _math.floor(a)
            d.setdefault(key, []).append((a % 1, b, c))
        for key, val in d.items():
            time = _Time(key+_JD_SHRT_SUB, format='jd')
            a, b, c = zip(*val)
            ax.plot(a, b, "o", label=time.strftime('%Y-%m-%d'))
            errs.append(ax.errorbar(a, b, yerr=c, fmt=" ",color="orange", visible=False))
        legend = ax.legend(loc='upper left', title="First day of night", bbox_to_anchor=(1, 0, 0.07, 1))
        if len(errs) > 10:
            scroll(fig, legend)
        box = deviations(_plt, ax, errs)
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
                continue
        date = _Time(flux.exp_middle).jd - _JD_SHRT_SUB
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


def deviations(plot, ax, errors):
    # legend = _plt.legend(loc='upper right')
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
