# coding=utf-8
from comptests import comptest, run_module_tests

from duckietown_{{cookiecutter.project_slug}} import FoobarAlgo

@comptest
def test_foo():

    c = FoobarAlgo(param1=1)



if __name__ == '__main__':
    run_module_tests()
