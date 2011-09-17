
class ListEvent(object):
    def matches(self, email):
        return False

    def handle(self, email):
        # fetch url resource, compare and alter subscriptions
        pass


class ConfirmSubscribeEvent(object):
    def matches(self, email):
        return False

    def handle(self, email):
        # respond with confirmation email
        pass

class ConfirmUnsubscribeEvent(object):
    def matches(self, email):
        return False

    def handle(self, email):
        # respond with confirmation email
        pass
    
events = (ListEvent(), ConfirmSubscribeEvent(), ConfirmUnsubscribeEvent())
