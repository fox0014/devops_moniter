#!/usr/bin/python  
# -*- coding:utf-8 -*-

import time,os,re
import pymysql
import pymysql.cursors
import My_Mysql


class my_Mysql_sql(My_Mysql.my_Mysql_init):
    def __init__(self,host1,user1,password1,port1):
        My_Mysql.my_Mysql_init.__init__(self,host1,user1,password1,port1)
    def the_sql_ping(self):
        self.conn.ping() 
    def the_sql_init(self,sql):
        tt=My_Mysql.my_Mysql_init.Query(self,sql)
        return tt
    def sql_processlist(self):
        return self.the_sql_init("SHOW FULL PROCESSLIST")
    def len_sql_processlist(self):
        return len(self.sql_processlist())
    def sql_status(self):
        return self.the_sql_init("SHOW GLOBAL STATUS")
    def sql_select_status(self):
        return self.the_sql_init("select * from information_schema.GLOBAL_STATUS")
    def dbname_db_data(self,dbname):        
        big_data1=self.the_sql_init("SELECT CONCAT(ROUND(SUM(data_length/1024/1024),2),'MB') AS DATA FROM information_schema.tables WHERE table_schema='%s'" % dbname)
        big_data_result=big_data1[0]['DATA']
        return str(big_data_result)     
    def sql_select_status_ques(self):
        my_status=self.sql_select_status()
        for my_pl_t1 in my_status:
            if my_pl_t1['VARIABLE_NAME'] == 'QUESTIONS':
                my_status_ques=my_pl_t1['VARIABLE_VALUE']
        return my_status_ques
    def sql_qps(self,**args):
        k1=self.sql_select_status_ques()
        time.sleep(args['sleep_time']) 
        k2=self.sql_select_status_ques()
        pingjun1=(int(k2)-int(k1))/args['sleep_time']
        if pingjun1<1:
            return 1
        else:
            return pingjun1
    def sql_processlist_log_Time(self,log_time):
        i=0
        my_len=self.sql_processlist()
        for my_pl_t1 in my_len:
            if (my_pl_t1['Time'] > log_time and my_pl_t1['Command'] != 'Sleep'):
                i+=1
            return i
    """ not need
    def GetPathSize(self,strPath):  
        if not os.path.exists(strPath):  
            return 0;  
        if os.path.isfile(strPath):  
            return os.path.getsize(strPath);  
        nTotalSize = 0;  
        for strRoot, lsDir, lsFiles in os.walk(strPath):  
            #get child directory size  
            for strDir in lsDir:  
                nTotalSize = nTotalSize + self.GetPathSize(os.path.join(strRoot, strDir));  
            #for child file size  
            for strFile in lsFiles:  
                nTotalSize = nTotalSize + os.path.getsize(os.path.join(strRoot, strFile));  
        return (nTotalSize/1024/1024/15);
    """
    def monitor_MySQL_replication(self):
        result1=self.the_sql_init("SHOW SLAVE STATUS;")
        result=result1[0]
        if result['Slave_IO_Running'] == "Yes" and result['Slave_SQL_Running'] == "Yes":
            return(2)
        else:
            return(0)
    def my_mysql_status(self,order):
        pattern1 = re.compile(r'\w+_db_data')
        if order in ['sql_processlist_log_Time']:
            return str(self.sql_processlist_log_Time(120))
        elif order in ['connected_clients']:
            return str(self.len_sql_processlist())
        elif order in ['sql_qps']:
            return str(self.sql_qps(sleep_time=5))
        elif order in ['monitor_MySQL_replication']:
            return str(self.monitor_MySQL_replication())
        elif pattern1.match(order):
            order1=re.split(r'_db_data',order)
            return str(self.dbname_db_data(order1[0]))        
        else:
            return 'your order is wrong'
        

if __name__ == '__main__':
    try:
        aa=my_Mysql_sql("10.62.11.51","admin","admin",3306)
        try:
            aa.the_sql_ping()
        except:
            print 'remote mysql have something wrong'
            aa=my_Mysql_sql("10.62.11.51","admin","admin",3306)
        print aa.my_mysql_status('sql_processlist_log_Time')
        print aa.my_mysql_status('connected_clients')
        print aa.my_mysql_status('sql_qps')
        print aa.my_mysql_status('monitor_MySQL_replication')
        print aa.my_mysql_status('evcharge_zabbix_pro_db_data')
    except Exception,e:
        print Exception,":",e