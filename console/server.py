#coding=utf-8

# task master
__author__ = 'John Wang'

import random
import time
import queue

from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def get_task():
    global task_queue
    return task_queue
def get_result():
    global result_queue
    return result_queue
def test():
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)

    manager = QueueManager(address=('localhost', 5000), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(100):
        n = random.randint(0, 10000)
        print('push task %s' % i)
        task.put(i)

    print('try get result...')
    while True:
        try:
            r = result.get(timeout=3600)
            print('Result:%s' % r)
            time.sleep(1)
        except:
            break


    manager.shutdown()
    print('master exit')

if __name__ == '__main__':
    freeze_support()
    test()


