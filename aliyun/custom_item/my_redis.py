#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python 2X

import sys
import socket
import re
import StringIO
import os
import redis
import time

class my_redis_A(object):
    def __init__(self,ipp):
        self.ipport = ipp
    def redis_con(self,order,ip,port,db=0):
        try:
            s=socket.socket()
            s.settimeout(5) 
            s.connect((ip,int(port)))
            s_redis1 = redis.Redis(host=ip,port=port)
            data_mntr = s_redis1.info()
            if (data_mntr == "" or data_mntr == None) :
                print "something wrong"
                sys.exit(1) 
            else:
                return data_mntr
        except Exception as e:
            print Exception,":", e
        finally:
            pass
    def redis_ip_list(self,ipp):
            result={}        
            key,value=ipp.split(':')
            result['ip']=key
            result['port']=value  
            return result
    def __redis_order_ready_go(self):
        try:
            order='go'   
            ipp2=self.ipport
            ip_list=self.redis_ip_list(ipp2)
            ip_result=self.redis_con(order,ip_list['ip'],ip_list['port'])
            ip_result           
            return ip_result
        except Exception as e:
            print Exception,":", e
    def redis_order_once(self,order):
        redis_result=self.__redis_order_ready_go()
        if order in order in ['used_memory_human','connected_clients']:
            my_result=redis_result[order]
            return str(my_result)
        else:
            return 'your order is wrong'
    def __redis_order_qps_once_count(self,order,time1):
        redis_result=self.__redis_order_ready_go()
        my_result=redis_result[order]
        time.sleep(time1)
        redis_result=self.__redis_order_ready_go()
        my_result1=redis_result[order]
        if my_result1 > my_result:
            return str((int(my_result1)-int(my_result))/5)
        else:
            return 0
    def redis_order_qps_once(self,order):
        if order == 'total_commands_processed':
            return str(self.__redis_order_qps_once_count(order,5))     
        elif order == 'keyspace_misses':
            return str(self.__redis_order_qps_once_count(order,5)) 
        else:
            return 'your order is wrong'
        
if __name__ == '__main__':
    a=my_redis_A('10.62.11.76:6379')
    print a.redis_order_qps_once('total_commands_processed')
    print a.redis_order_qps_once('keyspace_misses')
    print a.redis_order_once('used_memory_human')
    print a.redis_order_once('connected_clients')
