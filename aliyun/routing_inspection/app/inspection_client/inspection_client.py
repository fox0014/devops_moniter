# coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkcore.request import CommonRequest
import json
 

def mymain(accessKey,accessSecret,region):
    clt = AcsClient(
                    accessKey, accessSecret, region);
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    request.set_accept_format('json')
    request.set_PageSize(100)  # 每页条数
    request.set_PageNumber(1)  # 第几页
    # PageNumber, PageSize
    response = json.loads(clt.do_action_with_exception(request), encoding='utf-8')
    info_list= response.get('Instances').get('Instance')
    #遍历获取到的结果
    for info in info_list:
        assetNo = info.get('InstanceId')
        ecsName = info.get('InstanceName')       
        region = info.get('RegionId')
        zone = info.get('ZoneId')
        ecsType = info.get('InstanceType')
        cpu = str(info.get('Cpu'))
        mem = str(info.get('Memory'))
        bandWidth = str(info.get('InternetMaxBandwidthOut'));
        status = info.get('Status')
        OS = str(info.get('OSType'))
        OSName = info.get('OSName')
        publicipAddress = ''
        innerIpAddress = ''
        privateIpAddress = ''
        if info.get('PublicIpAddress').get('IpAddress'):
            ipAddress = info.get('PublicIpAddress').get('IpAddress')           
            if ipAddress:
                ipAddress = ipAddress[0]
                publicipAddress = ipAddress
        elif info.get('InnerIpAddress').get('IpAddress'):
            ipAddress = info.get('innerIpAddress').get('IpAddress')
            if ipAddress:
                ipAddress = ipAddress[0]
                innerIpAddress = ipAddress
        else:
            ipAddress = info.get('VpcAttributes').get('PrivateIpAddress').get('IpAddress')
            if ipAddress:
                ipAddress = ipAddress[0]
                privateIpAddress = ipAddress            
        createTime = info.get('CreationTime')
        expiredTime = info.get('ExpiredTime')  
        print  region,zone,ecsType,cpu,mem,ipAddress,assetNo,OS,OSName,expiredTime
 
if __name__ == '__main__':
#    accessKey = '' 
#参数传入key（阿里控制台获取）
#accessSecret = ''     
#参数传入secret（阿里控制台获取）
#region = 'cn-shanghai'         
#区域（cn-hangzhou） 
    mymain('','','cn-shanghai')