import app.gmail as gmail
import app.emails as emails

from app.sleepy_thread import *
from app.settings import *

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
    
    gmail.send(error_mail, 'Email not understood!\n\n%s' % email)

def main():
    filename = "delete_to_shutdown.txt"
    create_marker_file(filename)

    start_thread(check_inbox, filename, 30 * 60)
    start_thread(order_list, filename, 2 * 60 * 60)


if __name__ == "__main__":
    main()
