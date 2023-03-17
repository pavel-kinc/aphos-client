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

## Usage:

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
(mostly genereated)
 - [ComparisonObject](aphos_openapi/docs/ComparisonObject.md)
 - [ErrorMessage](aphos_openapi/docs/ErrorMessage.md)
 - [Flux](aphos_openapi/docs/Flux.md)
 - [FluxData](aphos_openapi/docs/FluxData.md)
 - [Night](aphos_openapi/docs/Night.md)
 - [PhotoProperties](aphos_openapi/docs/PhotoProperties.md)
 - [SpaceObject](aphos_openapi/docs/SpaceObject.md)
 - [SpaceObjectWithFluxes](aphos_openapi/docs/SpaceObjectWithFluxes.md)
 - [User](aphos_openapi/docs/User.md)