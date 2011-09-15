import imaplib
import email

class Inbox(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def unread(self):
        print 'Checking for unread emails'
        imap = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        imap.login(self.username, self.password)

        imap.select('Inbox')
        status, data = imap.search(None, 'UNSEEN')
        # msgs is a list of unread email numbers
        msgs = data[0].split()
        print 'Found %d messages' % len(msgs)

        for msg in msgs:
            print 'Fetching message id %s' % msg
            status, data = imap.fetch(msg, '(RFC822)')

            print 'Yielding fetched msg'
            yield email.message_from_string(data[0][1])

        print 'No more unread messages, closing'
        imap.close()
        imap.logout()
