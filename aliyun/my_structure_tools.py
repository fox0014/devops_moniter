#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python 2X



def dict_action_set(dict1,order1_permission,order1,ip1,key1,value1):
    tmp_list=dict1
    if order1 in order1_permission:
        if order1 in tmp_list.keys():
            for k,v in tmp_list.items():
                if isinstance(v, dict):
                    for k1,v1 in v.items():
                        if not v.has_key(ip1):
                            v.update({ip1:{key1:value1}})                        
                        elif k1 == ip1:
                            v1.update({key1:value1})
                        else:
                            pass
                else:   
                    return 'your dict structure wrong'
        else:
            tmp_list[order1]={ip1:{key1:value1}}
    else:
        return "your dict order wrong"
                                    
def dict_action_get(dict1,order1,ip1,key1):
    tmp_list=dict1
    if tmp_list:
        if tmp_list.has_key(order1):
            for k,v in tmp_list.items():
                if k == order1:
                    if v.has_key(ip1):
                        for k1,v1 in v.items():        
                            if k1 == ip1:
                                aa1=v1.get(key1,None)
                                if aa1:
                                    del v1[key1]
                                return aa1
                    else:
                        return "your ip is not suit"
        else:
            return "your dict order wrong"
        return tmp_list
    else:
        return "the dict is empty,please wait"
    
if __name__ == '__main__':
#{'redis': {'10.62.11.76:6379': {'used_memory_human': '5.18M'}}}
#{'redis': {'10.62.11.76:6379': {}}}
    tt1={}
    gogo_list=('redis','mysql')
    dict_action_set(tt1,gogo_list,'redis','10.62.11.76:6379','used_memory_human','5.18M')
    print tt1
    dict_action_get(tt1,'redis','10.62.11.76:6379','used_memory_human')
    print tt1