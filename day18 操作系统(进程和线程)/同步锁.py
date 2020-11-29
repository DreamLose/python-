"""
# 并发:指系统具有处理多个任务(动作)的能力
# 并行:指系统具有同时处理多个任务(动作)的能力
# 并行是并发的一个子集

同步:当进程执行到一个IO(等待外部数据)的时候, 等 一直等到数据成功
异步:当进程执行到一个IO(等待外部数据)的时候, 不等

任务:IO密集型,计算密集型
GIL:全局解释锁,因为有GIL,同意时刻,只有一个线程被cpu执行

对应IO密集型的任务.python的多线程是有意义的,可以采用多进程+协程
对于计算密集型任务,python的多线程就不推荐了,python就不适用了

协程: 协作式,非抢占性程序,本质上就是一个线程
优势: 没有切换的消耗,没有锁的概念
问题: 不能使用多核 (多进程+协程,解决并发的方案)
"""



import threading
import time
num = 100
def sub():
    global num
    print('ok')
    # 上锁
    lock.acquire()
    temp = num
    time.sleep(0.01)
    num = temp-1
    # 去锁
    lock.release()

l = []

lock = threading.Lock()
for i in range(100):
    t = threading.Thread(target=sub)
    t.start()
    l.append(t)

for i in l:
    i.join()


print(num)


