# import logging.config
# from datetime import datetime
#
# logging.config.fileConfig('aaa.conf')
# logger = logging.getLogger('MainLogger')
#
# fh = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))
# formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
# fh.setFormatter(formatter)
#
# logger.addHandler(fh)
# logger.debug("TEST")

"""
Utility file for getting logger object.
For each .py file one logger object is created and all data
to is logged to single file analyzerbot.log

"""

# import logging
# import logging.config
# import sys
#
# logger = logging.getLogger(__name__)
#
# logger.setLevel(logging.INFO)
#
# formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
#
# file_handler = logging.FileHandler('healthcheck.log')
# stream_handler = logging.StreamHandler()
#
# file_handler.setFormatter(formatter)
# stream_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)