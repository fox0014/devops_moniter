#!/usr/bin/env python
#coding=utf-8

from __future__ import absolute_import
import datetime
from mymain import app
from celery import Celery
from ..inspection_client.inspection_client_Regions import Regionsmain
from ..db.MyMongo import Mypy_mongo1

mongdb_list='10.68.60.114:27017','','','moniter',117,'AliyunServer','rs0','secondaryPreferred'

@app.task
def add(x, y):
    return x + y

@app.task
def aliyuntaskRegionsmain(accessKey,accessSecret,region):
    result = Regionsmain(accessKey,accessSecret,region)
    Today = Mypy_mongo1(server='10.68.60.114:27017',user='',passwd='',authSource='moniter',action_date=117,des_collections='Aliyunmetadata',replicaSet='rs0',readPreference='readPreference')
    Today.conn()
    Today.collecion_insert({'aliyuntype':'aliyunRegions','zone':result,'date':datetime.datetime.now()})
    return result

if __name__ == '__main__':
    result = add.delay(30, 42)
