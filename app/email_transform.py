import queue
import events

def consume(email):
    for event in events.events:
        if event.matches(email):
            # event.handle(email)
            return True
    return False

def listen_and_transform():
    for email in queue.messages('emails:unread'):
        if not consume(email):
            # TODO: mail the message to admin?
            print 'Email not understood: /n%s' % email
