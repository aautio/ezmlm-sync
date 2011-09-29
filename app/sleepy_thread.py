import os.path
import time
import threading

def start_thread(callback, filename, sleepytime):
     t = threading.Thread(target=sleepy_thread, args=(callback, filename, sleepytime))
     t.start()

def create_marker_file(filename):
    f = open(filename, 'w')
    f.write("ezmlm-sync might be running. Ask it to shutdown by deleting this file.")
    f.close()

def should_continue(filename):
    return os.path.isfile(filename)

def sleepy_thread(callback, filename, sleepytime):
    while should_continue(filename):
        callback()
        time.sleep(sleepytime)
