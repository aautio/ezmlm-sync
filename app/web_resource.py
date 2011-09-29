import urllib2
import utils
import gmail

from settings import web_resource_url as url
from settings import error_email

def poll():
    emails, errors = fetch_and_split(url)

    if errors:
        gmail.send(error_email, "Erronous emails detected: %s" % str(errors))

    return emails


def fetch_and_split(url):
    rows = [row.strip() for row in urllib2.urlopen(url)]
    return utils.split_with_condition(rows, utils.is_valid_email)



