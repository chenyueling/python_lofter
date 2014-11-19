#!/usr/bin/python
# coding=utf-8
__author__ = 'chenyueling'

import json
import utils.redisFactory




# {
# "s_data": "{\"date\":\"1\",\"status\":\"下雨\"}",
# "action": "ACTION_SERVICE_CREATE",
#  "title": "明天下雨提醒",
#  "api_secret": "09ltfmd29f0our68q5bjij2x",
#  "sid": "5857",
#  "c_data": [
#    {
#      "data": "{\"location\":\"珠海\"}",
#      "cid": "6f782524-22d4-48fc-b0f6-ab79d49bf178"
#    },
#    {
#      "data": "{\"location\":\"深圳\"}",
#      "cid": "c388eb26-c9f2-41ae-93c5-fdcc0ff8d26a"
#    }
#  ]
#}
#
#Service创建事件
def action_service_create(service_name, jsonObj):
    r = utils.redisFactory.getRedis()

    title = jsonObj['title']

    api_secret = jsonObj['api_secret']

    sid = jsonObj['sid']

    r.set('title' + ':' + sid, title)

    r.set('api_secret' + ':' + sid, api_secret)

    #
    s_dict = {}

    if jsonObj.has_key('s_data'):
        s_dataStr = jsonObj['s_data']
        s_data_dict = json.loads(s_dataStr)
        s_data_dict.update({'sid': sid})
        s_dict.update(s_data_dict)
        s_store_dict = r.hgetall('s_data' + ':' + sid)
        #合并出最新
        s_dict.update(s_store_dict)
        #只要是服务端传来的s_data不为空都要存储,如果服务
        if s_data_dict.__len__() != 0:
            r.hmset('s_data' + ':' + sid, s_dict)

    if jsonObj.has_key('c_data'):
        c_data_list_dict = jsonObj['c_data']
        #c_data_list_dict = json.loads(c_data)
        for item in c_data_list_dict:
            #s_data = jsonObj['s_data']
            data = item['data']
            item.pop('data')
            data_dict = json.loads(data)
            item.update(s_dict)
            item.update(data_dict)
            item.update({'sid': sid})
            r.hmset(service_name + ':' + item['cid'], item)

    result = Result('Success', '3000');

    return result


#用户互动事件
def action_service_ding(service_name, jsonObj):
    result = Result('Success', '3000');
    return result


#ClientService关注数变更事件
def action_service_followed_change(service_name, jsonObj):
    print service_name
    result = Result('Success', '3000');
    return result


# {
#   "data": "{\"date\":\"1\",\"status\":\"下雨\"}",
#   "action": "ACTION_CLIENT_SERVICE_CREATE",
#   "sid": "0556",
#   "cid": "bc6e20b4-a0f0-494f-8564-dc2490432e4e"
# }
#ClientService创建事件
def action_client_service_create(service_name, jsonObj):
    print jsonObj
    print service_name
    r = utils.redisFactory.getRedis()
    sid = jsonObj['sid']
    c_id_real = jsonObj['cid']
    s_data_dict = r.hgetall('s_data' + ':' + sid)
    data = jsonObj['data']
    data_dict = json.loads(data)
    data_dict.update({'cid':c_id_real})
    data_dict.update({'sid':sid})
    s_data_dict.update(data_dict)
    if s_data_dict.__len__() == 0:
        pass
    else:
        r.hmset(service_name + ':' + c_id_real, s_data_dict)

    result = Result('Success', '3000');
    return result


#Service更新事件
def action_service_update(service_name, jsonObj):
    r = utils.redisFactory.getRedis()

    title = jsonObj['title']

    api_secret = jsonObj['api_secret']

    sid = jsonObj['sid']

    r.set('title' + ':' + sid, title)

    r.set('api_secret' + ':' + sid, api_secret)

    #
    s_dict = {}

    if jsonObj.has_key('s_data'):
        s_dataStr = jsonObj['s_data']
        s_data_dict = json.loads(s_dataStr)
        s_data_dict.update({'sid': sid})
        s_dict.update(s_data_dict)
        s_store_dict = r.hgetall('s_data' + ':' + sid)
        #合并出最新
        s_dict.update(s_store_dict)
        #只要是服务端传来的s_data不为空都要存储,如果服务
        if s_data_dict.__len__() != 0:
            r.hmset('s_data' + ':' + sid, s_dict)

    if jsonObj.has_key('c_data'):
        c_data_list_dict = jsonObj['c_data']
        #c_data_list_dict = json.loads(c_data)
        for item in c_data_list_dict:
            s_data = jsonObj['s_data']
            item.update(s_dict)
            r.hmset(service_name + ':' + item['cid'], item)

    result = Result('Success', '3000');
    return result


class Result(object):
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def get_json(self):
        return json.dumps(self.__dict__)
