from multiprocessing import Process
import time
"""
# def test():
#     print('hhhh')
#     time.sleep(3)
# if __name__ == '__main__':
# 
# 
#     p1 = Process(target=test)
#     p1.daemon = True
#     p1.start()
#     p2 = Process(target=test)
#     p2.start()
#     print('end.....')
"""
import os

def info(titile):
    print('title:',titile)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    time.sleep(1)
    print(p.is_alive())
    time.sleep(1)
def f(name):
    info('function f')
    print('hello',name)

class MyProcess(Process):
    def __init__(self,num):
        super(MyProcess,self).__init__()
        self.num = num
    def run(self):
        time.sleep(1)
        print(self.pid,time.ctime())
        print(self.is_alive(),time.ctime())
        print(self.num,time.ctime())
        time.sleep(1)

if __name__ == '__main__':
    """
    # info('main process line')
    # time.sleep(1)
    # print('----------')
    # p = Process(target=info,args=('alex',))
    # p.start()
    # p.join()
    """

    p_list = []
    for i in range(10):
        p = MyProcess(i)
        p_list.append(p)

    for p in p_list:
        p.start()

    print('main process end')