#!/usr/bin/python
# -*- coding:utf-8 -*-

import argparse

def my_parser(prog='myprogram'):
    parser = argparse.ArgumentParser(prog='myprogram',description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max,
                      help='sum the integers (default: find the max)')
    args = parser.parse_args()
    return args
    

if __name__ == '__main__':
    my_args=my_parser(prog='myprogram')
    print(my_args.accumulate(my_args.integers))