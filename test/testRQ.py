import time

__author__ = 'chenyueling'


from apscheduler.scheduler import Scheduler
import utils.Queue
import utils.redisFactory

def task():
    print 'xxx'
    Q = utils.Queue.Q
    job = Q.enqueue('test.testRQ.test')
    print job.result
    time.sleep(2)

    print job.result
def test():
    r = utils.redisFactory.getRedis()
    #print x
    r.set('fuck','123456')
    return 'chenyueling'

schedudler = Scheduler(daemonic=False)



schedudler.add_interval_job(func=task,seconds=5)


schedudler.start()