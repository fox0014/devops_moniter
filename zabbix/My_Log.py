#!/usr/bin/python  
# -*- coding:utf-8 -*-

import logging
import logging.handlers



#日志
def mylog():
#创建一个logger
    logger = logging.getLogger('mypython_logger')
#Log等级总开关
    logger.setLevel(logging.DEBUG)
#创建一个handler，用于写入日志文件
    logfile='my_python.log'
#输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
#按天数轮转，保存5份
    rh = logging.handlers.TimedRotatingFileHandler(logfile,when='D',interval=1,backupCount=5)
    rh.setLevel(logging.DEBUG)
#定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(pathname)s - %(process)d - %(levelname)s: %(message)s")
    ch.setFormatter(formatter)
    rh.setFormatter(formatter)
#将logger添加到handler里面 
    logger.addHandler(ch)
    logger.addHandler(rh)
    return logger