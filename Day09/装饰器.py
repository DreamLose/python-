# 装饰器：本质就是函数，为其他函数添加附加功能
# 原则：1 不修改被修饰函数的源代码，
#      2 不修改被修饰函数的调用方式
# 装饰器 = 高阶函数 + 函数嵌套 + 闭包

# 高阶函数：函数接受的参数是一个函数名，函数的返回值是一个函数值，满足其中任意一个条件即为高阶函数

import time
# def foo():
#     print("来自foo")
# 高阶函数
# def test(func):
#     print(func)
#     return func
#     # func()
# foo = test(foo)
# foo()
# 不修改foo 源代码，不修改foo调用方式
# def timerN(func):
#     start_time = time.time()
#     func()
#     end_time = time.time()
#     print("函数运行时间 %s" % (end_time - start_time))
#     return func
#
# foo = timerN(foo)
# foo()
# print("==============")
# def timmer(func):
#     def wapper(*args,**kwargs):
#         start_time = time.time()
#         res = func(*args,**kwargs)
#         stop_time = time.time()
#         print("函数运行时间 %s" %(stop_time - start_time))
#         return res
#     return wapper
#
#
# @timmer
# def cal(li):
#     # star_time = time.time()
#     sumN = 0
#     for i in li:
#         sumN += i
#     # stop_time = time.time()
#     # print("函数运行时间 %s" %(stop_time -star_time))
#     return sumN
#
# res = cal(range(100))
# print(res)
#
# # 统计函数运行时间
#
# # 装饰器框架
#
# def test(func):
#     def wrapper(*args,**kwargs):
#         star_time = time.time()
#         res = func(*args,**kwargs)
#         stop_time = time.time()
#         print("函数运行时间 %s" % (stop_time - star_time))
#         return res
#     return wrapper
# @test
# def fun1(name,age,gen):
#     time.sleep(3)
#     print('test 函数运行完毕')
#     return "这是test的返回值name= %s,age= %s gen= %s" %(name,age,gen)
# # fun1 = test(fun1)  ===> @test
# res = fun1("alex",123,'男')
# print(res)
# # 语法糖： @test ==> fun1 = test(fun1)
# # 快速取出列表中的首项和最后一项
# li = [1,2,3,4,3,2,13,1223]
# a,*_,c = li
# print(a)
# print(c)
# a,*d,c = li
# print(a)
# print(c)
# print(d)
# a,*d,b,c = li
# print(a)
# print(c)
# print(d)
# print(b)
# # 交换
# a =1
# b =2
# a,b = b,a
# print("========")
# print(a)
# print(b)
user_list = [{"username":'alex',"passWd":"123"},
             {"username":'xiaocang',"passWd":"123456"},
             {"username":'xiaoming',"passWd":"322"},
             {"username":'xiaohong',"passWd":"223"},
             {"username":'xiaoxiao',"passWd":"343"},]
user_dic = {"username":'alex',"login":False}
def jiaoyan(func):
    def wrapper(*args,**kwargs):
        print("开始校验")
        if user_dic['username'] and user_dic['login']:
            res = func(*args, **kwargs)
            return  res
        userName = input("请输入用户名：").strip()
        passWd = input("请输入密码：").strip()
        for user_dict in user_list:
            if userName == user_dict["username"] and passWd == user_dict["passWd"]:
                user_dic["username"] = userName
                user_dic['login'] = True
                res = func(*args, **kwargs)
                return res
        return "用户名或者密码错误。。。。"
    return wrapper
@jiaoyan
def index():
    print("欢迎登陆")

@jiaoyan
def home(name):
    print("欢迎登陆 %s" %name)

index()
home("lala")

