import time
# def producer():
#     ret = []
#     for i in range(100):
#         time.sleep(0.1)
#         ret.append("包子 %s" %i)
#     return ret
#
# def consumer(res):
#     for index,baozi in enumerate(res):
#         time.sleep(0.1)
#         print("第%s个人，吃了%s" %(index,baozi))
#
# res = producer()
# consumer(res)

# yield 相当于return 控制的函数的返回值
# yield 另外一个特性，接受send传过来的值，赋值给frist
# def test():
#     print("开始了")
#     frist = yield 1
#     print("第一次",frist)
#     yield 2
#     print("第二次")
# t =test()
# print(t.__next__())
# print(t.send(None))
def consumer(name):
    print("我是【%s】,我准备吃包子了" %name)
    while True:
        baozi = yield
        time.sleep(1)
        print("%s 很开心的把【%s】吃掉了" %(name,baozi))

def producer():
    c1 = consumer("xiaocang")
    c2 = consumer("泷泽萝拉")
    c1.__next__()
    c2.__next__()
    for i in range(10):
        time.sleep(1)
        c1.send("白菜包子 %s" %i)
        c2.send("白菜包子 %s" % i)
producer()