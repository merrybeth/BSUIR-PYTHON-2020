from multiprocessing.dummy import Manager,Process

from library import models

IS_ACTIVE = False

def process_sent_queue(queue):
    while True:
        if not queue.empty():
            email = queue.get()
            email.send()


def new_send_email(email):
    if not IS_ACTIVE:
        new_send_email.queue = Manager().Queue()
        process = Process(target=process_sent_queue, args=(new_send_email.queue,))
        process.daemon = True
        process.start()
        models.IS_ACTIVE = True

    new_send_email.queue.put(email)