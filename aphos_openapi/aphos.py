"""Module providing pretty print."""
import _io
import os as _os
from pprint import pprint
# from typing import Optional
from typing import Optional as _Optional
from typing import List as _List
from typing import Union as _Union
from typing import Tuple as _Tuple
from astropy.coordinates import SkyCoord as _SkyCoord  # type: ignore

import aphos_openapi  # type: ignore
from aphos_openapi.models.coordinates import Coordinates
from aphos_openapi.models.graph_data import GraphData

# Defining the host is optional and defaults to http://localhost:8009
# See configuration.py for a list of all supported configuration parameters.
configuration = aphos_openapi.Configuration(
    host="https://ip-147-251-21-104.flt.cloud.muni.cz/"
    # host="http://localhost:8009"
)

DEFAULT_CATALOG = "UCAC4"

ALL_CATALOGS = "All catalogues"

_READ_ME = "https://test.pypi.org/project/aphos-openapi/"


def get_catalogs() -> _Optional[_List[str]]:
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = aphos_openapi.catalog_api.CatalogApi(api_client)

        try:
            # Find all catalogs
            return api_instance.get_catalogs()
        except aphos_openapi.OpenApiException as exc:
            print(exc)
            return None


def get_object(object_id: str, catalog: str = DEFAULT_CATALOG) \
        -> _Optional[aphos_openapi.models.SpaceObjectWithFluxes]:
    with aphos_openapi.ApiClient(configuration) as api_client:
        api_instance = aphos_openapi.space_object_api.SpaceObjectApi(api_client)

        try:
            return api_instance.get_space_object_by_id(object_id, catalog=catalog)
        except aphos_openapi.OpenApiException as exc:
            print(exc)
            return None


def get_objects_by_params(object_id: _Optional[str] = None, catalog: _Optional[str] = None,
                          name: _Optional[str] = None, coordinates: _Optional[Coordinates] = None,
                          min_mag: _Union[str, float, None] = None,
                          max_mag: _Union[str, float, None] = None) -> \
        _Optional[_List[aphos_openapi.models.SpaceObject]]:
    if min_mag is not None and min_mag >= 15 and max_mag is None:
        max_mag = 20
    local_args = locals().copy()

    try:
        params = dict()
        for key in local_args.keys():
            if local_args[key] is not None:
                if key == 'coordinates':
                    local_args[key] = str(local_args[key])
                params[key] = local_args[key]
        with aphos_openapi.ApiClient(configuration) as api_client:
            api_instance = aphos_openapi.space_object_api.SpaceObjectApi(api_client)
            return api_instance.find_space_objects_by_params(**params)
    except aphos_openapi.OpenApiException as exc:
        print(exc)
        return None


def get_var_cmp_by_ids(variable_id: str, comparison_id: str,
                       var_catalog: str = DEFAULT_CATALOG,
                       cmp_catalog: str = DEFAULT_CATALOG) \
        -> _Optional[aphos_openapi.models.ComparisonObject]:
    try:
        with aphos_openapi.ApiClient(configuration) as api_client:
            api_instance = aphos_openapi.space_object_api.SpaceObjectApi(api_client)
            return api_instance.get_comparison_by_identificators \
                (variable_id, comparison_id, original_cat=var_catalog, reference_cat=cmp_catalog)
    except aphos_openapi.OpenApiException as exc:
        print(exc)
        return None


def get_user(username: str) -> _Optional[aphos_openapi.models.User]:
    try:
        with aphos_openapi.ApiClient(configuration) as api_client:
            api_instance = aphos_openapi.user_api.UserApi(api_client)
            return api_instance.get_user_by_username(username)
    except aphos_openapi.OpenApiException as exc:
        print(exc)
        return None


def set_var_cmp_apertures(comparison: aphos_openapi.models.ComparisonObject,
                          night: aphos_openapi.datetime.date, var: _Optional[int] = None,
                          cmp: _Optional[int] = None) -> None:
    """
    Sets apertures based on night and desired indexes in comparison object and
    recalculates magnitude and deviation

    Args:
        comparison: ComparisonObject - object to which the apertures are set
        night: Array of nights to which the apertures are changing
        var: target index of aperture to set (from original star)
        cmp: target index of aperture to set (from reference star)
    """
    night_str = str(night.strftime("%d-%m-%Y"))
    for flux in comparison.data:

        if flux.night.first_date_of_the_night == night_str:

            ap_len = len(flux.apertures)
            ref_ap_len = len(flux.cmp_apertures)
            if not 0 <= var < ap_len or not 0 <= cmp < ref_ap_len:
                # in case of variable lengths, this needs to be modified with continue
                raise IndexError(f"Index out of bounds, use None or {0}-{min(ap_len, ref_ap_len)-1}")
            if var is None:
                flux.night.ap_to_be_used = str(var) if var is not None else "auto"

            if cmp is None:
                flux.night.cmp_ap_to_be_used = str(cmp) if cmp is not None else "auto"
            orig_ap = flux.apertures[var] if var is not None else flux.ap_auto
            ref_ap = flux.cmp_apertures[cmp] if cmp is not None else flux.cmp_ap_auto

            if not orig_ap == "saturated" and not ref_ap == "saturated":
                flux.magnitude = \
                    -2.5 * aphos_openapi.math.log(get_float(orig_ap) / get_float(ref_ap), 10)
                orig_dev = flux.aperture_devs[var] if var is not None else flux.ap_auto_dev
                ref_dev = flux.cmp_aperture_devs[cmp] if cmp is not None else flux.cmp_ap_auto_dev
                var_sq = (orig_dev / get_float(orig_ap)) ** 2
                cmp_sq = (ref_dev / get_float(ref_ap)) ** 2
                flux.deviation = (var_sq + cmp_sq) ** 0.5


def resolve_name_aphos(name: str) -> _Optional[_List[aphos_openapi.models.SpaceObject]]:
    try:
        astropy_coords = _SkyCoord.from_name(name)
    except:
        return None
    coord = Coordinates(astropy_coords, 1, radius_unit='s')
    res = get_objects_by_params(coordinates=coord)
    if res is not None and len(res) == 0:
        coord = Coordinates(astropy_coords, 3, radius_unit='s')
        res = get_objects_by_params(coordinates=coord)
    return res


def upload_files(path: str) -> _List[_Tuple[str, bool, str]]:
    with aphos_openapi.ApiClient(configuration) as api_client:
        api_instance = aphos_openapi.space_object_api.SpaceObjectApi(api_client)
        res = []
        if _os.path.isdir(path):
            files_threads = []
            for file in _os.listdir(path):
                os_path = _os.path.join(path, file)
                if _os.path.isfile(os_path):
                    csv_file = _io.FileIO(os_path, 'rb')
                    files_threads.append((file, api_instance.upload_csv(file=csv_file, async_req=True)))
            for file, thread in files_threads:
                try:
                    res.append((file, True, thread.get()))
                except aphos_openapi.OpenApiException as exc:
                    res.append((file, False, exc))
        else:
            csv_file = _io.FileIO(path, 'rb')
            try:
                res.append((path, True, api_instance.upload_csv(file=csv_file)))
            except aphos_openapi.OpenApiException as exc:
                res.append((path, False, exc))
        return res


def get_float(string: _Union[str, float]) -> float:
    """
    Function takes variable and returns float or throws exception.

    Args:
        string: string of float number

    Returns: float number from string or float

    """
    return float(string)


def info() -> None:
    """
    Prints useful documentation and info about this package.
    """
    print(f"help -> documentation -> {_READ_ME}")
    print("APhoS version: "
          + aphos_openapi.pkg_resources.require("aphos_openapi")[0].version)


# o = get_object("604-024943")
# print(o)
# print(type(o))
# k=get_object("604-024734")
# k = get_var_cmp_by_ids("805-031770", "781-038863")  # not saturated
# pprint(k)

# info()
# l = get_var_cmp_by_ids("805-031770", "807-030174")  # saturated
# set_var_cmp_apertures(l, aphos_openapi.datetime.date(2021,11, 6),5,5)
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

k = get_var_cmp_by_ids("605-025126", "604-024943", "UCAC4", "UCAC4")  # not saturated
# print(k)
# VarCmp getvarcmpbyids
# VAR vs CMP (orig vs ref)
# pprint(k)
date = aphos_openapi.datetime.date(2022,3, 22)
set_var_cmp_apertures(k, date, 0, 9)
pprint(k)
# print(k)
# k = GraphData(k, users=["xkrutak"], exclude=False, saturated=False)
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
#info()
#info()
