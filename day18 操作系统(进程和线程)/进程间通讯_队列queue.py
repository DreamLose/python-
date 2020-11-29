from multiprocessing import Process
from multiprocessing import Queue
import queue
import time
def foo(q):
    print('son',id(q))
    time.sleep(1)
    q.put(123)
    q.put('hello')
    pass

if __name__ == '__main__':
    q = Queue() # 进程队列
    print('main',id(q))
    p = Process(target=foo,args=(q,))



    p.start()

    print(q.get())
    print(q.get())