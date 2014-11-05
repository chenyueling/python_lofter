__author__ = 'chenyueling'

import redis




pool = redis.ConnectionPool(host='127.0.0.1', port=6379 , db=0)




def getRedis():
    print pool
    return redis.Redis(connection_pool=pool)
