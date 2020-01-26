import threading
import time

from send_email import send_email_with_text

TASKS = []
NUMBER_OF_TASKS = 10 
EMAIL_FROM = 'from_example@wxample.com'
EMAIL_TO = 'to_example@example.com'

def worker(text):
    send_email_with_text(text, EMAIL_FROM, EMAIL_TO)
    

def add_email_to_emails(text, timer):
    TASKS.append({"text": text, "timer": timer})
    t = threading.Timer(timer, worker, args=(text, ))
    t.start()

def get_last_tasks():
    return TASKS[-NUMBER_OF_TASKS:]
