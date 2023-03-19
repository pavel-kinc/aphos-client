# APhoS client for retrieving data in Python

This is Amateur Photometric Survey (APhoS) Application Programming Interface.  
Contains models and functions for work with data in APhoS database.  
Server is accessible from: https://ip-147-251-21-104.flt.cloud.muni.cz/  
Swagger UI (Interface for api of the server): https://ip-147-251-21-104.flt.cloud.muni.cz/swagger-ui/index.html  
Openapi json or yaml file (documentation of api): https://ip-147-251-21-104.flt.cloud.muni.cz/api-docs

## Installation of Package: `aphos_openapi`

Install: `pip install -i https://test.pypi.org/simple/ aphos-openapi`  
Upgrade: `pip unistall aphos_openapi` + Install (will be changed with going to real Pypi)
(If you have pip3 instead of pip, just use pip3)

## Usage Api models:

```
from aphos_openapi import aphos
from pprint import pprint   # just to show results and models

def my_function():
    aphos.help()
    star_objects = aphos.getObjectsByParams(min_mag="11.98", max_mag="12")
    pprint(star_objects[0])
    print("""
    -------------------------------
    """)
    comparison = aphos.getComparisonByIds("805-031770", "781-038863")
    pprint(comparison)

my_function()
```

## Usage Coordinates:

```
from aphos_openapi import aphos
from pprint import pprint   # just to show results and models

def my_function():
    aphos.help()
    star_objects = aphos.getObjectsByParams(min_mag="11.98", max_mag="12")
    pprint(star_objects[0])
    print("""
    -------------------------------
    """)
    comparison = aphos.getComparisonByIds("805-031770", "781-038863")
    pprint(comparison)

my_function()
```

## Usage GraphData:

```
from aphos_openapi import aphos
from pprint import pprint   # just to show results and models

def my_function():
    aphos.help()
    star_objects = aphos.getObjectsByParams(min_mag="11.98", max_mag="12")
    pprint(star_objects[0])
    print("""
    -------------------------------
    """)
    comparison = aphos.getComparisonByIds("805-031770", "781-038863")
    pprint(comparison)

my_function()
```

## Requirements:

* Python >=3.6,
* 'urllib3'>=1.25.3,
* 'python-dateutil',
* 'matplotlib',
* 'astropy'

## Support

pavelkinc230@gmail.com

### Additional information for functions and models of this package

## Documentation For Models
(Api models only, mostly genereated)
References work only in github: https://github.com/pavel-kinc/aphos-client/blob/main/README.md
 - [ComparisonObject](README.md#comparisonobject)
 - [ErrorMessage](README.md#errormessage)
 - [Flux](README.md#flux)
 - [FluxData](README.md#fluxdata)
 - [Night](README.md#night)
 - [PhotoProperties](README.md#photoproperties)
 - [SpaceObject](README.md#spaceobject)
 - [SpaceObjectWithFluxes](README.md#spaceobjectwithfluxes)
 - [User](README.md#user)

### ComparisonObject

#### Properties
| Name           | Type                                     | Description | Notes |
|----------------|------------------------------------------|-------------|-------|
| **variable**   | [**SpaceObject**](README.md#spaceobject) |             |       |
| **comparison** | [**SpaceObject**](README.md#spaceobject) |             |       |
| **data**       | [**[FluxData]**](README.md#fluxdata)     |             |       |

[[Back to Model list]](README.md#documentation-for-models)

### ErrorMessage

#### Properties
| Name        | Type    | Description | Notes      |
|-------------|---------|-------------|------------|
| **id**      | **str** |             | [optional] |
| **message** | **str** |             | [optional] |

[[Back to Model list]](README.md#documentation-for-models)

### Flux

#### Properties
| Name              | Type                                             | Description | Notes |
|-------------------|--------------------------------------------------|-------------|-------|
| **right_asc**     | **str**                                          |             |       |
| **declination**   | **str**                                          |             |       |
| **added_by**      | **str**                                          |             |       |
| **ap_auto**       | **float**                                        |             |       |
| **apertures**     | **[float]**                                      |             |       |
| **photo**         | [**PhotoProperties**](README.md#photoproperties) |             |       |
| **ap_auto_dev**   | **float**                                        |             |       |
| **aperture_devs** | **[float]**                                      |             |       |

[[Back to Model list]](README.md#documentation-for-models)

### FluxData

#### Properties
| Name                  | Type                         | Description | Notes |
|-----------------------|------------------------------|-------------|-------|
| **right_asc**         | **str**                      |             |       |
| **dec**               | **str**                      |             |       |
| **ap_auto**           | **str**                      |             |       |
| **ap_auto_dev**       | **float**                    |             |       |
| **apertures**         | **[str]**                    |             |       |
| **aperture_devs**     | **[float]**                  |             |       |
| **magnitude**         | **float**                    |             |       |
| **deviation**         | **float**                    |             |       |
| **username**          | **str**                      |             |       |
| **night**             | [**Night**](README.md#night) |             |       |
| **exp_middle**        | **str**                      |             |       |
| **cmp_ap_auto**       | **str**                      |             |       |
| **cmp_ap_auto_dev**   | **float**                    |             |       |
| **cmp_apertures**     | **[str]**                    |             |       |
| **cmp_aperture_devs** | **[float]**                  |             |       |

[[Back to Model list]](README.md#documentation-for-models)

### Night

#### Properties
| Name                         | Type    | Description | Notes |
|------------------------------|---------|-------------|-------|
| **first_date_of_the_night**  | **str** |             |       |
| **second_date_of_the_night** | **str** |             |       |
| **ap_to_be_used**            | **str** |             |       |
| **cmp_ap_to_be_used**        | **str** |             |       |

[[Back to Model list]](README.md#documentation-for-models)

### PhotoProperties

#### Properties
| Name               | Type         | Description | Notes |
|--------------------|--------------|-------------|-------|
| **exposure_begin** | **datetime** |             |       |
| **exposure_end**   | **datetime** |             |       |

[[Back to Model list]](README.md#documentation-for-models)

### SpaceObject

#### Properties
| Name             | Type      | Description | Notes |
|------------------|-----------|-------------|-------|
| **id**           | **str**   |             |       |
| **catalog**      | **str**   |             |       |
| **name**         | **str**   |             |       |
| **right_asc**    | **str**   |             |       |
| **declination**  | **str**   |             |       |
| **magnitude**    | **float** |             |       |
| **fluxes_count** | **int**   |             |       |

[[Back to Model list]](README.md#documentation-for-models)

### SpaceObjectWithFluxes
Extends SpaceObject by fluxes.

#### Properties
| Name             | Type                         | Description                              | Notes |
|------------------|------------------------------|------------------------------------------|-------|
| **fluxes**       | [**[Flux]**](README.md#flux) | Additional field compared to SpaceObject |       |
| **id**           | **str**                      |                                          |       |
| **catalog**      | **str**                      |                                          |       |
| **name**         | **str**                      |                                          |       |
| **right_asc**    | **str**                      |                                          |       |
| **declination**  | **str**                      |                                          |       |
| **magnitude**    | **float**                    |                                          |       |
| **fluxes_count** | **int**                      |                                          |       |

[[Back to Model list]](README.md#documentation-for-models)

### User

#### Properties
| Name            | Type    | Description | Notes |
|-----------------|---------|-------------|-------|
| **username**    | **str** | Unique      |       |
| **description** | **str** |             |       |

[[Back to Model list]](README.md#documentation-for-models)















