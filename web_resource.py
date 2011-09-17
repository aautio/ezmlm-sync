import urllib2
import utils
import queue

def poll_resource(url):
    emails, errors = fetch_and_split(url)

    if errors:
        queue.publish('resource:errors', errors)

    return emails


def fetch_and_split(url):
    rows = [row.strip() for row in urllib2.urlopen(url)]
    return utils.split_with_condition(rows, utils.is_valid_email)



