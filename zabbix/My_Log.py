#!/usr/bin/python  
# -*- coding:utf-8 -*-

import logging
import logging.config

#日志

def mylog():
    logging.config.fileConfig('config/logging.ini')
    logger = logging.getLogger('infoLogger')
#返回logger
    return logger