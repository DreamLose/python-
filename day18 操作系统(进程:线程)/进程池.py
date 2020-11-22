from multiprocessing import Process,Pool
import time,os

def Foo(i):
    time.sleep(1)
    print(i)
    return i+100,'我是Foo返回的'  # 返回的值在会调函数中的参数

def Bar(arg):
    print('pid-->',os.getpid())
    print('ppid-->',os.getppid())
    print('logger',arg)


if __name__ == '__main__':
    # 进程池 5个
    pool = Pool(5)
    for i in range(100):
        # pool.apply(func=Foo,args=(i,)) #同步接口
        # pool.apply_async(func=Foo,args=(i,))

        # 会调函数,某个动作或者函数执行成功后再去执行的函数
        # 执行在主进程 ,callback 函数执行在主进程
        pool.apply_async(func=Foo, args=(i,),callback=Bar)
    pool.close()
    pool.join()  # join 与 close 的调用顺序是固定的
    print('end')
