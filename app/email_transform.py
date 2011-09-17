import queue

def to_event(email):
    pass

def listen_and_transform():
    for email in queue.messages('emails:unread'):
        channel, message = to_event(email['data'])

        if channel and message:
            queue.publish(channel, message)
        else:
            # TODO: mail the message to admin?
            print 'Email not understood: /n%s' % email
