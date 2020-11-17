class Foo:
    def __getitem__(self, item):
        print("__getitem__",item)
        return self.__dict__[item]
    def __setitem__(self, key, value):

        print("__setitem__ key = %s;value = %s" %(key,value))
        self.__dict__[key] = value
    def __delitem__(self, key):
        print("__delitem__ key = ", key)
        self.__dict__.pop(key)

f1=Foo()
print(f1.__dict__)
# f1.name = "仓老师"  #会调用  __setattr__
f1['name'] = '小泽'
f1['age'] = 19
print(f1.__dict__)
print(f1['name'])
del f1['name']
print(f1.__dict__)

#  以[] 赋值或者删除 才会调用 __delitem__  __setitem__ 等, 以fi. 调用会触发 __setattr__ 等方法