#!/usr/bin/env python
#coding=utf-8

from __future__ import absolute_import
from celery import Celery
from app.config import celeryconfig


app = Celery('app', include=['app.tasks.tasks'])
app.config_from_object(celeryconfig)
 
if __name__ == '__main__':
    app.start()
