import gmail
import events
import time

def main():
    while True:
        for email in gmail.unread():
            for event in events.events:
                if event.matches(email):
                    #event.handle(email)
                    pass
                else:
                    print 'Email not understood!\n\n%s' % str(email)

        time.sleep(60) # 60 seconds

if __name__ == "__main__":
    main()
