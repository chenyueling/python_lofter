import traceback
from flask import logging
import model.message
from plugin.toutiao import toutiaoUtils
import utils.timeHelper
import utils.Queue


__author__ = 'chenyueling'

import utils.redisFactory

mark_news = 'toutiao_news'
mark_gallery = 'toutiao_gallery'


def toutiao_news_task():
    redis = utils.redisFactory.getRedis()
    set = redis.keys(mark_news + '*')
    print set
    try:
        for cid in set:

            if not utils.timeHelper.time_area(8, 20, 0, 8, 50, 0) and not utils.timeHelper.time_area(18, 20, 0, 18,
                                                                                                     50, 0):
                redis.hset(cid, 'notify', 'false')
                continue
            else:
                status = redis.hmget(cid, 'notify')[0]
                if status != None and status == 'true':
                    print status
                    continue
                else:
                    redis.hset(cid, 'notify', 'true')

            c_id_real = cid.split(':')[1]
            sid = redis.hmget(cid, 'sid')[0]

            article = toutiaoUtils.get_toutiao_news()
            api_secret = redis.get('api_secret' + ':' + sid)
            link = article[toutiaoUtils.LINK]
            title = article[toutiaoUtils.TITLE]
            summary = article[toutiaoUtils.SUMMARY]
            pushData = model.message.ArticleMessage(link, title, summary)
            cache_link = redis.hmget(cid, 'cache_link')
            print cache_link[0]
            print link
            print cid
            if (cache_link[0] == link):
                continue
            else:
                redis.hmset(cid, {'cache_link': link})
            try:
                Q = utils.Queue.Q
                print pushData.get_json()
                Q.enqueue('utils.push_task.push_article', pushData.get_json(), sid, c_id_real, api_secret)
            except Exception, e:
                print e
    except Exception, e:
        # logging.error(e)
        print traceback.format_exc()


def toutiao_gallery_task():
    redis = utils.redisFactory.getRedis()
    set = redis.keys(mark_gallery + '*')
    print set
    for cid in set:

        if not utils.timeHelper.time_area(8, 30, 0, 10, 50, 0) and not utils.timeHelper.time_area(18, 30, 0, 18, 50, 0):
            redis.hset(cid, 'notify', 'false')
            continue
        else:
            status = redis.hmget(cid, 'notify')[0]
            if status != None and status == 'true':
                continue
            else:
                redis.hset(cid, 'notify', 'true')

        c_id_real = cid.split(':')[1]
        sid = redis.hmget(cid, 'sid')[0]

        article = toutiaoUtils.get_toutiao_gallery()
        api_secret = redis.get('api_secret' + ':' + sid)
        link = article[toutiaoUtils.LINK]
        title = article[toutiaoUtils.TITLE]
        pushData = model.message.ArticleMessage(link, title)

        cache_link = redis.hmget(cid, 'cache_link')

        if (cache_link[0] == link):
            continue
        else:
            redis.hmset(cid, {'cache_link': link})
        try:
            Q = utils.Queue.Q
            print pushData.get_json()
            Q.enqueue('utils.push_task.push_article', pushData.get_json(), sid, c_id_real, api_secret)
        except Exception, e:
            print e


