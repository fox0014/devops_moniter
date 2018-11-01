#!/usr/bin/env python
#coding=utf-8

from celery import Celery
from inspection_client.inspection_client_Regions import Regionsmain
from db.MyMongo import Mypy_mongo1

app = Celery('tasks', broker='amqp://admin:admin@10.68.60.111:5673/devops',backend='redis://:admin@10.68.60.111:26379/1')
mongdb_list='10.68.60.114:27017','','','moniter',117,'AliyunServer','rs0','secondaryPreferred'

@app.task
def add(x, y):
    return x + y

@app.task
def aliyuntaskRegionsmain(accessKey,accessSecret,region):
    result = Regionsmain(accessKey,accessSecret,region)
    Today = Mypy_mongo1(server='10.68.60.114:27017',user='',passwd='',authSource='moniter',action_date=117,des_collections='AliyunServer',replicaSet='rs0',readPreference='readPreference')
    Today.conn()
    Today.collecion_insert({'zone':result})
    return result

if __name__ == '__main__':
    result = add.delay(30, 42)
