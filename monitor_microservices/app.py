#!/usr/bin/env python
"""
The script monitors the various microservices and posts their health check status in the room that has been configured

Usage:
    app.py --job_number=<job_number> --job_url=<job_url>
Options:
    --job_number=<job_number>                          #jenkins job number
    --job_url=<job_url>                                #jenkins job url
Example:
    app.py --job_number='8' --job_url='https://engci-private-sjc.cisco.com/jenkins/ss4/job/Nimbus/job/SS4/job/Microservices%20monitor/8/'
"""

import docopt
import requests
import healthcheck_config
import logging
import healthcheck_sparkpost

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('healthcheck.log')
stream_handler = logging.StreamHandler()

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class Microservices_HelathCheck():

    def LocusProdHealthCheck(self):
        logger.info("Checking the health check state of Locus on Production")
        locus_prod_vipurl = "https://locus-a.wbx2.com/locus"
        locus_healthget = "/api/v1/service_health"
        response = requests.get(url=locus_prod_vipurl+locus_healthget).json()
        if response.get("serviceState"):
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "State of Locus in Production: " + response.get("serviceState"))
        else:
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "Failed to get the health state of Locus in Production")

    def LocusIntHealthCheck(self):
        logger.info("Checking the health check state of Locus on Integration")
        locus_int_vipurl = "https://locus-intb.ciscospark.com/locus"
        locus_int_healthget = "/api/v1/service_health"
        response = requests.get(url=locus_int_vipurl+locus_int_healthget).json()
        if response.get("serviceState"):
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "State of Locus in Integration: " + response.get("serviceState"))
        else:
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "Failed to get the health state of Locus in Integration")

    def CalliopeProdHealthCheck(self):
        logger.info("Checking the health check state of Calliope on Production")
        calliope_prod_vipurl = "https://calliope-a.wbx2.com/calliope"
        calliope_prod_healthget = "/api/v1/service_health"
        response = requests.get(url=calliope_prod_vipurl+calliope_prod_healthget).json()
        if response.get("serviceState"):
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "State of Calliope in Production: " + response.get("serviceState"))
        else:
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "Failed to get the health state of Calliope in Production")

    def HecateProdHealthCheck(self):
        logger.info("Checking the health check state of Hecate on Production")
        hecate_prod_vipurl = "https://hecate-a.wbx2.com/hecate"
        hecate_prod_healthget = "/api/v1/service_health"
        response = requests.get(url=hecate_prod_vipurl+hecate_prod_healthget).json()
        if response.get("serviceState"):
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "State of Hecate in Production: " + response.get("serviceState"))
        else:
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "Failed to get the health state of Hecate in Production")

    def L2sipProdHealthCheck(self):
        logger.info("Checking the health check state of L2sip on Production")
        l2sip_prod_vipurl = "https://l2sip-a.wbx2.com/l2sip"
        l2sip_prod_healthget = "/api/v1/service_health"
        response = requests.get(url=l2sip_prod_vipurl+l2sip_prod_healthget).json()
        if response.get("serviceState"):
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "State of L2sip in Production: " + response.get("serviceState"))
        else:
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "Failed to get the health state of L2sip in Production")

    def ConversationHealthCheck(self):
        logger.info("Checking the health check state of Conversation on Production")
        conversation_prod_vipurl = "https://conv-a.wbx2.com/conversation"
        conversation_prod_healthget = "/api/v1/service_health"
        response = requests.get(url=conversation_prod_vipurl+conversation_prod_healthget).json()
        if response.get("serviceState"):
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "State of Conversation in Production: " + response.get("serviceState"))
        else:
            healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "Failed to get the health state of Conversation in Production")


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    job_number = args['--job_number']
    job_url = args['--job_url']
    healthcheck_sparkpost.post_message(healthcheck_config.ROOM_ID, "Build Number:[{}]({})".format(job_number[0], job_url[0]))
    Microservices_HelathCheck().LocusProdHealthCheck()
    Microservices_HelathCheck().LocusIntHealthCheck()
    Microservices_HelathCheck().CalliopeProdHealthCheck()
    Microservices_HelathCheck().HecateProdHealthCheck()
    Microservices_HelathCheck().L2sipProdHealthCheck()
    Microservices_HelathCheck().ConversationHealthCheck()


    #
    # production = {"conversation":"url", "l2sip":"url"}
    # service_fault = [];
    #
    # for service, url in production.iteritems():
    #     get(ur):
    #     if fault:
    #         service_fault.append(service)


