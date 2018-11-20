
set -e

template=git@github.com:duckietown/duckietown-project-template.git
template=.

cookiecutter \
    -c master18 \
    --no-input \
    -o output \
    -v \
    -f \
    ${template}  \
    project_name="Foobar library" project_slug=foobar \
    coveralls_repo_token=ZIgSe75hZ7zhTRHFng9v6RcgJMjTqWkMY
