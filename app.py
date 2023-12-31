from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys

logging.info('Welcome to the Custom log')

try:
    a=4/'6'
except Exception as e:
    raise AppException(e, sys)