#!/usr/bin/python  
# -*- coding:utf-8 -*-

def remove_uni(s):
    """remove the leading unicode designator from a string"""
    s2 = ''
    if s.startswith("u'"):
        s2 = s.replace("u'", "'", 1)
    elif s.startswith('u"'):
        s2 = s.replace('u"', '"', 1)
    return s2