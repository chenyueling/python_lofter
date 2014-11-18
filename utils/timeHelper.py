__author__ = 'chenyueling'

import time
import datetime

#setting time area ,in this time area return true else return flase
def time_area(start_h=0, start_m=0, start_sec=0, end_h=0, end_m=0, end_sec=0):
    ltime = time.localtime()
    start_time = datetime.datetime(ltime.tm_year, ltime.tm_mon, ltime.tm_mday, start_h, start_m, start_sec)
    endTime = datetime.datetime(ltime.tm_year, ltime.tm_mon, ltime.tm_mday, end_h, end_m, end_sec)

    start_time_stamp = time.mktime(start_time.timetuple())
    end_time_stamp = time.mktime(endTime.timetuple())
    currentTime = time.time()
    if currentTime > start_time_stamp and currentTime < end_time_stamp:
        return True
    else:
        return False

print time_area(19, 44, 50, 20, 15, 0)