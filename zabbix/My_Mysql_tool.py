#!/usr/bin/python  
# -*- coding:utf-8 -*-

import time,os,re
import My_Mysql


class my_Mysql_sql(My_Mysql.my_Mysql_init):
    def __init__(self,host,port,dbname,user,password,charset="utf8"):
        super(my_Mysql_sql,self).__init__(host,port,dbname,user,password,charset="utf8")
    def the_sql_ping(self):
        a,b= a,b=self.connect();
        a.ping() 
    def sql_processlist(self):
        return self.action_one("SHOW FULL PROCESSLIST")
    def len_sql_processlist(self):
        return len(self.sql_processlist())
    def sql_status(self):
        return self.action_one("SHOW GLOBAL STATUS")
    def sql_select_status(self):
        return self.action_one("select * from information_schema.GLOBAL_STATUS")
 

if __name__ == '__main__':
    try:
        aa=my_Mysql_sql("10.62.11.51",3306,"mytest01","admin","admin")
        try:
            aa.the_sql_ping()
            print aa.action_one("show databases")
        except:
            print 'remote mysql have something wrong'
            aa=my_Mysql_sql("10.62.11.51",3306,"mytest01","admin","admin")
    except Exception,e:
        print Exception,":",e
