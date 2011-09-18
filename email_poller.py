import app.gmail as gmail
import app.events as events
import time

def main():
    while True:
        for email in gmail.unread():
            consume(email)
            
        time.sleep(10) # 60 seconds

def consume(email):
    for event in events.events:
        if event.matches(email):
            event.handle(email)
            return
    
    print 'Email not understood!\n\n%s' % email
    

if __name__ == "__main__":
    main()
