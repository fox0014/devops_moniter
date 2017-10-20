#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python 2X

import my_redis
import cms_post
import re,sys,time
import ConfigParser
import my_structure_tools
import my_daemon
from multiprocessing.dummy import Pool as ThreadPool

redis_result1 = {}
gogo_list = ('redis', 'mysql')
name_list2 = ('keyspace_misses', 'connected_clients', 'used_memory_human', 'total_commands_processed')
ip = '10.161.137.208:7397'



def redis_pull(order):    
    if order in ['keyspace_misses', 'total_commands_processed']:           
        the_test_begin_print()
        b = my_redis.my_redis_A(ip)
        b1 = b.redis_order_qps_once(order)
        b1=re.sub("[A-Z a-z]", "", b1)
        my_structure_tools.dict_action_set(redis_result1, gogo_list, 'redis', ip, order, b1)
        the_test_end_print()         
    elif order in ['used_memory_human', 'connected_clients']:
        the_test_begin_print()
        b = my_redis.my_redis_A(ip)       
        b1 = b.redis_order_once(order)
        b1=re.sub("[A-Z a-z]", "", b1)
        my_structure_tools.dict_action_set(redis_result1, gogo_list, 'redis', ip, order, b1)
        the_test_end_print()
    else:
        return 'your order is wrong'
    
def redis_push(order):
    key1 = order
    the_test_begin_print()
    b1 = my_structure_tools.dict_action_get(redis_result1, 'redis', ip, key1)
# aliyun
    if order == 'keyspace_misses':
        cms_post.post("1869047806262459", "pro_redis_info", b1, "None", "info_id=redis_client_misskey_qps")
    elif order == 'connected_clients':
        cms_post.post("1869047806262459", "pro_redis_info", b1, "None", "info_id=redis_connect")
    elif order == 'used_memory_human':
        cms_post.post("1869047806262459", "pro_redis_info", b1, "None", "info_id=redis_men_used")
    elif order == 'total_commands_processed':
        cms_post.post("1869047806262459", "pro_redis_info", b1, "None", "info_id=redis_qps")
    else:
        pass
        
def the_test_begin_print():
    pass
#    print "all begins %s" % time.ctime()

def the_test_end_print():
    pass
#    print "all end %s" % time.ctime()

def my_main_redis_set(order, num):
    pool = ThreadPool(num)
    pool.map_async(order, name_list2)
    pool.close()
    pool.join()
    
class MyDaemon(my_daemon.Daemon):  
    def run(self):  
        while True:
            my_main_redis_set(redis_pull, 4)
            my_main_redis_set(redis_push, 2) 
            time.sleep(40)
        
if __name__ == "__main__":  
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:  
        if 'start' == sys.argv[1]:  
            daemon.start()  
        elif 'stop' == sys.argv[1]:  
            daemon.stop()  
        elif 'restart' == sys.argv[1]:  
            daemon.restart()  
        else:  
            print "Unknown command"  
            sys.exit(2)  
        sys.exit(0)  
    else:  
        print "usage: %s start|stop|restart" % sys.argv[0]  
        sys.exit(2)       
    
