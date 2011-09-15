import redis

def r():
    return redis.Redis()

def publish(channel, message):
    subscribers = r().publish(channel, message)
    print "published message on %s to %s subscribers" % (channel, subscribers)
