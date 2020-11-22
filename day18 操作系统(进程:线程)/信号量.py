import threading
import time

class MyThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print('线程-->',self.name)
            time.sleep(5)
            semaphore.release()


if __name__ == '__main__':
    # 定义同时可以开几个线程
    semaphore = threading.Semaphore(5)
    thrs = []
    for i in range(100):
        thrs.append(MyThread())
    for t in thrs:
        t.start()


