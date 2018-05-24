#!/usr/bin/python  
# -*- coding:utf-8 -*-

import time,os,re
import My_Mysql
import shelve



class my_Mysql_status(My_Mysql.my_Mysql_init):
    def __init__(self,host,port,dbname,user,password,charset="utf8"):
        super(my_Mysql_status,self).__init__(host,port,dbname,user,password,charset="utf8")
    def the_sql_init(self):
        connect,cursor=self.connect()
        return connect
    def the_sql_cursor(self):
        connect,cursor=self.connect()
        return cursor
    def the_sql_ping(self):
        mysql=self.the_sql_init()
        mysql.ping() 
    def sql_processlist(self):
        return len(self.action_one("SHOW FULL PROCESSLIST"))
    def dbname_db_data(self,dbname):        
        big_data1=self.action_one("SELECT CONCAT(ROUND(SUM(data_length/1024/1024),2),'MB') AS DATA FROM information_schema.tables WHERE table_schema='%s'" % dbname)
        big_data_result=big_data1[0]
        return str(big_data_result)
    

class my_Mysql_status_cache(My_Mysql.my_Mysql_init):
    def __init__(self,host,port,dbname,user,password,charset="utf8"):
        super(my_Mysql_status_cache,self).__init__(host,port,dbname,user,password,charset="utf8")
    def cache_init(self,filename='mysql_cache_db'):
        cache = shelve.open(filename, writeback=True)
        return cache
    def cache_close(self):
        self.cache_init().close()
    def cache_read(self):
        cache=self.cache_init()
        return cache
    def the_sql_init(self):
        connect,cursor=self.connect()
        return connect
    def the_sql_cursor(self):
        connect,cursor=self.connect()
        return cursor
    def the_sql_ping(self):
        mysql=self.the_sql_init()
        mysql.ping() 
    def sql_processlist(self):
        cache=self.cache_init()
        len_list=len(self.action_one("SHOW FULL PROCESSLIST"))
        cache['mysql_rtstatus']={"sql_processlist": len_list}
        return len_list
    def dbname_db_data(self,dbname):        
        big_data1=self.action_one("SELECT CONCAT(ROUND(SUM(data_length/1024/1024),2),'MB') AS DATA FROM information_schema.tables WHERE table_schema='%s'" % dbname)
        big_data_result=big_data1[0]
        return str(big_data_result)
    def dbname_db_data_all(self):
        my_temporary={}
        namelist=self.action_one('SHOW DATABASES')
        cache=self.cache_init()
        for name in namelist:
            if name[0] != "information_schema" and name[0] !="performance_schema":
                print name
                data1=self.dbname_db_data(name)
                my_temporary[name]=data1
        cache['mysql_data']=my_temporary

     

if __name__ == '__main__':
    try:
        aa=my_Mysql_status_cache("10.62.11.51",3306,"mytest01","admin","admin")
        try:
            aa.the_sql_ping()
            aa.dbname_db_data_all()
            print aa.sql_processlist()
            print aa.cache_read()
            aa.cache_close()
        except Exception,e:
            print 'remote mysql have something wrong %s' % e
            aa=my_Mysql_status_cache("10.62.11.51",3306,"mytest01","admin","admin")
    except Exception,e:
        print Exception,":",e
