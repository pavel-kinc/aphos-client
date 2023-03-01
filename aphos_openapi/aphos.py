from pprint import pprint

import aphos_openapi
from aphos_openapi.models.coordinates import Coordinates

# Defining the host is optional and defaults to http://localhost:8009
# See configuration.py for a list of all supported configuration parameters.
configuration = aphos_openapi.Configuration(
    host="https://ip-147-251-21-104.flt.cloud.muni.cz/"
    #host="http://localhost:8009"
)

default_catalog = "UCAC4"


def getCatalogs():
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = aphos_openapi.catalog_api.CatalogApi(api_client)

        try:
            # Find all catalogs
            return api_instance.get_catalogs()
        except aphos_openapi.ApiException as e:
            print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)


def getObject(object_id, catalog=default_catalog):
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = aphos_openapi.space_object_api.SpaceObjectApi(api_client)

        try:
            return api_instance.get_space_object_by_id(object_id, catalog=catalog)
        except aphos_openapi.ApiException as e:
            print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)


def getObjectsByParams(object_id=None, catalog=None, name=None, coordinates=None, min_mag=None, max_mag=None):
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = aphos_openapi.space_object_api.SpaceObjectApi(api_client)

        try:
            params = dict()
            local_args = locals().copy()
            for key in aphos_openapi.getcallargs(getObjectsByParams).keys():
                if key in local_args and local_args[key] is not None:
                    if(key == 'coordinates'):
                        local_args[key] = str(local_args[key])
                        print(local_args[key])
                    params[key] = local_args[key]
            return api_instance.find_space_objects_by_params(**params)
        except aphos_openapi.ApiException as e:
            print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)


def getComparisonByIds(originalId, referenceId, originalCat=default_catalog, referenceCat=default_catalog):
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = aphos_openapi.space_object_api.SpaceObjectApi(api_client)

        try:
            return api_instance.get_comparison_by_identificators \
                (originalId, referenceId, original_cat=originalCat, reference_cat=referenceCat)
        except aphos_openapi.ApiException as e:
            print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)


def getUser(username):
    # Enter a context with an instance of the API client
    with aphos_openapi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = aphos_openapi.user_api.UserApi(api_client)

        try:
            return api_instance.get_user_by_username(username)
        except aphos_openapi.ApiException as e:
            print("Exception when calling CatalogApi->get_catalogs: %s\n" % e)


def setComparisonApertures(comparison, night: aphos_openapi.datetime.date, orig=None, ref=None):
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
                flux.magnitude = -2.5 * aphos_openapi.math.log(getFloat(orig_ap) / getFloat(ref_ap), 10)
                orig_dev = flux.aperture_devs[orig] if orig is not None else flux.ap_auto_dev
                ref_dev = flux.ref_aperture_devs[ref] if ref is not None else flux.ref_ap_auto_dev
                flux.deviation = ((orig_dev/getFloat(orig_ap))**2 + (ref_dev/getFloat(ref_ap))**2)**0.5


def getFloat(string):
    try:
        return float(string)
    except:
        return None

def hello():
    print("hello" + " aphos version " + aphos_openapi.pkg_resources.require("aphos_openapi")[0].version)

def help():
    print("""help -> README.md -> https://test.pypi.org/project/aphos-openapi/\nTODO""")


o=getObject("805-031770")
#pprint(o)
print(type(o))
k=getObject("604-024734")
k = getComparisonByIds("805-031770", "781-038863")  # not saturated
#pprint(k)
#k = getComparisonByIds("605-025126", "606-024588")  # not saturated
#pprint(k)
help()
l = getComparisonByIds("805-031770", "807-030174")  # saturated
pprint(l)
date = aphos_openapi.datetime.date(2021,11, 6)
setComparisonApertures(l, date, 9, 9)
pprint(l)
#pprint(c)
#c = Coordinates(right_asc="21:41:55.291", declination="71:18:41.12", radius=0.05)
#pprint(c)
#c=Coordinates("21:41:55.291+71:18:41.12", 0.05)
#pprint(c.right_asc)
#coords = '{{"rightAsc": "{}",  "declination": "{}","radius": {}}}'.format("21:41:55.29", "71:18:41.12", 0.05)
#coords = Coordinates("21:41:55.291+71:18:41.12", 0.05)
#print(coords)
#c=getObjectsByParams(coordinates=coords)
#pprint(c)
