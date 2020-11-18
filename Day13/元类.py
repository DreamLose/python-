# 元类-->类的类,是类的模板 type 是python的内置元类
class Foo:
    pass
f1 = Foo()
print(Foo)
# print(type(f1))
#
# print(type(Foo))

# type 创建类 (类名,继承对象,属性)
def __init__(self,name):
    self.name=name
FFo = type('FFo',(object,),{'x':1,'__init__':__init__})
print(FFo)
print(FFo.__dict__)
f2 = FFo('小苍')
print(f2.x)
print(f2.name)