"""
# python3  中统一新式类为一下格式
# class Chinese:
#     pass
# 经典类
class Chinese:
    pass
# 新式类--python2 中
class Chinese(object):
    pass
print(Chinese)
p1 = Chinese() # s实例化
print(p1)
"""



class Chinese:
    '这是一个中国的类'
     # 数据属性
    government="共产党"
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def eatFunc(self):
        print("%s 正在吃饭。。。。" %self.name)
    def chadui(self):
        print("%s正在插队。。。" %self.name)

print(Chinese.government)
# p1 = Chinese()
# print(p1.government)
# Chinese.eatFunc()
# print(dir(Chinese))
# 查看类的属性字典，Chinese.government 相当于到  __dict__ 中找
print(Chinese.__dict__)

p1 = Chinese('小泽玛丽',14,'男')
print(p1.__dict__)
print(p1.government)
p1.eatFunc()
"""
# 类的内容
print(Chinese.__name__)  # 类的名称  Chinese
print(Chinese.__doc__) # 类的文档字符串(类的说明) '这是一个中国的类'
print(Chinese.__base__) # 类的第一个父类 <class 'object'>
print(Chinese.__bases__) # 类的所有父类构成的元组
print(Chinese.__dict__) # 类的属性
print(Chinese.__module__) # 类定义所在的模块
print(Chinese.__class__) # 对应的类
"""
# 查看属性
print(Chinese.government)

# 修改属性
Chinese.government = "中国共产党"
print(p1.government)
print(Chinese.government)
# 删除属性
del Chinese.government

#增加属性
Chinese.country = "China"
Chinese.location = "亚洲"
print(Chinese.__dict__)

# 增加方法
def eat_food(self,food):
    print("%s 正在吃%s" %(self.name,food))
Chinese.eat_food = eat_food


p1.eat_food("包子")
p1.country = "lll"
print(Chinese.country)
print(p1.country)