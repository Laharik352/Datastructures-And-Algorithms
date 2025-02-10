#!/usr/bin/env python
"""
    Posts a message in room mentioned
    :param room_id: Spark Room Id
    :param message: Message to be posted in the room
"""

import json
import app
import logging
import requests
import healthcheck_config

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('healthcheck.log')
stream_handler = logging.StreamHandler()

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

room_id = {'Test': '039d4d00-25bc-11e8-a6c5-8b3c9ec34d95'}

spark_url = 'https://api.ciscospark.com/v1/messages'
bearer_token = 'MDgwMTQ5NGUtZWViOS00NzYyLWE1ZTItOGM4NmMzYTFhNDMxZmE4MjY3OGUtYmM5'


def post_message(room_id, message):

    headers = {'Content-Type':'application/json','Authorization': 'Bearer ' + bearer_token}
    payload = {'roomId':room_id, 'markdown':message}
    logger.info('Message:' + message)
    res = requests.post(spark_url, data=json.dumps(payload), headers=headers)
    logger.info(res.text)
    if res.status_code == 200:
        logger.info('Successfully posted the message')
        return True
    else:
        logger.info('Message could not be posted, error: ' + str(res.status_code))
        return False
