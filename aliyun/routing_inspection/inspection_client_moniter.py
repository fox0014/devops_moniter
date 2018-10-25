#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json


def Regionsmain(accessKey,accessSecret,region):
    client = AcsClient(accessKey,accessSecret,region)
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('metrics.cn-hangzhou.aliyuncs.com')
    request.set_method('POST')
    request.set_version('2018-03-08')
    request.set_action_name('QueryMetricData')
    request.add_query_param('Dimensions', {'dimension':'xxx'})
    request.add_query_param('Metric', 'CPUUtilization')
    request.add_query_param('Project', 'acs_ecs_dashboard')
    request.add_query_param('RegionId', 'cn-shanghai')
    request.add_query_param('Period', '604800')
    request.add_query_param('StartTime', '2018-10-16 00:00:00')
    request.add_query_param('EndTime', '2018-10-23 00:00:00')
    response = client.do_action_with_exception(request)
    return response


if __name__ == '__main__':
    print Regionsmain('', '','cn-shanghai')