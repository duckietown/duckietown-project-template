# coding=utf-8
__version__ = "{{cookiecutter.version}}"

import logging

logging.basicConfig()
logger = logging.getLogger("dt-{{cookiecutter.project_slug}}")
logger.setLevel(logging.DEBUG)

logger.info("{{cookiecutter.python_package}} %s" % __version__)

from .algo import *

