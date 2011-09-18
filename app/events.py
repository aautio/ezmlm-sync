import re
import web_resource
from utils import emailregex, diffs_of_lists

listregex = re.compile("Hi! This is the ezmlm program\. I'm managing the\n(" \
    + emailregex + ") mailing list\.\n\nI'm working for my " \
    + "owner, who can be reached\nat (" + emailregex + ")\.\n\n" \
    + "Subscribers to this list are:\n\n" \
    + "((?:" + emailregex + "\n)*)")

class ListEvent(object):
    def matches(self, email):
        return listregex.search(email) != None

    def handle(self, email):
        list_emails = listregex.search(email).group(3).split()
        url_emails = web_resource.poll()
        
        # compare and alter subscriptions
        sub, unsub = diffs_of_lists(url_emails, list_emails)
        # TODO send email (1 is enough)


cseregex = re.compile("Hi! This is the ezmlm program\. I'm managing the\n(" \
    + emailregex + ") mailing list\.\n\nI'm working for my " \
    + "owner, who can be reached\nat (" + emailregex + ")\.\n\n" \
    + "To confirm that you would like\n\n   (" + emailregex + ")\n\n" \
    + "added to the .* mailing list, please send\nan empty reply " \
    + "to this address:\n\n   (" + emailregex + ")")
                         
class ConfirmSubscribeEvent(object):
    def matches(self, email):
        return cseregex.search(email) != None

    def handle(self, email):
        # respond with confirmation email
        confirm_to = cseregex.search(email).group(4)
        # send email to confirm_to

cuseregex = re.compile("Hi! This is the ezmlm program\. I'm managing the\n(" \
    + emailregex + ") mailing list\.\n\nI'm working for my " \
    + "owner, who can be reached\nat (" + emailregex + ")\.\n" \
    + "A request has been made to remove\n\n   (" + emailregex + ")\n\n" \
    + "from the .* mailing list\. If you agree, please send\nan empty reply " \
    + "to this address:\n\n   (" + emailregex + ")")

class ConfirmUnsubscribeEvent(object):
    def matches(self, email):
        return cuseregex.search(email) != None

    def handle(self, email):
        # respond with confirmation email
        confirm_to = cuseregex.search(email).group(4)
        pass
    
events = (ListEvent(), ConfirmSubscribeEvent(), ConfirmUnsubscribeEvent())
