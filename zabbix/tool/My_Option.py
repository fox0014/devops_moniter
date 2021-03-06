#!/usr/bin/python
# -*- coding:utf-8 -*-

import argparse
import sys

def my_parser(prog='myprogram'):
    parser = argparse.ArgumentParser(prog=prog,description='data some info.',usage='%(prog)s [options] -v [-mq] ',epilog='good luck')
    parser.add_argument('--datasource', required = True,metavar='Source', const='db',choices = ['mysql', 'redis'],nargs='?',help='choose the source')
    parser.add_argument('--version','-v',action='version', version='%(prog)s 1.0')
    parser.add_argument("-mq", "--mysqlqps",nargs='?',help="print qps")
    parser.add_argument("--dbdata",dest = "dbdata",nargs='?',help="print dbdata")
    args = parser.parse_args()
    return args
    

if __name__ == '__main__':
    my_args=my_parser(prog='Myprogram')
    if my_args.mysqlqps:
        print my_args.mysqlqps