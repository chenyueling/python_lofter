#!/usr/bin/python
# coding=utf-8
from rq import Connection, Worker

__author__ = 'chenyueling'

import utils.redisFactory
import lofterUtils

import utils.Queue
import model.message

import exceptions

mark = 'lofter'


def task():
    redis = utils.redisFactory.getRedis()
    set = redis.keys(mark + '*')
    print set
    for cid in set:

        if not utils.timeHelper.time_area(8, 0, 0, 8, 20, 0) or not utils.timeHelper.time_area(18, 00, 0, 18, 20, 0):
            redis.hset(cid, 'notify', 'false')
            return
        else:
            status = redis.hmget(cid,'notify')
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

        cache_link = redis.get('cache_link' + ':' + c_id_real)

        if (cache_link == link):
            continue
        else:
            redis.set('cache_link' + ':' + c_id_real, link)
        try:
            Q = utils.Queue.Q
            Q.enqueue('utils.push_task.push_article', pushData.get_json(), sid, c_id_real, api_secret)
        except Exception, e:
            print e