#!/usr/bin/env python
import argparse
import itertools
import logging
import os
import requests
import time

# Script config
CERTS_URL = 'https://review-api.udacity.com/api/v1/me/certifications.json'
ASSIGN_URL = 'https://review-api.udacity.com/api/v1/projects/{pid}/submissions/assign.json'
REVIEW_URL = 'https://review.udacity.com/#!/submissions/{sid}'
WAIT_URL = 'https://review-api.udacity.com/api/v1/submission_requests/{rid}/waits'
REQUESTS_PER_SECOND = 1 # Please leave this alone.

logging.basicConfig(format = '|%(asctime)s| %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
rid= "343573";

def request_reviews(token):
    headers = {'Authorization': token, 'Content-Length': '0'}

    certs_resp = requests.get(CERTS_URL, headers=headers)
    certs_resp.raise_for_status()

    certs = certs_resp.json()
    project_ids = [cert['project']['id'] for cert in certs if cert['status'] == 'certified']

    logger.info("PIDs: {}".format(str(project_ids)))
    logger.info(".....")

    for pid in itertools.cycle(project_ids):
        #logger.info("polling again for submissions")
        wait_resp = requests.get(WAIT_URL.format(rid=rid), headers=headers)
        waits = wait_resp.json()
        waitarr = [wait['position'] for wait in waits]
        #logger.info("wait: " + waitarr[0])
        resp = requests.post(ASSIGN_URL.format(pid = pid), headers=headers)
        if resp.status_code == 201:
            submission = resp.json()

            logger.info("")
            logger.info("=================================================")
            logger.info("A process found!")
            logger.info("View it here: " + REVIEW_URL.format(sid = submission['id']))
            logger.info("=================================================")
            logger.info("......")

        elif resp.status_code == 404:
            logger.debug("{} returned {}: No process available."
                .format(resp.url, resp.status_code))
        elif resp.status_code in [400, 422]:
            logger.debug("{} returned {}: Process limit reached."
                .format(resp.url, resp.status_code))

        else:
            resp.raise_for_status()

        time.sleep(1.0 / REQUESTS_PER_SECOND)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description =
	"Poll the Udacity reviews API to claim projects to review."
    )
    parser.add_argument('--auth-token', '-T', dest='token',
	metavar='TOKEN', type=str,
	action='store', default=os.environ.get('UDACITY_AUTH_TOKEN'),
	help="""
	    Your Udacity auth token. To obtain, login to review.udacity.com, open the Javascript console, and copy the output of `JSON.parse(localStorage.currentUser).token`.  This can also be stored in the environment variable UDACITY_AUTH_TOKEN.
	"""
    )
    parser.add_argument('--debug', '-d', action='store_true', help='Turn on debug statements.')
    args = parser.parse_args()

    if not args.token:
    	parser.print_help()
    	parser.exit()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    request_reviews(args.token)

