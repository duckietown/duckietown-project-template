
[![CircleCI](https://circleci.com/gh/duckietown/duckietown-project-template.svg?style=shield)](https://circleci.com/gh/duckietown/duckietown-project-template)


# Duckietown Project Template


This repo contains a template for a Python/ROS library for Duckietown.


To create a repository starting from this template, first install the latest Cookiecutter:

    $ pip install -U cookiecutter

Then you can run:

    $ cookiecutter -c master18 https://github.com/duckietown/duckietown-project-template.git

Answer the questions and you will create the template for your repository.

## Example

The repo [duckietown-foobar][foobar] is generated using [go.sh](go.sh).


[foobar]: https://github.com/duckietown/duckietown-foobar 

## Next steps


For the next steps, you need to ask a TA to:

1. Create repository `duckietown-PROJ`.
2. Activate CircleCI for the repository.
3. Activate Coveralls for the repo (TA: also remember to set the subdir). The TA will give you a "coverall repo token". It looks like "ZIgSe75hZ7zhTRHFngXXXXJMjTqWkMY". Put this token in the Makefile.


Remember to change `master18` into `master18`:

    git branch -m master18 master
