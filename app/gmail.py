import imaplib
import smtplib
import email

from app.settings import gmail_username as username
from app.settings import gmail_password as password

def send(to_addrs, msg = ""):
    print 'Sending mail to %s' % str(to_addrs)
    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.starttls()
    smtp.login(username, password)
    
    smtp.sendmail(username, to_addrs, str(msg))
    
    print 'Mail sent'
    smtp.quit()

    
def unread():
    print 'Checking for unread emails'
    imap = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    imap.login(username, password)
    
    imap.select('Inbox')
    status, data = imap.search(None, 'UNSEEN')
    # msgs is a list of unread email numbers
    msgs = data[0].split()
    print 'Found %d messages' % len(msgs)
    
    for msg in msgs:
        print 'Fetching message id %s' % msg
        status, data = imap.fetch(msg, '(RFC822)')

        print 'Yielding fetched msg'
        yield data[0][1]

    print 'No more unread emails'
    imap.close()
    imap.logout()
