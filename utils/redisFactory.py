#!/usr/bin/python
# coding=utf-8
__author__ = 'chenyueling'

import redis


import utils.config

pool = redis.ConnectionPool(host=utils.config.REDIS_HOST, port=utils.config.REDIS_PORT , db=0)




def getRedis():
    print pool
    return redis.Redis(connection_pool=pool)
