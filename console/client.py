#coding=utf-8

# task client
__author__ = 'John Wang'

from multiprocessing.managers import BaseManager
import queue, random, time
from multiprocessing import freeze_support
task_queue = queue.Queue()
result_queue = queue.Queue()

class Queuemanager(BaseManager):
    pass


def test():
    Queuemanager.register('get_task_queue')
    Queuemanager.register('get_result_queue')

    server_addr = '127.0.0.1'
    print('connect to server %s...' % server_addr)
    m = Queuemanager(address=(server_addr, 5000), authkey=b'abc')
    m.connect()
    task = m.get_task_queue()
    result = m.get_result_queue()

    while True:
        try:
            n = task.get(timeout=10)
            print(n)
            print('run task %d * %d' % (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            result.put(r)
            time.sleep(1)
        except:
            print('task queue is empty')
            break

    print('work exit')

if __name__ == '__main__':
    freeze_support()
    test()
