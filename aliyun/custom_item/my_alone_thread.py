#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python 2X

import my_redis
import threading
import time




threads = []
def redis_ye(ip,order):
    b=my_redis.my_redis_A(ip)
    b1=b.redis_order_qps_once(order)
    print b1

def main_test():
    for i in range(10):
        t1 = threading.Thread(target=redis_ye,args=('10.62.11.76:6379','total_commands_processed'))
        threads.append(t1)
    for t in threads:
        print "all begins %s" %time.ctime()
        t.setDaemon(True)
        t.start()
    [t.join(timeout=20) for t in threads]
    print "all over %s" %time.ctime()
    



if __name__ == '__main__':
    main_test()