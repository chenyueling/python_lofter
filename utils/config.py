#!/usr/bin/python
# coding=utf-8

# when we create new service should add service name to ALLOW_SERVICE
# split by ','

ALLOW_SERVICE = 'lofter,'


##lofter account

USERNAME = 'chen_yueling@163.com'
PASSWORD = 'xxxxxxxx'

DING_SERVER_HOST = 'http://127.0.0.1:10015'

NOTFY_URL = DING_SERVER_HOST + '/v1/service/{service_id}/{c_id}/push'



## redis

REDIS_HOST = '127.0.0.1'

REDIS_PORT = '6379'
