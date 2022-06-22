### Tests status:
[![Actions Status](https://github.com/renata-nerenata/python_project_iubh/workflows/Linter/badge.svg)](https://github.com/renata-nerenata/python_project_iubh/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a48adcf1d95882daed37/test_coverage)](https://codeclimate.com/github/renata-nerenata/python_project_iubh/test_coverage)

## Task
Python-program that uses training data to choose the four ideal functions which are the
best fit out of the provided functions.

## Project structure
.
├── LICENSE
├── Makefile           <- Makefile with commands like
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── ideal.csv      <- Datasets for 50 ideal functions
│   ├── train.csv      <- 4 training datasets.
│   └── test.csv       <- One test dataset.
│
├── reports            <- Generated analysis in LaTeX.
│   └── figures        <- Generated figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to generate data from csv files
│   │   └── make_dataset.py
│   │
│   ├── models         
│   │   └──  evaluate_score.py <- Scripts to generate evaluation metric - the sum of all deviations squared (Least-Square)
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
├──task                <- The test of the assignment
│
└──tests               <- Unit-tests

## Environment
Create an enviroment with all used libraries

``` python -m venv env ```

``` source env/bin/activate ```

``` pip install -r requirements.txt ```