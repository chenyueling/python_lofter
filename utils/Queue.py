__author__ = 'chenyueling'


from rq import Queue

from redisFactory import getRedis

r = getRedis()
Q = Queue('xxxx',connection=r)






