import os.path
import time
import threading

import app.gmail as gmail
import app.emails as emails

from app.settings import *

def create_marker_file(filename):
    f = open(filename, 'w')
    f.write("email_poller.py is running. " \
            + "You can shut it down by deleting this file. " \
            + "The shutdown sequence will take a few minutes.")
    f.close()

def should_continue(filename):
    return os.path.isfile(filename)

def sleepy_thread(callback, filename, sleepytime):
    while should_continue(filename):
        callback()
        time.sleep(sleepytime)

def order_list():
    gmail.send(ezmlm_listname + "-list@" + ezmlm_domain)

def check_inbox():
    for email in gmail.unread():
        consume(email)

def consume(email):
    for e in emails.types:
        if e.matches(email):
            e.handle(email)
            return
    
    print 'Email not understood!\n\n%s' % email        

def main():
    filename = "keepalive.txt"
    create_marker_file(filename)
    print "Starting poller threads. Shut it down by deleting %s" % filename

    t1 = threading.Thread(target=sleepy_thread, args=(check_inbox, filename, 30 * 60))
    t2 = threading.Thread(target=sleepy_thread, args=(order_list, filename, 2 * 60 * 60))
    
    t1.start()
    t2.start()
    

if __name__ == "__main__":
    main()
