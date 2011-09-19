import app.gmail as gmail
import app.emails as emails
import time

def main():
    while True:
        for email in gmail.unread():
            consume(email)

        # check inbox every 10 minutes
        time.sleep(60 * 10)

def consume(email):
    for e in emails.types:
        if e.matches(email):
            e.handle(email)
            return
    
    print 'Email not understood!\n\n%s' % email
    

if __name__ == "__main__":
    main()
