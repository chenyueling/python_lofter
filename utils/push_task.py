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
    print auth
    headers = {
        'Authorization': 'Basic %s' % auth,
        'Content-Type': 'application/json',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip,deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control':'max-age=0',
        'Accept-Charset':'utf-8',
        'Connection':'keep-alive',
        'Content-Type':'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686 (x86_64)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'
    }
    request = urllib2.Request(posturl, postData, headers)
    response = urllib2.urlopen(request)
    result = json.loads(response.read())
    print '开始'
    time.sleep(175)
    print '结束'
    if result['code'] == 3000:
        return 'success'
    else:
        return 'fail'

# auth = base64.encodestring('5944' + ':' + 'bvb6r9oxmdl3obd9ure7tz3u')
#print  auth

print json.loads('{"code":3000,"content":"Success"}')['code'] == '3000'
