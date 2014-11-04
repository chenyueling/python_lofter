from flask import Flask
from flask import request
import json
import logging

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'ding-factory'


@app.route('/factory/py/lofter',methods=['POST'])
def process():
    try:
        data = json.loads(request.data)['c_data'][1]['data']
        print json.loads(data)['location']
    except Exception,e:
        logging.error(e)
    return '1'
if __name__ == '__main__':
    app.run()
