
# Duckietown Project Template


This repo contains a template for a Python/ROS library for Duckietown
using the templating system [Cookiecutter](https://github.com/audreyr/cookiecutter).


To create a repository starting from this template, first install the latest Cookiecutter:

    $ pip install -U cookiecutter

Then you can run:

    $ cookiecutter -c master18 https://github.com/duckietown/duckietown-project-template.git

Answer the questions and you will create the template for your repository.

## Features

- [x] Python setup.py
- [x] PyPI
- [x] Unit tests
- [x] Code coverage
- [x] Code coverage using Coveralls
- [x] CircleCI integration
- [ ] Duckiebook template
- [ ] ROS node template
- [ ] Support for YAML configuration files (easy_algo)
- [ ] Support for challenge definition/submission
- [ ] Docker containers


## Example

The repo [duckietown-foobar][foobar] is generated using this template.


[foobar]: https://github.com/duckietown/duckietown-foobar 

## Next steps


For the next steps, you need to ask a TA to:

1. Create repository `duckietown-PROJ`.
2. Activate CircleCI for the repository.
3. Activate Coveralls for the repo (TA: also remember to set the subdir). The TA will give you a "coverall repo token". It looks like "ZIgSe75hZ7zhTRHFngXXXXJMjTqWkMY". Put this token in the Makefile.


Remember to change `master18` into `master18`:

    git branch -m master18 master
