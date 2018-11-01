#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json


def Regionsmain(accessKey,accessSecret,region):
    Regionslist=[]
    client = AcsClient(accessKey,accessSecret,region)
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('ecs.aliyuncs.com')
    request.set_method('POST')
    request.set_version('2014-05-26')
    request.set_action_name('DescribeRegions')
    response = client.do_action_with_exception(request)
    response = json.loads(response,encoding='utf-8')
    Regionslists=response.get('Regions').get('Region')
    for list in Regionslists:
        Regionslist.append(list['RegionId'])
    return Regionslist


if __name__ == '__main__':
    print Regionsmain('', '','cn-shanghai')
