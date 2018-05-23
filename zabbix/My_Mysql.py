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
        
    def __del__(self):
       #关闭连接，释放资源  
        a,b=self.connect();
        a.close()

    
    def connect(self):
        conn=pymysql.Connect(host=self.host,port=self.port,db=self.dbname,user=self.user,passwd=self.password,charset=self.charset);
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
        if sql:
            for sqlList in sql:
                executeResult = self.action_one(sqlList)
                finalResultList.append(executeResult)
        else:
            print("ERROR:param sqlList is empty.")
        return finalResultList    
     
    def action_one(self,sql):                      #查找操作  
        """执行单条sql语句"""
        if sql and isinstance(sql,str):
            con,cursor=self.connect()
            executeResult = ""
            try:
                cursor.execute(sql)
                executeResult = cursor.fetchall()
                con.commit()
                return (executeResult);  
            except Exception as e:
                print("ERROR：execute sql failed.errorInfo =",e)
                print("ERROR:FUNCTION action_one execute failed.sqlLine =",sql)
                con.rollback()
                return str(e)
        else:
            print("ERROR:param sqlLine is empty or type is not str.sqlLine = ",sql)
     
    def close(self):
        a,b=self.connect();
        b.close()
        a.close()
        
