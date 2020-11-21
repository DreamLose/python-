import threading
import time

def music():
    print('开始听音乐 %s' %time.ctime())
    time.sleep(3)
    print('结束听音乐 %s' %time.ctime())
def game():
    print('开始打游戏 %s' %time.ctime())
    time.sleep(5)
    print('结束打游戏 %s' %time.ctime())

# setDaemon(True) #守护进程,跟主线程一块结束,必须在start()方法调用前设置,这个方法基本和join相反
# 主线程跟子线程分别运行,如果当主线程完成想退出时,会检验子线程是否完成,如果子线程未完成,则主线程会等待子线程完成后再退出,
# 但有时我们需要的是只要主线程完成了,不管子线程是否完成,都要和主线程一起退出,这时就可以使用setDaemon 方法
if __name__ == '__main__':
    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=game)
    # t1.setDaemon(True) #守护进程,跟主线程一块结束
    t1.start()
    # t1.join()  # 等待子线程执行完在执行以后代码
    t2.setDaemon(True)  # 守护进程,跟主线程一块结束
    t2.start()

    # t1.join()  # 等待子线程执行完在执行以后代码
    # t2.join()

    print('ending %s' %(time.ctime()))



"""
run():用以表示线程活动的方法
start():启动线程活动
isAlive():返回线程是否活动
getName():返回线程名
setName():设置线程名

threading模块的一些方法
threading.currentThread() : 返回当前线程变量
threading.enumerate():返回一个包含正在运行的线程list,正在运行的线程启动后,结束前,不包含启动前和终止后的线程
threading.activeCount():返回正在运行的线程数量,与len(threading.enumerate()) 有相同的结果


"""