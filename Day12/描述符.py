# 数据描述符

# 优先级
# 类属性> 数据描述符>实例属性>非数据描述符>找不到

class Foo:

    # 数据描述符  __get__ __set__ __delete__
    def __get__(self, instance, owner):
        print("__get__方法 instance = %s owner = %s" %(instance,owner))
    def __set__(self, instance, value):
        print("__set__方法 instance = %s value = %s" %(instance,value))
        instance.__dict__['x'] = value
    def __delete__(self, instance):
        print("__delete__方法 instance = %s" % instance)


class Bar:
    x = Foo()
    def __init__(self,n):
        self.x = n

b1 = Bar(10)
print(b1.__dict__)
print(b1.x)
print(Bar.__dict__)
# print(b1.x.__dict__)