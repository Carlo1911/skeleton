import os
from celery import Celery
import logging
logger = logging.getLogger('Celery')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skeleton.settings')

app = Celery('skeleton')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

