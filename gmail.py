import imaplib
import smtplib
import email

class Outbox(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def send(self, to_addrs, msg = ""):
        print 'Sending mail to %s' % str(to_addrs)
        smtp = smtplib.SMTP('smtp.gmail.com:587')
        smtp.starttls()
        smtp.login(self.username, self.password)
        
        smtp.sendmail(self.username, to_addrs, str(msg))

        print 'Mail sent'
        smtp.quit()


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

        print 'No more unread emails'
        imap.close()
        imap.logout()
