#!/usr/bin/python
# coding=utf-8
import json
import logging
import traceback

from flask import Flask, Response
from flask import request
from apscheduler.scheduler import Scheduler

import service.serverService
import utils.config
import plugin.lofter.lofterUtils
import plugin.lofter.lofterTask

import plugin.toutiao.toutiaoTask
import plugin.toutiao.toutiaoUtils


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'ding-factory'


@app.route('/factory/py/<service_name>', methods=['POST'])
def process(service_name):
    try:
        print service_name
        jsonData = json.loads(request.data)
        print request.data
        action = jsonData["action"]
        isAllow = False
        for item in utils.config.ALLOW_SERVICE.split(','):
            if service_name == item:
                isAllow = True
        if service_name is None or service_name == '' or not isAllow:
            return 'No such Service'

        result = ''

        if action == 'ACTION_SERVICE_CREATE':
            result = service.serverService.action_service_create(service_name, jsonData)
        elif action == 'ACTION_SERVICE_UPDATE':
            result = service.serverService.action_service_update(service_name, jsonData)
        elif action == 'ACTION_CLIENT_SERVICE_CREATE':
            result = service.serverService.action_client_service_create(service_name, jsonData)
        elif action == 'ACTION_SERVICE_FOLLOWED_CHANGE':
            result = service.serverService.action_service_followed_change(service_name, jsonData)
        elif action == 'ACTION_SERVICE_DING':
            result = service.serverService.action_service_ding(action, jsonData)


    except Exception, e:
        logging.error(e)
        print traceback.format_exc()
        result.code = "1001"
        result.message = "unknow Exception"
        resp = Response(result.get_json())
        return resp

    resp = Response()
    resp.data = result.get_json()
    resp.mimetype = "application/json"

    return resp





xxx = ''

schedudler = Scheduler(daemonic=False)

schedudler.add_interval_job(func=plugin.lofter.lofterTask.task, seconds=10)
schedudler.add_interval_job(func=plugin.toutiao.toutiaoTask.toutiao_gallery_task, seconds=10)
schedudler.add_interval_job(func=plugin.toutiao.toutiaoTask.toutiao_news_task, seconds=10)
# schedudler.add_interval_job(func=plugin.lofter.lofterTask.task(''),seconds=20)



if __name__ == '__main__':
    schedudler.start()
    app.run(port=8888)


