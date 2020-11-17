# l = list('hello')
# print(l)
"""
str函数 或者print函数   --> obj.__str__()
repr函数或者交互式解释器 --->obj.__repr__()
如果 __str__()没有被定义,那么就会使用__repr__()来代替输出
注意:这两个方法的返回值必须是字符串,否则会抛出异常

"""

class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '名字是 %s 年龄是 %s' %(self.name,self.age)
    def __repr__(self):
        return 'repr 名字是 %s 年龄是 %s' %(self.name,self.age)
f1 = Foo('仓仓',12)
repr(f1) # --->repr(f1) --> f1.__repr__()  # repr 解释器触发
print(f1)  # str()-->f1.__str__()如果找不到 --> f1.__repr__() 来替代
