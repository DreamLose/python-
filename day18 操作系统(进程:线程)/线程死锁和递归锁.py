import threading
import time
class MyThread(threading.Thread):
    def actionA(self):
        r_lock.acquire()
        print(self.name,'gotA',time.ctime())
        time.sleep(2)
        r_lock.acquire()
        print(self.name, 'gotB', time.ctime())
        time.sleep(1)
        r_lock.release()
        r_lock.release()
    def actionB(self):
        r_lock.acquire()
        print(self.name, 'gotB', time.ctime())
        time.sleep(2)
        r_lock.acquire()
        print(self.name, 'gotA', time.ctime())
        time.sleep(1)
        r_lock.release()
        r_lock.release()
    def run(self):
        self.actionA()
        self.actionB()


if __name__ == '__main__':
    # A = threading.Lock()
    # B = threading.Lock()

    # 解决死锁,递归锁
    r_lock = threading.RLock()
    l = []
    for i in range(5):
        t = MyThread()
        t.start()
        l.append(t)
    for i in l:
        i.join()

    print('end-----')


