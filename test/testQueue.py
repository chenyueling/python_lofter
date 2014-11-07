__author__ = 'chenyueling'

#!/usr/bin/env python
# coding=utf-8
'''''
@author: homer
@see: ithomer.net
'''

import Queue
import threading
import urllib, urllib2
import time

myqueue = Queue.Queue(maxsize=0)
queue = Queue.Queue()
hosts = ["http://1","http://2","http://3"]


lock = threading.Lock()
def printMsg(msg):
    global lock
    if lock.acquire():
        print(msg)
        lock.release()

class ThreadUrl(threading.Thread):
    def __init__(self, queue, htint):
        threading.Thread.__init__(self)
        self.queue = queue
        self.Ht = htint


    def run(self):
        print 'run run run ' + self.getName()
        while True:
            host = self.queue.get()

            printMsg("thread_id: " + self.getName() + ";\t htint: " + str(self.Ht) + " --- host: " + host)
            printMsg("qsize: %d" % self.queue.qsize())
            if self.queue.empty():
                printMsg("queue is empty of " + self.getName())
            self.queue.task_done()

    def start(self):
        print self
        print 'YYYYYYYYYYYY' + self.getName()
        return super(ThreadUrl, self).start()


def main():
    # spawn a pool of threads, and pass them queue instance
    for i in range(5):
        t = ThreadUrl(queue, 'x')
        t.setDaemon(True)
        t.start()
        # populate queue with data
        #for host in hosts:
        for x in range(5):
            printMsg("xxxxxxxxxxxxxxxxxxxxxxx")
            queue.put(str(x))
            print queue
        queue.join()

if __name__ == "__main__":
    start = time.time()
    main()
    time.sleep(1)
    costTime = time.time() - start - 1
    print "Elapsed Time: %s (s)" % costTime
