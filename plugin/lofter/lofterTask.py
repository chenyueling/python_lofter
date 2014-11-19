#!/usr/bin/python
# coding=utf-8
from rq import Connection, Worker

__author__ = 'chenyueling'

import utils.redisFactory
import lofterUtils

import utils.Queue
import model.message

import utils.timeHelper

import exceptions

mark = 'lofter'


def task():
    redis = utils.redisFactory.getRedis()
    set = redis.keys(mark + '*')
    print set
    for cid in set:

        if not utils.timeHelper.time_area(8, 0, 0, 13, 40, 0) and not utils.timeHelper.time_area(18, 0, 0, 20, 20, 0):
            redis.hset(cid, 'notify', 'false')
            return
        else:
            status = redis.hmget(cid, 'notify')[0]
            if status != None and status == 'true':
                return
            else:
                redis.hset(cid, 'notify', 'true')

        c_id_real = cid.split(':')[1]
        sid = redis.hmget(cid, 'sid')[0]
        tag = redis.hmget(cid, 'tag')[0]

        print sid
        # tag = '原画'
        print tag
        article = lofterUtils.get_article_byTag(tag)
        api_secret = redis.get('api_secret' + ':' + sid)
        link = article[0]['link']
        title = article[0]['title']
        pushData = model.message.ArticleMessage(link, title)

        cache_link = redis.hmget(cid, 'cache_link')
        print cache_link[0]
        if (cache_link[0] == link):
            continue
        else:
            redis.hmget(cid, {'cache_link': cache_link})
        try:
            Q = utils.Queue.Q
            print pushData.get_json()
            Q.enqueue('utils.push_task.push_article', pushData.get_json(), sid, c_id_real, api_secret)
        except Exception, e:
            print e

redis = utils.redisFactory.getRedis()
cid = "lofter:08f6c8d9-048c-4c16-92e9-6b0c53f09737"
status = redis.hmget(cid, 'notify')[0]
print status
if status != None and status == 'true':
    print 'xxx'
else:
    print status