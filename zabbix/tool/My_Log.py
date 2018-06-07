#!/usr/bin/python  
# -*- coding:utf-8 -*-

import logging
import logging.config

#日志

def mylog(confile):
    logging.config.fileConfig(confile)
    logger = logging.getLogger()
#返回logger
    return logger