#!/usr/bin/env python
#python 3
#pymongo3.7.1
# -*- coding:utf-8 -*-

import pymongo
import sys
import datetime
import time,random
import threading
import logging
import logging.handlers

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#log console output
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)-5s %(name)-5s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
#log RotatingFileHandler output
#Rthandler = logging.handlers.RotatingFileHandler('./Mymongoclean.log',maxBytes=10*1024*1024,backupCount=5)
#Rthandler.setLevel(logging.INFO)
#Rthandler.setFormatter(formatter)
#handler to logging
logging.getLogger('').addHandler(console)
#logging.getLogger('').addHandler(Rthandler)

class Mypy_mongo1(object):
    def __init__(self,**Ent_Data):
        self.db01=None
        self.Authmon1=Ent_Data
        self.now_1=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_1=(datetime.datetime.now() - datetime.timedelta(days = self.Authmon1['action_date'])).strftime("%Y-%m-%d %H:%M:%S")
        self.des_collections=self.Authmon1['des_collections']
    def conn(self):
        '''
        replicaSet
            uri = "mongodb://%s:%s@%s/?replicaSet=elinkmongo!1&authSource=%s&connectTimeoutMS=300000&readPreference=%s" % (
    "qs", "qs123456", "10.62.11.76:37017,10.62.11.77:37018,10.62.11.75:37018","qs","secondaryPreferred")
        '''       
        try:
            if not self.Authmon1['user']:
                uri = "mongodb://%s/?replicaSet=%s&authSource=%s&readPreference=%s" % (
                    self.Authmon1['server'],
                    self.Authmon1['replicaSet'],
                    self.Authmon1['authSource'],
                    self.Authmon1['readPreference']
                    )
            elif self.Authmon1['replicaSet'] and self.Authmon1['readPreference']:
                uri = "mongodb://%s:%s@%s/?replicaSet=%s&authSource=%s&readPreference=%s" % (
                    self.Authmon1['user'], 
                    self.Authmon1['passwd'],
                    self.Authmon1['server'],
                    self.Authmon1['replicaSet'],
                    self.Authmon1['authSource'],
                    self.Authmon1['readPreference']
                    )
            else:
                uri = "mongodb://%s:%s@%s/?authSource=%s" % (
                    self.Authmon1['user'], 
                    self.Authmon1['passwd'],
                    self.Authmon1['server'],
                    self.Authmon1['authSource']
                    )
            client02=pymongo.MongoClient(uri)
            client02.admin.command('ismaster')
            db = client02.get_database(self.Authmon1['authSource'])
            self.db01=db
            return db
        except Exception as e:
            logging.error('msg:%s'% e)
            sys.exit()
    def collecion_count(self):
        dblist=self.db01.collection_names()
        dbcollecion_info=self.db01[self.des_collections].count()
        logging.info('Dbname: %s ,IP: %s ,Collections: %s' % (self.Authmon1['authSource'],self.Authmon1['server']+':',dblist))
        logging.info('Dbname: %s ,IP: %s ,%s conunt: %s' % (self.Authmon1['authSource'],self.Authmon1['server']+':',self.des_collections,dbcollecion_info))
    def collecion_del(self):
        item3 = self.db01[self.des_collections].delete_many({'createdAt':{"$lt":self.date_1}})
        now_1=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info('Dbname: %s ,IP: %s ,%s Collections %s del count: %s' % (self.Authmon1['authSource'],self.Authmon1['server']+':',now_1,self.Authmon1['authSource'],item2.deleted_count)) 
    def collecion_insert(self,data):
        item3 = self.db01[self.des_collections].insert(data)
        now_1=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info('Dbname: %s ,IP: %s ,%s Collections %s del count: %s' % (self.Authmon1['authSource'],self.Authmon1['server']+':',now_1,self.Authmon1['authSource'],item3)) 

def my_mongo_del(server,user,passwd,authSource,action_date,des_collections,replicaSet,readPreference):
    Today = Mypy_mongo1(server=server,user=user,passwd=passwd,authSource=authSource,action_date=action_date,des_collections=des_collections,replicaSet=replicaSet,readPreference=readPreference)
    Today.conn()
    Today.collecion_insert({"name":"sun","rank":"3"})
    Today.collecion_count()

if __name__ == '__main__':
    s1_list='10.68.60.114:27017','','','moniter',117,'AliyunServer','rs0','secondaryPreferred'
    s_list=s1_list
    rr=random.randint(5,15)
    s=threading.Timer(rr,my_mongo_del,(s_list))
    logging.debug("now thead {}".format(threading.activeCount()))
    logging.debug("threading active = {} \n".format(threading.enumerate()))
    s.start()
