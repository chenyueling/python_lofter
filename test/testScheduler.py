__author__ = 'chenyueling'

import time
from apscheduler.scheduler import Scheduler
import plugin.lofter.lofterTask
schedudler = Scheduler(daemonic = False)


@schedudler.cron_schedule(second='*', day_of_week='0-5', hour='8-10,13-15')
def quote_send_sh_job():
    print 'a simple cron job start at' , time.datetime.now()

schedudler.add_interval_job(plugin.lofter.lofterTask.task(),seconds=2)



schedudler.start()
