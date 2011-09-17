
events = (ListEvent(), ConfirmSubscribeEvent(), ConfirmUnsubscribeEvent())

class ListEvent(object):
    def matches(email):
        return False

    def handle(email):
        # fetch url resource, compare and alter subscriptions
        pass


class ConfirmSubscribeEvent(object):
    def matches(email):
        return False

    def handle(email):
        # respond with confirmation email
        pass

class ConfirmUnsubscribeEvent(object):
    def matches(email):
        return False

    def handle(email):
        # respond with confirmation email
        pass
    
