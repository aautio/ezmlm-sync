import redis

def r():
    return redis.Redis()

def publish(channel, message):
    subscribers = r().publish(channel, message)
    print "published message on %s to %s subscribers" % (channel, subscribers)

def messages(channel):
    p = r().pubsub()
    p.subscribe(channel)
    for message in p.listen():
        yield message
