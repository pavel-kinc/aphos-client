# APhoS client for retrieving data in Python

This is Amateur Photometric Survey (APhoS) Application Programming Interface.
Contains models and functions for work with data in APhoS database.

## Installation of Package: `aphos_openapi`

Install: `pip install -i https://test.pypi.org/simple/ aphos-openapi`
Upgrade: `pip unistall aphos_openapi` + Install (will be changed with going to real Pypi)
(If you have pip3 instead of pip, just use pip3)

## Usage:

```
from aphos_openapi import aphos

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

Python >=3.6

## Support

pavelkinc230@gmail.com

## Additional information for functions and models of this package

TODO