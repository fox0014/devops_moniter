#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python 2X

import my_redis
import time
import re
import ConfigParser
import my_structure_tools
from multiprocessing.dummy import Pool as ThreadPool


redis_result1={}
gogo_list=('redis','mysql')
name_list2=('keyspace_misses','keyspace_misses','total_commands_processed','keyspace_misses','connected_clients','used_memory_human','total_commands_processed')
ip='10.62.11.76:6379'

#with open('my_Monitor.conf', 'r') as f:
#    conf1=ConfigParser.ConfigParser()
#    conf1.read('my_Monitor.conf')
#    conf1_redis_server_list1=conf1.options('redis_server')
#    conf1_redis_server_default_port=conf1.get('redis_server_deafult','server_deafult_port')


def redis_pull(order):    
    if order in ['keyspace_misses','total_commands_processed']:           
        the_test_begin_print()
        b=my_redis.my_redis_A(ip)
        b1=b.redis_order_qps_once(order)
        the_test_end_print()
        my_structure_tools.dict_action_set(redis_result1,gogo_list,'redis',ip,order,b1)            
    elif order in ['used_memory_human','connected_clients']:
        the_test_begin_print()
        b=my_redis.my_redis_A(ip)       
        b1=b.redis_order_once(order)
        my_structure_tools.dict_action_set(redis_result1,gogo_list,'redis',ip,order,b1)
    else:
        return 'your order is wrong'
    
def redis_push(order):
    key1=order
    the_test_begin_print()
    my_structure_tools.dict_action_get(redis_result1,'redis',ip,key1)    
    the_test_end_print()
    
    
def the_test_begin_print():
    pass
#    print "all begins %s" % time.ctime()

def the_test_end_print():
    pass
#    print "all end %s" % time.ctime()

def my_main_redis_set(order,num):
    pool = ThreadPool(num)
    pool.map_async(order,name_list2)
    pool.close()
    pool.join()
    

    
if __name__ == '__main__':
    my_main_redis_set(redis_pull,4)    
#    print [re.sub("[A-Z a-z]", "", x) for x in redis_result1]
    print redis_result1
    my_main_redis_set(redis_push,2)
    print redis_result1


