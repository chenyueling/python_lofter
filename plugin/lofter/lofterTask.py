#!/usr/bin/python
# coding=utf-8
__author__ = 'chenyueling'

import utils.redisFactory
import lofterUtils

import utils.Queue

import exceptions

mark = 'lofter'


def task(Queue=None):
    redis = utils.redisFactory.getRedis()
    set = redis.keys(mark + '*')
    for key in set:
        print key
        cid = key
        c_id_real = cid.split(':')[1];
        sid = redis.hget(cid, 'sid')
        tag = redis.hget(cid, 'tag')
        print sid
        tag = '原画'
        print
        print lofterUtils.get_article_byTag(tag)
        api_secret = redis.get('api_secret' + ':' + sid)

        print api_secret
        Q = utils.Queue.Q
        try:
            Q.enqueue('1','2','3')
            Q.empty()
        except Exception ,e:
            print e

        print utils.Queue.Q

