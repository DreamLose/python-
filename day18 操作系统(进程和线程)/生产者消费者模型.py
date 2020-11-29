

import time,random
import queue,threading
q = queue.Queue()

def Producer(name):
    count = 0
    while count < 10:
        print('制作食材......')
        time.sleep(random.randrange(3))
        q.put(count)
        print('生产者 %s 已经生产了 %s 个包子' %(name,count))
        count += 1
        #
        q.task_done()
        print('ok ....')

def Consumer(name):
    count = 0
    while count < 10:
        time.sleep(random.randrange(4))
        if not q.empty():
            data = q.get()
            q.join()
            # print(data)
            print('\033[32;1m消费者 %s 已经吃了 %s 个包子..\033[0m' %(name,data))
        else:
            print('没有包子了')
        count +=1

p1 = threading.Thread(target=Producer,args=('A',))
c1 = threading.Thread(target=Consumer,args=('B',))
c2 = threading.Thread(target=Consumer,args=('C',))
c3 = threading.Thread(target=Consumer,args=('D',))

p1.start()
c1.start()
c2.start()
c3.start()





