import time

def Consumer(name):
    print('---------->ready to eat baozi..')
    while True:
        new_baozi = yield
        print('[%s] is eating baozi %s' %(name,new_baozi))

def Producer():
    r = con.__next__()
    r2 = con2.__next__()

    n = 0
    while True:
        time.sleep(1)
        print("\033[32:1m[producer]\033[0m is making baozi %s and %s" %(n,n+1))
        con.send(n)
        con2.send(n+1)
        n += 2


if __name__ == '__main__':
    con = Consumer('诸葛亮')
    con2 = Consumer('貂蝉')
    Producer()
