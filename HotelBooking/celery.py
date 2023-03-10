from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE","HotelBooking.settings")
app=Celery("HotelBooking")
app.conf.enable_utc=False
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings,namespace="CELERY")

app.conf.beat_schedule = {
    'add-every-day-morning':{
        'task': 'Hotel.task.per_task'
        ,
        # 'schedule': crontab(minute=00,hour=9),
        'schedule': crontab(minute="*/1")
    }
}

#CELERY BEAT SETTING

app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')













# import os

# from celery import Celery

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HotelBooking.settings')

# app = Celery('HotelBooking')

# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django apps.
# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print('Hello from celery')


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')