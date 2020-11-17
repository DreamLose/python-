class Foo:
    x = 1
    def __init__(self,y):
        self.y = y

    def __getattr__(self, item):
        print("执行__getattr__,你访问的属性 [%s] 不存在" %(item))
    def __delattr__(self, item):
        print("执行__delattr__", item)
        self.__dict__.pop(item)

    # self.y = y  ==> 会触发这个函数
    def __setattr__(self, key, value):
        # 可以进行属性设置过程的控制
        print("执行__setattr__key ==%s,value==%s" %(key,value))
        # self.key = value  # 会触发无限递归
        self.__dict__[key] = value
f1 = Foo(10)
print(f1.y)
f1.z = 2
print(f1.age )
# print(getattr(f1,'y'))
# print(f1.ewrwrw)  # 调用不存在的属性,会调用 __getattr__
#
# del f1.y  # 删除操作会调用 __delattr__
# del f1.x




