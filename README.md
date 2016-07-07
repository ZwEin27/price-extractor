# dig-price-extractor
A pure python utility to extract price from text


## About

The phone-price-extractor aims to extract price with units from text of [DIG](http://usc-isi-i2.github.io/dig/) project for 2016 MEMEX workshop

currently for hourly price only based on specific purpose of DIG project


## Install

    python setup.py install

or

    pip install digpe

## Example Usage

initialize pnmatcher

    from digpe import DIGPE

    digpe = DIGPE()

use pnmatcher for url

    text = "????FiveStarExperience? \n \n   Incall donation \n15min50?20mins60?hhr80?hr120?\n8327911957 Lola"

    extractions = digpe.extract(text)

    # print extractions
    # [{"price": "120", "price_unit": "", "time_unit": "hr"}]


## Spark Usage

1. upload following four files into your spark environment

    - spark_workflow.sh
    - spark_workflow.py
    - spark_dependencies/python_main.zip
    - spark_dependencies/python_lib.zip

2. run `spark_workflow.sh` for spark workflow


## Project Layout

- The `pnmatcher/` directory holds the python code.
- The `spark_dependencies/` directory contains two zip files that are used for spark workflow. (no implemented yet, will be in production after 2016 MEMEX Workshop)
- The `tests/` holds test scripts to evaluate the program.

## Credit

### Library
- [dig-sparkutil](https://github.com/usc-isi-i2/dig-sparkutil)
