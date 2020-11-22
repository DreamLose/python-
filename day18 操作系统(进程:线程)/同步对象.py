import threading,time

class Boss(threading.Thread):
    def run(self):
        print("Boss: 今天要加班到22:00")
        print(event.isSet())  # False
        event.set()
        time.sleep(5)
        print("Boss: <22:00> 可以下班了")
        print(event.isSet())
        event.set()

class Worker(threading.Thread):
    def run(self):
        event.wait() # event如果没有被设定,阻塞线程,一旦event被设定,等同于pass
        print("Worker:...要加班")
        time.sleep(1)
        event.clear()
        event.wait()
        print("Worker:...ohYeah!")


if __name__ == '__main__':
    event = threading.Event()

    threads = []
    for i in  range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('ending....')