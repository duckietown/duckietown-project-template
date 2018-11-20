set -e
cookiecutter \
    -c master18 \
    --no-input \
    -o output \
    -v \
    git@github.com:duckietown/duckietown-project-template.git  \
    project_name="Foobar library" project_slug=foobar
