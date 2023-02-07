import datetime
import math
import time
from inspect import signature, getcallargs, getargvalues, currentframe

import aphos_openapi
from pprint import pprint

from aphos_openapi.api import catalog_api
from aphos_openapi.api import flux_api
from aphos_openapi.api import space_object_api
from aphos_openapi.api import user_api
from aphos_openapi.model import flux
from aphos_openapi.model.error_message import ErrorMessage
from aphos_openapi.model.flux_data import FluxData

# Defining the host is optional and defaults to http://localhost:8009
# See configuration.py for a list of all supported configuration parameters.
configuration = aphos_openapi.Configuration(
    host="http://localhost:8009"
)

default_catalog = "UCAC4"


def getCatalogs():
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = catalog_api.CatalogApi(api_client)

        try:
            # Find all catalogs
            return api_instance.get_catalogs()
        except aphos_openapi.ApiException as e:
            print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)


def getObject(object_id, catalog=default_catalog):
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = space_object_api.SpaceObjectApi(api_client)

        try:
            return api_instance.get_space_object_by_id(object_id, catalog=catalog)
        except aphos_openapi.ApiException as e:
            print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)


def getObjectsByParams(object_id=None, catalog=None, name=None, coordinates=None, min_mag=None, max_mag=None):
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = space_object_api.SpaceObjectApi(api_client)

        try:
            params = dict()
            local_args = locals().copy()
            for key in getcallargs(getObjectsByParams).keys():
                if key in local_args and local_args[key] is not None:
                    params[key] = local_args[key]
            return api_instance.find_space_objects_by_params(**params)
        except aphos_openapi.ApiException as e:
            print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)


def getComparisonByIds(originalId, referenceId, originalCat=default_catalog, referenceCat=default_catalog):
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = space_object_api.SpaceObjectApi(api_client)

        try:
            return api_instance.get_comparison_by_identificators \
                (originalId, referenceId, original_cat=originalCat, reference_cat=referenceCat)
        except aphos_openapi.ApiException as e:
            print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)


def getUser(username):
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = user_api.UserApi(api_client)

        try:
            return api_instance.get_user_by_username(username)
        except aphos_openapi.ApiException as e:
            print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)


def setComparisonApertures(comparison, night: datetime.date, orig=None, ref=None):
    night_str = str(night.strftime("%d-%m-%Y"))
    for flux in comparison.data:
        if flux.night.first_date_of_the_night == night_str:
            ap_len = len(flux.apertures)
            if orig is None or 0 <= orig < ap_len:
                flux.night.ap_to_be_used = str(orig) if orig is not None else "auto"
            ref_ap_len = len(flux.ref_apertures)
            if ref is None or 0 <= ref < ref_ap_len:
                flux.night.ref_ap_to_be_used = str(ref) if ref is not None else "auto"
            orig_ap = flux.apertures[orig] if orig is not None else flux.ap_auto
            ref_ap = flux.ref_apertures[ref] if ref is not None else flux.ref_ap_auto
            if not orig_ap == "saturated" and not ref_ap == "saturated":
                flux.magnitude = -2.5 * math.log(getFloat(orig_ap) / getFloat(ref_ap), 10)
    return comparison


def getFloat(string):
    try:
        return float(string)
    except:
        return None

def hello():
    print("hello")


#o=getObject("805-031770")
#pprint(o)
#print(type(o))
# k=getObject("805-031770")
#k = getComparisonByIds("805-031770", "781-038863")  # not saturated
# pprint(k)

#l = getComparisonByIds("805-031770", "807-030174")  # saturated
# pprint(l)
#date = datetime.date(2021, 11, 6)
#c = setComparisonApertures(k, date, 0, 9)
# pprint(k)
#pprint(c)
