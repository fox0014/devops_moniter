#!/usr/bin/python  
# -*- coding:utf-8 -*-

import time,os,re
import pymysql
import pymysql.cursors


#mysql 方法操作 

class my_Mysql_init(object):
    def __init__(self,host,port,dbname,user,password,charset="utf8"):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.charset = charset
    
    def connect(self):
        conn=pymysql.connect(self.host,self.port,self.dbname,self.user,self.password,self.charset);
        cur=conn.cursor();
        return conn,cur
        
    def action_many(self,sql):                      #查找操作  
        """
                            批量执行sql
        exp:    action_many([sql_1,
                                sql_2,
                                sql_3,
                                ......
                                ])
        """  
        finalResultList = []
        if sqlList:
            for sql in sqlList:
                executeResult = self.action_one(sql)
                finalResultList.append(executeResult)
        else:
            print("ERROR:param sqlList is empty.")
        return finalResultList    
     
    def action_one(self,sql):                      #查找操作  
        """执行单条sql语句"""
        if sql and isinstance(sql,str):
            connect,cursor=self.connect()
            executeResult = ""
            try:
                cursor.execute(sql)
                executeResult = cursor.fetchall()
                connect.commit()
                return (executeResult);  
            except Exception as e:
                print("ERROR：execute sql failed.errorInfo =",e)
                print("ERROR:FUNCTION executeSql execute failed.sqlLine =",sql)
                connect.rollback()
                return str(e)
        else:
            print("ERROR:param sqlLine is empty or type is not str.sqlLine = ",sql)
     
    def close(self):
        self.connect.close();
        
   # def __del__(self):                    #关闭连接，释放资源  
     #   self.cur.close(); 
    #    self.conn.close();
