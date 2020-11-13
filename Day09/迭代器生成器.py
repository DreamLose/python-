

"""
import time

lis = [1,2,3]
# l_iter = lis.__iter__()
# print(l_iter.__next__())
# print(l_iter.__next__())
# for 循环会调用 lis中的 __iter__() 方法，在调用__next__()
# 模拟for循环
list_iter = lis.__iter__()
print(next(list_iter))  # next()-----> list_iter.__next__()
while True:
    try:
        print(list_iter.__next__())
    except StopIteration:
        print("遍历完成，循环终止")
        break

"""

# ==========生成器=====可以理解为一种数据类型，自动实现了迭代器协议
"""
# 第一种生成器方式，常规函数用 yield 语句返回 而不是return ，yield一次只能返回一个结果
def test():
    print("开始生成器")
    yield 1
    time.sleep(3)
    print('2112')
    yield 2
    time.sleep(3)
    print('3232')
    yield 3
    time.sleep(3)
    print('werwewew')
    yield 4
g = test()
print(g)
print(g.__next__())
print(g.__next__())

# 第二种表现形式  ===？生成器表达式
# 三元表达式
name = "hhh"
# 如果name =="xioaming" ，返回"SB", 否则返回"ll"
res = "SB" if name =="xioaming" else "ll"
print(res)

# 列表解析
egg_list = []
for i in range(10):
    egg_list.append("鸡蛋 %s" %i)
print(egg_list)
# 列表解析 ：缺点数据大的时候会占内存
egg_list = [ "鸡蛋 %s" %i for i in range(10)]
print(egg_list)
# 列表解析  三元
egg_list = [ "鸡蛋 %s" %i for i in range(10) if i > 5]
print(egg_list)
# 生成器表达式 更节省内存
laomuj = ("鸡蛋 %s" %i for i in range(10))
print(laomuj)
print(laomuj.__next__())
print(next(laomuj))

"""
# 缺点： 占用空间大，效率低
# def productEgg():
#     ret = []
#     for i in range(100):
#         ret.append("鸡蛋 %s" %i)
#     return ret
# print(productEgg())

def productEgg():
    for i in range(100):
       yield "鸡蛋 %s" %i

productFun = productEgg()
egg = productFun.__next__()
print("xx来取鸡蛋 %s" %egg)

