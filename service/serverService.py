#!/usr/bin/python
# coding=utf-8
__author__ = 'chenyueling'

import json
import utils.redisFactory




# {
#  "s_data": "{\"date\":\"1\",\"status\":\"下雨\"}",
#  "action": "ACTION_SERVICE_CREATE",
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

    r.set('title' + ':' + sid , title)

    r.set('api_secret' + ':' + sid,api_secret)

    if jsonObj.has_key('c_data'):
        c_data_list_dict = jsonObj['c_data']
        #c_data_list_dict = json.loads(c_data)

    for item in c_data_list_dict:
        print json.dumps(item)
        if jsonObj.has_key('s_data'):
            s_data = jsonObj['s_data']
            s_data_dict = json.loads(s_data)
            item.update(s_data_dict)
            r.hmset(service_name + ':' + item['cid'],item)

    result = Result('Success','3000');

    return result


#用户互动事件
def action_service_ding(service_name, jsonObj):
    print service_name
    return service_name


#ClientService关注数变更事件
def action_service_followed_change(service_name, jsonObj):
    print service_name
    return service_name


#ClientService创建事件
def action_client_service_create(service_name, jsonObj):
    print service_name
    return service_name


#Service更新事件
def action_service_update(service_name, jsonObj):
    print service_name
    return service_name



class Result(object):
    def __init__(self,message,code):
        self.message = message
        self.code = code

    def get_json(self):
        return json.dumps(self.__dict__)
