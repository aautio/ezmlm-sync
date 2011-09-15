import gmail
import time
import queue
import sys

def main():
    username, password = sys.argv[1:]
    
    inbox = gmail.Inbox(username, password)

    while True:
        for email in inbox.unread():
            queue.publish('emails:unread', email)

        time.sleep(60) # 60 seconds

if __name__ == "__main__":
    main()
