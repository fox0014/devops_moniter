#!/usr/bin/python
# -*- coding:utf-8 -*-

import time,os,re
import tool.data.My_Mysql,tool.My_Log,tool.My_Config,tool.logic.My_Tool
import shelve
import sys,json
import logging

reload(sys)
sys.setdefaultencoding('utf-8') 
logger = logging.getLogger(__name__)


class my_Mysql_status(tool.data.My_Mysql.my_Mysql_init):
    def __init__(self,host,port,dbname,user,password,charset="utf8"):
        super(my_Mysql_status,self).__init__(host,port,dbname,user,password,charset="utf8")
    def the_sql_init(self):
        connect,cursor=self.connect()
        my_conId=self.action_one('SELECT CONNECTION_ID();')    
        logger.info("%s is connect ID %s" % (self.host,my_conId[0]['CONNECTION_ID()']))
        return connect
    def the_sql_cursor(self):
        connect,cursor=self.connect()
        return cursor
    def the_sql_ping(self):
        mysql=self.the_sql_init()
        mysql.ping() 
    def sql_processlist(self):       
        return len(self.action_one("SHOW FULL PROCESSLIST"))
    def dbname_db_all(self):
        namelist=self.action_one('SHOW DATABASES')        
        return namelist
    def dbname_db_data(self,dbname):        
        big_data1=self.action_one("SELECT CONCAT(ROUND(SUM(data_length/1024/1024),2),'MB') AS DATA FROM information_schema.tables WHERE table_schema='%s'" % dbname)
        return big_data1[0]
    def dbname_db_data_all(self):
        my_temporary={}
        namelist=self.dbname_db_all()
        for name in namelist:
            #转下编码，py2的痛点
            name1=name['Database']
            if name1 != "information_schema" and name1 !="performance_schema":
                data1=self.dbname_db_data(name1)
                my_temporary[name1]=data1['DATA']
        return my_temporary
    def dbname_global_status(self,order):
        return self.action_one("SHOW GLOBAL STATUS where variable_name = '%s'" % (order))
    

class my_Mysql_status_cache(tool.data.My_Mysql.my_Mysql_init):
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
        return big_data1
    def dbname_db_data_all(self):
        my_temporary={}
        namelist=self.action_one('SHOW DATABASES')  
        cache=self.cache_init()
        for name in namelist:
            #转下编码，py2的痛点
            name1=name['Database']
            if name1 != "information_schema" and name1 !="performance_schema":
                data1=self.dbname_db_data(name1)              
                print data1
                my_temporary[name1]=data1
        cache['mysql_data']=my_temporary

     

if __name__ == '__main__':
    logconfile=os.path.join(os.path.dirname(sys.argv[0]),"config","logging.ini")
    mysqlconfile=os.path.join(os.path.dirname(sys.argv[0]),"config","data.ini")
    logger=tool.My_Log.mylog(logconfile)
    try:
        myconfig=mysqlconfile
        dbhost=tool.My_Config.getConfig(myconfig,"my_mysql","dbhost")
        dbport=int(tool.My_Config.getConfig(myconfig,"my_mysql","dbport"))
        dbname=tool.My_Config.getConfig(myconfig,"my_mysql","dbname")
        dbuser=tool.My_Config.getConfig(myconfig,"my_mysql","dbuser")
        dbpassword=tool.My_Config.getConfig(myconfig,"my_mysql","dbpassword")
        dbcharset=tool.My_Config.getConfig(myconfig,"my_mysql","dbcharset")
        my_secret = tool.logic.My_Tool.prpcrypt('fansfansfansfans')
        dbpassword = my_secret.decrypt(dbpassword)
        aa=my_Mysql_status(dbhost,dbport,dbname,dbuser,dbpassword)
        try:
            aa.the_sql_ping()
            print aa.dbname_db_all()
            print aa.dbname_db_data_all()
            print aa.sql_processlist()
            aa.sql_processlist()
            aa.sql_processlist()
            print aa.dbname_global_status('Com_commit')
            aa.close()
            logger.info("%s is close" % (dbhost))
#            bb=aa.cache_read()
#            print json.dumps(bb)
#            aa.cache_close()
        except Exception,e:
            logger.exception('remote mysql have something wrong %s' % e)
            aa=my_Mysql_status(dbhost,dbport,dbname,dbuser,dbpassword)
    except Exception,e:
        logger.exception('something wrong %s' % e)
