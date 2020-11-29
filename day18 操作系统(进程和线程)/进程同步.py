import os
import time
import random
from multiprocessing import Process, Lock


def work(l, n):
    l.acquire()
    print('%s: %s is running' % (n, os.getpid()))
    time.sleep(random.random())
    print('%s: %s is done' % (n, os.getpid()))
    l.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=work, args=(lock, i))
        p.start()
