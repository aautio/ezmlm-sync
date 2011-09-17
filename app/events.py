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
    + "added to the .* mailing list, please send\nan empty reply " \
    + "to this address:\n\n   (" + emailregex + ")"
                         
class ConfirmSubscribeEvent(object):
    def matches(self, email):
        return re.search(cseregex, email) != None

    def handle(self, email):
        # respond with confirmation email
        confirm_to = re.search(cseregex, email).group(4)
        # send email to confirm_to

cuseregex = "Hi! This is the ezmlm program\. I'm managing the\n(" \
    + emailregex + ") mailing list\.\n\nI'm working for my " \
    + "owner, who can be reached\nat (" + emailregex + ")\.\n" \
    + "A request has been made to remove\n\n   (" + emailregex + ")\n\n" \
    + "from the .* mailing list\. If you agree, please send\nan empty reply " \
    + "to this address:\n\n   (" + emailregex + ")"

class ConfirmUnsubscribeEvent(object):
    def matches(self, email):
        return re.search(cuseregex, email) != None

    def handle(self, email):
        # respond with confirmation email
        confirm_to = re.search(cuseregex, email).group(4)
        pass
    
events = (ListEvent(), ConfirmSubscribeEvent(), ConfirmUnsubscribeEvent())
