import urllib2
import utils

from settings import web_resource_url as url

def poll():
    emails, errors = fetch_and_split(url)

    if errors:
        queue.publish('resource:errors', errors)

    return emails


def fetch_and_split(url):
    rows = [row.strip() for row in urllib2.urlopen(url)]
    return utils.split_with_condition(rows, utils.is_valid_email)



