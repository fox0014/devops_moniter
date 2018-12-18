#!/usr/bin/env python
#coding=utf-8

from __future__ import absolute_import
from datetime import timedelta

CELERY_RESULT_BACKEND = 'redis://:admin@10.68.60.111:26379/1'
BROKER_URL = 'amqp://admin:admin@10.68.60.111:5672/devops'
CELERY_TIMEZONE = 'Asia/Shanghai'
BROKER_POOL_LIMIT = None

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'app.tasks.tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
        },
}


