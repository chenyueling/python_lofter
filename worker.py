#!/usr/bin/python
# coding=utf-8
import logging

__author__ = 'chenyueling'
import os
import redis
from rq import Worker, Queue, Connection
import traceback
listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)
#conn = redisFactory.getRedis()
if __name__ == '__main__':
    with Connection(conn):
        try:
            worker = Worker(map(Queue, listen))
            worker.work()
        except Exception,e:
             logging.error(e)
             print traceback.format_exc()
