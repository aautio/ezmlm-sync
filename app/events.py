import re
from utils import emailregex

class ListEvent(object):
    def matches(self, email):
        return False

    def handle(self, email):
        # fetch url resource, compare and alter subscriptions
        pass

cseregex = "Hi! This is the ezmlm program\. I'm managing the\n(" \
    + emailregex + ") mailing list\.\n\nI'm working for my " \
    + "owner, who can be reached\nat (" + emailregex + ")\.\n\n" \
    + "To confirm that you would like\n\n   (" + emailregex + ")\n\n" \
    + "added to the lista mailing list, please send\nan empty reply " \
    + "to this address:\n\n   (" + emailregex + ")"
                         
class ConfirmSubscribeEvent(object):
    def matches(self, email):
        return re.search(cseregex, email) != None

    def handle(self, email):
        # respond with confirmation email
        confirm_to = re.search(cseregex, email).group(4)
        # send email to confirm_to

class ConfirmUnsubscribeEvent(object):
    def matches(self, email):
        return False

    def handle(self, email):
        # respond with confirmation email
        pass
    
events = (ListEvent(), ConfirmSubscribeEvent(), ConfirmUnsubscribeEvent())
