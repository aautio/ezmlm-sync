import app.gmail as gmail
import app.emails as emails

from app.settings import error_email

def check_inbox():
    for email in gmail.unread():
        consume(email)

def consume(email):
    for e in emails.types:
        if e.matches(email):
            e.handle(email)
            return

    gmail.send(error_email, 'Email not understood!\n\n%s' % email)

def main():
    check_inbox()

if __name__ == "__main__":
    main()
