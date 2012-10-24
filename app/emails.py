import re
import web_resource
from utils import emailregex, diffs_of_lists

from settings import ezmlm_listnames as listnames
from settings import ezmlm_domain as domain

import gmail

listregex = re.compile("Hi! This is the ezmlm program\. I'm managing the\r?\n(" \
    + emailregex + ") mailing list\.\r?\n\r?\nI'm working for my " \
    + "owner, who can be reached\r?\nat (" + emailregex + ")\.\r?\n\r?\n\r?\n?" \
    + "Subscribers to this list are:\r?\n\r?\n" \
    + "((?:" + emailregex + "\r?\n)*)")

class ListEmail(object):
    def matches(self, email):
        return listregex.search(email) != None

    def handle(self, email):
        # compare and alter subscriptions
        result = listregex.search(email)
        listname = self.get_listname(result.group(1))
        list_emails = result.group(3).split()
        
        url_emails = web_resource.poll(listname)
        
        sub, unsub = diffs_of_lists(url_emails, list_emails)

        sub = map(self.to_subscribe_cmd(listname), sub)
        unsub = map(self.to_unsubscribe_cmd(listname), unsub)

        if sub + unsub:
            gmail.send(sub + unsub)
        

    def to_subscribe_cmd(self, listname):
        def f(email):
            return "%s-subscribe-%s@%s" % (listname, email.replace('@', '='), domain)
        return f
        
    def to_unsubscribe_cmd(self, listname):
        def f(email):
            return "%s-unsubscribe-%s@%s" % (listname, email.replace('@', '='), domain)
        return f

    def get_listname(self, listaddress):
        return listaddress[:listaddress.rfind("@")]


cseregex = re.compile("Hi! This is the ezmlm program\. I'm managing the\r?\n(" \
    + emailregex + ") mailing list\.\r?\n\r?\nI'm working for my " \
    + "owner, who can be reached\r?\nat (" + emailregex + ")\.\r?\n\r?\n?" \
    + "I respectfully request your permission to add\r?\n\r?\n   (" \
    + emailregex + ")\r?\n\r?\nto the subscribers of the .* mailing list. " \
    + "This request\r?\neither came from you, or it has already been verified " \
    + "by\r?\nthe potential subscriber.\r?\n\r?\nTo confirm, please send an " \
    + "empty reply to this address:\r?\n\r?\n   (" + emailregex + ")")
                         
class ConfirmSubscribeEmail(object):
    def matches(self, email):
        return cseregex.search(email) != None

    def handle(self, email):
        # respond with confirmation email
        confirm_to = cseregex.search(email).group(4)
        gmail.send(confirm_to)

cuseregex = re.compile("Hi! This is the ezmlm program\. I'm managing the\r?\n(" \
    + emailregex + ") mailing list\.\r?\n\r?\nI'm working for my " \
    + "owner, who can be reached\r?\nat (" + emailregex + ")\.\r?\n\r?\n?" \
    + "A request has been made to remove\r?\n\r?\n   (" + emailregex + ")\r?\n\r?\n" \
    + "from the .* mailing list\. If you agree, please send\r?\nan empty reply " \
    + "to this address:\r?\n\r?\n   (" + emailregex + ")")

class ConfirmUnsubscribeEmail(object):
    def matches(self, email):
        return cuseregex.search(email) != None

    def handle(self, email):
        # respond with confirmation email
        confirm_to = cuseregex.search(email).group(4)
        gmail.send(confirm_to)
    
types = (ListEmail(), ConfirmSubscribeEmail(), ConfirmUnsubscribeEmail())
