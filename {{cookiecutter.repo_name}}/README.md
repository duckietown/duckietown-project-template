[![CircleCI](https://circleci.com/gh/duckietown/{{cookiecutter.repo_name}}.svg?style=shield)](https://circleci.com/gh/duckietown/{{cookiecutter.repo_name}})

[![Coverage Status](https://coveralls.io/repos/github/duckietown/{{cookiecutter.repo_name}}/badge.svg?branch=master18)](https://coveralls.io/github/duckietown/{{cookiecutter.repo_name}}?branch=master18)

[![PyPI status](https://img.shields.io/pypi/status/{{cookiecutter.pypi_package}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.pypi_package}}/)


[![PyPI pyversions](https://img.shields.io/pypi/pyversions/{{cookiecutter.pypi_package}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.pypi_package}}/)


# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}


## Installation from source

This is the way to install within a virtual environment created by 
using `pipenv`:

    $ pipenv install
    $ pipenv shell
    $ cd lib-{{cookiecutter.project_slug}}
    $ pip install -r requirements.txt
    $ python setup.py develop --no-deps
    
   
## Unit tests

Run this:

    $ make -C lib-{{cookiecutter.project_slug}} tests-clean tests
    
The output is generated in the folder in `lib-{{cookiecutter.project_slug}}/out-comptests/`.
