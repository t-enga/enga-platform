from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platfinal.settings')

app = Celery('platfinal')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'my_scheduled_task': {
        'task': 'backtasks.task.my_scheduled_task',
        'schedule': timedelta(minutes=1),
    },
}

app.conf.timezone = 'UTC'
