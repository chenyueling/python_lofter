from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'ding-factory'


@app.route('/factory/py/lofter')
def

if __name__ == '__main__':
    app.run()
