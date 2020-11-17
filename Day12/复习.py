# isinstance(obj,cls) # 检查一个对象obj是否是类cls的对象
class Foo(object):
    # pass
    def __init__(self,name):
        self.name=name
    def __getattr__(self, item):
        print("===执行__getattr__",item)
        # return self.__dict__[item]
        # print(self)
        # return
    def __getattribute__(self, item):
        print("===执行__getattribute__", item)
        raise AttributeError(item)  #只有这里抛出了AttributeError 异常后才会执行__getattr__
obj = Foo('小明')

res = isinstance(obj,Foo)
print(res)
# 是否是子类
res = issubclass(Foo,object)
print(res)
print(obj.name)   # === 存在 ===只执行__getattribute__
# print(obj.age)  # === 不存在 ===只执行__getattribute__  raise AttributeError('跑出异常')