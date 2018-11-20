
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
