#!/usr/bin/env python
#coding=utf-8


from celery import Celery

app = Celery('tasks', broker='amqp://admin:admin@10.68.60.111:5673/devops',backend='redis://admin@10.68.60.111:26379/1')

@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    result = add.delay(30, 42)