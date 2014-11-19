#!/usr/bin/python
# coding=utf-8

# when we create new service should add service name to ALLOW_SERVICE
# split by ','

ALLOW_SERVICE = 'lofter,toutiao_news,toutiao_gallery'


##lofter account

USERNAME = 'chen_yueling@163.com'
PASSWORD = 'xxxxxxxx'

#DING_SERVER_HOST = 'http://127.0.0.1:10015'

DING_SERVER_HOST = 'http://demo.91dd.cc:10015'

NOTFY_URL = DING_SERVER_HOST + '/v1/service/{service_id}/{c_id}/push'



## redis

#REDIS_HOST = '127.0.0.1'
REDIS_HOST = 'demo.91dd.cc'
REDIS_PORT = '20016'
