# coding=utf-8 
__version__ = '1.0.0'

import logging

logging.basicConfig()
logger = logging.getLogger('dt-foobar')
logger.setLevel(logging.DEBUG)

logger.info('duckietown-foobar %s' % __version__)

from .foo import *

