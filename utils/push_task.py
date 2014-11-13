#!/usr/bin/python
# coding=utf-8

import urllib2
import base64

__author__ = 'chenyueling'

import utils.config
import json
import time


def push_article(postData, sid, cid, api_secret):
    posturl = utils.config.NOTFY_URL.replace('{service_id}', sid).replace('{c_id}', cid)
    print posturl
    # 秘钥
    auth = base64.encodestring(sid + ":" + api_secret).replace("\n", '')
    headers = {
        'Authorization': 'Basic %s' % auth,
        'Content-Type': 'application/json',
    }
    request = urllib2.Request(posturl, postData, headers)
    response = urllib2.urlopen(request)
    result = json.load(response.read())
    print '开始'
    time.sleep(175)
    print '结束'
    if result['code'] == '3000':
        return 'success'
    else:
        return 'fail'

#auth = base64.encodestring('5944' + ':' + 'bvb6r9oxmdl3obd9ure7tz3u')
#print  auth

