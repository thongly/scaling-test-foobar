from celery import shared_task

@shared_task
def say_hello(name):
    print 'Hello, %s' % name