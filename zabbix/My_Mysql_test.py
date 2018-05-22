#!/usr/bin/python  
# -*- coding:utf-8 -*-

import time,os,re
import My_Mysql

mysql = My_Mysql.my_Mysql_init("10.62.11.51",3306,"mytest1","admin","admin")
#执行单行sql
ret1 = mysql.action_one("show databases")

#批量执行
ret2 = mysql.action_many([
                            "show databases",
                            "show tables",
                            "update students_info set name = '王大花D' where id = 2",
                            "select * from students_info",
                            "error sql test"
                            #异常sql测试
                              ])

print("ret1 = ",ret1)
print("---------------------")
for i in ret2:
    print(i)