from celery.decorators import task
from celery.utils.log import get_task_logger
from skeleton.celery import app

logger = get_task_logger(__name__)


@app.task(name='test_celery')
def print_name_celery(name):
    """print name for test"""
    logger.info('Celery Test')
    print(f'My name is {name}')